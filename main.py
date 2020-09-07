import pandas as pd
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

Netflix = pd.read_csv('data/netflix_titles.csv')

@app.route('/', methods=['GET'])
def home():
    return "<h1>TV Shows and Movies listed on Netflix</h1>" \
           "<p>This dataset consists of tv shows and movies available on Netflix as of 2019. </p>" \
           "<p>Ref: https://www.kaggle.com/shivamb/netflix-shows </p>"

@app.route('/api/v1/resources/movies/all',methods=['GET'] )
def api_all():
    return Netflix.to_dict(orient='index')

@app.route('/api/v1/resources/movies/',methods=['GET'] )
def api_filter():
    yr = ''
    movie_type = ''

    if 'year' in request.args:
        yr = int(request.args['year'])

    if 'type' in request.args:
        movie_type = request.args['type']

    results = Netflix
    if (movie_type=='' and yr == ''):
        return 'Error, please provide at least one parameter for filter (year, type)'
    else:
        if yr!='':
            results = results.loc[results.release_year == yr]
        if movie_type!='':
            if movie_type == 'movie':
                results = results.loc[results.type == 'Movie']
            elif movie_type == 'tv':
                results = results.loc[results.type == 'TV Show']

    return results.to_dict(orient='index')

app.run()