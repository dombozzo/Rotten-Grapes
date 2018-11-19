# Rotten Grapes

Paradigms Final Project --
Dominic J. Bozzo, Matthew J. Malir, Ale J. Lopez, Luke J. Wurl

### Overview
Rotten Grapes is a wine recommendation system similar to the movie recommendation system Rotten Tomatoes.
Users can review a bottle of wine with a score of 0-100 and a description of the bottle.
Users can view the highest rated wines and information about these wines including the vineyard and province.

### API
The intial data comes from the dataset that can be found at https://www.kaggle.com/zynicide/wine-reviews.
The wine database consists of 3 main groups of data: users, wines, and reviews.
Users consists of a dictionary where the key is the user's id and the value is a dictionary consisting of the user's name and twitter handle.
Wines consists of a dictionary where the key is the wine's id and the value is a dictionary cosisting of information about that bottle of wine (province, region, etc.).
Finally, reviews is a dataframe that contains all of the users' reviews of the wine bottles.
Our API uses these three groupings of data to store and extract relevant information.
For each of these three groupings, the API allows for the getting, setting, and deleting of information.
We have included functions that allow us to get a specific user's review for a specific wine bottle, receive information on a specific variety (average rating for all bottles belonging to such variety, name of the variety, and a list of the wine bottles that belong to it), and even set a new review, using a specific user id and wine bottle id.

Down the road this will set up nicely for GET, PUT/POST, and DELETE calls.
We will build off of these API methods to create the RESTful web service.

### Testing
To test the API there is a test script `test_api.py` that calls the API methods from `_wine_database.py`
The python files use python3, so run the script with the following command: `python3 test_wine_db.py`.