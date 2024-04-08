from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title} {self.price}"
