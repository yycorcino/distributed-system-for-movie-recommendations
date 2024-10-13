import pandas as pd
import sys

# for genre ids
genre_mapping = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}

def get_user_genres(user_rated_movies): 
    """
    List of genres collected based on user list.
    """

    user_genres = []
    for genre_ids in user_rated_movies['genre_id']:
        genres = eval(genre_ids)  
        user_genres.extend(genres)  
    return set(user_genres) 

def genre_check(genre_ids, user_genres):
    """
    Checks genres of movies recommended align with user interest.
    """

    movie_genres = eval(genre_ids)
    return any(int(genre) in user_genres for genre in movie_genres)

def get_genres(genre_ids):
    """
    Checks for genre id and its matching genre type for output.
    """

    genres = eval(genre_ids)
    return [genre_mapping[int(genre)] for genre in genres]

def get_recommendations(user_id): 
    user_rated_movies = user_ratings_df[(user_ratings_df['user_id'] == user_id) & (user_ratings_df['user_rating'] >= 5)]

    if user_rated_movies.empty:
        print(f"No data found for User {user_id}.")
        return

    user_genres = get_user_genres(user_rated_movies)

    recommended_movies = movies_df[movies_df['vote_average'] >= 5]
    recommended_movies = recommended_movies[recommended_movies['genre_ids'].apply(lambda x: genre_check(x, user_genres))]
    recommended_movies['genres'] = recommended_movies['genre_ids'].apply(get_genres)

    output_columns = ['id', 'title', 'release_date', 'vote_average', 'genres']
    top_recommendations = recommended_movies[output_columns]

    randomized_recommendations = top_recommendations.sample(frac=1).reset_index(drop=True)  
    top_random_recommendations = randomized_recommendations.head(10)

    print(f"\nRecommended Movies for User {user_id}:\n")
    for index, row in top_random_recommendations.iterrows():
        print(f"Movie ID: {row['id']}")
        print(f"Title: {row['title']}")
        print(f"Release Date: {row['release_date']}")
        print(f"Vote Average: {row['vote_average']}")
        print(f"Genres: {', '.join(row['genres'])}\n")

if __name__ == "__main__":
    print("Starting ...")

    # edit the file path for Hadoop 
    movies_df = pd.read_csv('gs://genre-movies/master_movies.csv')
    user_ratings_df = pd.read_csv('gs://genre-movies/users_list.csv')

    user_input_id = int(sys.argv[1]) 
    get_recommendations(user_input_id)