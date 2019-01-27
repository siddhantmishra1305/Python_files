import sendgrid

def send_email(to_addr,from_addr,filename,filepath):
    
    client = sendgrid.SendGridClient("SENDGRIDKEY")
    message = sendgrid.Mail()
    message.add_to(to_addr)
    message.set_from(from_addr)
    message.set_subject("A good subject")
    message.set_html("body of the message goes here")
    message.add_attachment(filename,filepath)
    client.send(message)

if __name__ == "__main__":
    """
    Run "pip install sendgrid"
    
    Send Email with Attachment.
    
    Arguments
    ----------
    - to_address
    - from_address
    - filename
    - filepath
    
    Usage
    ----------
    python sendViolationEmail siddhant@iwizardsolutions.com admin@iwizardsolutions.com Violation1 Violation1.png    
    
    """
    send_email('test@example.com','test1@example.com','test.png','testImage.png')
    
