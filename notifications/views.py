from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class MessageView(View):
    # returns JSON list of users recent notifications
    @login_required(login_url='login')
    def get_notifications(request):
        notification_list = [{
            "title": "Anfrage",
            "message": "Lorem ipsum dolor sit amet, consectetur adipisicing elit",
            "is_read": 0,
        }, {
            "title": "Akzeptiert",
            "message": "Lorem ipsum dolor ",
            "is_read": 1,
        }, {
            "title": "Aktueller User (Test)",
            "message": str(request.user),
            "is_read": 0,
        }]
        return JsonResponse(notification_list, safe=False)

    # add a new notification for the user
    def add_notification(request, user_id, message):
        return
