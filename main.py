from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Registrant
import myweb
import pages
import free_email
import util

class View(webapp.RequestHandler):
    def get(self):
        query = Registrant.all()
        registrants = query.fetch(999) #you can only have 999 results at once. todo: fix this
        self.response.out.write(pages.view(registrants))
           
        
class MainPage(webapp.RequestHandler):
    email = "drewalex@gmail.com"
    paypal = "http://google.com"
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('Hello, webapp World!')
        self.response.out.write(pages.test_form())
    def post(self):
        posts = myweb.get_post_vars()
        registrant = Registrant()
        for i in posts:
            setattr(registrant, i, posts[i])
            #self.response.out.write(i + ":" + posts[i] + "<br>")
        registrant.put()
        mailed = free_email.email(self.email, self.email, "New Registrant for timetoblossom",util.stringObj(registrant, """
New registrant
Name: {{first}} {{last}}
Email: {{email}}
"""))        
        if mailed == True:
            self.redirect(self.paypal)
        else:
            self.response.out.write("Sorry, something went wrong, please hit back and try again.")
        

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                       ('/view', View)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()