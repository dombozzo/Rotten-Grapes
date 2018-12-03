# Rotten Grapes

Paradigms Final Project --
Dominic J. Bozzo, Matthew J. Malir, Ale J. Lopez, Luke J. Wurl

REPO LINK: https://gitlab.com/dbozzo/rotten-grapes.git

### Overview
Rotten Grapes is a wine recommendation system similar to the movie recommendation system Rotten Tomatoes.
Users can review a bottle of wine with a score of 0-100 and a description of the bottle.
Users can view the highest rated wines and information about these wines including the vineyard and province.
This document outlines our API, Web Service, and Web Client in detail, and is followed by a summary of steps for executing the Rotten Grapes system.

### API
The initial data comes from the dataset that can be found at https://www.kaggle.com/zynicide/wine-reviews.
The wine database consists of 3 main groups of data: users, wines, and reviews.
Users consists of a dictionary where the key is the user's id and the value is a dictionary consisting of the user's name and twitter handle.
Wines consists of a dictionary where the key is the wine's id and the value is a dictionary cosisting of information about that bottle of wine (province, region, etc.).
Finally, reviews is a dataframe that contains all of the users' reviews of the wine bottles.
Our API uses these three groupings of data to store and extract relevant information.
For each of these three groupings, the API allows for the getting, setting, and deleting of information.
We have included functions that allow us to get a specific user's review for a specific wine bottle, receive information on a specific variety (average rating for all bottles belonging to such variety, name of the variety, and a list of the wine bottles that belong to it), and even set a new review, using a specific user id and wine bottle id.

Down the road this will set up nicely for GET, PUT/POST, and DELETE calls.
We will build off of these API methods to create the RESTful web service.

### Testing the API
To test the API there is a test script `test_api.py` located at `/tests/api/test_api.py` that calls the API methods from `_wine_database.py`
The python files use python3, so run the script with the following command: `python3 test_api.py` from the proper directory.


### Using the Web Service
Our cherrypy server is available on port # `52087` -> http://student04.cse.nd.edu:52087

PLEASE REMEMBER TO START THE SERVER `python3.6 main.py` IN MAIN DIRECTORY PRIOR TO MAKING ANY REQUESTS.

The web service can be accessed by making HTTP GET, POST, PUT, & DELETE requests to the resources specified in
RESTful JSON specification table (please refer to file restful_json_specification.pdf). Please note that our resources do not maintain functionality beyond what is
mentioned in the table (i.e. not all resources support all request types).

For example, to get information about a specific user, follow this format:

    r = requests.get('http://student04.cse.nd.edu:52087/users/'+ str(user_id)))

In general, follow this format to access (and interact) with our resources:

    GET/POST/PUT/DELETE to 'http://student04.cse.nd.edu:52087/' + resource [+ key + body]

To test our resources, we have included a suite of python files (within `tests/server` directory). For your
convenience, we have included a file named `test_ws.py`, which will simultaneously launch all unit tests. Do this
simply by running the command `./test_ws.py` in your `tests/server` directory. If you wish to test a specific resource, please run the appropriate file within the `tests/server` dir.


### Interacting with the Web Client
Once the server is running, one can utilize the web client by navigating to `http://student04.cse.nd.edu/lwurl/grapes/` in your favorite browser.

At this screen, the user is greeted with a playful photo of the Rotten Grapes founders upon entry to the site. 
The user will then be able to log in in the top left corner, or create a new profile if they are new to the site. Then, they can search by variety_id in the top right
corner. This will search through our reviews database to present the user with the top rated wines in this variety. For example, the user can view the best
Pinot Noir's by searching for variety number 690. Due to limitations of the JSON interpreter provided to us for our javascript code, we were unable to implement
this search by name. This is simply because the JSON iterpreter was unable to process some special characters from our data set. 

Once the user queries for a variety, they can view more information about a specific wine by clicking "More Information" under each wine that pops up. This can be done for each wine.
As always, the user can log in and log out to preserve their sessions on Rotten Grapes.

To test the web client, we ensured that the user interface produced the same visual output that our test scripts for the api and the server produced. From this, we were able
to catch a vital error in the POST functionality of our reviews resource. We were eventually able to verify that all of the functionality works as anticipated. Our 
javascript code simply served to call functions which were already tested in our api and server tests, so this result was expected.


## Summary: Steps for Execution
1. Clone this repository
2. Start the server by executing the command `python3.6 main.py` where python3.6 points to /afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python
3. Navigate on your browser of choice to `http://student04.cse.nd.edu/lwurl/grapes/`
4. Interact as you please! 
