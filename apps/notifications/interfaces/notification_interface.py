from apps.notifications.views import add_notification as app_add_notification


# add a new notification for the user with user_id
def add_notification(user_id, title, content):
    return app_add_notification(user_id, title, content)
