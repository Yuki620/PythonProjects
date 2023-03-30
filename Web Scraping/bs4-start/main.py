from bs4 import BeautifulSoup
#import lxml
import requests

response = requests.get('https://news.ycombinator.com')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
title = soup.find_all(name="a")
#title_line = soup.find_all(name="span", class_="titleline")
title_line = soup.select("span.titleline a")
subline_score = soup.select("span.subline span.score")
#title = soup.select(".heading")
article_texts = []
article_links = []
for article_tag in title_line:
    text = article_tag.getText()
    link = article_tag.get("href")
    if article_tag.find("span") == None: 
        article_texts.append(text)
        article_links.append(link)

article_upvote = [ int(article_tag.getText().split(' ')[0]) for article_tag in subline_score]
max_upvote = article_upvote.index(max(article_upvote))
print(article_texts)
print(article_links)
print(article_upvote)
print(article_texts[max_upvote])
print(article_links[max_upvote])





# article_title = title_line.getText()
# article_link = title_line.get("href")
# article_upvote = subline_score.getText()
# print(article_title)
# print(article_link)
# print(article_upvote)



# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)

#print(soup.prettify())

#print(soup.p) # This gives us the first paragraph

#use this to get all the tags
# an anchor tag marks all hypertext links
#all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)
#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))

#heading = soup.find(name="h1", id="name")
#print(heading)

# section_heading = soup.find(name="h3", class_ ="heading")
# print(section_heading.get("class"))

#company_url = soup.select_one(selector="p a")
#print(company_url.get("href"))

#name = soup.select_one(selector="#name") # pound sign for id
#print(name)

# headings = soup.select(".heading") # . to select the class of headings
# print(headings)