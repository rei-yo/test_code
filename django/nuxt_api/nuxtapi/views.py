from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
    
class GetUserData(APIView):
    def get(self, request, *args, **kwargs):

        data = {'userdata': [{'userid': '1', 'username':'Jack' },
                             {'userid': '2', 'username':'Lily' },
                             {'userid': '3', 'username':'Emily' },
                             {'userid': '4', 'username':'Chloe' },
                             {'userid': '5', 'username':'Lucas' },
                             {'userid': '6', 'username':'Oliver' },
                             {'userid': '7', 'username':'Benjamin' },
                             {'userid': '8', 'username':'Charlotte' },
                             {'userid': '9', 'username':'James' },
                             {'userid': '10', 'username':'William' }
                            ]
                }

        return JsonResponse(data)

get_user_view =  GetUserData.as_view()
