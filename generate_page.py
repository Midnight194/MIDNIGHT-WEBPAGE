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
        h1 {
            font-size: 3em;
            margin-bottom: 10px;
        }
        p {
            font-size: 1.2em;
            color: #bbbbbb;
        }
        button {
            margin-top: 30px;
            background-color: #1e88e5;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 1em;
            cursor: pointer;
            border-radius: 6px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #1565c0;
        }
        .form-container {
            margin-top: 40px;
            display: none;
            text-align: left;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            background: #1e1e1e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px #00000099;
        }
        .form-container input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
        }
        .form-container input[type="submit"] {
            background-color: #1e88e5;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>WELCOME TO MIDNIGHT WEB</h1>
    <p>STAY INFORMED IN THE DARKNESS</p>

    <button onclick="showForm()">LEARN</button>

    <div class="form-container" id="signupForm">
        <h2>Sign Up with Gmail</h2>
        <form onsubmit="handleSubmit(event)">
            <label for="email">Gmail:</label><br>
            <input type="email" id="email" name="email" placeholder="example@gmail.com" required><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" placeholder="Enter password" required><br>
            <input type="submit" value="Submit">
        </form>
    </div>

    <script>
        function showForm() {
            document.getElementById("signupForm").style.display = "block";
        }

        function handleSubmit(event) {
            event.preventDefault(); // Prevent page reload

            const email = document.getElementById("email").value;
            const password = document.getElementById("password").value;

            alert("✅ Successfully ready to surf in the shadows!\\nEmail: " + email);
            document.getElementById("signupForm").style.display = "none";
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_code)


