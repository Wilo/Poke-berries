from django.db import models


class Berry(models.Model):
    name = models.CharField(max_length=140)
    growth_time = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "pokeapi_berry"
