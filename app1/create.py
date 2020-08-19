from app import db
from app.models import Animals

db.drop_all()
db.create_all()
