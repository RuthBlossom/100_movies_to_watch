# Movie Titles Web Scraper

This Python script utilizes the Requests and BeautifulSoup libraries to scrape movie titles from a webpage and save them to a text file.

## Features

- **Web Scraping**: The script makes a GET request to a specified URL, extracts movie titles from the HTML content, and saves them to a text file.
- **Reversed Order**: The movie titles are extracted in reverse order to maintain the original ranking.
- **File Output**: The script writes the movie titles to a text file named "movies.txt" with each title on a new line.

## How It Works

The script performs the following steps to scrape movie titles:

1. **URL Definition**: The URL of the webpage to be scraped is defined.
2. **HTTP Request**: A GET request is made to the URL, and the HTML content of the webpage is stored in a variable.
3. **HTML Parsing**: The BeautifulSoup library is used to parse the HTML content and extract specific elements (movie titles).
4. **Title Extraction**: All HTML elements with the name "h3" and class "title" are found, and their text content (movie titles) is extracted.
5. **Order Reversal**: The order of the movie titles is reversed to maintain the original ranking.
6. **File Writing**: The movie titles are written to a text file named "movies.txt", with each title on a new line.

## Usage

1. Run the script using a Python interpreter.
2. The script will scrape the movie titles from the specified webpage and save them to a text file named "movies.txt".

## Customization

You can customize the script in the following ways:

- **URL**: Change the URL to scrape movie titles from a different webpage.
- **Output File**: Modify the filename and file path to save the movie titles to a different location.
- **HTML Parsing**: Adjust the BeautifulSoup parsing logic to extract different types of content from the webpage.

## Prerequisites

Before running the script, ensure you have Python installed on your system. Additionally, install the required libraries using pip:

```
pip install requests beautifulsoup4
```

