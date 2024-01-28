from smtplib import SMTP
from email.message import Message
from dataclasses import dataclass


@dataclass
class BeyondMail:
    '''
    Main class to send emails

    Attributes
    ----------
    email: str
        Sender email
    
    password: str
        Sender password or key to login in host server

    smtp_host: str
        String that must contain the email server host and 
        email server port in format: <host>:<port>

        You can use the constants at "Host" class
    '''
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
        ''' This method login client in host server '''
        self.smtp_server.starttls()
        self.smtp_server.login(self.email, self.password)
        self.authenticated = True

    def logout(self):
        ''' This method logout client in host server '''
        self.smtp_server.quit()
        self.authenticated = False

    def send_email(self, emails_to: list[str], subject: str, message: str):
        '''
        This method sends emails to the specified email list.
        
        Params
        ------
        emails_to: list[str]
            List of recipient emails to send
        
        subject: str
            Title of the message
        
        message: str
            Body of the email that will be sent
        '''
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
