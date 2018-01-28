from flask import Flask, jsonify, render_template, request
import random
import GoddardBot
import serialBot

app = Flask(__name__)

app.emotions = GoddardBot.Emotions()


@app.route('/get_rest')
def get_rest():
    rest_mod = random.randint(1, 5)
    hun_val = -10 - rest_mod
    hap_val = 7 + rest_mod
    dis_val = -7 - rest_mod
    app.emotions.mod_hun(hun_val)
    app.emotions.mod_hap(hap_val)
    fri_val = app.emotions.mod_dis(dis_val)
    return jsonify({'result': fri_val})


@app.route('/get_feed')
def get_feed():
    feed_mod = random.randint(1, 5)
    hun_val = 10 + feed_mod
    hap_val = 8 + feed_mod
    dis_val = -4 - feed_mod
    app.emotions.mod_hun(hun_val)
    app.emotions.mod_hap(hap_val)
    fri_val = app.emotions.mod_dis(dis_val)
    return jsonify({'result': fri_val})


@app.route('/get_play')
def get_play():
    play_mod = random.randint(1, 5)
    hap_val = 10 + play_mod
    hun_val = -10 - play_mod
    app.emotions.mod_hap(hap_val)
    fri_val = app.emotions.mod_hun(hun_val)
    return jsonify({'result': fri_val})


@app.route('/get_train')
def get_train():
    train_mod = random.randint(1, 5)
    dis_val = 10 + train_mod
    hun_val = -7 - train_mod
    hap_val = -3 + train_mod
    app.emotions.mod_hap(hap_val)
    app.emotions.mod_hun(hun_val)
    fri_val = app.emotions.mod_dis(dis_val)
    return jsonify({'result': fri_val})


@app.route('/get_heal')
def get_heal():
    heal_mod = random.randint(1, 5)
    sic_val = 10 + heal_mod
    dis_val = 5 + heal_mod
    hap_val = -3 - heal_mod
    app.emotions.mod_sic(sic_val)
    app.emotions.mod_dis(dis_val)
    fri_val = app.emotions.mod_hap(hap_val)
    # serial bot call for each

    return jsonify({'result': fri_val})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
