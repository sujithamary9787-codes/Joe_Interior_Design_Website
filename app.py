from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "secret"  # needed for flash messages

# Email credentials
EMAIL = "wilsonjerome8940@gmail.com"      # Replace with your Gmail
PASSWORD = "babo onyh naow jpyi"    # Gmail App password

# ------------------- ROUTES -------------------

# Home page
@app.route('/')
def home():
    return render_template('home.html')  # Separate home.html

# Services page
@app.route('/services')
def services():
    return render_template('services.html')  # Separate services.html

# About page
@app.route('/about')
def about():
    return render_template('about.html')  # Separate about.html

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Separate contact.html

# Handle GET QUOTE form submission (used on all pages)
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        phone = request.form['phone']
        location = request.form['location']
        details = request.form['details']

        # Create email
        msg = MIMEText(f"""
New Quote Request

Name: {name}
Phone: {phone}
Location: {location}
Details: {details}
        """)
        msg['Subject'] = "New Interior Quote"
        msg['From'] = EMAIL
        msg['To'] = EMAIL

        # Send email
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        flash("Quote Successfully!")

    except Exception as e:
        print(e)
        flash("Error sending quotes, try again")

    # Return back to the referring page
    return redirect(request.referrer or '/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)






