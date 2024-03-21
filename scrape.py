import requests
from bs4 import BeautifulSoup
import pprint

# Get the HTML content of the news page
res = requests.get("https://news.ycombinator.com/news")
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(res.text, "html.parser")
# Select the news links and subtext elements
links = soup.select(".titleline > a")
subtext = soup.select(".subtext")

# Function to sort stories by the number of votes
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)

# Function to create a custom list of news stories with votes greater than 99
def create_custom_hn(links, subtext):
    hn = []  # List to hold the news stories
    for idx, item in enumerate(links):
        title = item.getText()  # Get the title text
        href = item.get("href", None)  # Get the link URL
        vote = subtext[idx].select(".score")  # Get the vote element
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))  # Extract the vote count
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return hn

# Number of pages to scrape and current page counter
number_of_pages = 1
current_page_number = 1
hn_list = []  # List to hold all the news stories

# Loop through the specified number of pages
for page in range(number_of_pages + 1):
    hn_list.extend(create_custom_hn(links, subtext))  # Add the news stories to the list
    # Fetch the next page
    res = requests.get("https://news.ycombinator.com/news" + f"?p={current_page_number}")
    current_page_number += 1
    # Parse the new page
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".titleline > a")
    subtext = soup.select(".subtext")

# Print the sorted list of news stories
pprint.pprint(sort_stories_by_votes(hn_list))