# Rotten Grapes

Paradigms Final Project --
Dominic J. Bozzo, Matthew J. Malir, Ale J. Lopez, Luke J. Wurl

REPO LINK: https://gitlab.com/dbozzo/rotten-grapes.git

### Overview
Rotten Grapes is a wine recommendation system similar to the movie recommendation system Rotten Tomatoes.
Users can review a bottle of wine by providing a score of 0-100 and a justification for doing so.
Users can view the highest rated wines and information about these wines including the vineyard, province, price, etc.
This document outlines our API, Web Service, and Web Client in detail, and is followed by a summary of steps for interacting with the Rotten Grapes system.

### API
The initial data comes from a csv file that can be found at https://www.kaggle.com/zynicide/wine-reviews.
Our database consists of 3 main data categories: users, wines, and reviews.
Users is stored as a dictionary where the key is the user id and the value is a dictionary consisting of the user's name and twitter handle.
Wines is stored as a dictionary where the key is the wine id and the value is a dictionary consisting of information about that bottle of wine (province, region, etc.).
Finally, reviews is stored as a dataframe that contains all of the users' reviews of the wine bottles (1 row per review).
Our API uses these three groupings of data to store and extract relevant information.
For each of these three groupings, the API allows for the getting, setting, and deleting of information.
We have included functions that allow us to get a specific user's review for a specific wine bottle, receive information on a specific variety (average rating for all bottles belonging to such variety, name of the variety, and a list of the wine bottles that belong to it), and even set a new review, using a specific user id and wine bottle id.

These functions are later utilized to execute GET, PUT/POST, and DELETE calls and create the RESTful web service.

### Testing the API
To test the API there is a test script `test_api.py` located at `/tests/api/test_api.py` that calls the API methods from `_wine_database.py`
The python files use python3, so run the script with the following command: `python3 test_api.py` from the proper directory.


### Using the Web Service
Our cherrypy server is available on port # `52087` -> http://student04.cse.nd.edu:52087

PLEASE REMEMBER TO START THE SERVER `python3.6 main.py` IN MAIN DIRECTORY PRIOR TO MAKING ANY REQUESTS.

The web service can be accessed by making HTTP GET/POST/PUT/DELETE requests to the resources specified in the
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
Once the server is running, one can utilize the web client by navigating to http://student04.cse.nd.edu/lwurl/grapes/ in your favorite browser.

The user is immediately greeted by a playful photo of the Rotten Grapes dev team. 
The user will then be able to sign in at the top left corner, or create a new user profile if they so choose. 
The user can now 1) search by variety id 2) create a new review 3) sign out. 

1) A search by variety id will present the user with the top rated wines in the specified variety (listed by score in descending order). 
For example, the user can view the best Pinot Noir's by searching for variety number 690. We planned to implement the query by name rather than by id, but
the database contains special characters (accent marks, etc.) that cannot be processed by the javascript JSON interpreter.
Once the user queries for a variety, they can view more information about a specific wine by clicking "More Information" under each wine that pops up. This can be done for each wine.

NOTE: search box is in top right corner

2) To create a review, simply click the create review button. This will open a form where bottle id, score, and description can all be entered.
Once the review is submitted, try searching by variety id to find your review!

NOTE: create review button is in top right corner

3) The user can log in and log out to preserve his/her sessions on Rotten Grapes.

NOTE: sign in/out button in top left corner

To test the web client, we verified that the UI produced the same output as our test scripts for the api and the server. 
During the UI testing process, we were able to catch (and fix) a critical error in the POST functionality of our reviews resource. 
We were eventually able to conclude that all functionalities of UI work as expected. 
Since our javascript code simply served to call functions that had already been tested in earlier stages of development, 
few errors were found when testing the UI.


## Summary: Steps for Execution
1. Clone this repository
2. Start the server by executing the command `python3.6 main.py` where python3.6 points to /afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python
3. Navigate on your browser of choice to http://student04.cse.nd.edu/lwurl/grapes/
4. Interact as you please! 
