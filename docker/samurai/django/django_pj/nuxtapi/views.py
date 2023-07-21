from django.shortcuts import render
from .models import UserData
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializer import UserDataSerializer

class GetUserData(APIView):
    def get(self, request, *args, **kwargs):

        data    = UserData.objects.all()
        
        # data = {'userdata': [{'userid': '1', 'username':'Jack' },
        #                      {'userid': '2', 'username':'Lily' },
        #                      {'userid': '3', 'username':'Emily' },
        #                      {'userid': '4', 'username':'Chloe' },
        #                      {'userid': '5', 'username':'Lucas' },
        #                      {'userid': '6', 'username':'Oliver' },
        #                      {'userid': '7', 'username':'Benjamin' },
        #                      {'userid': '8', 'username':'Charlotte' },
        #                      {'userid': '9', 'username':'James' },
        #                      {'userid': '10', 'username':'William' }
        #                     ]
        #         }
        print("data", data)
        
        data_list = []
        for d in data:
            name = {"userid": d.id, "username":d.username}    
        # name_list = [d.username for d in data]
        # id_list = [d.id for d in data]
            data_list.append(name)
        
        data = {"userdata":data_list}
        
        return JsonResponse(data)

get_user_view =  GetUserData.as_view()
