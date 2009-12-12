from google.appengine.api import mail
from google.appengine.runtime import apiproxy_errors

def email(to, sender, subject, body):
    try:
        mail.send_mail(to=to, sender=sender, subject=subject, body=body)
        return True
    except apiproxy_errors.OverQuotaError, message:
        # Log the error.
        logging.error(message)
        # Display an informative message to the user.
        return False
