from django.db import models
from django.urls import reverse
from datetime import date

READ = (
    ('Small', 'Read a little'),
    ('Medium', 'Read a bit'),
    ('Lot', 'Readed A lot')
)

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    chapter = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'manga_id': self.id})
    def fed_for_today(self):
        return self.readme_set.filter(date=date.today()).count() >= len(READ)

class ReadMe(models.Model):
    date = models.DateField('Read Me Date')
    read = models.CharField(
        max_length=6,
        choices=READ,
        default=READ[0][0]
    )
    manga = models.ForeignKey(
        Manga,
        on_delete=models.CASCADE
    )
    # def __str__(self):
    #     return f"{self.get_meal_display()} on {self.date}"
    class Meta:
        ordering = ['-date']

class Read(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('read_detail', kwargs={'pk': self.id})
