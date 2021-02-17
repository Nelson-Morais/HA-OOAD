"""
Django bazaar Models
@author Kevin Lucas Simon, Christina Bernhardt ,Nelson Morais
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.notifications.models import Message


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
