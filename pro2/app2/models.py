from django.db import models

TYPE_CHOICES = (("books","Books"),
("articles","Articles"),
("papers","Papers"))

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/",default="#")
    type = models.CharField(max_length=128,choices=TYPE_CHOICES)

    def __str__(self):
        return self.description

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    feed = models.CharField(max_length=200)
    radio = models.CharField(max_length=128)

    def __str__(self):
        return self.name