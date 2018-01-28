from flask import Flask, jsonify, render_template, request
import random
import TextRobo

app = Flask(__name__)

app.hap, app.hun, app.dis, app.sic = TextRobo.init_emots()
app.fri = TextRobo.calc_friend(app.hap, app.hun, app.dis, app.sic)

@app.route('/getRest')
def get_rest():
    app.hap += 5
    return jsonify(result=app.hap)

@app.route('/getFeed')
def get_feed():
    a = random.randint(1, 20)
    return jsonify(result=a)

@app.route('/getPlay')
def get_play():
    a = 7
    return jsonify(result=a)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
