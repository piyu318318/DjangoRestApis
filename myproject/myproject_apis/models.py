from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'  # it will create table which has table name liabrary

    def __str__(self):
        return self.userName