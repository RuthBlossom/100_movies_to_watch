# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to be scraped
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Make a GET request to the URL and store the HTML content in 'response'
response = requests.get(URL) # Make a GET request to the specified URL and store the response.
website_html = response.text # Extract the HTML content from the response

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(website_html, "html.parser") # Create a BeautifulSoup object to parse the HTML content.

# Find all HTML elements with the name "h3" and class "title"
all_movies = soup.find_all(name="h3", class_="title")

# Extract the text content of each movie title and store them in a list
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the order of the movie titles list
movies = movie_titles[::-1]

# Open a file named "movies.txt" in write mode and write each movie title to a new line
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
      # terate through the reversed movie titles list and write each title to the file, appending a newline character after each title.



'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.



The [::-1] is a slicing syntax in Python used to reverse a sequence (such as a list, string, or tuple). Here's a breakdown of how it works:

The first colon : represents the start index of the slice.
The second colon : represents the end index of the slice.
The third part (-1) represents the step or the increment value.
When used as [::-1], it means:

Start from the end of the sequence.
Move towards the beginning.
The step is -1, which means go backward one step at a time.
So, [::-1] effectively reverses the order of the elements in the sequence.
'''