from twilio.rest import Client

def send_message(message,url):
    account_sid = 'TWILIO_ACCOUNT_SID' 
    auth_token = 'TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=message,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+911234561239',
                              media_url=url
                          )

if __name__ == "__main__":
    """
    Run "pip install twilio"
    Send Whatsapp Message with Attachment.
    
    Arguments
    ----------
    - message
    - file_url
    
    Usage
    ----------
    python WhatsAppMsg "https://www.gstatic.com/webp/gallery/1.jpg"    
    
    """
    send_message("Detected","https://www.gstatic.com/webp/gallery/1.jpg")
    