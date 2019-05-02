from sklearn.neighbors import NearestNeighbors
from flask_cors import CORS
from flask import Flask, request
from tqdm import tqdm

import pickle
import numpy as np
import pandas as pd
import json

# initial server
app = Flask(__name__)
CORS(app)

"""
.##.....##..#######..########..########.##......
.###...###.##.....##.##.....##.##.......##......
.####.####.##.....##.##.....##.##.......##......
.##.###.##.##.....##.##.....##.######...##......
.##.....##.##.....##.##.....##.##.......##......
.##.....##.##.....##.##.....##.##.......##......
.##.....##..#######..########..########.########
"""
ratings = pd.read_csv('./data/ratings.csv')
features = pickle.load(open('./data/preprocess/processed_infos.p', 'rb'))
info = pickle.load(open( "./data/preprocess/infos_tmdb.p", "rb" ))
text = pickle.load(open('./data/preprocess/texts_gpt2.p', 'rb'))

id_features = set(features.keys())
id_info     = set(info.keys())
id_text     = set(text.keys())

id_all      = id_features.intersection(id_info).intersection(id_text)
id_all      = sorted(id_all)

ratings = ratings.loc[ratings.movieId.isin(id_all)]
counting = ratings.groupby(['movieId']).size().reset_index()
counting.columns = ['movieId', 'count']

dict_features = {}
for i in tqdm(id_all):
    tmp = {}
    tmp.update(info[i])
    tmp.update(features[i])
    tmp.update({"text": text[i]})
    dict_features[i] = tmp

def transform(obj):
    # tmp = obj['text']
    # tmp = obj['popularity']
    tmp = np.append(obj['text'], obj['popularity'])
    tmp = np.append(tmp, obj['budget'])
    tmp = np.append(tmp, obj['revenue'])
    tmp = np.append(tmp, obj['runtime'])
    tmp = np.append(tmp, obj['vote_average'])
    tmp = np.append(tmp, obj['vote_count'])
    return tmp

def __getRandom(n=6):
    # random index
    _id = id_all.copy()
    np.random.shuffle(_id)
    _id = _id[:n]
    # movies_info = list(map(lambda i: dict_features[i], _id))

    return _id

# training
X = []
for i in tqdm(id_all):
    X.append(transform(dict_features[i]))

X = np.array(X)
X[np.isnan(X)] = 0

model = NearestNeighbors(metric='cosine').fit(X)

name_all = []
for i in id_all:
    name_all.append({
        "title": str(dict_features[i]['original_title']),
        "idx": str(i)
    })

def __getSimilar(obj, n=6):
    _id = model.kneighbors([transform(obj)], n, return_distance=False)
    _id = np.array(id_all)[_id]
    return _id[0]

def __getRequest():
    try:
        req = json.loads(request.data.decode('utf-8'))
        return req
    except:
        return None

def __getInfo(_id):
    data   = dict_features[_id]
    poster = 'http://image.tmdb.org/t/p/original' + data['poster_path']
    link   = data['homepage']
    title  = data['original_title']
    return {
        "title": title,
        "link": link,
        "poster": poster
    }
def __getPopular(n=5):
    _id = counting.sort_values('count', ascending=False)['movieId'].head().values
    return _id

"""
.########...#######..##.....##.########.########
.##.....##.##.....##.##.....##....##....##......
.##.....##.##.....##.##.....##....##....##......
.########..##.....##.##.....##....##....######..
.##...##...##.....##.##.....##....##....##......
.##....##..##.....##.##.....##....##....##......
.##.....##..#######...#######.....##....########
"""


@app.route('/getNames', methods=['GET', 'POST'])
def getNames():
    # print('Get Names')
    return json.dumps({
        "list_name": name_all
    })

@app.route('/getSimilar', methods=['GET', 'POST'])
def getSimilar():
    '''
        {
            id: xxx
        }
    '''
    # print('getSimilar')
    req = __getRequest()
    _id = __getSimilar(dict_features[int(req['id'])])
    results = list(map(__getInfo, _id))
    # print(results)
    return json.dumps({
        "result": results
    })

@app.route('/getRandom', methods=['GET', 'POST'])
def getRandom():
    _id = __getRandom(10)
    results = list(map(__getInfo, _id))
    return json.dumps({
        "result": results
    })

@app.route('/getPopular', methods=['GET', 'POST'])
def getPopular():
    _id = __getPopular(5)
    results = list(map(__getInfo, _id))
    return json.dumps({
        "result": results
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
