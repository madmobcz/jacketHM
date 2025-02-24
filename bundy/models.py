from django.db import models

class Jacket(models.Model):
    TYPE_CHOICES = [
        ('kabát', 'Kabát'),
        ('bunda', 'Bunda'),
        ('bomber', 'Bomber'),
    ]
    typ = models.CharField(max_length=20, choices=TYPE_CHOICES)
    color = models.CharField(max_length=7, default="#ffffff")  # Ukládáme hex kód

    def __str__(self):
        return f"{self.typ} ({self.color})"

    def get_image_url(self):
        return f"/static/bundy/{self.typ}.png"
