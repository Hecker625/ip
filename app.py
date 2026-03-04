from datetime import datetime
from flask import Flask, request, render_template
from flask import send_file
import zoneinfo, requests

# Pacific Time
tz = zoneinfo.ZoneInfo("America/Los_Angeles")

now = datetime.now(tz)
formatted = now.strftime("%m-%d-%Y %I:%M %p %S seconds")

app = Flask(__name__)

@app.route("/")
def home():
    user_ip = request.access_route[0]
    url = f"https://api.iplocation.net/?ip={user_ip}"
    headers = {"Accept" : "application.json"}
    response = requests.get(url, headers=headers)
    data = response.json()

    now = datetime.now(tz)
    formatted = now.strftime("%m-%d-%Y %I:%M %p %S seconds")

    with open("file.txt", "a") as f:
        f.write("\n")
        f.write(formatted)
        f.write(": \n")
        f.write(str(data))

    return render_template("index.html", ip=user_ip)

@app.route("/logs")
def logs():
    return send_file("file.txt", as_attachment=True)
    
app.run(host="0.0.0.0", port=80)
