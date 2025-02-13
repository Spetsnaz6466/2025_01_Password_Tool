from smtplib import *


_email= "juanecastilloch2@gmail.com"
_receiver= "juanecastilloch2@gmail.com"
text ="Hola Mono"
message = "Hola Mono"

server = smtplib.SMTP( host= "smtp.gmail.com",port=587)

server.starttls()
server.login(_email,"gyzprtrqehmrbnam")

server.sendmail(_email,_receiver,text)
