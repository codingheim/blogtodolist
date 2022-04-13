from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb://songsooyong:<sparta>@cluster0-shard-00-00.oce1s.mongodb.net:27017,cluster0-shard-00-01.oce1s.mongodb.net:27017,cluster0-shard-00-02.oce1s.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-fc9srx-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
  return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
  name_receive = request.form["name_give"]
  comment_receive = request.form["comment_give"]

  doc = {
    'name' :name_receive,
    'comment' : comment_receive
  }
  db.homework.insert_one(doc)
  return jsonify({'msg': '응원남기기 완료!'})


@app.route("/homework", methods=["GET"])
def homework_get():
  comment_list = list(db.homework.find({},{'_id':False}))
  return jsonify({'fans': comment_list})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
