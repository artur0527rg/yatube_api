#  импортируйте в код всё необходимое
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'pub_date', 'text')
        read_only_fields = ('author',)
        model = Post
