from scrapy_ft_jobs_sites.items import LeadItem

class IndeedParser:
    """
    Method to parse Indeed response
    """
    soup = None
    source = None


    def __init__(self, soup, source):
        self.soup = soup
        self.source = source


    def parse_response(self):
        results = []
        item = LeadItem()
        postings = self.soup.find_all("div", {"itemtype": "http://schema.org/JobPosting"})

        category = self.soup.find("input", {"name": "q"})['value']

        for current in postings:
            item['title'] = current.h2.a["title"]
            item['source_url'] = "https://www.indeed.com" + current.h2.a["href"]
            item['source'] = "".join(self.source)
            item['category'] = category

            try:
                item['company'] = current.find("span", {"itemprop": "name"}).a.text.strip()
            except:
                item['company'] = ""

            try:
                item['location'] = current.find("span", {"itemprop": "address"}).text.strip()
            except:
                item['location'] = ""

            try:
                item['blurb'] = current.find("span", {"itemprop": "description"}).text.strip()
            except:
                item['blurb'] = ""

            results.append(item)
        return results