import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    nick_name = Column(String(250), unique=False)

class Followers(Base):
    __tablename__ = 'Followers'
    # Here we define columns for the table Followers.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_from_id = Column(Integer, ForeignKey('user.from.id'))
    user = relationship(User)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    likes = Column(nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    link = Column(String())
    url = (String(1000))
    posts_id = Column(Integer, ForeignKey('posts.id'))
    followers_id = Column(Integer, ForeignKey('followers.id'))
    


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = (String(300))
    autor = (String(250))
    posts_id = Column(Integer, ForeignKey('posts.id'))
    followers_id = Column(Integer, ForeignKey('followers.id'))



    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e