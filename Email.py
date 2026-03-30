import smtplib
import imaplib

def connect_smtp(server_url, username, password, port=587):
    """
    Connect to an SMTP server (for sending emails).
    """
    try:
        print(f"Connecting to SMTP server at {server_url}:{port}...")
        server = smtplib.SMTP(server_url, port)
        server.starttls() # Secure the connection
        server.login(username, password)
        print("Successfully connected and logged in to SMTP server!")
        return server
    except Exception as e:
        print(f"SMTP Connection failed: {e}")
        return None

def connect_imap(server_url, username, password, port=993):
    """
    Connect to an IMAP server (for reading emails).
    """
    try:
        print(f"Connecting to IMAP server at {server_url}:{port}...")
        # IMAP typically uses SSL on port 993
        mail = imaplib.IMAP4_SSL(server_url, port)
        mail.login(username, password)
        print("Successfully connected and logged in to IMAP server!")
        return mail
    except Exception as e:
        print(f"IMAP Connection failed: {e}")
        return None

if __name__ == "__main__":
    # --- Configuration ---
    # Replace these with your actual email provider's URL, your username, and your password.
    # For example, Gmail's SMTP is 'smtp.gmail.com' and IMAP is 'imap.gmail.com'
    
    SMTP_URL = "smtp.example.com"
    IMAP_URL = "imap.example.com"
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password" # Use app passwords if you have 2FA enabled
    
    # 1. Connect for Sending (SMTP)
    smtp_server = connect_smtp(SMTP_URL, USERNAME, PASSWORD)
    if smtp_server:
        # ... You can send emails here ...
        smtp_server.quit()
        print("Closed SMTP connection.")
        
    print("-" * 30)
    
    # 2. Connect for Reading (IMAP)
    imap_server = connect_imap(IMAP_URL, USERNAME, PASSWORD)
    if imap_server:
        # ... You can read emails here ...
        imap_server.logout()
        print("Closed IMAP connection.")
