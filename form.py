import simplejson

def just_form():
    return """<form method="post" action = "/">
<table cellpadding = "10" style = "table-layout:fixed; width: 500px;" >  
<tr>
    <td style="width:200px"></td>
    <td></td>
</tr>
<tr> 
    <td colspan="2"><b>Part 1:  Participant Information</b></td>
</tr>
<tr> 
    <td>First Name</td> 
    <td><input type="text" name="first"></td> 
</tr> 
 
<tr> 
    <td>Last Name</td> 
    <td><input type="text" name="last"></td> 
</tr> 
 
<tr> 
    <td>Preferred Name (This name will appear on name-tag):</td> 
    <td><input type="text" name="name"></td> 
</tr> 
 
<tr> 
    <td>Date of Birth</td> 
    <td>
        <input type="text" name="dob">
        <div><i>Girls who have not yet turned 17 and girls turning 12. by December 31, 2010</i></div>        
    </td> 
</tr> 
 
<tr> 
    <td>Street Address</td> 
    <td><input type="text" name="address"></td> 
</tr> 
 
<tr> 
    <td>City</td> 
    <td><input type="text" name="city"></td> 
</tr> 
 
<tr> 
    <td>State</td> 
    <td><input type="text" name="state"></td> 
</tr> 
 
<tr> 
    <td>Zip Code</td> 
    <td><input type="text" name="zip"></td> 
</tr> 
 
<tr> 
    <td>Country</td> 
    <td><input type="text" name="country"></td> 
</tr> 
 
<tr> 
    <td>Cell Phone</td> 
    <td><input type="text" name="cell"></td> 
</tr> 
 
<tr> 
    <td>Home Phone</td> 
    <td><input type="text" name="home"></td> 
</tr> 
 
<tr> 
    <td>Email Address</td> 
    <td><input type="text" name="email"></td> 
</tr> 
 
<tr> 
    <td>T-Shirt Size</td> 
    <td><input type="text" name="t_shirt_size"></td> 
</tr> 
 

<tr>
    <td colspan="2">
        <b>Roomate Request</b>
    </td>
</tr>

<tr>
    <td colspan="2">
        Four Girls Per Room.  Roommates must be no more than one year apart in age (unless related).  Each girl must indicate her roommate request on her registration form. 
        <br />
        Most girls will be coming without prior roommate selections.  Girls will be placed with girls their own age.    
    </td>
</tr>
<tr> 
    <td>Roomate First Name </td> 
    <td><input type="text" name="roomate_first_1"></td> 
</tr> 
 
<tr> 
    <td>Roomate Last Name </td> 
    <td><input type="text" name="roomate_last_1"></td> 
</tr> 
 
<tr> 
    <td>Roomate First Name  </td> 
    <td><input type="text" name="roomate_first_2"></td> 
</tr> 
 
<tr> 
    <td>Roomate Last Name  </td> 
    <td><input type="text" name="roomate_last_2"></td> 
</tr> 
 
<tr> 
    <td>Roomate First Name   </td> 
    <td><input type="text" name="roomate_first_3"></td> 
</tr> 
 
<tr> 
    <td>Roomate Last Name   </td> 
    <td><input type="text" name="roomate_last_3"></td> 
</tr> 
 
<tr>
    <td colspan="2"></td>
</tr>

<tr>
    <td colspan="2"><b>Part 2:  Parent/Guardian Information:</b></td>
</tr>

<tr> 
    <td>First Name</td> 
    <td><input type="text" name="parent_first"></td> 
</tr> 
 
<tr> 
    <td>Last Name</td> 
    <td><input type="text" name="parent_last"></td> 
</tr> 
 
<tr> 
    <td>Email Address</td> 
    <td><input type="text" name="parent_email"></td> 
</tr> 
 
<tr> 
    <td>Cell Phone</td> 
    <td><input type="text" name="parent_cell"></td> 
</tr> 
 
<tr> 
    <td>Home Phone</td> 
    <td><input type="text" name="parent_home"></td> 
</tr> 
<tr>    
    <td colspan="2">
    <input type="checkbox" name = "approve" />    
    I approve of my daughter's participation in the Young Women's Conference and certify that she is in good health and able to participate in the conference's activities.  I give consent for my daughter to receive medical attention, if required, in the event of illness or accident.  I agree to be responsible for any expenses such treatments require.</td>
</tr>
<tr>
    <td>Please describe any special physical, emotional, or medical concerns or limitations that may affect your daughter: </td>
    <td>
        <textarea name = "limitations"></textarea>    
    </td>
</tr>
<tr>
    <td>Please list any required medication:</td>
    <td>
        <textarea name = "medication"></textarea>    
    </td>
</tr>
<tr>
    <td>Please list any known food, drug, or other allergies:</td>
    <td>
        <textarea name = "allergies"></textarea>    
    </td>
</tr>

<tr>
    <td colspan="2"><b>Medical Release:</b> This release authorizes the emergency treatment for your daughter if she becomes ill or injured while attending Young Women's Conference and parents/ guardians cannot be reached.</td>    
</tr>

<tr> 
    <td>Emergency Contact Name</td> 
    <td><input type="text" name="emergency_name"></td> 
</tr> 
 
<tr> 
    <td>Emergency Contact Phone Number</td> 
    <td><input type="text" name="emergency_number"></td> 
</tr> 
 
<tr> 
    <td>Health/Medical Insurance Company</td> 
    <td><input type="text" name="ins_co"></td> 
</tr> 
 
<tr> 
    <td>Policy Number</td> 
    <td><input type="text" name="policy_number"></td> 
</tr>
<tr>
    <td colspan="2"><b>Medical Treatment Consent:</b></td>    
</tr>
<tr>
    <td colspan="2">I,<input type="text" name="i_parent">, parent and or/legal guardian of <input type="text" name="i_daughter" />approve of my daughter's attendance at the Young Women's Conference (YWC) and give my permission for any/all emergency treatment deemed necessary by a licensed practitioner for my child if I am unavailable. I understand this authorization does not cover major surgery unless the medical opinions of one other physician or dentist, concurring in the necessity for such surgery, are obtained prior to the performance of surgery. I agree to be responsible for any expenses incurred for such treatment. YWC insurance does not cover illness (such as cold symptoms, stomach aches, etc.) or pre-existing conditions. Participants and their parents will be responsible for any costs associated with treatment in event of an emergency. This consent is valid from June 14, 2010 to June 18, 2010
<br />
Each participant is included in a YWC limited coverage ($100,000 maximum benefit) accident insurance policy while they are under the Immediate approved direction and supervision of YWC. I understand that if my daughter leaves the required supervision of her counselor and/or staff without permission or leaves campus after hours or without permission, she will not be covered by the YWC insurance.
<br />
I understand that participants will be sent home if any drugs, alcohol, or cigarettes are found in their possession or use during the week. Young Women's Conference reserves the right to ensure the safety and well being of all participants and will dismiss a participant for misconduct or unsociable behavior as determined by the Directors. Fighting, stealing, shoplifting, possessing any harmful weapons, leaving campus unsupervised, leaving the dorms after curfew, and deliberately damaging university or program property are grounds for being sent home early. Anyone being sent home will be responsible for all transportation costs and registration fees will not be refunded.</td>    
</tr>
<tr>
    <td colspan="2">CANCELLATION POLICY:  Notice of cancellation must be received in writing.  A $100 cancellation fee will  be applied to all cancellations.  NO registration refunds will be made after April 1, 2010.</td>    
</tr>

<tr>
    <td colspan="2"><input type="checkbox" name = "agree_cancellation" />    I have read and agree to the cancellation policy</td>    
</tr>
<tr>
    <td>Our closing event will be Friday from 11:00 to 11:45 AM to share our weeklong experiences.  Please indicate the number of guests (0-4) who will be attending this closing event: </td>    
    <td>
        <select name = "guests_closing">
            <option value="0">0</option>             
            <option value="1">1</option>        
            <option value="2">2</option>        
            <option value="3">3</option>        
            <option value="4">4</option>        
        </select>
    </td>
</tr>
<tr>
    <td>Please tell us how you heard about Young Women's Conference? (Please be specific)</td>    
    <td>
        <textarea name = "how_heard"></textarea>    
    </td>
</tr>


</table>
<input type="submit" value="Submit">
"""


def form(row):
    import cgi
    for x in row:
        val = cgi.escape(row[x])
        del row[x]
        x = cgi.escape(x)
        row[x] = val
    return """<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
<script src="http://gist.github.com/raw/256759/15a5ba42e7f70bbc7c459064501cb964c706de99/jquery-json.js"></script>""" + " some fields might replace &amp; with &amp;amp; and &lt; with &amp;lt; etc. " + just_form() + """<input type = "submit" value = "Submit">
</form>""" + "<div id = 'row' style='display:none;'>" + simplejson.dumps(row, indent = 4) + "</div>" + """
<script>
$(document).ready(function(){
    var info = $('#row').html()
    info = $.evalJSON(info)
    for (var i in info) {
        var field = $('[name="'+i+'"]')        
        if (field.length > 0) {
            $('[name="'+i+'"]').val(info[i])
        }    
    }
    
    var checks = ["approve","agree_cancellation"]
    for (var i in checks) {
        if (checks[i] in info) {
            $('[name="'+ checks[i] +'"]').attr('checked',true)        
        }
    }
})
</script>


"""

