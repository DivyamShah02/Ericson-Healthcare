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

    cred = credentials.Certificate(r"ehunt-e7f03-firebase-adminsdk-ug5u7-470c2046f6.json")
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
    device_id = "fV-chZ6ZTXySP6NOGTUnSE:APA91bG1VUmPufYx4EF9FbmpwyHnDQvhiMGsppgYdYak20QIdd22GulSXjchV07fnexkB-16JlPNmf7GGY6e_dygCCwWGKHm1_Y7FKhqoVEORtVDKgYfgTI"
    title = "Investigation Completed!"
    description = "This is a test notification sent via Firebase!"
    # image_url = "https://prium.github.io/freya/v2.1.0/assets/img/img_1.jpg"  # Optional
    
    description = '''Dear Divyam Shah,\n1002, PA claim of Divyam Shah, from City Hospital has been closed by Divyam Shah.\nTeam EHPL'''
    send_push_notification(device_id, title, description)
