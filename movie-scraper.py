from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')

movie_containers = html_soup.find_all('div', class_= 'lister-item mode-advanced')

first_movie = movie_containers[0]

# Gives us first h3 in the div
# print(first_movie.h3)

# Movie Title
first_movie_title = first_movie.h3.a.text

# Year_of_release
first_year = first_movie.h3.find('span', class_= 'lister-item-year text-muted unbold').text

# IMDB Rating
first_rating = float(first_movie.strong.text)   # Since the first occurence of strong is here

# Metascore
first_metascore = first_movie.find('span', class_='metascore favorable').text

# Number_of_votes
first_number_of_votes = first_movie.find('span', attrs={'name': 'nv'})
first_votes = int(first_number_of_votes['data-value'])


## Scraping for all movies
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_containers:
    if container.find('div', class_='ratings-metascore') is not None:
        name = container.h3.a.text
        names.append(name)

        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)

        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        m_score = container.find('span', class_='metascore').text
        metascores.append(int(m_score))

        vote = container.find('span', attrs={'name': 'nv'})['data-value']
        votes.append(int(vote))

test_df = pd.DataFrame({
    'movie' : names,
    'year' : years,
    'imdb' : imdb_ratings,
    'metascore' : metascores,
    'votes' : votes
})
