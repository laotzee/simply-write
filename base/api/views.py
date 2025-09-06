from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PromptSerializer
from ..models import Prompt, Tag
from django.http import HttpResponse, HttpRequest

def standard_json(response_status: int, data: dict | None, message:str=None) -> dict:
    """
    Formats the json responses for the API
    :param response_status: either 1 to indicate success or 0 for error
    :param data: either a dictionary containing the response data or None
    :param message: optional message for the response
    :return: formatted dictionary
    """
    if response_status != 1 and response_status !=0:
        raise ValueError(f'response_status must be either 1 for success or 0 for error')

    success = 'success'
    error = 'error'
    response = {
        'status': success if response_status == 1 else error,
        'data': data,
        'message': message,
    }
    return response

@api_view(['GET'])
def get_prompt(request: HttpRequest) -> Response:
    """returns a single model prompt as JSON"""
    prompt = Prompt.objects.order_by('?').first()
    if prompt:
        serialized_prompt = PromptSerializer(prompt)
        response = standard_json(1, serialized_prompt.data)
        return Response(response, status.HTTP_200_OK)
    else:
        response = standard_json(0,
                                 None,
                                 'Apologies, something went wrong',)
        return Response(response, status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def generic_func(request: HttpRequest) -> Response:
    """Generic func for an API"""

    response = standard_json(0, None)
    return Response(response, status.HTTP_404_NOT_FOUND)
