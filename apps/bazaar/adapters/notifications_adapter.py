from ShareCare.settings import INSTALLED_APPS
from apps.notifications.interfaces.notification_interface import add_notification as interface_add_notification


# add a new notification for the user with user_id interface_add_notification
def add_notification(user_id, title, content):
    if 'apps.notifications' in INSTALLED_APPS:
        return interface_add_notification(user_id, title, content)
    else:
        return
