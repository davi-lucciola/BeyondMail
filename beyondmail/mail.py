from smtplib import SMTP
from email.message import Message
from dataclasses import dataclass


@dataclass
class BeyondMail:
    email: str
    password: str
    smpt_host: str

    def __post_init__(self):
        self.smtp_server: SMTP = SMTP(self.smpt_host)
        self.authenticated: bool = False

    def __str__(self) -> str:
        return f'<SMTP:{self.email}>'

    def __enter__(self):
        self.login()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.logout()

    def login(self):
        self.smtp_server.starttls()
        self.smtp_server.login(self.email, self.password)
        self.authenticated = True

    def logout(self):
        self.smtp_server.quit()
        self.authenticated = False

    def send_email(self, emails_to: list[str], subject: str, message: str):
        if not self.authenticated:
            raise RuntimeError('Unauthenticated.')
        
        if len(emails_to) == 0:
            raise RuntimeError("The list of emails can't be empty.")
        
        emails_to: str = ', '.join(emails_to)

        body = Message()
        body['From'] = self.email
        body['To'] =  emails_to
        body['Subject'] = subject
        body.add_header('Content-Type', 'text/html')
        body.set_payload(message)

        self.smtp_server.sendmail(self.email, emails_to, body.as_string())