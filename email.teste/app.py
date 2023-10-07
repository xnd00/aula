##  pip install pywebview 
##  pyinstaller --onefile --noconsole app.py

from flask import Flask, jsonify, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webview


## inicializando app
app = Flask(__name__)
webview.create_window('Newton PY - Teste E-mail', app)

@app.route('/')
def principal():
    host = 'smtp.sparkpostmail.com'
    port = 587
    user = 'SMTP_Injection'
    password = '64d8967f91b0d264864bb66b6a88e5bbbbf808a5'
    remetente = 'naoresponda.ti@newtonpaiva.br'

    return render_template('index.html',host = host,port = port, password = password,remetente = remetente, user = user)


@app.route('/enviar',methods = ['POST'])
def enviar():
    host = request.form.get('host')
    port = request.form.get('port')
    user = request.form.get('user')
    password = request.form.get('password')
    remetente = request.form.get('remetente')

    server = smtplib.SMTP(host, port)
    dest = request.form.get('destinatario')
    message = request.form.get('menssagem')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    email_msg = MIMEMultipart()
    email_msg['From'] = remetente
    email_msg['To'] = dest
    email_msg['Subject'] = 'Email testes by Python'
    email_msg.attach(MIMEText(message, 'plain'))
    server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.quit()

    return f'E-mail enviado para {dest}!'


##app.run(port=80,host='localhost',debug=False)
webview.start()