from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    appearances = db.Column(db.Integer, nullable=True)
    clean_sheets = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Player {self.name}>"
