from django.http import JsonResponse
from django.shortcuts import render
from .models import User
import logging
import json

log = '%(lineno)d ** %(asctime)s ** %(message)s'
logging.basicConfig(filename='user_views.log', filemode='a', format=log, level=logging.DEBUG)


def registration(request):
    try:
        data = json.loads(request.body)
        if request.method == 'POST':
            user_registration = User.objects.create(username=data.get("username"),
                                                    password=data.get("password"),
                                                    first_name=data.get("first_name"),
                                                    last_name=data.get("last_name"),
                                                    email=data.get("email"),
                                                    phone_number=data.get("phone_number"),
                                                    location=data.get("location"))
            return JsonResponse({"message": f"Data save successfully {user_registration.username}",
                                 "data": {"id": user_registration.id}}, status=201)
        return JsonResponse({"message": "Method not allow"}, status=400)
    except Exception as e:
        logging.exception(e)
        return JsonResponse({"message": "Unexpected error"}, status=400)


def login(request):
    try:
        data = json.loads(request.body)
        if request.method == 'POST':
            login_user = User.objects.filter(username=data.get("username"), password=data.get("password")).first()
            if login_user is not None:
                return JsonResponse({'message': f'User {login_user.username} is successfully login'}, status=200)
            else:
                return JsonResponse({'message': 'Invalid username/password'}, status=200)
        return JsonResponse({'message': 'Method not allow'}, status=400)
    except Exception as e:
        logging.exception(e)
        return JsonResponse({'message': 'Unexpected error'}, status=400)
