import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'project1storage12'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '+f8HZpv7391JMu+5mwdjHH6Qi1kD8dW5TpScXnoX+iHqAwEhXnoQhWViykSeLEYo510p2PVmXC1Oy+AStuhtdoQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'project1-sv.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'project1-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'khai'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = "Y1V7Q~Xkk4shJtZzstqkdhxP7BydP216eRo-s"

    AUTHORITY = "https://login.microsoftonline.com/common"  
    CLIENT_ID = "af68d23a-3ded-4082-b16c-11b489e8fc50"

    REDIRECT_PATH = "/getAToken" 
    SCOPE = ["User.Read"] 

    SESSION_TYPE = "filesystem"