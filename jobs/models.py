from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class Skills(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'

    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.skills

class Currency(models.Model):
   class Meta:
       verbose_name_plural = 'Currency'

   currency = models.CharField(max_length=3)

   def __str__(self):
       return self.currency


class Budget(models.Model):
   class Meta:
       verbose_name_plural = 'Budget'

   budget = models.CharField(max_length=100)

   def __str__(self):
       return self.budget

class Jobs(models.Model):
   class Meta:
       verbose_name_plural = 'Jobs'

   name = models.CharField(max_length=250)
   description = models.TextField()
   image = models.ImageField(blank=True, null=True)
   added = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   skills = models.ForeignKey(Skills)
   currency = models.ForeignKey(Currency)
   budget = models.ForeignKey(Budget)
   user = models.ForeignKey(User)

   def get_absolute_url(self):
       return reverse('jobs-update', kwargs={'pk': self.pk})

   def __str__(self):
       return self.name