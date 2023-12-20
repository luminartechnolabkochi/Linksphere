from django.contrib import admin



from social.models import Stories,Posts

admin.site.register(Stories)
admin.site.register(Posts)


# python manage.py createsuperuser

# >username
# >email
# password>
# confirmpswd>
# procedd y/n y