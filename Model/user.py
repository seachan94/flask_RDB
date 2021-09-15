
import os
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_sqlalchemy import SQLAlchemy
from app import db
import bcrypt


class User(db.Model):
    __table__name__ = 'user'
    email_id  = db.Column(db.VARCHAR,primary_key = True,nullable=False)
    user_name = db.Column(db.VARCHAR,nullable=False)
    haing_pw = db.Column(db.VARCHAR,nullable=False)

    def __init__(self,email,name,password):
        self.email = email
        self.name = name
        self.pw = self.set_password(password)

    def __repr__(self):
        return f"<User('{self.email}', '{self.name}', '{self.pw}')>"
 
    def set_password(self, password):
        
        return  bcrypt.hashpw(password.encode('utf-8'),
                                      bcrypt.gensalt())
        