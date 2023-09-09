import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv  # Para ler informações a partir de um arquivo CSV

# Configurações do servidor SMTP do Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "seu_email@gmail.com"  # Insira o seu e-mail do Gmail
smtp_password = "sua_senha"  # Insira a senha do seu e-mail (ou utilize OAuth2)

# Crie uma conexão SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Leitura das informações a partir de um arquivo CSV
with open("lista_emails.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Ignora o cabeçalho do arquivo CSV
    for row in reader:
        to_email = row[0]  # Assume que a primeira coluna contém os endereços de e-mail
        subject = "Assunto do E-mail"
        message = "Corpo do e-mail"

        # Crie o conteúdo do e-mail
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = to_email
        msg["Subject"] = subject

        # Adicione o corpo do e-mail
        msg.attach(MIMEText(message, "plain"))

        # Envie o e-mail
        server.sendmail(smtp_username, to_email, msg.as_string())

# Encerre a conexão SMTP
server.quit()
