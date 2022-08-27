import requests 
from bs4 import BeautifulSoup as bs 

# Get the GitHub username from user input
github_user = input('Inform the GitHub username: ') 

# Make a request to that URL
url = 'https://github.com/' + github_user 
r = requests.get(url) 

# Parse and find the avatar image element
soup = bs(r.content, 'html.parser') 
profile_image = soup.find('img', {'alt': 'Avatar'})['src']

# Print the profile image link
print(profile_image)
