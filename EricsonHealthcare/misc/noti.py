import firebase_admin
from firebase_admin import credentials, messaging


def send_push_notification(device_id, title, description, image_url=None):
    """
    Sends a push notification via Firebase Cloud Messaging (FCM).
    
    Args:
        cfm_number (str): The token or topic to which the notification is sent.
        title (str): Title of the notification.
        description (str): Body of the notification.
        image_url (str, optional): URL of the image to include in the notification. Defaults to None.
    """

    cred = credentials.Certificate(r"firebase_creds.json")
    firebase_admin.initialize_app(cred)

    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=description,
            image=image_url,
        ),
        token=device_id  # This sets the target as a specific device
    )

    try:
        # Send the message via FCM
        response = messaging.send(message)
        print(f"Notification sent successfully! Response: {response}")

        return True
    
    except Exception as e:
        print(f"Failed to send notification: {e}")
        return False

# Example usage
if __name__ == "__main__":
    device_id = "er_OhE-RTLSwqr-UqrG2TQ:APA91bF10bRdPrZ3W9XRZ78ykFUY1iTicKUN3zJGCNH0HXDotlYGnXdtA9GBrKwVq8f1wRt2OEt_Mh7pvP02gMMnQrO-KYUB2NwIcbHQaUAt2bCIwovZgu8"  #this is the cfm number 
    title = "Investigation Completed!"
    description = "This is a test notification sent via Firebase!"
    # image_url = "https://prium.github.io/freya/v2.1.0/assets/img/img_1.jpg"  # Optional
    
    description = '''Dear Divyam Shah,\n1002, PA claim of Divyam Shah, from City Hospital has been closed by Divyam Shah.\nTeam EHPL'''
    send_push_notification(device_id, title, description)
