from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER

def EmailTemplate(sender, bank, accnum, amount, country, refnum):
    return(
        '    <div style="border: 2px solid black; padding: 20px">\n' +
        '      <h2>Transaction Notification - <span style="color: #1cb8b9">Successful!</span></h2>\n' +
        '      <p>The following transaction you performed was successful;</p><br/>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Sender Name:</li>\n' +
        '          <li style="font-weight: bold;">'+sender+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Bank Name:</li>\n' +
        '          <li style="font-weight: bold; text-transform: capitalize;">'+bank+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Account Number:</li>\n' +
        '          <li style="font-weight: bold">'+accnum+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Amount Transferred:</li>\n' +
        '          <li style="font-weight: bold">'+amount+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Country:</li>\n' +
        '          <li style="font-weight: bold">'+country+'</li>\n' +
        '      </ul><br />\n' +
        '        <p>Your reference number is: <strong>'+refnum+'</strong></p>\n' +
        '        <p>Please keep this mail in a safe place as you may need it in future for references</p>\n' +
        '        <p>For enquiries, please send a mail to our help-desk at <a href="mailto:contact-admin@etransecurepay.com">contact-admin@etransecurepay.com</a>,\n' +
        '            ensure not to reply to this email address </p>\n' +
        '        <p>\n' +
        '            Thanks and Regards\n' +
        '        </p>\n' +
        '        <p><strong><i>Team etransecurePay</i></strong></p>\n' +
        '        <p><a href="http://www.etransecurepay.com">etransecurepay.com</a></p>\n' +
        '    </div>\n'
    )

def EnquiryTemplate(fullname, email, telephone, message):
    return(
        '    <div style="border: 2px solid black; padding: 20px">\n' +
        '      <p>The following enquiry was issued to etransecurepay</p><br/>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Full Name:</li>\n' +
        '          <li style="font-weight: bold;">'+fullname+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Email Address:</li>\n' +
        '          <li style="font-weight: bold; text-transform: capitalize;">'+email+'</li>\n' +
        '      </ul>\n' +
        '      <ul style="list-style: none; margin: 10px 0; padding: 0">\n' +
        '          <li style="width: 150px;  float: left">Telephone:</li>\n' +
        '          <li style="font-weight: bold">'+telephone+'</li>\n' +
        '      </ul>\n' +
        '        <p>'+message+'</p>\n' +
        '    </div>\n'
    )

def SendMail(sender, bank, accnum, amount, country, refnum, receiver):
    subject = 'ETRANSECUREPAY - TRANSACTIONS'
    html_content = EmailTemplate(sender, bank, accnum, amount, country, refnum)
    plain_message = "ETRANSECUREPAY transaction services"

    send_mail(subject, sender, plain_message, [receiver],fail_silently=False, html_message=html_content)

def SendEnquiry(fullname, email, telephone, message):
    subject = 'ETRANSECUREPAY - ENQUIRY'
    html_content = EnquiryTemplate(fullname, email, telephone, message)
    plain_message = "ETRANSECUREPAY transaction services"

    send_mail(subject, email, plain_message, ["adefemigreat1995@gmail.com"], fail_silently=False, html_message=html_content)