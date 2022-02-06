# Spekit_Task
### Django Server Application.

#### Django Admin dashboard credentials
email: admin@spekit.com
username: admin
password: 123456789#

## Steps to Setup and Run Server
1. Run 'python manage.py makemigrations' and then 'python manage.py migrate'.
2. Dump seed data into database by running the command 'python manage.py loaddata data\data_to_dump.json'. It will dump some sample data into database
3. Run the server 'python manage.py runserver'.

## About Structure.
It is Django server application. I have created three apps for different tables.

Apps:
1. folders
2. documents
3. topics

Models, Views, Serializers and Urls are implemented in each app.
Link to Postman collection with sample API's https://www.getpostman.com/collections/a1a229e59d3fc5f7c20e.

## API Endpoints
### 1. Folders
1. get all folders.
GET {domain}/folders/ returns all folders
2. Add Folder.
POST {domain}/folders/ Add new folder with provided topic.
Sample Request Data.
{
    "name": "client feedback1",
    "info": "default folder",
    "icon": "default icon",
    "topics" : [
        1,
        4
    ]
}
3. Get Folders of provided topic.
GET {domain}/folders/topic_folders/?topic=policy

### 2. Documents
1. get all docments.
GET {domain}/documents/ returns all documents
2. Add Document.
POST {domain}/documents/ Add new document with provided topic and folder.
Sample Request Data.
{
    "name": "widget details",
    "type": "pdf",
    "size": "2 mb",
    "folder": 1,
    "topics" : [
        5,
        3
    ]
}
3. Get Documents of provided folder and topic. i.e get all the documents of folder "default" with topic "policy".
cases:
http://127.0.0.1:8000/documents/topic_documents/?folder=default&topic=policy
http://127.0.0.1:8000/documents/topic_documents/?folder=default
http://127.0.0.1:8000/documents/topic_documents/?topic=policy

### 3. Topics
1. get all topics.
GET {domain}/topics/ returns all topics
2. Add Topic.
POST {domain}/topics/ Add new topic.
Sample Request Data.
{
    "name": "widget",
    "short_description": "policy short desc",
    "long_description": "policy long description"
}
3. Get All Topic of folder or document.
cases:
http://127.0.0.1:8000/topics/object_topics/?document=leave%20policy
http://127.0.0.1:8000/topics/object_topics/?folder=default

## Database
There are total 5 tables.
1. Folder
2. Document
3. Topic
4. FolderTopic (Bridge Table of Folder and Topic)
5. DocumentTopic (Bridge Table of Document and Topic)