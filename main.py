import requests
import smtplib
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/7c616e690b3c7d9c8027").json()

@app.route('/index.html') 
@app.route('/')
def get_all_posts():
    return render_template("index.html", post_data = response)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", sent=True)
    return render_template("contact.html", sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

my_email = "mitreshdabhi007@gmail.com"
password = "gsibwvathjplvlzj"

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}" 
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
                from_addr = my_email,
                to_addrs = my_email,
                msg = email_message
                )
        print("email sent 0000000000000000000000000000000")

if __name__ == "__main__":
    app.run(debug=True)
