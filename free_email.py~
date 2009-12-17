from google.appengine.api import mail
from google.appengine.runtime import apiproxy_errors
import util
def email(sender, to, subject, body):
    try:
        mail.send_mail(to=to, sender=sender, subject=subject, body=body)
        return True
    except apiproxy_errors.OverQuotaError, message:
        # Log the error.
        logging.error(message)
        # Display an informative message to the user.
        return False

#send an email with bluehost
def blue_email(sender,to, subject, body):
    """Using my script on bluehost to send an email"""
    from google.appengine.api import urlfetch
    import urllib
    payload = {
        'to' : to,
        'from' : sender,
        'subject' : subject,
        'body'  : body,
        'password' : 'ooglie booglie'
    }
    resp = urlfetch.fetch(url="http://timetoblossom.clstff.com",
        payload=urllib.urlencode(payload), 
        method='POST',
        deadline=10)
    if resp.content == "true":
        return True
    else:
        return False
    
