from flask import Flask, request
import base64

app = Flask(__name__)

flag = 'RkxBR3tTU1JGX0QwX04wN183UlU1N183SDNfVTUzUn0='

@app.route("/")
def hidden():
    # Only allow requests from localhost
    print(request.remote_addr)
    if request.remote_addr != "127.0.0.1" and request.remote_addr != "10.10.0.11":
        return """<h1>Access Denied</h1>
        <h2 style="color: #800">Attention!</h2>
        <p>This is a restricted area. Get out of here immediately!</p>
        """, 403
    return """<h1 style="color: #800; text-decoration: underline">W31C0M3 70 1337 20N3!</h1>
    <p>""" + base64.b64decode(flag).decode('utf-8') + """</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
