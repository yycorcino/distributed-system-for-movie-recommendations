<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">Distributed System For Movie Recommendations</h3>

  <p align="center">
   Developed by: Sebastian Corcino and Gaozong Lo
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

This project uses Google Cloud Platform (GCP) to host Apache Spark and Hadoop via Dataproc. Utilizing the Google Console, we are able to submit jobs to emulate the user loading home their "For You Page".

Our system utilizes PySpark to create a job that recommends movies to a selected user based on their  previous movie ratings. The system operates on a movie dataset and user dataset stored in Google Cloud Storage (GCP) via a bucket path, which is accessed by the PySpark job. 
How it works:
1. **Data Loading**: The job loads the necessary data files from GCP. 
2. **Filtering and Recommendation**: The system asks the user for a user ID to generate a personalized list of 10 movies. It identifies the user’s preferred genres based on their previous movie rankings that scored a 5 or higher. It then selects a list of 10 random movies that also have an average rating of 5 or higher. 
3. **Output**: The system generates and presents a list of 10 movies to recommend to the selected user. The output includes details such as the movie title, release date, vote average, and genre(s). 

### Creating GCP Bucket

Create a new bucket and upload the following files:
- `rec_movies.py`
- `master_movies.csv`
- `users_list.csv`

### Usage

How to submit jobs?

- Submit a job via Google Console

  ```
    gcloud dataproc jobs submit pyspark <gs://genre-movies/rec_movie.py> --cluster=<apache-hadoop-instance> --region=<us-central1> -- <user_id>
  ```

    _Replace <{data}> according to your setup._
    _Replace bucket path (in our case {genre-movies}) to your bucket path._

### Creating Data

How to create your own data with [The Movie Database](https://developer.themoviedb.org/docs/getting-started)?

1. Create API Key for TMDB

   ```
   API_KEY=1234
   ```
    _Put inside .env file_

2. Run fetch_movies.py

    ```
    python3 fetch_movies.py
    ```

3. Run create_usr_data.py
    ```
    python3 create_usr_data.py
    ```
    _Edit variable "user_genre_preferences" for custom user movie list._
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### How to run our system

1. Create dataproc cluster.
2. Create a bucket and upload files.
3. Start cluster and navigate to the ssh terminal located in VM Instances tab.
4. Run the script and enter user ID.