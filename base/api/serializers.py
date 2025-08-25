from rest_framework.serializers import ModelSerializer
from ..models import Prompt, Tag

class PromptSerializer(ModelSerializer):

    class Meta:

        model = Prompt
        fields = '__all__'

class TagSerializer(ModelSerializer):

    class Meta:

        model = Tag
        fields = '__all__'
