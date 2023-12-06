from django.db import models

# Create your models here.

class Contact(models.Model):
    facebook = models.URLField(("Facebook"), max_length=200)
    x = models.URLField(("X Profile Link"), max_length=200)
    telegram = models.URLField(("Telegram Link"), max_length=200)
    linkedIn = models.URLField(("LinkedIn Profile"), max_length=200)
    whatsapp = models.URLField(("WhatsApp Link"), max_length=200)
    phone = models.CharField(("Phone"), max_length=13)
    email =models.EmailField(("Email"), max_length=254)
    email2 = models.EmailField(("Email"), max_length=254)


    def __str__(self):
        return "Faith Contact"
    

class Message(models.Model):
    name = models.CharField(("Name"), max_length=50)
    email = models.EmailField(("Email"), max_length=254)
    title = models.CharField(("Title"), max_length=50)
    message = models.TextField(("message"))


    def __str__(self):
        return self.name
    