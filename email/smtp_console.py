import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'smtp.sparkpostmail.com'
port = 587
user = 'SMTP_Injection'
password = '4308a8ddee5c6064ec7666046169c9128b99bacc'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = '''
Este e-mail foi enviado a partir dos dados de conta SparkPst 
SMTP:  smtp.sparkpostmail.com 
Porta: 587 
Usuario: SMTP_Injection
Senha:  4308a8ddee5c6064ec7666046169c9128b99bacc
'''
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = 'naoresponda.ti@newtonpaiva.br'
email_msg['To'] = 'alexandre.araujo@newtonpaiva.br'
email_msg['Subject'] = 'Teste de envido de E-mail'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()
