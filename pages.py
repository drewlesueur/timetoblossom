

def view(records):
    ret = ["<table border = '1'>"]
    for record in records:
        #for item in record:
            #ret.append(str(item) + ": " + str(record[item]) + "\n<br />")
        ret.append("<tr>")
        ret.append("<td>" + str(record['first']) + " " + str(record['last']) + "</td>")
        ret.append("<td>" + str(record['created']) + "</td>")        
        ret.append("<td><a href='form/"+ str(record.key()) +"'>View submission</a></td>")
        ret.append("</tr>")
    return "".join(ret)
