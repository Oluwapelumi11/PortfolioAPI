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
    

