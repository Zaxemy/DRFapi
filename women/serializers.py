import io
from rest_framework import serializers

from women.models import Women
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = ("title", "content", "category", "user", "is_published")
