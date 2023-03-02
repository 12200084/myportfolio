from django.db import models
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)
# Create your models here.


class herosection(models.Model):
    hero_greeting = models.CharField(max_length=200)
    hero_title = models.CharField(max_length=200)
    hero_intro = models.TextField(max_length=1000)
    hero_img_link = models.CharField(max_length=5000)
    # hero_img = models.ImageField()


class myproject(models.Model):
    project_name = models.CharField(max_length=200)
    project_desc = models.TextField(max_length=2000)
    project_link = models.CharField(max_length=1000)
    image_link = models.CharField(max_length=5000)
    # image = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return self.project_name
    # project_img = models.ImageField()


class serviceoffer(models.Model):
    iconname = models.CharField(max_length=1000)
    service_title = models.CharField(max_length=500)

    def __str__(self):
        return self.service_title


class skills(models.Model):
    skill_title = models.CharField(max_length=100)
    skills_in_percent = models.IntegerField()

    def __str__(self):
        return self.skill_title


class projectcount(models.Model):
    countdown_title = models.CharField(max_length=1000)
    countdown = models.CharField(max_length=1000)


class copyright(models.Model):
    copyright = models.CharField(max_length=500)


class maplocation(models.Model):
    present_location = models.CharField(max_length=500)
    location_map_api_link = models.TextField(max_length=5000)

    def __str__(self):
        return self.present_location

class learing_resource(models.Model):
    title = models.CharField(max_length=500)
    resource_link = models.CharField(max_length=5000)

class socialmedia_link(models.Model):
    instagram_link = models.CharField(max_length=1000)
    linked_link = models.CharField(max_length=1000)
    facebook_link = models.CharField(max_length=1000)
