from flask_sqlalchemy import SQLAlchemy
from utils import generate_id

db = SQLAlchemy()

class URL(db.Model):
	id = db.Column(db.String(10), primary_key = True, default=generate_id())
	url = db.Column(db.String(2048))