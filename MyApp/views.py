from django.shortcuts import render
import json
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class AgeView(View):
    def post(self, request):
        data = json.loads(request.body)
        birth_year = data.get("birth_year")
        current_year = data.get("current_year")
        age = current_year - birth_year
        result = {
            "birth_year" : birth_year,
            "current_year" : current_year,
            "age" : age
        }
        return JsonResponse(result)