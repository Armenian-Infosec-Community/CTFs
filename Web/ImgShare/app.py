import os, re, socket, struct, hashlib, time, threading, random, string
from urllib.parse import urlparse, urlsplit, unquote_plus, unquote
import requests
from flask import Flask, request, jsonify, render_template, send_file, abort, session, redirect, url_for, flash
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import base64
from datetime import datetime

LEVEL = int(os.getenv("LEVEL", "1"))

app = Flask(__name__)
CORS(app)
app.secret_key = "imgshare_secret_key_2025"

def ensure_flag_file():
    flag_path = "/private/secret.txt"
    rel_path = os.path.join(os.getcwd(), "private", "secret.txt")

    try:
        parent = os.path.dirname(flag_path)
        if parent and not os.path.exists(parent):
            try:
                os.makedirs(parent, exist_ok=True)
            except Exception:
                pass

        if os.path.exists(flag_path):
            return

        if os.path.exists(rel_path):
            return

        os.makedirs(os.path.dirname(rel_path), exist_ok=True)
        with open(rel_path, "a"):
            pass

    except Exception:
        return

ensure_flag_file()

import socket
import struct
import ipaddress
import re

def is_local(hostname):
    if not hostname:
        return False
    
    hostname = hostname.lower().strip()
    
    hostname = hostname.strip('[]')
    
    localhost_variants = {
        'localhost', 'localhost.localdomain', 'localhost.local',
        '127.0.0.1', '127.1', '127.0.1', '0127.0.0.1', '0x7f.0.0.1',
        '::1', '0:0:0:0:0:0:0:1', '0000:0000:0000:0000:0000:0000:0000:0001',
        '0.0.0.0', '0', '0.0', '0.0.0', '000.000.000.000',
        'local', 'localdomain', 'home',
        '2130706433',
        '0x7f000001',
        '017700000001',
    }
    
    if hostname in localhost_variants:
        return True
    
    localhost_patterns = [
        r'^localhost\..*',
        r'.*\.localhost$',
        r'^.*\.local$',
        r'^.*\.localdomain$',
        r'^test$',
        r'^example$',
        r'^invalid$',
    ]
    
    for pattern in localhost_patterns:
        if re.match(pattern, hostname):
            return True
    
    try:
        if hostname.isdigit():
            ip_int = int(hostname)
            if ip_int == 0 or (ip_int >> 24) == 127:
                return True
            try:
                ip = socket.inet_ntoa(struct.pack('!I', ip_int))
                return is_private_ip(ip)
            except (struct.error, OSError):
                pass
        
        elif hostname.startswith('0x'):
            try:
                ip_int = int(hostname, 16)
                if ip_int == 0 or (ip_int >> 24) == 127:
                    return True
                ip = socket.inet_ntoa(struct.pack('!I', ip_int))
                return is_private_ip(ip)
            except (ValueError, struct.error, OSError):
                pass
        
        elif hostname.startswith('0') and len(hostname) > 1 and all(c in '01234567' for c in hostname):
            try:
                ip_int = int(hostname, 8)
                if ip_int == 0 or (ip_int >> 24) == 127:
                    return True
                ip = socket.inet_ntoa(struct.pack('!I', ip_int))
                return is_private_ip(ip)
            except (ValueError, struct.error, OSError):
                pass
        
        elif '.' in hostname and any(part.startswith(('0x', '0')) for part in hostname.split('.')):
            parts = hostname.split('.')
            try:
                ip_parts = []
                for part in parts:
                    if part.startswith('0x'):
                        ip_parts.append(str(int(part, 16)))
                    elif part.startswith('0') and len(part) > 1:
                        ip_parts.append(str(int(part, 8)))
                    else:
                        ip_parts.append(part)
                reconstructed_ip = '.'.join(ip_parts)
                return is_private_ip(reconstructed_ip)
            except (ValueError, IndexError):
                pass
        
        else:
            try:
                ip = socket.gethostbyname(hostname)
                return is_private_ip(ip)
            except socket.gaierror:
                pass
            
            return is_private_ip(hostname)
            
    except Exception:
        return True
    
    return False

def is_private_ip(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        
        if ip.is_loopback:
            return True
            
        if ip.is_private:
            return True
            
        if ip.is_link_local:
            return True
            
        if ip.is_unspecified:
            return True
            
        if ip.is_multicast:
            return True
            
        if isinstance(ip, ipaddress.IPv4Address):
            if str(ip).startswith('127.'):
                return True
            if str(ip).startswith('0.'):
                return True
                
        elif isinstance(ip, ipaddress.IPv6Address):
            if ip == ipaddress.IPv6Address('::1'):
                return True
            if str(ip).startswith('::'):
                return True
                
        return False
        
    except (ipaddress.AddressValueError, ValueError):
        return True

if __name__ == "__main__":
    test_cases = [
        "localhost", "127.0.0.1", "127.1", "127.0.1", 
        "::1", "0:0:0:0:0:0:0:1", "0.0.0.0",
        "2130706433", "0x7f000001", "017700000001",
        "0x7f.0.0.1", "0177.0.0.1", "localhost.localdomain",
        "test.localhost", "app.local", "192.168.1.1",
        "10.0.0.1", "172.16.0.1", "example.com",
        "google.com", "0", "127", "0x7f", "0177"
    ]
    
    for case in test_cases:
        result = is_local(case)
        print(f"{case:20} -> {'BLOCKED' if result else 'ALLOWED'}")

def resize_image_from_url(url, target_width=300, target_height=200):
    print(f"[RESIZER] Processing URL: {url}")
    
    try:
        parsed = urlparse(url)
    except Exception as e:
        raise ValueError(f"Invalid URL: {e}")

    if LEVEL == 1:
        if parsed.scheme not in ("http", "https"):
            raise ValueError("Only HTTP/HTTPS protocols allowed")

        try:
            session = requests.Session()
            resp = session.get(url, timeout=10, verify=False, allow_redirects=False)

            while resp.is_redirect or resp.status_code in (301, 302, 303, 307, 308):
                redirect_url = resp.headers.get("Location")
                if not redirect_url:
                    break

                redirect_parsed = urlparse(redirect_url)
                if redirect_parsed.hostname and redirect_parsed.hostname.lower() in ['localhost', '127.0.0.1']:
                    raise ValueError("Blocked local address in redirect chain")

                resp = session.get(redirect_url, timeout=10, verify=False, allow_redirects=False)

            content = resp.content

        except Exception as e:
            raise ValueError(f"HTTP fetch failed: {e}")

    elif LEVEL == 2:
        if parsed.scheme not in ("http", "https"):
            raise ValueError(f"Only HTTP/HTTPS protocols allowed")

        if is_local(parsed.hostname):
            raise ValueError("Blocked local address in initial URL")

        try:
            session = requests.Session()
            resp = session.get(url, timeout=10, verify=False, allow_redirects=False)

            while resp.is_redirect or resp.status_code in [301, 302, 303, 307, 308]:
                redirect_url = resp.headers.get('Location')
                if not redirect_url:
                    break
                
                redirect_parsed = urlparse(redirect_url)
                
                if redirect_parsed.hostname and redirect_parsed.hostname.lower() in ['localhost', '127.0.0.1']:
                    raise ValueError("Blocked local address in redirect chain")
                
                resp = session.get(redirect_url, timeout=10, verify=False, allow_redirects=False)

            content = resp.content

        except Exception as e:
            raise ValueError(f"HTTP fetch failed: {e}")

    encoded_content = base64.b64encode(content).decode()
    return f"data:image/png;base64,{encoded_content}"

users_db = {
    "admin": {
        "password": "admin123",
        "email": "admin@imgshare.com",
        "joined": "2025-01-01"
    },
    "user": {
        "password": "password",
        "email": "user@imgshare.com", 
        "joined": "2025-01-15"
    }
}

photos_db = [
    {
        "id": 1,
        "title": "Mountain Flags",
        "description": "A beautiful view of Mount Everest.",
        "url": "https://www.makalutravel.com/images/temp/banner.jpg",
        "thumbnail": resize_image_from_url("https://www.makalutravel.com/images/temp/banner.jpg"),
        "user": "admin",
        "uploaded": datetime.now().strftime("%Y-%m-%d"),
        "views": 0
    },
    {
        "id": 2,
        "title": "Kathmandu Scene",
        "description": "A carved sculpture from Nepal with detailed traditional patterns.",
        "url": "https://alittleadrift.com/wp-content/uploads/2010/10/kathmandu-nepal.jpg",
        "thumbnail": resize_image_from_url("https://alittleadrift.com/wp-content/uploads/2010/10/kathmandu-nepal.jpg"),
        "user": "admin",
        "uploaded": datetime.now().strftime("%Y-%m-%d"),
        "views": 0
    }
]

@app.route("/redirect", methods=["GET"])
def redirect_service():
    target_url = request.args.get('url')
    if not target_url:
        return "Missing 'url' parameter", 400
    
    return redirect(target_url, code=302)

@app.route("/private/secret.txt", methods=["GET"])
def private_secret():
    if request.remote_addr not in ['127.0.0.1', '::1']:
        return "Access denied: Internal endpoint only", 403
    
    try:
        with open("/private/secret.txt", "r") as f:
            return f.read(), 200, {"Content-Type": "text/plain"}
    except:
        try:
            with open("private/secret.txt", "r") as f:
                return f.read(), 200, {"Content-Type": "text/plain"}
        except:
            return "Flag file not found", 404

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        
        if username in users_db and users_db[username]["password"] == password:
            session["user"] = username
            flash(f"Welcome back, {username}!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials", "error")
    
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))

@app.route("/image/<int:image_id>")
def view_image(image_id):
    if "user" not in session:
        return redirect(url_for("login"))
    
    photo = next((p for p in photos_db if p["id"] == image_id), None)
    if not photo:
        abort(404)
    
    photo["views"] += 1
    
    current_index = next((i for i, p in enumerate(photos_db) if p["id"] == image_id), None)
    next_photo = None
    if current_index is not None and current_index < len(photos_db) - 1:
        next_photo = photos_db[current_index + 1]
    
    return render_template('image_view.html', photo=photo, next_photo=next_photo, LEVEL=LEVEL)

@app.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template('index.html', photos=photos_db, LEVEL=LEVEL)

@app.route("/upload", methods=["POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))
    
    image_url = request.form.get("image_url", "").strip()
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    
    if not image_url or not title:
        flash("Image URL and title are required", "error")
        return redirect(url_for("index"))
    
    try:
        thumbnail_data = resize_image_from_url(image_url)
        
        new_photo = {
            "id": len(photos_db) + 1,
            "title": title,
            "description": description,
            "url": image_url,
            "thumbnail": thumbnail_data,
            "user": session["user"],
            "uploaded": datetime.now().strftime("%Y-%m-%d"),
            "views": 0
        }
        
        photos_db.insert(0, new_photo)
        
        flash("Image processed and uploaded successfully!", "success")
            
    except Exception as e:
        flash(f"Upload failed: {str(e)}", "error")
    
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
