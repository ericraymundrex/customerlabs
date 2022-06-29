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
├── account
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── customerlabs
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── settings.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── wsgi.cpython-39.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── data_handler
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── destination
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── admin.cpython-39.pyc
│   │   ├── apps.cpython-39.pyc
│   │   ├── models.cpython-39.pyc
│   │   ├── serializers.cpython-39.pyc
│   │   ├── urls.cpython-39.pyc
│   │   └── views.cpython-39.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-39.pyc
│   │       └── __init__.cpython-39.pyc
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```
