from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Registrant
import myweb
import pages
import free_email
import util
from google.appengine.api import datastore
from datetime import datetime

class Test(webapp.RequestHandler):
    def get(self):
        import os
        for i in os.environ:
            self.response.out.write(i + ":" + os.environ[i] + "\n")
class Form(webapp.RequestHandler):
    def get(self, the_key):
        import form
        record = datastore.Get(the_key)
        self.response.out.write(form.form(record))
class View(webapp.RequestHandler):
    def get(self):
        query = datastore.Query("registrant")
        query.Order('created')
        records = query.Get(999)
        self.response.out.write(pages.view(records))
        #self.response.out.write(str(records))

class IPN(webapp.RequestHandler):
    pass

class Pay():
    pass
       
class MainPage(webapp.RequestHandler):
    email = "carla@timetoblossom.com, drewalex@gmail.com"
    #paypal = "http://google.com"
    def get(self):
        import form
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.out.write('Hello, webapp World!')
        self.response.out.write(form.just_form())        
        #self.response.out.write(pages.test_form())
    def post(self):
        posts = myweb.get_post_vars()
        posts['created'] = str(datetime.now())
        registrant = Registrant()
        obj = datastore.Entity(kind = "registrant")
        obj.update(posts) 
        datastore.Put(obj) #also could put a list of objs #what if this fails
        #self.response.out.write(obj.key())
        
        mailed = free_email.email(self.email, "drewalex@gmail.com", "New Registrant for timetoblossom", """
Timetoblossom.com
New Registrant
""" + obj['first'] + " " + obj['last'] + """ registered
See details at
http://timetoblossom.latest.clstff.appspot.com/view
""")        
        if mailed == True:
            self.redirect("http://www.timetoblossom.com/pages/pay.htm")
        else:
            self.redirect("http://www.timetoblossom.com/pages/pay.htm")
            #self.response.out.write("Sorry, something went wrong, please hit back and try again.")
        

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/view', View),
                                      ('/ipn', IPN),
                                      (r'/form/(.*)$', Form),
                                      #(r'/pay/(.*)$)',Pay),
                                      ('/test',Test)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
