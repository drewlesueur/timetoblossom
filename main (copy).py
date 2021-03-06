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

           
class Help(webapp.RequestHandler):
    def get(self):
        form1 = [
            ['First Name' , 'first'],
            ['Last Name' , 'last'],
            ['Preferred Name (This name will appear on name-tag):' , 'name'],
            ['Date of Birth' , 'dob'],
            ['Street Address' , 'address'],
            ['City' , 'city'],
            ['State' , 'state'],
            ['Zip Code' , 'zip'],
            ['Country' , 'country'],
            ['Cell Phone' , 'cell'],
            ['Home Phone' , 'home'],
            ['Email Address' , 'email'],
            ['T-Shirt Size' , 't_shirt_size'],
            ['Roomate First Name ' , 'roomate_first_1'],
            ['Roomate Last Name ' , 'roomate_last_1'],
            ['Roomate First Name  ' , 'roomate_first_2'],
            ['Roomate Last Name  ' , 'roomate_last_2'],
            ['Roomate First Name   ' , 'roomate_first_3'],
            ['Roomate Last Name   ' , 'roomate_last_3'],       	    
            ['First Name' , 'parent_first'],
            ['Last Name' , 'parent_last'],
            ['Email Address' , 'parent_email'],
            ['Cell Phone' , 'parent_cell'],
            ['Home Phone' , 'parent_home'],
            ['Emergency Contact Name' , 'emergency_name'],
            ['Emergency Contact Phone Number' , 'emergency_number'],
            ['Health/Medical Insurance Company' , 'ins_co'],
            ['Policy Number' , 'policy_number']            
        ]
        self.response.out.write(util.make_form(form1))
       
        
class MainPage(webapp.RequestHandler):
    email = "drewalex@gmail.com"
    #paypal = "http://google.com"
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
                                      ('/view', View),
                                      ('/help', Help)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
