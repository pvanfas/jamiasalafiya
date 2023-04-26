from django.db import models
from versatileimagefield.fields import VersatileImageField


class Wish(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Wish"
        verbose_name_plural = "Wishes"

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128, blank=True, null=True)
    file = models.FileField(max_length=128, blank=True, null=True)
    cover = VersatileImageField("Cover Image", upload_to="books/covers/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return str(self.title)


class Message(models.Model):
    name = models.CharField(max_length=128)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return str(self.name)


class News(models.Model):
    title = models.CharField(max_length=128)
    photo = VersatileImageField("News Image", upload_to="books/covers/")
    date = models.DateField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "Newses"

    def __str__(self):
        return str(self.title)


class About(models.Model):
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    magazine_subtitle = models.CharField(max_length=128)
    magazine_description = models.TextField()
    magazine_cover = VersatileImageField(
        "Magazine cover Image", upload_to="books/magazine_cover/"
    )
    magazine_mockup = VersatileImageField(
        "Magazine Mockup Image", upload_to="books/magazine_mockup/"
    )
    magazine_file = models.FileField(max_length=128)

    class Meta:
        verbose_name = "About Magazine"
        verbose_name_plural = "About Magazine"

    def __str__(self):
        return str(self.phone)


class Social(models.Model):
    media = models.CharField(max_length=128)
    link = models.URLField(max_length=128)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"

    def __str__(self):
        return str(self.media)
