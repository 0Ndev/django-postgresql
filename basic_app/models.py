from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Cheatsheet(models.Model):
    title = models.CharField(max_length=255)
    cheatsheet = models.FileField(upload_to='cheatsheets/')
    # cheatsheet = models.FilePathField()
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    # image_url = models.CharField(max_length=500, default=None, blank=True)
    # category = models.ManyToManyField(Category)
    category = models.ForeignKey(
        Category, related_name='category', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
