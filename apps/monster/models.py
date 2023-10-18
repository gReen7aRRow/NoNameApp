from django.db import models
from django.contrib.auth.models import User

class Monster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/monsters/', blank=True)
    price = models.IntegerField()
    productivity = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class MonsterCounter(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.owner}_{self.monster}'
