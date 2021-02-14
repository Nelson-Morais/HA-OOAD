from django.shortcuts import render
from django.views import View


class MessageView(View):
    # displays recent users notifications
    def get_notifications(self):
        return

    # add a new notification for the user
    def add_notification(self, user_id, message):
        return
