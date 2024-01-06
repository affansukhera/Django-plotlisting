from django.db import models


class ResetPassword(models.Model):
    old_password = models.CharField(max_length=100)
    new_password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.old_password
