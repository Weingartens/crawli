import cloudscraper
import time
import re
from datetime import datetime
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

class UniversalCrawler:
    def __init__(self, base_url):
        # Create cloudscraper to bypass Cloudflare protection
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
            }
        )
        
        self.base_url = base_url
        self.visited_urls = set()
        self.video_urls = set()
        self.session_start = datetime.now()
        
    def get_filename(self):
        # Create filename with current date
        current_date = datetime.now().strftime("%m.%d.%Y")
        return f"crawler_output_{current_date}.txt"
    
    def is_valid_video_url(self, url):
        # Check if URL matches the desired schema
        # Pattern: base_url/[ID]/video/[Name]
        pattern = re.escape(self.base_url) + r'[^/]+/video/[^/]+'
        return re.match(pattern, url) is not None
    
    def should_ignore_url(self, url):
        # Check if URL should be ignored (playlist etc.)
        return 'playlist' in url.lower()
    
    def extract_urls_from_page(self, html_content, base_url):
        # Extract all URLs from a page
        soup = BeautifulSoup(html_content, 'html.parser')
        urls = set()
        
        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute URLs
            full_url = urljoin(base_url, href)
            
            # Only URLs from the same domain
            if base_url in full_url:
                urls.add(full_url)
        
        return urls
    
    def fetch_page(self, url):
        # Fetch a page with Cloudflare protection
        try:
            print(f"📡 Loading page: {url}")
            response = self.scraper.get(url, timeout=30)
            
            if response.status_code == 200:
                print(f"✅ Successfully loaded (Status: {response.status_code})")
                return response.text
            else:
                print(f"❌ Error loading page (Status: {response.status_code})")
                return None
                
        except Exception as e:
            print(f"❌ Error loading {url}: {str(e)}")
            return None
    
    def save_results(self):
        # Save found URLs to file
        filename = self.get_filename()
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Crawler Output - Crawl from {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")
            
            for url in sorted(self.video_urls):
                f.write(url + "\n")
            
            f.write(f"\nTotal {len(self.video_urls)} video URLs found.\n")
        
        print(f"💾 Results saved to: {filename}")
    
    def crawl(self, max_pages=50):
        # Main function for crawling
        print("🚀 Universal Crawler started")
        print(f"📅 Date: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print("-" * 50)
        
        urls_to_visit = [self.base_url]
        pages_crawled = 0
        
        while urls_to_visit and pages_crawled < max_pages:
            current_url = urls_to_visit.pop(0)
            
            # URL already visited?
            if current_url in self.visited_urls:
                continue
            
            # Ignore playlist URLs
            if self.should_ignore_url(current_url):
                print(f"⏭️  Ignoring playlist URL: {current_url}")
                continue
            
            # Load page
            html_content = self.fetch_page(current_url)
            if not html_content:
                continue
            
            self.visited_urls.add(current_url)
            pages_crawled += 1
            
            # Extract URLs from page
            found_urls = self.extract_urls_from_page(html_content, current_url)
            
            for url in found_urls:
                # Collect video URLs
                if self.is_valid_video_url(url):
                    if url not in self.video_urls:
                        self.video_urls.add(url)
                        print(f"🎥 New video URL found: {url}")
                
                # Add new URLs to visit list
                elif url not in self.visited_urls and not self.should_ignore_url(url):
                    urls_to_visit.append(url)
            
            # Output status
            print(f"📊 Status: {len(self.video_urls)} videos found, {pages_crawled} pages crawled")
            
            # Rate limiting: wait 1 second
            print("⏳ Waiting 1 second...")
            time.sleep(1)
        
        print("\n" + "="*50)
        print(f"✅ Crawling completed!")
        print(f"📈 Statistics:")
        print(f"   - Video URLs found: {len(self.video_urls)}")
        print(f"   - Pages crawled: {pages_crawled}")
        print(f"   - Total duration: {datetime.now() - self.session_start}")
        
        # Save results
        if self.video_urls:
            self.save_results()
        else:
            print("⚠️  No video URLs found!")

def main():
    # Main function with interactive input
    print("Universal Video URL Crawler")
    print("="*30)
    
    try:
        base_url = input("Enter the base URL to crawl (e.g. https://youtube.com/): ").strip()
        max_pages = input("Maximum pages to crawl (default: 50): ").strip()
        max_pages = int(max_pages) if max_pages else 50
        
        crawler = UniversalCrawler(base_url)
        crawler.crawl(max_pages)
        
    except KeyboardInterrupt:
        print("\n⏹️  Crawling stopped by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
