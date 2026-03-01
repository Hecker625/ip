from datetime import datetime
from flask import Flask, request, render_template
from flask import send_file
import zoneinfo

# Pacific Time
tz = zoneinfo.ZoneInfo("America/Los_Angeles")

now = datetime.now(tz)
formatted = now.strftime("%m-%d-%Y %I:%M %p %S seconds")

app = Flask(__name__)

@app.route("/")
def home():
    user_ip = request.access_route[0]

    now = datetime.now(tz)
    formatted = now.strftime("%m-%d-%Y %I:%M %p %S seconds")

    with open("file.txt", "a") as f:
        f.write("\n")
        f.write(user_ip)
        f.write(": ")
        f.write(formatted)

    return render_template("index.html", ip=user_ip)

@app.route("/logs")
def logs():
    file = input ("Enter password: ")
    if file == "ihackedyourip":
        return send_file("file.txt", as_attachment=True)
        
    else:
        pass
    
app.run(host="0.0.0.0", port=80)