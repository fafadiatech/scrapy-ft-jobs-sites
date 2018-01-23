import os
from hashlib import md5
from datetime import datetime

from scrapy_ft_jobs_sites.settings import CRAWLER_DIR

MAX_HASH_CHARS = 8


def check_or_create_directory(spider_name):
    """
    this is used to create directory for storing the html content
    for a given spider on its domain name
    """

    crawl_id = md5(str(datetime.now().strftime("%Y%m%d"))
                   ).hexdigest()[:MAX_HASH_CHARS]
    base_directory = os.path.join(CRAWLER_DIR[0], spider_name)

    all_directories = [base_directory, os.path.join(base_directory, crawl_id)]

    # this is used to check if the directory exists or not then its creates one
    for current_dir in all_directories:
        if not os.path.exists(current_dir):
            os.mkdir(current_dir)

    return crawl_id


def cache_response(spider_name, html_response):
    """
    this method is used to save HTML response to disk
    """
    crawl_id = check_or_create_directory(spider_name)
    page_id = md5(str(datetime.now())).hexdigest()[:MAX_HASH_CHARS]
    file_path = os.path.join(CRAWLER_DIR[0], spider_name, crawl_id, page_id)
    with open(file_path, "w") as file_to_save:
        file_to_save.write(html_response.encode("utf-8"))
        file_to_save.close()
