from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# Getting a particular tag
print(soup.title)
print(soup.title.string)

# Prettify
soup.prettify()

# Find all
all_anchor_tags = soup.find_all(name='a')

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id='name')

section_heading = soup.find(name='h3', class_='heading')

### Using CSS Selectors to find any item on a webpage
books_and_teaching = [heading for heading in soup.select('.heading') if heading.text == 'Books and Teaching']  
print(books_and_teaching)