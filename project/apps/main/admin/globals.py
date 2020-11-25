from django.contrib import admin
from django.contrib.auth.models import Group, User

from settings import PROJECTNAME


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = PROJECTNAME
admin.site.site_title = '{} Admin'.format(PROJECTNAME)
admin.site.index_title = 'Welcome to {}'.format(PROJECTNAME)
