import os
import unittest
import requests

from bs4 import BeautifulSoup

from scrapy_ft_jobs_sites.spiders.parsers import IndeedParser

class IndeedParserTest(unittest.TestCase):
    """
    Test case to check parsing logic for IndeedParser
    """

    TEST_URL = "https://www.indeed.com/q-django-jobs.html"
    TEST_HTML_FILE = os.path.join("indeed", "test.html")
    SOURCE = "indeed.com"

    response = None
    soup = None

    def setUp(self):
        html_response = requests.get(self.TEST_URL)
        self.assertEqual(html_response.status_code, 200)
        self.soup = BeautifulSoup(html_response.text, 'html.parser')


    def test_parser(self):
        parser = IndeedParser(self.soup, self.SOURCE)
        actual_results = parser.parse_response()
        self.assertNotEqual(actual_results, None)


if __name__ == "__main__":
    unittest.main()