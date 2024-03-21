# hacker_news_scraper

This script scrapes news articles from Hacker News that have more than 99 points and sorts them by the number of votes.

## How It Works

The script uses `requests` and `BeautifulSoup` to parse the HTML of Hacker News and extract news stories with a significant number of votes.

## Requirements

- Python 3
- `requests` library
- `beautifulsoup4` library

## Installation

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

### Usage

Run the script to scrape the news articles:

python scrape.py

### Customization

You can modify the number_of_pages variable to scrape more pages.
