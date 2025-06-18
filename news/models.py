from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(
        max_length=200,
    )

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("news:redactor_detail", kwargs={"pk": self.pk})
