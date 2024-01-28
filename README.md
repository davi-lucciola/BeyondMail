# Beyond Mail

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/davi-lucciola/BeyondMail/main/images/LibName.png" />
</div>

Beyond Mail its an **open source** project made for sending emails easily with python.

```python
import os
from beyondmail import BeyondMail, Host


# Getting Credentials from Env Variables
my_email = os.get('EMAIL')
password = os.get('PASSWORD')

# Sending Email
with BeyondMail(my_email, password, Host.GMAIL) as mail_client:
  mail_client.send_email(['email@exemple.com'], 'Subject', 'Content')
```

## Documentation

### BeyondMail

`BeyondMail` is the main class of the lib, when you create an instance of this class, you can "login" in the SMTP Server and then, send your emails.

If you try send email without login, an error will be thrown. 

```python
import os
from beyondmail import BeyondMail, Host


# Getting Credentials from Env Variables
my_email = os.get('EMAIL')
password = os.get('PASSWORD')

# Sending Email
mail_client = BeyondMail(my_email, password, Host.GMAIL)
mail_client.login()

mail_client.send_email(['email@exemple.com'], 'Subject', 'Content')

mail_client.logout()
```

You can also use python `context api` (with) to sending your emails like the first exemple, when you use the context api the instance calls the `login()` and `logout()` methods by yourself.

### Hosts

For use one email server, its just get the constant in `Host` class.

**OBS:** The hosting support are in progress, if you want to colaborate to our project, please make a **pull request**.

- Gmail
- Outlook

<hr>