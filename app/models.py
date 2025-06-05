from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # tells SQLAlchemy to map to your MySQL table

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


