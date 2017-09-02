import os
import random
import unittest
import requests

from bs4 import BeautifulSoup

from scrapy_ft_jobs_sites.spiders.parsers import IndeedParser, GlassdoorParser

class BaseParserTestCase(object):
    """
    Base class for all parser tests
    """
    class BaseTest(unittest.TestCase):
        TEST_URL = ""
        SOURCE = ""
        UA = [user_agent.strip() for user_agent in open(os.path.join("misc", "uas.txt")).readlines()]

        response = None
        soup = None
        parser_class = None

        def setUp(self):
            current_ua = random.choice(self.UA)
            headers = {'User-Agent': random.choice(self.UA)}
            html_response = requests.get(self.TEST_URL, headers=headers)
            self.assertEqual(html_response.status_code, 200)
            self.soup = BeautifulSoup(html_response.text, 'html.parser')


        def test_parser(self):
            parser = self.parser_class(self.soup, self.SOURCE)
            actual_results = parser.parse_response()
            self.assertNotEqual(actual_results, None)
            self.assertNotEqual(len(actual_results), 0)

            for item in actual_results:
                self.assertEqual(item['source'], self.SOURCE)


class IndeedParserTest(BaseParserTestCase.BaseTest):
    """
    Test case to check parsing logic for IndeedParser
    """

    TEST_URL = "https://www.indeed.com/q-django-jobs.html"
    SOURCE = "indeed.com"

    response = None
    soup = None
    parser_class = IndeedParser


class GlassdoorParserTest(BaseParserTestCase.BaseTest):
    """
    Test case to check parsing logic for GlassdoorParser
    """

    TEST_URL = "https://www.glassdoor.co.in/Job/us-django-jobs-SRCH_IL.0,2_IN1_KO3,9.htm?countryRedirect=true"
    SOURCE = "glassdoor.co.in"

    response = None
    soup = None
    parser_class = GlassdoorParser


if __name__ == "__main__":
    unittest.main()