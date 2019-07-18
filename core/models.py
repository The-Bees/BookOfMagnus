from django.contrib import admin
from django.db import models


class Affiliation(models.Model):

    name = models.TextField(unique=True)
    legion = models.BooleanField(default=False)

    def __str__(self):
        return self.name

@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):
    """Affiliation Admin"""


class Character(models.Model):

    # Types
    EMPEROR = "EMPEROR"
    SIGILLITE = "SIGILLITE"
    PRIMARCH = "PRIMARCH"
    ASTARTES = "ASTARTES"

    TYPE_CHOICES = (
        (EMPEROR, "The Emperor"),
        (SIGILLITE, "The Sigillite"),
        (PRIMARCH, "Primarch"),
        (ASTARTES, "Astartes")
    )

    name = models.TextField(unique=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """Character Admin"""


# Create your models here.
class Book(models.Model):

    NOVEL = "NOVEL"
    ANTHOLOGY = "ANTHOLOGY"
    NOVELLA = "NOVELLA"

    TYPE_CHOICES = (
        (NOVEL, "Novel"),
        (ANTHOLOGY, "Anthology"),
        (NOVELLA, "Novella")
    )

    title = models.TextField(unique=True)
    author = models.TextField(null=True, blank=True)
    series_no = models.PositiveIntegerField()
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    primary_characters = models.ManyToManyField(to=Character, related_name="primary_characters")
    dramatis_personae = models.ManyToManyField(to=Character, related_name="dramatis_personae")
    follows = models.ManyToManyField(to='Book')
    blurb = models.TextField(null=True, blank=True)

    # If anthology it should contain stories?

    def __str__(self):
        return self.title

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book Admin"""
