### customerlabs

#### To run the Project:
To run in localhost:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

To run in Docker:
```
docker build .
docker run <Container_id>
```

#### REST End Points:
Find ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) collection here: [Click Here](https://github.com/ericraymundrex/customerlabs/blob/main/Postman_test_cases.postman_collection.json)
|Purpose| End Point | Request Type | Body | Header |
|--------|-----------|--------------|-------|--------|
|Account|http://127.0.0.1:8000/account/| GET/POST | ```{"email_id": "","account_name": "","website": ""}```| NA|
|Account|http://127.0.0.1:8000/account/<account_id>| GET/DELETE | NA| NA|
|Destination|http://127.0.0.1:8000/Destination/| POST | ```{"destination_url": "","HTTP_methos_for_destination": ""}```| ```app-id:"" , app-sectet: ""```|
|Destination|http://127.0.0.1:8000/Destination/| GET | NA| NA|
|Destination|http://127.0.0.1:8000/Destination/<pk_destination>| GET/DELETE | NA| NA|
|Incomming Data|http://127.0.0.1:8000/server/incoming_data/| POST |```{"data1":"","data2":""}```| ```"cl-x-token":""```|


File Structure
```
customerlabs
├── Dockerfile
├── account          [App]
├── customerlabs     [Project]
├── data_handler     [App]
├── db.sqlite3       [Sample Database - have all data in POSTMAN]
├── destination      [App]
├── manage.py
└── requirements.txt
```
