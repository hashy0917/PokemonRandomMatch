#!/usr/bin/python3
from flask import Flask, jsonify, make_response
import queue
import random

api = Flask(__name__)
que = queue.Queue()

@api.route('/api', methods=['GET', 'POST'])
def put_user(userName):
    if que.empty():
    # queが空の場合trueが帰る
        x = [random.randint(0, 9) for p in range(0, 8)]
        matchCode = ''.join(list(map(str, x)))
        que.put(userName)
        que.put(matchCode)
        return """{}""".format(str(matchCode))
    else:
        name = que.get()
        code = que.get()
        return """{},{}""".format(str(code),str(name))

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