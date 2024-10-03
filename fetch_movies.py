import requests 
import pandas as pd
import os
from dotenv import load_dotenv
import time

def get_genre_list():
    """
    Fetch and store genre list to "genre.csv".
    """
    print(f"Fetching genre list.")
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ['API_KEY']}"
    }

    try:
        response = requests.get(url, headers=headers)

        # only if request is successful
        if response.status_code == 200:
            genre = response.json() 
            genre = pd.DataFrame(genre["genres"])
            genre.to_csv("genre.csv", index=False)
        else:
            print(f"An error occurred in get_genre_list. {response.status_code} Ending.")
            exit()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def make_movie_request(genre, year, page):
    """
    Fetch movie by genre, year, and page.
    """
    print(f"Fetching genre: {genre}, year: {year}, page: {page}.")
    url = f"https://api.themoviedb.org/3/discover/movie?language=en-US&with_genres={genre}&primary_release_year={year}&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.environ['API_KEY']}"
    }
    try:
        response = requests.get(url, headers=headers)

         # only if request is successful
        if response.status_code == 200:
            movies = response.json() 
            return movies
        else:
            print(f"An error occurred in make_movie_request. {response.status_code} Ending.")
            exit()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    
    load_dotenv() # loads api key secret into this file

    # call once and store genres
    if not os.path.exists("genre.csv"):
        get_genre_list()

    genres = pd.read_csv("genre.csv")
    
    game = True
    while game:
        # get movies at a specific genre, year, and page
        print(genres)
        genre = input("Enter id of corresponding genre (-1 to exit): ") # 28

        if genre == "-1":
            "Ending.."
            exit()

        year_range = input("Enter year range (e.g. 2019-2024): ") 
        start_year, end_year = map(int, year_range.split('-'))
        years = list(range(start_year, end_year + 1))

        max_page = 11
        for year in years:
            page = 1
            while page != max_page:
                response = make_movie_request(genre, year, page)

                # store in movies.csv
                movies = pd.DataFrame(response["results"])
                if os.path.exists("movies.csv"):
                    # movies.csv exist add to csv
                    movies.to_csv("movies.csv", mode='a', header=False, index=False)
                    print(f"(Append movies.csv) Added movies to movies.csv from genre: {genre}, year: {year}, page {page}.")
                else:
                    # movies.csv doesn't exist create csv
                    movies.to_csv("movies.csv", index=False)
                    print(f"(Create movies.csv) Added movies to movies.csv from {genre}, year: {year}, page {page}.")
                    
                time.sleep(5) # makes sure max request isn't met

                # continue until max page is reached
                if response["page"] != max_page:
                    page += 1

    print(f"Complete finding genre: {genres.loc[genre['id'] == genres, 'name'][0]}")