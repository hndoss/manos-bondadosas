from django.db import models


class Beneficiary(models.Model):
    sex_options = [
        ('M', 'Male'),
        ('F', 'Femenine')
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=30)
    age = models.PositiveIntegerField(blank=False)
    sex = models.CharField(blank=False, max_length=1, choices=sex_options)
    email = models.EmailField(blank=False, max_length=254)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'