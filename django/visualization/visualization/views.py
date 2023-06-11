from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

class IndexView(View):

    def get(self, request, *args, **kwargs):

        return render(request,"visualization/index.html")

index   = IndexView.as_view()

# class GetValuesAPI(APIView):

#     def get(self, request, *args, **kwargs)
#     all_customer_data = 