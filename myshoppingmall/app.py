from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def homework():
   return render_template('index.html')

## 주문 목록 가져오기(Read) API
@app.route('/order', methods=['GET'])
def listing():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})

## 주문을 목록에 추가하기(POST) API
@app.route('/order', methods=['POST'])
def saving():
    # 1. 클라이언트에게 데이터 받기
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    # 2. mongoDB에 데이터 넣기
    doc = {
        'name': name_receive,
        'count' : count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg':'주문이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)