from flask import Flask, jsonify, render_template, request
from emotions import Emotions

app = Flask(__name__)

app.emotions = Emotions()
@app.route('/get_fri')
def get_fri():
    fri_val = app.emotions.calc_friend_score()
    return jsonify({'result':fri_val})

@app.route('/get_rest')
def get_rest():
    fri_val = app.emotions.get_rest()
    return jsonify({'result':fri_val})

@app.route('/get_feed')
def get_feed():
    fri_val = app.emotions.get_feed()
    return jsonify({'result':fri_val})

@app.route('/get_play')
def get_play():
    fri_val = app.emotions.get_play()
    return jsonify({'result':fri_val})

@app.route('/get_train')
def get_train():
    fri_val = app.emotions.get_train()
    return jsonify({'result':fri_val})

@app.route('/get_heal')
def get_heal():
    fri_val = app.emotions.get_heal()
    return jsonify({'result':fri_val})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
