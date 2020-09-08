# RestApi
Find deployed version of this API here: http://pari125.pythonanywhere.com/ <br>
This API is used to retreived info from Netflix dataset. This dataset consists of tv shows and movies available on Netflix as of 2019 (Ref: https://www.kaggle.com/shivamb/netflix-shows).<br>
Manual to retrieve data:
- api/v1/resources/movies/all: To get all data
- /api/v1/resources/movies/: to filter data by passing arguments such as year (to filter release ) & type (to filter type of movies/films)
  - year are numeric variable such as 2017
  - type are movie or tv
