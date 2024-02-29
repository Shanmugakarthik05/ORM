from django.db import models
from django.contrib import admin
class Book(models.Model):
   bookid=models.IntegerField(primary_key=True);
   bookname=models.CharField(max_length=30);
   bookprice=models.IntegerField();
   author=models.CharField(max_length=20);
   qty=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
   list_display=("bookid","bookname","bookprice","author","qty");
