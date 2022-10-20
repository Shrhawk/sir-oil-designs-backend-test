# Sir-oil Designs Backend Test

## Features

+ Python FastAPI backend.
+ Database Design(MongoDB).
+ Authentication
+ User Feed( According to location and old activities)

## Using the applications

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```shell
 python3 -m venv venv
```

2. Install the modules listed in the `requirements.txt` file and pre-commits for code quality

```shell
pip3 install -r requirements.txt
pre-commit install
```

3. Create a `.env` file in the root directory of the project and add the following variables:

```shell
DATABASE_URL=<database_url>
secret_key=<secret_key>
```

4. Run the mongo using docker:

```shell
docker run -d --name daisy-db -p 27012:27017 mongo
```

5. Start the application:

```shell
python main.py
```

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080).

6. Problem 1 Database Design ERD:

![ERD Diagram](Final ERD.png)

7. Problem 2 User Feed: Post will be shown according to user location and its old activities e.g: likes and played games etc.
8. Add Dummy Data: it will create dummy users, events, games etc.
   1. Request:
      ```shell
       curl -X 'GET' 
       'http://0.0.0.0:8080/initiate_data' 
       -H 'accept: application/json' 
       ```
   2. Response
      ```json
      {
         "message": "Initial data created"
      }
      ```
9. Login: to get access token
   1. Request:
      ```shell
       curl -X 'POST' 
      'http://0.0.0.0:8080/user/login' 
      -H 'accept: application/json' 
      -H 'Content-Type: application/json' 
      -d '{
      "username": "string1",
      "password": "string1"
      }'
       ```
   2. Response
      ```json
      {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjM1MTVjYzVmYzM4MjJlNTdkNjM1NDdiIiwiZXhwaXJlcyI6MTY2NjI3ODk2My41NDA4MzF9.mkaeQWh79DByLOFCOg_hO9YnYST60v01UVV6pfUGIOE"
      }
      ```
10. SignUp: to create new user
    1. Request:
       ```shell
        curl -X 'POST' 
         'http://0.0.0.0:8080/user/user_signup' 
         -H 'accept: application/json' 
         -H 'Content-Type: application/json' 
         -d '{
         "created_on": "2022-10-20T19:35:36.302728",
         "updated_on": "2022-10-20T19:35:36.302735",
         "username": "string",
         "email": "user@example.com",
         "password": "string",
         "bio": "string",
         "loc": [0]
       }'
        ```
       2. Response
          ```json
          {
            "created_on": "2022-10-20T19:35:36.302728",
            "updated_on": "2022-10-20T19:35:36.302735",
            "username": "string",
            "email": "user@example.com",
            "bio": "string",
            "loc": [0],
            "id": "string"
          }
          ```
11. User Details: to get user details like its information, events posted, game played etc 
    1. Request:
          ```shell
           curl -X 'POST' 
            'http://0.0.0.0:8080/user/user_signup' 
            -H 'accept: application/json' 
            -H 'Content-Type: application/json' 
            -d '{
            "created_on": "2022-10-20T19:35:36.302728",
            "updated_on": "2022-10-20T19:35:36.302735",
            "username": "string",
            "email": "user@example.com",
            "password": "string",
            "bio": "string",
            "loc": [0]
          }'
           ```
    2. Response
       ```json
       {
         "created_on": "2022-10-20T19:35:36.302728",
         "updated_on": "2022-10-20T19:35:36.302735",
         "username": "string",
         "email": "user@example.com",
         "bio": "string",
         "loc": [0],
         "id": "string"
       }
       ```
12. User Feed: Post will be shown according to user location and its old activities e.g: likes and played games etc.
    1. Request
        ```shell
         curl -X 'POST'
         'http://0.0.0.0:8080/post/user_feed'
         -H 'accept: application/json'
         -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjM1MTVjYzVmYzM4MjJlNTdkNjM1NDdiIiwiZXhwaXJlcyI6MTY2NjI3ODk2My41NDA4MzF9.mkaeQWh79DByLOFCOg_hO9YnYST60v01UVV6pfUGIOE'
         -d '' 
       ```
    2. Response
       ```json
       [
         {
           "created_on": "2022-10-20T14:36:20.629Z",
           "updated_on": "2022-10-20T14:36:20.629Z",
           "title": "string",
           "description": "string",
           "status": "string",
           "loc": [0],
           "user_id": "string",
           "total_likes": 0,
           "details": {
             "created_on": "2022-10-20T14:36:20.629Z",
             "updated_on": "2022-10-20T14:36:20.629Z",
             "title": "string",
             "description": "string",
             "location": "string",
             "date": "string",
             "time": "string",
             "public": true,
             "user_id": "string",
             "game_id": "string"
           }
         }
       ]
       ```
![API Swagger](API Swagger.png)
