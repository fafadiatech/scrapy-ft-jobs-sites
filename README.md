# Collection of Scrapy Spiders for Jobs Sites

This is a scrapers for Job Aggregator written with Scrapy

## Authors

- Sidharth Shah {sidharth@fafadiatech.com}

## Included Sites

- Indeed
- Glassdoor
- CarrerBuilder
- Monster
- TimesJob
- Shine
- Django Gig
- Has Job
- Angle.co
- Naukri
- Glassdoor
- Monster India
- Placement India
- Jora
- Trovit
- Hirist
- Python Job Boards

## Usage

- `scrapy crawl indeed -t json -o indeed.json`, replace `indeed` with one of the above mentioned sites

## Testing
- Run test suite for parser by calling `python test_parsers.py` from root directory of the project

## Worklog

- Aug 30 2017
	- First commit
- Sep 3 2017
	- Refactored Spiders and Parsers
	- Added `test_parsers.py` which is test suite used for checking parser