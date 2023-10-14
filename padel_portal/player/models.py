from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(AbstractUser):
    """ Every user is a player. """
    pass
