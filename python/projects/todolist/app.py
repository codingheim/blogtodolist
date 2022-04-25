from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import certifi
from datetime import datetime


ca = certifi.where()
app = Flask(__name__)

client = MongoClient(
    'mongodb://songsooyong:ausehskf4$@cluster0-shard-00-00.oce1s.mongodb.net:27017,cluster0-shard-00-01.oce1s.mongodb.net:27017,cluster0-shard-00-02.oce1s.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-fc9srx-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('calendar.html')

@app.route('/todo/calendar',methods=['POST'])
def calendar_post():
    date_receive = request.form['date_give']
    num_receive = request.form['num_give']
    todo_receive = request.form['todo_give']
    done_receive = request.form['done_give']


    doc = {
        'date':date_receive,
        'num':num_receive,
        'todo':todo_receive,
        'done':done_receive,
    }

    db.todo_percent.insert_one(doc)

    return jsonify({'msg':'응원완료'})


@app.route('/todo/calendar', methods=['GET'])
def calendar_get():
    todo_list = list(db.todo_percent.find({}, {'_id': False}))
    return jsonify({'todos': todo_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
