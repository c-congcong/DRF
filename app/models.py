from django.db import models


# Create your models here.


class User(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other"),
    )

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = "users"
        verbose_name = "name"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Employee(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other"),
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=64)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pic = models.ImageField(upload_to="pic", default="pic/1.png")

    class Meta:
        db_table = "employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Students(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "other")
    )

    st_name = models.CharField(max_length=30)
    age = models.IntegerField()
    st_id = models.CharField(max_length=12)
    gender = models.SmallIntegerField(choices=gender_choices, default=1)

    class Meta:
        db_table = "ba_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.st_name
