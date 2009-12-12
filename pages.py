def test_form():
    return """
test form
<form action='/' method="POST">
first: <input type = "text" name = "first"><br />
last: <input type = "text" name = "last"><br />
email: <input type = "text" name = "email"><br />
<input type = "submit" value="send">
</form>


"""

def view(registrants):
    ret = ""
    for registrant in registrants:
        ret = ret + "name: " + str(registrant.first) + " " + str(registrant.last) + "<br />"
        ret = ret + "email: " + str(registrant.email) + "<br />"
        ret += "<hr/ >"
    return ret
