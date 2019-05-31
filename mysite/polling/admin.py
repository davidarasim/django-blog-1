from django.contrib import admin
from polling.models import Poll
print('[DKA /polling/admin.py]') # DKA
admin.site.register(Poll)
