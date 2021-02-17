"""
Notification Interface for external Apps

@author Kevin Lucas Simon, Nelson Morais, Christina Bernhardt
Projekt OOAD Hausarbeit WiSe 2020/21
"""
from apps.notifications.views import NotificationView


def add_notification(user_id, title, content):
    """
      Add a new notification for the user with user_id
      :param user_id: ID of the user to be notified
      :param title: Title of the notification
      :param content: content (text) of the notification
      :return: remote call of the notification handler
      """
    return NotificationView.add_notification(user_id, title, content)
