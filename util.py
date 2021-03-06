#import re

from google.appengine.api import datastore
from datetime import datetime
def start_session(obj):
    ssid = obj.request.cookies.get('ssid', None)
    if ssid:
        return ssid        
        #obj.response.headers.add_header('Set-Cookie', 'ssid=%s' % urllib.urlencode(auth_save))
    else:
        session = datastore.Entity(kind = "session")
        session['created'] = str(datetime.now())
        datastore.Put(session)
        ssid = session.key()
        obj.response.headers.add_header('Set-Cookie', 'ssid=%s' % ssid)
        return ssid

def put_session(obj,vals):
    ssid = start_session(obj)
    try:
        session = datastore.Get(ssid)
        session.update(vals)
        datastore.Put(session)
    except:
        pass
    return

def get_session(obj):
    try:
        ssid = start_session(obj)
        session = datastore.Get(ssid)
        return session
    except:
        return []
def clear_session(obj):
     obj.response.headers.add_header('Set-Cookie', 'ssid=; expires=Wed, 11-Sep-1985 11:00:00 GMT')

def stringObj(obj, st):
    """string formating stuff """
    start = st.find("{{")
    end = st.find("}}")
    st = st[0:start] + getattr(obj, st[start+2:end]) + st[end+2:]
    if st.find("{{", end+2) == -1:
        return st
    else:
        return stringObj(obj, st)

def str_csv(text):
    if '"' in text or "," in text or "\r" in text or "\n" in text:
        #text = text.replace('"', '""')        
        text = text.replace('"', "[quote]")
        text = text.replace("\r", "[return]")
        text = text.replace("\n", "[return]")
        text = text.replace(",", "[comma]")
        return '"' + text + '"'
    else:
        return text
    

def array_to_xls(objs, headings):
    import cgi
    ret = ["<table><tr>"]
    for x in headings:
        ret.append("<td>" + x + "</td>")
    ret.append("</tr>")
    for obj in objs:
        ret.append("<tr>")
        for heading in headings:
            ret.append("<td>" + cgi.escape(obj[heading]) + "</td>")
        ret.append("</tr>")
    ret.append("</table>")
    return "".join(ret)
            
        

def array_to_csv(objs):
    keys = []
    ret = []
    for obj in objs:
        for key in obj:
            if key not in keys:
                keys.append(key)
    for key in keys:
        ret.append(str_csv(key))
        ret.append(', ')
    ret = ret[0:-1]
    ret.append("\r\n")
    
    for obj in objs:
        for key in keys:
            if key in obj:
                ret.append(str_csv(obj[key]))
            else:
                ret.append('""')
            ret.append(', ')
        ret = ret[0:-1]
        ret.append("\r\n")
    return "".join(ret)


def make_form(arr):
    ret = """
<table>
"""    
    for i in arr:
        ret += """
<tr>
    <td>""" + i[0] + """<td>
    <td><input type="text" name=\""""+ i[1] +"""\"></td>
</tr>
"""
    ret += "</table>"
    return ret



"""
class T:
    a = "4"
    b = "5"

t = T()

print stringObj(t,"i have {{a}} time {{b}}")  
"""        

    
