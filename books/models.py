from django.db import models


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=55)


# Books lambda function load pictures in table field
def upload_books_image(instance, filename):
   return f"{instance.book_id}, {filename}"

class Books(models.Model):
    book_id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=55)
    release_date = models.DateField()
    create_at = models.DateField(auto_now_add=True)

    photo = models.ImageField(upload_to=upload_books_image, blank=True, null=True, default="")
