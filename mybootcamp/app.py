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

@app.route('/createteam')
def createteam():
  return render_template('createteam.html')

@app.route('/nationalteam')
def nationalteam():
  return render_template('nationalteam.html')

@app.route('/nationalteam')
def national_cheer_post():
  nickname_receive = request.form['nickname_give']
  player_receive = request.form['player_give']
  comment_receive = request.form['comment_give']

  doc = {
    'nickname': nickname_receive,
    'player':player_receive,
    'comment':comment_receive
  }

  db.nationalteam.insert_one(doc)

  return jsonify({'msg':'응원 완료!'})

@app.route('/nationalteam', methods=["GET"])
def national_cheer_get():
  national_cheer_list = list(db.nationalteam.find({},{'_id' : False}))
  return jsonify({'players': national_cheer_list})


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

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
