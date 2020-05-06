# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, url_for, request

from .utils import find_content, OpenGraphImage

app = Flask(__name__)

app.config.from_object('config')

@app.route('/result')
def result():
    gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    description=find_content(gender).description
    img = OpenGraphImage(uid, user_name, description)
    profile_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    og_url = url_for('index', img=img, _external=True)
    print(profile_pic)
    return render_template('result.html.j2',
        user_name=user_name,
        description=description,
        user_image=profile_pic,
        og_url=og_url)

@app.route('/contents/<int:content_id>/')
def content(content_id):
    return '%s' % content_id

@app.route('/')
@app.route('/index')
def index():
    description = """Toi, tu n'as pas peur d'être seul ! Les grands espaces et les aventures sont faits pour toi. D'ailleurs, Koh Lanta est ton émission préférée ! Bientôt tu partiras les cheveux au vent sur ton radeau. Tu es aussi un idéaliste chevronné. Quelle chance !"""
    page_title = "Le test ultime"
    og_description = "Découvre qui tu es vraiment en faisant le test ultime !"

    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index',img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)
    else:
        og_url= url_for('index', _external=True)
        og_image = url_for('static',filename='tmp/sample.jpg', _extertnal=True)

    return render_template('index.html.j2',
        user_name='Julio',
        user_image=url_for('static', filename='img/profile.png'),
        description=description,
        blur=True,
        page_title = page_title,
        og_url=og_url,
        og_image=og_image,
        og_description = og_description)


if __name__ == "__main__":
    app.run()
