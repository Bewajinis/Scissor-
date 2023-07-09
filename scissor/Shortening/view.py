from flask_restx import Namespace, Resource
from flask import Flask, request, redirect, url_for, render_template
from ..utils import db
from ..models.Url import Url
from ..models.User import User
from datetime import datetime
import validators


short_url= Namespace('short', description="a namespace for url shortening")



@short_url.route('/shorten')
class ShortenUrl(Resource):
    def post(self):
        if request.method == 'POST':
            url = request.form['url']
            short_id = request.form['custom_url']

            if short_id and Url.query.filter_by(short_url=short_url).first() is not None:
                return redirect(url_for('index'))

            if not url:
                return redirect(url_for('index'))

            if not short_id:
                short_id = generate_short_link(5)

            new_link = Url(
                original_url=url, short_id=short_id, created_at=datetime.utcnow())
            db.session.add(new_link)
            db.session.commit()
            short_url = request.host_url + short_id

            return render_template('index.html', short_url=short_url)

        return render_template('index.html')




@short_url.route('/analytics')
class Linked(Resource):
    def get(self):
        return{'message': "hello analytics"}
    

@short_url.route("/")
class LinkedHistory(Resource):
    def get(self):
        print("got my linked page")
        return {"mesage": "Thank you for everything"}



@short_url.route('/analytics')
class Analytics(Resource):
    def get(self):
        return{'message': "hello analytics"}
    
@short_url.route("/")
class HomeP(Resource):
    def get(self):
        print("Got here")
        return {"mesage": "HEllo World"}
