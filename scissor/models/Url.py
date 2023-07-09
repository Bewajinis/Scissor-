import string
from ..utils import db
from flask import Flask
from datetime import datetime
from random import choices



class Url(db.Model):
    __tablename__ = 'url'
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255))
    short_url = db.Column(db.String(10),  unique=True)
    vists = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url=()

    
    def generate_short_link(self, characters: int):
        characters = string.digits + string.ascii_letters
        short_url = "".join(choices(characters, k=5))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url 

    # def __repr__(self):
    #     return f"<Url(id={self.id}, long_url='{self.long_url}', short_url='{self.short_url}')>"
