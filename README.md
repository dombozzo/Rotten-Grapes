# Rotten Grapes

Paradigms Final Project --
Dominic J. Bozzo, Matthew J. Malir, Ale J. Lopez, Luke J. Wurl

### Overview
Rotten Grapes is a wine recommendation system similar to the movie recommendation system Rotten Tomatoes.
Users can add bottles of wine to review and review the wines with a score of 0-100 and a description of the bottle.
Users can view the highest rates wines and information about these wines including the vineyard and province.

### API
The intial data comes from the dataset that can be found at https://www.kaggle.com/zynicide/wine-reviews.
The wine database consists of 3 main groups of data: users, wines, and reviews.
Users consists of a dictionary where the key is the user's id and the value is a dictionary consisting of the user's name and twitter handle.
Wines consists of a dictionary where the key is the wine's id and the value is a dictionary cosisting of information about that bottle of wine.
Finally, reviews is a dataframe the contains all of the reviews of wine bottles from all users.
Our API uses these three groupings of data to store and extract relevant information.
For each of these three groupings, the API allows for the getting, setting, and deleting of information.
Down the road this will set up nicely for GET, PUT/POST, and DELETE calls.
We will build off of these API methods to create the RESTful web service.

### Testing
To test the API there is a test script `test_wine_db.py` that calls the API methods from `_wine_database.py`
The python files use python3, so run the script like: `python3 test_wine_db.py`.