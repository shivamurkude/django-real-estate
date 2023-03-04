from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def email_validator(self,email):
        try: 
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))
    
    def create_user(self,username,first_name,last_name,email,password,**extra):

        if not username:
            raise ValueError(_('You must provide a username'))
        
        if not first_name:
            raise ValueError(_('You must provide a first name'))
        if not last_name:
            raise ValueError(_('You must provide a last name'))
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Base User address :An email address is required. "))
        
        user =self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra
        )

        user.set_password(password)
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username,first_name,last_name,email,password,**extra):

        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        extra.setdefault("is_active", True)

        if extra.get("is_staff") is not True:

            raise ValueError(_("Superuser must have is_staff=True"))
        if extra.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        if not password:
            raise ValueError(_("Superuser must have password"))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email must be provided"))
        
        user=self.create_user(
            username,first_name,last_name,email,password,**extra
        )

        user.save(using=self._db)

        return user

