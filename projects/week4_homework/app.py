from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order():
    # 1. 클라이언트로부터 데이터를 받기
    name = request.form['name']
    count = request.form['count']
    addr = request.form['addr']
    phoneNum = request.form['phoneNum']

    orderInfo = {
        'name': name,
        'count': count,
        'addr': addr,
        'phoneNum': phoneNum
    }
    db.orders.insert_one(orderInfo)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})

# API 역할을 하는 부분


@app.route('/order', methods=['GET'])
def viewOrder():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders':orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
