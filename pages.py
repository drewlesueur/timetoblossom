def buy_now_test():
    ret = """
<html>
<head></head>
<body>
    <img src="http://www.timetoblossom.com/images/timetoblossom_99.gif" />
    <a href="http://www.timetoblossom.com/pages/pay.htm">Redirecting to PayPal</a>
    <form id = 'f' style = 'display:none;' action="https://www.paypal.com/cgi-bin/webscr" method="post">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="hosted_button_id" value="10494358">
    <input type="image" src="https://www.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>

    <script>
        document.getElementById('f').submit();
    </script>
</body>
</html>
"""
    return ret
    

#todo pass thru half or full
def buy_now(payment):
    full = ""
    half = ""
    test = ""
    if payment == "Full Payment":
        full = ' selected = "selected" '
    elif payment == 'Half Payment':
        half = ' selected = "selected" '
    elif payment == 'Test Payment':
        test = ' selected = "selected" '
    ret = """
<html>
<head></head>
<body>
    <img src="http://www.timetoblossom.com/images/timetoblossom_99.gif" />
    <a href="http://www.timetoblossom.com/pages/pay.htm">Redirecting to PayPal</a>
    <form style = "display:none;" id = 'f' action="https://www.paypal.com/cgi-bin/webscr" method="post">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="hosted_button_id" value="10385280">
    <table>
    <tr><td><input type="hidden" name="on0" value="Full/Half Payment">Full/Half Payment</td></tr><tr><td><select name="os0">
	    <option value="Full Payment" """ + full + """>Full Payment $398.00</option>
	    <option value="Half Payment" """ + half + """>Half Payment $199.00</option>
        <option value="Test Payment" """ + test + """>Test Payment $0.01</option>
    </select> </td></tr>
    </table>
    <input type="hidden" name="currency_code" value="USD">
    <input type="image" src="http://www.timetoblossom.com/images/button.gif" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>
    <script>
        document.getElementById('f').submit();
    </script>
</body>
</html>
"""
    return ret


def key_subset(obj, arr):
    ret = {}    
    for x in arr:
        ret[x] = obj[x]
    return ret

def xls(records):
    import util
    new_records = []    
    headings = ["name", "last", "address", "city", "state", "zip", "cell", "home", "email", "t_shirt_size", "roomate_first_1", "roomate_last_1", "roomate_first_2", "roomate_last_2", "roomate_first_3", "roomate_last_3", "parent_first", "parent_last", "parent_email", "parent_cell", "parent_home"]
    for record in records:
        new_record = key_subset(record, headings)
        new_records.append(new_record)
    #return util.array_to_csv(new_records)
    return util.array_to_xls(new_records, headings)

def view(records):
    import access
    import cgi
    ret = []
    ret.append(access.logout_link())
    ret.append(" <a href='/registrants.xls'>download</a>")
    ret.append("<table border = '1'>")
    ret.append("<tr><th>Name</th><th>Date</th><th>Email Sent?</th><th>View</th></tr>")
    for record in records:
        #for item in record:
            #ret.append(str(item) + ": " + str(record[item]) + "\n<br />")
        record.setdefault('email_sent', 'no')
        ret.append("<tr>")
        ret.append("<td>" + cgi.escape(str(record['first']) + " " + str(record['last'])) + "</td>")
        ret.append("<td>" + cgi.escape(str(record['created'])) + "</td>")
        ret.append("<td>" + cgi.escape(str(record['email_sent'])) + "</td>")         
        ret.append("<td><a href='form/"+ str(record.key()) +"'>View submission</a></td>")
        ret.append("</tr>")
    return "".join(ret)
