from django.db import models

# Create your models here.
from django.db import models
# Create your models here.

# add this


class Shop(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=400)
    # 'Y' -RECOMMENDED, 'N'-AVOID, 'X'-NEUTRAL
    category = models.CharField(default='Y', max_length=1)
    modified_on = models.DateTimeField()

    def _str_(self):
        return self.name
