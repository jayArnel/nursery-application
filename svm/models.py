from django.db import models

# Create your models here.


class Dataset(models.Model):
    name = models.TextField()

    class Meta:
        app_label = 'svm'

    def __unicode__(self):
        return self.name


class Attribute(models.Model):
    dataset = models.ForeignKey(Dataset, related_name='attributes')
    name = models.TextField()
    verbose_name = models.TextField()
    description = models.TextField()
    is_feature = models.BooleanField()

    class Meta:
        app_label = 'svm'

    def __unicode__(self):
        return self.name


class Label(models.Model):
    attribute = models.ForeignKey(Attribute, related_name='labels')
    name = models.TextField()
    verbose_name = models.TextField()
    description = models.TextField()
    code = models.PositiveIntegerField()

    class Meta:
        app_label = 'svm'

    def __unicode__(self):
        return self.name
