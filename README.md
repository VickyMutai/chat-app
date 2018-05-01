# Chat App api

### Prerequisites

###### Requirements

Python 3.6.3


### Installing
Create virtual
- python3.6 -m venv virtual
Activate virtual
- source/bin/activate

#### Install all the requirements
- pip install -r requirements.txt

#### Databases
for postgresql users;
  * Go to settings;
    - Change user,password, name(database name) on the database settings.
for sqlite users;
  * Go to settings;
    - replace the database section with the following;
        - DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
      

### Make migrations
- python manage.py makemigrations
- python manage.py migrate

#### Run application
- python manage.py runserver

#### Testing API endpoints
##### Authentication

For this functionality we used [Djoser](http://djoser.readthedocs.io/en/latest/introduction.html) - REST implementation of Django authentication system. It handles all the auth/ endpoints.
Example

Creating a new user
```
$ curl -X POST http://127.0.0.1:8000/auth/users/create/ --data 'username=mike&password=siliconvalley'
{"email": "", "username": "mike", "id": 1}
```

To access the user details
```
$ curl -X GET http://127.0.0.1:8000/auth/me/
{"detail": "Authentication credentials were not provided."}
```
The error is because we didn't provide the token which is required for all app/ endpoints. To generate a token we do

```
$ curl -X POST http://127.0.0.1:8088/auth/token/create/ --data 'username=mike&password=siliconvalley'
{"auth_token":"bc968ac5c0410b3e83b81805d804438a5c2425d3"}
```
We can now use the token for all the other endpoints. Running the same request again: 

```
$ curl -X GET http://127.0.0.1:8000/auth/me/ -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3'
{"email":"","id":4,"username":"mike"}
```
##### Chat
Aside from the auth/ endpoints which handle authentification. We have two main API views
- ChatView. Accepts POST and PATCH requests. For creating chat groups/rooms
- ChatMessageView. Accepts GET and POST requests. For sending and getting messages to/from a chat group.

Using the user we created and token given we can create a chat group and send messages to it.
Creating a chat group:

```
curl -X POST http://127.0.0.1:8000/app/chats/ -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3'
{"message":"New room created","uri":"bf9116670fae470","status":"SUCCESS"}
```
The uri is a random string generated that uniquely identifies each chat room. To get messages from the chat room

```
curl -X GET http://127.0.0.1:8000/app/chats/bf9116670fae470/messages -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3'
```
It doesn't return anything since no messages have been sent to that particular chat room. To send a message

```
$ curl -X POST http://127.0.0.1:8000/app/chats/bf9116670fae470/messages/ -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3' --data message="The force is strong"
{"message":"The force is strong","user":{"id":4,"username":"mike","email":""},"uri":"bf9116670fae470","status":"SUCCESS"}
```
And another one

```
curl -X POST http://127.0.0.1:8000/app/chats/bf9116670fae470/messages/ -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3' --data message="Phantom Menace was the best"
{"message":"Phantom Menace was the best","user":{"id":4,"username":"mike","email":""},"uri":"bf9116670fae470","status":"SUCCESS"}
```
Using the uri for the chat room we can get all the messages sent there like so

```
curl -X GET http://127.0.0.1:8000/app/chats/bf9116670fae470/messages -H 'Authorization: Token bc968ac5c0410b3e83b81805d804438a5c2425d3'
{"messages":[{"user":{"id":4,"username":"mike","email":""},"message":"The force is strong"},{"user":{"id":4,"username":"mike","email":""},"message":"Phantom Menace was the best"}],"id":10,"uri":"bf9116670fae470"}
```
