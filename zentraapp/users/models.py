from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    friend_list = ArrayField(models.IntegerField(), blank=True, default=list)
    last_login = models.DateTimeField(blank=True, null=True)

    # Custom related names to avoid clashes with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Avoids conflict with auth.User.groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Avoids conflict with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def add_friend(self, friend_id):
        if friend_id not in self.friend_list:
            self.friend_list.append(friend_id)
            self.save()


