
# FP Youtube API Project

Installation procedure using docker

## Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Basic Requirements:

- Server should call the YouTube API continuously in background (async) with some interval (say 15 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerize the project.
- It should be scalable and optimised. 

## Environment Variables In web_server/app

To run this project, you will need to add the following environment variables to your .env file


`API_KEY_1`= 

`MONGO_DB_CRED`=

`DB_NAME`=

`COLLECTION_NAME`=

`API_KEY_2`=


## Environment Variables In Worker

`REDIS_DB_CRED` = 

`INSERT_QUERY` = 

`INSERT_VOLUME` =

`API_KEY_1`= 

`MONGO_DB_CRED`=

`DB_NAME`=

`COLLECTION_NAME`=

`API_KEY_2`=


## BUILD INSTRUCTIONS

Simple Installaton

Install FP Youtube API Project

The command below, build the complete application using docker-compose

* Redis
* Celery Worker
* Celery Beat
* FastAPI web application

```bash
  docker-compose up
```



    
## Run Locally

Clone the project

```
  git clone https://github.com/mogiiee/fp-youtube-api.git
```

Go to the project directory

```
  cd fp-youtube-api

```
Set up a virtual environment for the project:
```
python3 -m venv virtualenv
```

Install dependencies

```
  pip3 install requirements.txt
```

Go to the web_server

```
    cd web-server
```

Start the server

```bash
uvicorn app.main:app --reload
```

Go to the url 

```bash
http://localhost:8000/docs or http://127.0.0.1:8000/docs
```


## Operating Swagger

Be greeted with 4 different endpoints 

![alt text](https://cdn.discordapp.com/attachments/980468845519175743/986541393625350184/Screenshot_2022-06-15_at_1.32.04_PM.png)


* root endpoint just greets you in a wonderful way

## Insert Endpoint
* insert method is a POST request which takes 2 arguments namely "number_of_inserts" and "insert_query"
* number_of_inserts if the number of documents you want to insert in mongoDB and insert_query is what you want to search

![alt text](https://cdn.discordapp.com/attachments/980468845519175743/986542853419307048/Screenshot_2022-06-15_at_1.38.57_PM.png)

## Search Endpoint

* Search endpoint searches from the database and sends back a response in the body
* takes 3 arguments Query(which can take complex and multiple queries (BONUS POINT 3 :) )

* limit and page arguement is used to paginate the response of the endpoint

![alt text](https://cdn.discordapp.com/attachments/980468845519175743/986543937147797545/Screenshot_2022-06-15_at_1.43.16_PM.png)

## Get All Data

* Gets all the data from the database when asked for int eh 2 arguements, namely limit( how many documents you require) and page (how many pages) in a paginated format.

![alt text](https://cdn.discordapp.com/attachments/980468845519175743/986544609960276008/Screenshot_2022-06-15_at_1.45.47_PM.png)

## Default Options

- celery beat operates at every 15 seconds, can be changed
- The insert query has been set to football can be changed in worker/env.sample 
- Get your Youtube API credentials from [here](https://console.cloud.google.com/apis/credentials?project=august-shield-332408)
- Have 2 tokens in order to minimise risk of error incase of quota completion

