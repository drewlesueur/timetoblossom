import re

def stringObj(obj, st):
    """string formating stuff """
    start = st.find("{{")
    end = st.find("}}")
    st = st[0:start] + getattr(obj, st[start+2:end]) + st[end+2:]
    if st.find("{{", end+2) == -1:
        return st
    else:
        return stringObj(obj, st)

"""
class T:
    a = "4"
    b = "5"

t = T()

print stringObj(t,"i have {{a}} time {{b}}")  
"""        

    