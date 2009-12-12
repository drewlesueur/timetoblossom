from google.appengine.ext import db

class Registrant(db.Model):
    first = db.StringProperty()
    last = db.StringProperty()
    email = db.StringProperty()
