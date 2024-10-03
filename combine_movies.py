import pandas as pd

if __name__ == "__main__":
    """
    Combine comedy, action, horror, and drama genres
    """

    # read all dataframes
    df1 = pd.read_csv("movie-dataset/movies.csv") 
    df2 = pd.read_csv("movie-dataset/movies2.csv") 

    # combine the dataframes
    master_movies = pd.concat([df1, df2], ignore_index=True)

    # count the duplicates
    duplicates = master_movies[master_movies.duplicated(subset='id', keep=False)]
    count_of_dups = duplicates['id'].nunique()  
    
    print(f"Count of duplicated movies IDs: {count_of_dups}")
    print("The duplicated entries: ")
    print(duplicates)

    # drop duplicates and store to master_movies.csv
    master_movies = master_movies.drop_duplicates(subset='id', keep='first')
    master_movies.to_csv("movie-dataset/master_movies.csv", index=False)
    print("movie-dataset/master_movies.csv is created.")
        