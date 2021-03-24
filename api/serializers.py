from rest_framework import serializers

from pages.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','rubric','foto_post','images','url','body','post_data','post_update')


