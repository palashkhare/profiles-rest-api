from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# from rest_framework.authtoken.models import Token

class UserProfileManager(BaseUserManager):
    """Class to manage user profile manager.
        BaseUserManager : This class manage User profile. Since we have modified
        User model we will have to redefine UserProfileManager
    """

    def create_user(self, email, name, password=None):
        """This function is called by django to create user"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """A new super user is created"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# This has to be defined in settins to tell django which auth model should be used
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DB model for users
        AbstractBaseUser and PermissionMixin classes are the classes needed to
        modify predefined user model.

        USERNAME_FIELD : This can define custom username feild. In our case we
        will make username feild as 'email'

        REQUIRED_FEILDS : This feild defines mandatory feilds. This can be done
        apart from balnk=False
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrive short name of user"""
        return self.name

    def __str__(self):
        """return string repressentation of our user"""
        return self.email

class ProfileFeedItems(models.Model):
    """Profilr Status Update"""
    # Relation is setup with authorized user.
    # We are using the variable settings.AUTH_USER_MODEL because in case we
    # change default user model, It will not need to change the haardcode model
    # class

    # user_profile = models.ForeignKey(
    #    settings.AUTH_USER_MODEL,
    #    on_delete=models.CASCADE,
    # )

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
    )

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text
