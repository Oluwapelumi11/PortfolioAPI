from django.core.mail import EmailMessage
from django.template.loader import get_template



class Mail():
    def __init__(self,name,title,email,message):
        self.name = name
        self.title = title
        self.email = email
        self.message = message


    def to_client(self):
        name = self.name.split(' ')[0]
        template = get_template('emails/thank-you.html')
        context = {'name': name, 'title': "Thank You for Reaching Out!",}
        content = template.render(context)
        msg = EmailMessage('Thank You From #Oluwapelumi', content, "oluwapelumiezekiel1@gmail.com", to=[self.email,])
        msg.send()

    def to_me(self):
 
        template = get_template('emails/mine.html')
        context = {'name': self.name,'email':self.email, 'title': self.title,'message':self.message}
        content = template.render(context)
        msg = EmailMessage('New Message From Portfolio', content, "oluwapelumiezekiel1@gmail.com", to=["franciswest283@gmail.com",])
        msg.send()



