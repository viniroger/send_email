# Send email to multiple recipients

See att.pdf file to see how sent default email should appear. How to use send_mail.py script to send an email to mutiple recipients from a list (rec.csv, with name and email adress):

1. Install YagMail: `conda install -c conda-forge yagmail premailer`
2. Define email subject and file names from variables at script:
recipients, body text, attachments and logo image (leave empty if not using)
3. Edit yagmail.SMTP arguments with sender email and the name that will appear like sender
4. Edit variables msg1 and msg2 to define the initial and final greetings
5. About body text file, "\n" indicates skip line and you can use HTML tags

To send the email, you need create a project in a project in the Google Cloud Console and enable the Google Workspace API (see more at https://developers.google.com/workspace/guides/create-project). You must also create credentials for use (GMAIL API option “user data” and OAuth client ID like “computer app”). Using the API as a test (unpublished), you must also include the email that will make the submissions in the authorized list (even if it is the email of the account itself) in the “OAuth Allow screen”.

When running the script for the first time, you will be prompted for email and a verification code, provided by a URL printed on the screen at that time. This information will be saved (and later consulted) in the “credentials.json” file – it overwrites the originally downloaded file. By default, the validity of these credentials is 1 day, so you need:

1. Go to the credentials (https://console.cloud.google.com/apis/credentials)
2. Click on “edit” the client to “reset secret”
3. Download the JSON file, save with same name/path used at "yagmail.SMTP" method
4. Execute the script and enter authorized sender email
5. Navigate to the URL thta will be printed to auth (maybe one or two "continues")
6. Copy generated code, go to terminal and paste the code there

As long as the credentials are valid, you can send the emails.
