import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Correo:
    def __init__(self):
        #Se crea la conexión con el servidor smtp y TLS
        self.fromaddr = "correo"
        self.msg = MIMEMultipart()
        self.msg['From'] = self.fromaddr
        self.msg['Subject'] = "Link de registro"
        self.server = smtplib.SMTP('smtp.office365.com', 25)
        self.server.connect("smtp.office365.com",587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.fromaddr, "clave")
        

    def enviar_correo(self, correo, cliente_id):
        #Se añaden los datos faltantes al correo
        toaddr = correo
        self.msg['To'] = toaddr
        #El mensaje es el link con el usuario
        body = f"¡Gracias por registrarte! Guarda tu contraseña aquí: http://localhost:3000/confirmacion/{cliente_id}"
        self.msg.attach(MIMEText(body, 'plain'))
        text = self.msg.as_string()
        self.server.sendmail(self.fromaddr, toaddr, text)
        self.server.quit()

