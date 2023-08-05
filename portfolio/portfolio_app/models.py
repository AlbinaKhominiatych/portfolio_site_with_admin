from django.db import models
from datetime import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Name(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profession(models.Model):
        profession = models.CharField(max_length=100)

        def __str__(self):
            return f"{self.profession}"

class Description(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"{self.description}"

class Experience(models.Model):
    start_year = models.IntegerField(choices=[(year, year) for year in range(2000, datetime.now().year + 1)])
    end_year = models.IntegerField(choices=[(year, year) for year in range(2000, datetime.now().year + 1)])
    position = models.CharField(max_length=100)
    description_experience = models.TextField()

    def clean(self):
        if self.start_year >= self.end_year:
            raise models.ValidationError("Start year must be less than end year.")

    def __str__(self):
        return f"{self.position} ({self.start_year}-{self.end_year})"

