import pandas as pd
import numpy as np

def get_user_movies(preferred_genres, n=10):
    """
    Get all movies based on preferred genres and choose 10 random.
    """

    # get all movies based on preferred genres
    movie_list = movies_df[movies_df['genre_names'].apply(lambda x: any(genre in x for genre in preferred_genres))]
    movie_list = movie_list[['id', 'title', 'genre_ids']]

    # pick 10 random movies in list
    movie_list = movie_list.sample(n=min(n, len(movie_list)))

    # create a random rating between 5 - 10
    movie_list['user_rating'] = np.random.randint(5, 11, size=len(movie_list))

    return movie_list

if __name__ == "__main__":
    """
    Generate unique user movie list based on genre preference.
    """

    movies_df = pd.read_csv('movie-dataset/master_movies.csv')  
    genres_df = pd.read_csv('movie-dataset/genre.csv')

    genre_dict = dict(zip(genres_df['id'], genres_df['name']))

    # extrapolate "genre_ids" column to its name to "genre_names"
    movies_df['genre_names'] = movies_df['genre_ids'].apply(lambda x: ', '.join([genre_dict[g] for g in eval(x)]))
    
    # create users based on preference
    user_movie_lists = pd.DataFrame()
    user_genre_preferences = {
        '1': ['War', 'Western'],
        '2': ['Action'],
        '3': ['Romance'],
        '4': ['Action', 'Comedy', 'Crime'],
        '5': ['History', 'Science Fiction', 'Thriller'],
        '6': ['Drama', 'Fantasy']
    }

    # generate list 
    for user_id, preferences in user_genre_preferences.items():
        movie_list = get_user_movies(preferences)
        movie_list['user_id'] = user_id
        user_movie_lists = pd.concat([user_movie_lists, movie_list], ignore_index=True)
    
    user_movie_lists.to_csv("movie-dateset/users_list.csv")
    