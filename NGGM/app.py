from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbEx                     # 'dbEx'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/list')
def list_page():
   return render_template('list.html')

@app.route('/api/view', methods=['GET'])
def count_ex():
   count_ex = db.exDB.count()
   return jsonify({'result': 'success','count_ex':count_ex})

@app.route('/api/list_view', methods=['GET'])
def view_ex_list():
   ex_list = list(db.exDB.find({},{'_id':False, 'exImg':True, 'exTitle':True}))
   return jsonify({'result': 'success','ex_list':ex_list})

if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)