from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")

movie_title = [ tag.getText() for tag in reversed(titles)]

with open('movies.txt', 'w') as fp:
    for title in movie_title:
        fp.write(f"{title} \n")