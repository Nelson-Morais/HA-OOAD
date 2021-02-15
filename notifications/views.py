from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from notifications.models import Message


# returns JSON list of users recent notifications
@login_required(login_url='login')
def get_notifications(request):
    output_data = []
    notification_list = Message.objects.filter(user_owner_id=request.user.id).order_by('-created_at')[:15]
    for notification in notification_list:
        new_object = {
            "title": notification.title,
            "content": notification.content,
        }
        output_data.append(new_object)
    return JsonResponse(output_data, content_type='application/json', safe=False)


# add a new notification for the user
def add_notification(user_id, title, content):
    new_notification = Message(user_owner_id=user_id, title=title, content=content)
    new_notification.save()
    return
