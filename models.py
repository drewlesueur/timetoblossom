from google.appengine.ext import db

#todo: make a form that will take any number of fields
#thats the beauty of app engine's datastare (bigtable)!!!
class Registrant(db.Model):
    first = db.StringProperty()
    last = db.StringProperty()
    email = db.StringProperty()
    
