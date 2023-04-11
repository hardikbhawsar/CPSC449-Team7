from flask_sqlalchemy import SQLAlchemy

#initializing an instance of SQLALchemy
db = SQLAlchemy()
#Class defination of the tables used in project
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    organisation = db.Column(db.String(50),nullable=False)
    address =  db.Column(db.Text(),nullable=False)
    city =  db.Column(db.String(30),nullable=False)
    state =  db.Column(db.String(30),nullable=False)
    country = db.Column(db.String(30),nullable=False)

    def __repr__(self)->str:
        return 'User>>> {self.username}'
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
