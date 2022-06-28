# 파이썬 Flask 사용법 : https://hleecaster.com/flask-introduction/

import json
import flask
from flask import Flask, render_template, request
import my_text
import numpy as np

app = Flask(__name__)

# Flask에서는 URL을 방문 할 때 준비된 함수가 트리거되도록 바인딩 하기 위해 route() 데코레이터를 사용
# @app.route('/경로') 를 쓸 때 URL 경로는 반드시 “/” (슬래시)로 시작해야 한다.


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=['GET'])
def api():
    # URL 매개 변수 추출하기 --- (*3)
    q = request.args.get('q', '')
    if q == '':
        return '{"label": "내용을 입력해주세요", "per":0}'
    print("q=", q)
    # 텍스트 카테고리 판별하기 --- (*4)
    label, per, no = my_text.check_genre(q)
    # 결과를 JSON으로 출력하기
    return json.dumps({
        "label": label,
        "pre": np.round(per, 2)*100,
        "genre_no": no
    })


if __name__ == "__main__":
    app.run(debug=True)
