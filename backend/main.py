#!/usr/bin/python3
from flask import Flask, jsonify, make_response, request
import queue
import random

que = queue.Queue()
api = Flask(__name__)

@api.route('/api/v1', methods=['POST'])
def post():
    myname = request.get_data()
    print(myname)
    if que.empty():
        x = [random.randint(0, 9) for p in range(0, 8)]
        matchCode = ''.join(list(map(str, x)))
        que.put(myname)
        que.put(matchCode)
        return make_response(jsonify({"name":"自分の名前"+str(myname.decode("utf-8")),"code":str(matchCode)}), 202)
    else:
        name = que.get()
        code = que.get()
        return make_response(jsonify({"name":"あいての名前"+str(name.decode("utf-8")),"code":str(code)}), 202)

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)

"""
<h1>あなたのあいことばは {} です。</h1>
<h1>マッチングまでしばらくお待ちください。</h1>
"""

"""
<h1>対戦相手が見つかりました。</h1>
<h1>相手のトレーナー名は {} です</h1>
<h1>あいことばは {} です</h1>
"""