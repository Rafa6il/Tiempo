## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is a simple weather forecast web service based on Flask and a python script which accesses to this service.

The web service is setup on app.py. The script takes the user query and sends it to openweathermap.com to get the
current temperature from the city the user has chosen. All query responses are JSON objects.

Query.py is the client script that creates the query for the forecast service.
	
## Technologies
Project is created with:
* Python 3.9.5
* Flask==2.0.1
* pyowm==3.2.0
	
## Setup
To run this project, install the dependencies locally using freeze:

```
$ cd ../tiempo
$ pip install -r requirements.txt
```