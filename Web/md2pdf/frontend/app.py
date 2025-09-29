from flask import Flask, request, redirect, send_file, render_template
import uuid
import os
import subprocess
import markdown

app = Flask(__name__)

@app.route("/")
def under_construction():
    return render_template("under_construction.html")

@app.route("/converter")
def index():
    return render_template("index.html")

@app.route("/admin")
def admin():
    # Only allow requests from localhost
    if request.remote_addr != "127.0.0.1":
        return """<h1 style="color: #800">Attention! Internal use ONLY!</h1>
        <p>This page has been moved to (http://admin:1337)</p>
        """, 403
    return redirect('http://admin:1337')


@app.route("/convert", methods=["POST"])
def convert():
    user_input = request.form.get("md", "")

    # ✅ Convert Markdown to HTML
    rendered_html = markdown.markdown(user_input)

    html_template = f"""
    <html>
      <head><meta charset="utf-8"></head>
      <body>{rendered_html}</body>
    </html>
    """

    uid = str(uuid.uuid4())
    html_path = f"/tmp/{uid}.html"
    pdf_path = f"/tmp/{uid}.pdf"

    # Write the HTML input to a file
    with open(html_path, "w") as f:
        f.write(html_template)

    # ✅ Call wkhtmltopdf via subprocess
    subprocess.run(["wkhtmltopdf", html_path, pdf_path], check=True)

    return send_file(pdf_path, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
