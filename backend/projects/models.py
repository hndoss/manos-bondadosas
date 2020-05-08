from django.db import models


class Project(models.Model):
    # state_options = [
    #     ('E', 'Enabled'),
    #     ('D', 'Disabled')
    # ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=30)
    description = models.CharField(blank=False, max_length=30)
    # state = models.IntegerField(blank=False)

    def __str__(self):
        return self.name
