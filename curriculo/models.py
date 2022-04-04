from django.db import models

class DadosPessoa(models.Model):
    name = models.TextField()
    tel = models.TextField()
    mail = models.TextField()
    birth = models.DateTimeField()

    def __str__(self):
        return self.name

