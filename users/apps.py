from django.apps import AppConfig
#from django.db.models.signals import post_save
#from django.contrib.auth.models import User


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

    # def ready(self): when you dont mention recever decorators in singnals
    #     post_save.connect(create_profile, sender=User)
    #     post_save.connect(save_profile, sender=User)