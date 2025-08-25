from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PromptSerializer, TagSerializer
from ..models import Prompt, Tag

@api_view(['GET', 'POST'])
def get_prompt(request):
    """
    returns a single model prompt as JSON
    """
    prompt = Prompt.objects.order_by('?').first()
    obj = PromptSerializer(prompt)
    return Response(obj.data)

@api_view(['GET', 'POST'])
def generic_func(request):
    """
    Generic func for base
    """
    obj = {
        'template_obj': 'Currently using a templatte'
    }
    return Response(obj.data)
