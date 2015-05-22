![python](https://img.shields.io/badge/python-2.7%2C%203.x-blue.svg) ![python](https://img.shields.io/badge/django-1.7-blue.svg) [![Scrutinizer Build pass](https://scrutinizer-ci.com/g/Deathangel908/djangochat/badges/build.png)](https://scrutinizer-ci.com/g/Deathangel908/djangochat) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Deathangel908/djangochat/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Deathangel908/djangochat/?branch=master) [![Code Health](https://landscape.io/github/Deathangel908/djangochat/master/landscape.svg?style=flat)](https://landscape.io/github/Deathangel908/djangochat/master) [![Codacy Badge](https://www.codacy.com/project/badge/b508fef8efba4a5f8b5e8411c0803af5)](https://www.codacy.com/public/nightmarequake/djangochat)
Web chat based on WebSockets.
================================================

Basically written in **Python** with [django](https://www.djangoproject.com/) it uses asynchronous web framework [Tornado](http://www.tornadoweb.org/) for handling realtime messages. Broadcasting messages are being sent by means of [redis](http://redis.io/) [pub/sub](http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) feature using Python [tornado-redis](https://github.com/leporo/tornado-redis) backend. It can be run on both **Windows** and **Linux** and tested on **Python 2.7** and **Python 3.x**

Get dependencies:
================
 1. *Python2.7* or *Python 3.x* both are supported
 2. *pip* for getting dependencies
 3. *redis* for holding session and pubsub messages
 3. Download static content such as jquery...
 4. Create the database

Windows:
 1. Install python with pip https://www.python.org/downloads/
 2. Add pip and python to PATH variable
 3. Open cmd as Administrator and run `pip install -r requirements.txt`
 4. Install redis from https://github.com/rgl/redis/downloads
 5. Unzip static content to story/static directory https://www.dropbox.com/sh/p9efgb46pyl3hj3/AABIDVckht4SGZUDAnU7dlD7a?dl=1
 6. Open cmd and run `python manage.py init_db` from project directory

Ubuntu:
 1. `apt-get install python`
 2. `apt-get install pip`
 3. `add-apt-repository -y ppa:rwky/redis` `apt-get install -y redis-server`

Archlinux:
 1. `pacman -S python`
 2. `pacman -S pip`
 3. `pacman -S community/redis`

Next steps are common for Linux:
 4. `pip install -r requirements.txt`
 5. `sh download_content.sh`
 6. `python manage.py init_db`

Start the chat:
==============
 1. Start session holder: `redis-server`
 2. Start WebSocket listener: `python manage.py start_server`
 3. Start the Chat: `python manage.py runserver 0.0.0.0:80000`

#TODO
* USE init or on_open
* show system messages on navbar
* allow to edit username for anonymous
* don't refresh userlist on closing tab if there's an open tab 
* remove connections set, there's a lot of issues like when user close a single tab, and there're still open websockets but the user is missing frm list already
* user private messages sent only to single websocket got by username, thus a user missed messages if there're 2+ tabs
* show if user's reconnecting
* since post to 10 getmessages loads 1st, username is not set and self messages writes as others colors
* tornadoi2
* add logger
* deploy on server
* right room width (add space to roght size from scroll if userdlist is closed)
* on start 10 messages includes foreign private ones 
* timezone
* show gender icon in userlist 
* make login dropdown smaller
* check profile save button uses only bootsrap
* add chat rooms
* implement smiles
* Gradient text disappear on top