from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="postgres://iayueqzzskyrvm:b13886b0f74f378d98542feceeccd94a151152701922c653406893b5ad2d6985@ec2-18-235-20-228.compute-1.amazonaws.com:5432/d6jgb3s11rm4ug"
#os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
