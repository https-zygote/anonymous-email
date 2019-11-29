# coded by http.zygote my first project
import requests

print("\nAnonymous Email by anonymouse.org")
print("coded by http.zygote")
to = raw_input('to: ')
Insert subject = raw_input('subject: ')
Insert message = raw_input('message: ')

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("[+] EMAIL HAS BEEN SENT")
    print("[+] this anonymous email will have a 12 hour delay for more privacy")

If 'email has not been sent' in email_req.text:
 print("[+]email failed to send try again")
