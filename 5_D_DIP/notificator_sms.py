from .notificator_interface import NotificatorInterface


class NotificatiorSMS(NotificatorInterface):
    def send_notification(self, message: str):
        print(f"Sendind SMS: {message}")
