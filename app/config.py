import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '#gtEyO4Yf#VW+GXU47=0G*unQ(PrXVgIzl=ZlLLRIZmd(WE3G7#R9K5SmH3*__oQ*=p8lAshs3UNM#Jhc)LZww-xj9+!ArgX).@DL8nbL?WuFmHQRUV6rAN)'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False