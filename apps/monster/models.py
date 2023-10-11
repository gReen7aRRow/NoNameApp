from django.db import models

class Monster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/monsters/', default=None)
    price = models.IntegerField()
    productivity = models.IntegerField()

    def __str__(self) -> str:
        return self.name
