from django.db import models


# Create your models here.
class Hobbies(models.Model):

    def __str__(self):
        return self.hobby_name + "- " + self.hobby_desc

    hobby_name = models.CharField(max_length=200)
    hobby_desc = models.CharField(max_length=500)
    hobby_image = models.CharField(max_length=500, default="https://www.iesabroad.org/files/blog/images/amueller/2017-10-23/default_featured_image_29.jpg")


class Portfolio(models.Model):

    def __str__(self):
        return self.portfolio_name + "- " + self.portfolio_desc

    portfolio_name = models.CharField(max_length=200)
    portfolio_desc = models.CharField(max_length=500)
    portfolio_image = models.CharField(max_length=500, default="https://c4.wallpaperflare.com/wallpaper/715/222/467/laptop-macintosh-neon-keyboards-wallpaper-preview.jpg")


class Contact(models.Model):
    c_name = models.CharField(max_length=200, default='')
    c_email = models.CharField(max_length=200, default='')
    c_message = models.CharField(max_length=500, default="Personal Message goes here.")

    def __str__(self):
        return self.c_name + ' --- ' + self.c_email + ' ---  ' + self.c_message
