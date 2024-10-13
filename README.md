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

This project uses Google Cloud Platform(GCP) to host Apache Spark and Hadoop via Dataproc. Utilizing the Google Console, we are able to submit jobs to emulate the user loading home there "For You Page".

### Usage

How to submit jobs?

- Submit a job via Google Console

  ```
    gcloud dataproc jobs submit pyspark <gs://genre-movies/rec_movie.py> --cluster=<apache-hadoop-instance> --region=<us-central1> -- <user_id>
  ```

    _Replace <{data}> according to your setup._

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
