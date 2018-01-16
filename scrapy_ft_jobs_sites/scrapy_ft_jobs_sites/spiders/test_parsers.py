import os
from bs4 import BeautifulSoup

from parsers import IndeedParser

def test_indeed_parser():
    with open(os.path.join("test_data", "indeed.html")) as html:
        soup = BeautifulSoup(html.read(), 'html.parser')
        parser = IndeedParser(soup, "indeed.com")
        response = parser.parse_response()
        print response
        assert response is not None
        assert len(response) != 0
