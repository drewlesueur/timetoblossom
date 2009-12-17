from google.appengine.api import users

def wall(my):
    user = users.get_current_user()
    if user:
        return user
    else:
        my.redirect(users.create_login_url(my.request.uri))
        return False
        
        


def login_url():
    pass

def logout_link():
    return "<a href = '" + users.create_logout_url("/") + "'>logout</a>"

