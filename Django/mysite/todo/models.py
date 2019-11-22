from django.db import models

#クラス名がテーブル名と対応
class Post(models.Model):
    body = models.CharField(max_length=200)