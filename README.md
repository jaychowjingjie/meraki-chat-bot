# Base Spark Bot framework using Ngrok

This is a base Spark Bot framework that you can use to start a Spark Bot project if you are developing on your local machine. Ngrok is used to establish a tunnel to your local Spark Bot application. There is no need to update the webhook manually each time you launch ngrok. The application does that for you automatically.

The application does not have any business logic defined, you will have to add it. When a new message is posted to the Bot, it will simply be displayed on the terminal.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
* [ngrok](http://ngrok.com) - Tunneling utility that exposes local servers behind NATs and firewalls to the public internet over secure tunnels.
* [Python 3.x](http://www.python.org) - Python interpreter
* [Flask](http://flask.pocoo.org/)  - Flask is a microframework for Python based on Werkzeug and Jinja 2
* Spark Bot - create a spark bot. See https://developer.ciscospark.com/bots.html
* Spark webhook - create a webhook using your Bot's token. See https://developer.ciscospark.com/webhooks-explained.html


### Installing

Download and extract [ngrok](http://ngrok.com/download). Then launch it.

```
$ ./ngrok http 8080
```

Install [Flask](http://flask.pocoo.org/) framework for Python using pip.

```
$ pip install Flask
```

Rename `settings_template.py` file to `settings.py` and update the variables - `bot_token`, `bot_id`, `webhook_name`, `webhook_id`. If you choose to run ngrok on a different machine, you should update the `ngrok_url` variable.

Launch the Python application. Remember to run ngrok on 8080 first, then launch the bot. Then interact with the bot on webex teams.
```
$ python3 app.py
```

On Spark, create a 1-1 room with the Spark Bot, and start posting messages in that room. You will notice the posted messages being printed by your application on the terminal.


## Authors

* **Hantzley Tauckoor** - [linkedin](http://linkedin.com/in/hantzley) [@hantzley](http://twitter.com/hantzley)
