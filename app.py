import os
from flask import Flask, render_template, request, redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# --- CONFIGURATION ---
SENDER_EMAIL = "wilsonjerome8940@gmail.com" 
# Use the 16-character code from Google App Passwords
APP_PASSWORD = "babo onyh naow jpyi" 
RECIPIENT_EMAIL = "wilsonjerome8940@gmail.com"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_quote', methods=['POST'])
def send_quote():
    name = request.form.get('name')
    phone = request.form.get('phone')
    location = request.form.get('location')
    details = request.form.get('details')

    msg = EmailMessage()
    msg.set_content(f"New Inquiry Received:\n\nName: {name}\nPhone: {phone}\nLocation: {location}\nDetails: {details}")
    msg['Subject'] = f"Joe Interiors Inquiry - {name}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT",
5000))
    app.run(host='0.0.0.0',port=port)








