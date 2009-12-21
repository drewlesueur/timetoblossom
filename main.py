from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Registrant
import myweb
import pages
import free_email
import util
from google.appengine.api import datastore
from datetime import datetime
import access
import settings

class Test(webapp.RequestHandler):
    def get(self):
        import os
        for i in os.environ:
            self.response.out.write(i + ":" + os.environ[i] + "\n")
class Form(webapp.RequestHandler):
    def get(self, the_key):
        user = access.wall(self)
        if user:
            if (user.nickname() in settings.admins):
                import form
                record = datastore.Get(the_key)
                self.response.out.write(form.form(record))
            else:
                self.redirect('/')
      


class CSV(webapp.RequestHandler):
    def get(self):
        user = access.wall(self)
        if user:
            if (user.nickname() in settings.admins):        
                query = datastore.Query("registrant")
                query.Order('created')
                records = query.Get(999)
                #self.response.headers.add_header("Content-Type", 'text/csv')
                self.response.headers.add_header("Content-Disposition", "attachment; filename=csv.csv")
                self.response.out.write(pages.csv(records))
                #self.response.out.write(str(records))
  
class View(webapp.RequestHandler):
    def get(self):
        user = access.wall(self)
        if user:
            if (user.nickname() in settings.admins):        
                query = datastore.Query("registrant")
                query.Order('created')
                records = query.Get(999)
                self.response.out.write(pages.view(records))
                #self.response.out.write(str(records))

class IPN(webapp.RequestHandler):
    pass

class Pay():
    pass

#for automatically submitting the paypal form
class Paypal_submit(webapp.RequestHandler):
    def get(self):
        util.start_session(self)
        session = util.get_session(self)
        payment = 'Full Payment'        
        if 'payment' in session:
            payment = session['payment']
        self.response.out.write(pages.buy_now(payment))

#after a registrant paid
class Paid(webapp.RequestHandler):
    def get(self):
        util.start_session(self)
        session = util.get_session(self)
        if ('key' in session):
            form = datastore.Get(session['key'])
        if 'email' in session:
            self.response.out.write(session['email'])
            mailed = free_email.blue_email(settings.from_email, session['email'] + ", " + settings.to_email, settings.thank_you_subject, settings.thank_you_body)
            if mailed:
                form['email_sent'] = 'yes'
            else:
                form['email_sent'] = 'no'        
        else:
            form['email_sent'] = 'no'
            self.response.out.write("Thank you")
        datastore.Put(form)        
        self.redirect(settings.thank_you_url)

class MainPage(webapp.RequestHandler):
    #paypal = "http://google.com"
    def get(self):
        import form
        #self.response.headers['Content-Type'] = 'text/html'
        #self.response.out.write('Hello, webapp World!')
        self.response.out.write(form.just_form())        
        #self.response.out.write(pages.test_form())
    def post(self):
        util.start_session(self)##
        posts = myweb.get_post_vars()
        posts['created'] = str(datetime.now())
        obj = datastore.Entity(kind = "registrant")
        obj.update(posts) 
        if 'os0' in obj: # os0 is wether it's half or full payment
            pass
        else:
            obj['os0'] = 'Full Payment'
        datastore.Put(obj) #also could put a list of objs #what if this fails
        #self.response.out.write(obj.key())
        util.put_session(self,{'email': posts['email'], 'key':obj.key(), 'payment' : obj['os0']}) #saving some cookies, key is most important others save lines of code
        #mailed = free_email.email(self.email, "drewalex@gmail.com", "New Registrant for timetoblossom", """
        mailed = free_email.blue_email(settings.from_email, settings.to_email, "New Registrant for timetoblossom", """
Timetoblossom.com
New Registrant
""" + obj['first'] + " " + obj['last'] + """ registered
See details at
http://timetoblossom.latest.clstff.appspot.com/view
""")        
        if mailed == True:
            obj['email_sent_to_carla'] = "yes"            
            #self.redirect("http://www.timetoblossom.com/pages/pay.htm")
        else:
            obj['email_sent_to_carla'] = "no"            
            #self.redirect("http://www.timetoblossom.com/pages/pay.htm")
            #self.response.out.write("Sorry, something went wrong, please hit back and try again.")
        datastore.Put(obj) #save the email info
        self.redirect("/paypal_submit")
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/view', View),
                                      ('/csv.csv', CSV),
                                      ('/ipn', IPN),
                                      (r'/form/(.*)$', Form),
                                      #(r'/pay/(.*)$)',Pay),
                                      ('/test',Test),
                                      ('/paypal_submit', Paypal_submit),
                                      ('/paid', Paid)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
