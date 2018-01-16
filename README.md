# Collection of Scrapy Spiders for Jobs Sites

This is a scrapers for Job Aggregator written with Scrapy

## Authors

- Shalini Chaturvedi
- Yamini Parab
- Tejashree Mane
- Jitendra Varma
- Ravi Pal
- Oankar Marathe
- Nilam Pal
- Sidharth Shah

## Setup instructions

1. Setup virtualenv and activate it E.g. `virtualenv ~/envs/scrapy-ft-jobs-site` and `source ~/envs/scrapy-ft-jobs-site/bin/activate`
1. Install the requirements `pip install -r requirements.txt`
1. Test a crawl `scrapy crawl indeed -t json -o indeed.json`

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