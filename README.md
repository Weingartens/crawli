# 🕷️ Crawli - Universal Web Crawler

Crawli is a powerful and user-friendly web crawler designed for systematic extraction of URLs and content from modern websites. It combines advanced crawling technologies with intelligent filtering and offers an intuitive, interactive interface.

## ✨ Features

- **🛡️ Modern Web Compatibility**: Bypasses Cloudflare and other anti-bot protections using specialized scraping libraries
- **🎯 Intelligent URL Extraction**: Recognizes and collects URLs based on configurable patterns and schemas  
- **⏱️ Rate Limiting**: Implements responsible crawling speeds to protect target servers
- **📁 Automatic Data Organization**: Creates daily output files with timestamps for better data management
- **🔍 Flexible Filtering**: Ignores unwanted URL types and focuses on relevant content
- **💬 Interactive Interface**: Provides real-time feedback on crawling progress and discovered results

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Method 1: Quick Installation (System-wide)

```
pip install cloudscraper beautifulsoup4 requests
```

### Method 2: Virtual Environment (Recommended)

#### On Linux/macOS:
```
# Check if python3-venv is installed (Debian/Ubuntu)
sudo apt update
sudo apt install python3-venv

# Create project directory
mkdir crawli-project
cd crawli-project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install cloudscraper beautifulsoup4 requests

# Download the crawler script
# (Place your crawler.py file in this directory)

# Run the crawler
python crawler.py

# When finished, deactivate virtual environment
deactivate
```

#### On Windows:
```
# Create project directory
mkdir crawli-project
cd crawli-project

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install cloudscraper beautifulsoup4 requests

# Download the crawler script
# (Place your crawler.py file in this directory)

# Run the crawler
python crawler.py

# When finished, deactivate virtual environment
deactivate
```

### Method 3: Using requirements.txt

Create a `requirements.txt` file:
```
cloudscraper>=1.2.60
beautifulsoup4>=4.12.0
requests>=2.31.0
```

Then install:
```
# With virtual environment activated
pip install -r requirements.txt

# Or system-wide
pip install -r requirements.txt
```

### Fixing "externally-managed-environment" Error

If you encounter this error on modern Linux distributions:

```
# Option 1: Use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install cloudscraper beautifulsoup4 requests

# Option 2: Use system packages (limited availability)
sudo apt install python3-requests python3-bs4
# Note: cloudscraper usually not available via apt

# Option 3: Use pipx for isolated installation
sudo apt install pipx
pipx install cloudscraper
# Note: This method may require additional configuration
```

## 📖 Usage

### Quick Start

1. **Setup Environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or venv\Scripts\activate on Windows
   pip install cloudscraper beautifulsoup4 requests
   ```

2. **Run Crawler:**
   ```
   python crawler.py
   ```

3. **Follow Interactive Prompts:**
   ```
   Universal Video URL Crawler
   ==============================
   Enter the base URL to crawl (e.g. https://de.spankbang.com/): https://yoursite.com/
   Maximum pages to crawl (default: 50): 100
   ```

### Example Session

```
Universal Video URL Crawler
==============================
Enter the base URL to crawl (e.g. https://de.spankbang.com/): https://example.com/
Maximum pages to crawl (default: 50): 25

🚀 Universal Crawler started
📅 Date: 06/11/2025 18:47:32
--------------------------------------------------
📡 Loading page: https://example.com/
✅ Successfully loaded (Status: 200)
🎥 New video URL found: https://example.com/abc123/video/sample
📊 Status: 1 videos found, 1 pages crawled
⏳ Waiting 1 second...
```

## ⚙️ Configuration

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| Base URL | Root URL to start crawling | Interactive input | `https://example.com/` |
| Max Pages | Maximum pages to crawl | 50 | `100` |
| Rate Limit | Delay between requests | 1 second | Fixed |

## 📤 Output

The crawler saves discovered URLs in a text file with the following naming convention:

```
crawler_output_MM.DD.YYYY.txt
```

### Output Format

```
Crawler Output - Crawl from 06/11/2025 18:47:32
============================================================

https://example.com/abc123/video/sample-video
https://example.com/def456/video/another-video
https://example.com/ghi789/video/third-video

Total 3 video URLs found.
```

## 🔧 Technical Details

### URL Pattern Matching

Crawli looks for URLs matching the pattern:
```
{base_url}/[ID]/video/[name]
```

### Filtering Rules

- ✅ **Includes**: URLs containing `/video/` in the path
- ❌ **Excludes**: URLs containing `playlist` (case-insensitive)

### Anti-Detection Features

- Uses cloudscraper to bypass Cloudflare protection
- Mimics real browser behavior with proper headers
- Implements respectful crawling with rate limiting

## ⚠️ Important Notes

- **Respect Terms of Service**: Always check and comply with website terms of service and robots.txt
- **Rate Limiting**: Default 1-second delay between requests - adjust if needed
- **Cloudflare Limitations**: Cloudscraper may not work with all modern Cloudflare protections
- **Ethical Usage**: Use responsibly and respect server resources

## 🔄 Alternative Solutions

If cloudscraper fails, consider these alternatives:

```
# Option 1: Selenium with undetected-chromedriver
pip install selenium undetected-chromedriver

# Option 2: Playwright with stealth
pip install playwright playwright-stealth
```

## 🐛 Troubleshooting

### Common Issues

**"externally-managed-environment" Error**
```
# Solution: Use virtual environment
python3 -m venv venv && source venv/bin/activate
pip install cloudscraper beautifulsoup4 requests
```

**"No module named 'cloudscraper'" Error**
```
# Make sure virtual environment is activated
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Then install missing packages
pip install cloudscraper beautifulsoup4 requests
```

**Cloudflare Blocking**
- Try using different user agents
- Consider switching to Selenium-based approach
- Increase delays between requests

**No URLs Found**
- Verify the base URL is accessible
- Check if the target site uses the expected URL pattern
- Review filtering rules in the code

### Environment Verification

Check if your environment is properly set up:

```
# Check Python version
python --version

# Check installed packages
pip list

# Verify specific packages
python -c "import cloudscraper; print('cloudscraper installed')"
python -c "import bs4; print('beautifulsoup4 installed')"
python -c "import requests; print('requests installed')"
```

## 📋 Requirements

```
cloudscraper>=1.2.60
beautifulsoup4>=4.12.0
requests>=2.31.0
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 💡 Roadmap

- [ ] Add support for custom URL patterns
- [ ] Implement proxy rotation
- [ ] Add database storage option
- [ ] Create GUI interface
- [ ] Add multi-threading support

## 🙋‍♂️ Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with detailed information

---

⭐ **Star this repo if you find it useful!**
```
