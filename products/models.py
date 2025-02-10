from django.db import models
from ckeditor.fields import RichTextField


class Settings(models.Model):
    name_site = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=100)
    time_to_work = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name_plural = 'Настройки'
        verbose_name = 'настройки'


class Slider(models.Model):
    nad_title = models.CharField(max_length=30, verbose_name="Над Заголовком")
    photo = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    little_title = models.CharField(max_length=100, verbose_name="Под Заголовок")
    click_button = models.CharField(
        max_length=255, verbose_name="Ссылка", 
        help_text="https://t.me/afina_fabric"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'слайдер'


class Advantage(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(upload_to='images/', verbose_name="фото иконка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блок "Преимущества"'
        verbose_name = 'Блок "Преимущества"'


class WhoWe(models.Model):
    img1 = models.ImageField(upload_to='images/', verbose_name="фото #1")
    img2 = models.ImageField(upload_to='images/', verbose_name="фото #2")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    desc = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Блок "Кто Мы?"'
        verbose_name = 'Блок "Кто Мы?"'
