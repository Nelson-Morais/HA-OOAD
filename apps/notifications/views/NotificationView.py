"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.


NotificationView controls the Notifications of the System

@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

from apps.notifications.models import Message


class NotificationView(View):
    """Notification views class"""

    @login_required(login_url='login')
    def get_notifications(request):
        """
        :param request: HTTP request
        :return: returns Json response containing the Users notifications
        """
        output_data = []
        notification_list = Message.objects.filter(user_owner_id=request.user.id).order_by('-created_at')[:15]
        for notification in notification_list:
            new_object = {
                "title": notification.title,
                "content": notification.content,
            }
            output_data.append(new_object)
        return JsonResponse(output_data, content_type='application/json', safe=False)

    def add_notification(user_id, title, content):
        """
        add a new notification for the user
        :param user_id: User ID to be notified
        :param title: Title of the notification
        :param content: content (text) of the notification
        :return: return
        """
        new_notification = Message(user_owner_id=user_id, title=title, content=content)
        new_notification.save()
        return
