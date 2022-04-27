from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient(
  'mongodb://songsooyong:ausehskf4$@cluster0-shard-00-00.oce1s.mongodb.net:27017,cluster0-shard-00-01.oce1s.mongodb.net:27017,cluster0-shard-00-02.oce1s.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-fc9srx-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
  return render_template('mainindex.html')

@app.route('/teaminfo')
def teaminfo():
  return render_template('teaminfo.html')

@app.route('/player', methods=["POST"])
def player_post():
  name_receive = request.form['name_give']
  address_receive = request.form['address_give']
  position_recevice = request.form['position_give']
  tellnum_recevice = request.form['tellnum_give']

  doc = {
    'name' : name_receive,
    'address': address_receive,
    'position' :position_recevice,
    'tellnum' : tellnum_recevice
  }
  db.playersinfo.insert_one(doc)

  return jsonify({'msg':'선수등록완료'})

@app.route('/player', methods=["GET"])
def player_get():
  player_list = list(db.playersinfo.find({},{'_id' : False}))
  return jsonify({'players': player_list})


@app.route('/createteam')
def createteam():
  return render_template('createteam.html')

@app.route('/registerteam', methods=['POST'])
def team_post():
  name_receive = request.form['name_give']
  people_receive = request.form['people_give']
  age_receive = request.form['age_give']
  league_receive = request.form['league_give']
  tellnum_receive = request.form['tellnum_give']

  doc = {
    'name':name_receive,
    'people':people_receive,
    'age':age_receive,
    'league':league_receive,
    'tellnum':tellnum_receive
  }
  db.createteam.insert_one(doc)
  return jsonify({'msg':'팀등록 완료!'})

@app.route('/registerteam', methods=['GET'])
def team_get():
  team_list = list(db.createteam.find({}, {'_id': False}))
  return jsonify({'team': team_list})


@app.route('/nationalteam')
def nationalteam():
  return render_template('nationalteam.html')

@app.route('/teamcheer' ,methods=['POST'])
def national_cheer_post():
  nickname_receive = request.form['nickname_give']
  player_receive = request.form['player_give']
  comment_receive = request.form['comment_give']

  doc = {
    'nickname': nickname_receive,
    'player': player_receive,
    'comment': comment_receive
  }

  db.nationalteam.insert_one(doc)

  return jsonify({'msg':'응원 완료!'})

@app.route('/teamcheer', methods=["GET"])
def national_cheer_get():
  national_cheer_list = list(db.nationalteam.find({},{'_id' : False}))
  return jsonify({'cheer_list': national_cheer_list})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
