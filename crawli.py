# pip install pyyaml tenacity tqdm pandas

import logging
import cloudscraper
import time
import re
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
from pathlib import Path
from tenacity import retry, stop_after_attempt, wait_exponential

# Setup logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('crawler.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('CrawliCrawler')

class CrawliAdvanced:
    def __init__(self, base_url, config=None):
        self.logger = setup_logging()
        self.base_url = base_url
        self.config = config or self.load_default_config()
        
        # Create cloudscraper with error handling
        try:
            self.scraper = cloudscraper.create_scraper(
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                }
            )
            self.logger.info("Cloudscraper initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize cloudscraper: {e}")
            raise
        
        self.visited_urls = set()
        self.video_urls = set()
        self.session_start = datetime.now()
        self.stats = {
            'pages_crawled': 0,
            'urls_found': 0,
            'errors': 0,
            'retries': 0
        }
    
    def load_default_config(self):
        """Load default configuration"""
        return {
            'max_pages': 50,
            'delay': 1.0,
            'timeout': 30,
            'max_retries': 3,
            'output_format': 'txt',
            'include_patterns': [r'/video/'],
            'exclude_patterns': [r'/playlist/']
        }
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def fetch_page_with_retry(self, url):
        """Fetch page with retry logic"""
        try:
            self.logger.info(f"Fetching page: {url}")
            response = self.scraper.get(url, timeout=self.config['timeout'])
            
            if response.status_code == 200:
                self.logger.info(f"Successfully loaded page: {url}")
                return response.text
            else:
                self.logger.warning(f"HTTP {response.status_code} for {url}")
                return None
                
        except Exception as e:
            self.stats['retries'] += 1
            self.logger.error(f"Error fetching {url}: {e}")
            raise
