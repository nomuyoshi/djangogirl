from django.contrib import admin
# Postモデルをimport
from .models import Post

# モデルをadminページで見れるようにするために
# Postモデルを登録
admin.site.register(Post)
