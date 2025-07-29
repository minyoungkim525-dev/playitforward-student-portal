from flask import Flask, render_template
import json
import os
import socket

# Helper: find a free port for local dev
def find_free_port(default_port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("", default_port))
            return default_port
        except OSError:
            s.bind(("", 0))
            return s.getsockname()[1]

# Try to use livereload in dev
try:
    from livereload import Server
except ImportError:
    Server = None

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable static caching

def load_mock_data():
    with open('mock_data/neon_student.json') as f:
        return json.load(f)

@app.route('/')
def dashboard():
    student = load_mock_data()
    return render_template('dashboard.html', student=student)

@app.route('/grades')
def grades():
    student = load_mock_data()
    return render_template('grades.html', student=student)

@app.route('/assignments')
def assignments():
    student = load_mock_data()
    return render_template('assignments.html', student=student)

@app.route('/calendar')
def calendar():
    student = load_mock_data()
    return render_template('calendar.html', student=student)

@app.route('/profile')
def profile():
    student = load_mock_data()
    return render_template('profile.html', student=student)

@app.route('/materials')
def materials():
    student = load_mock_data()
    return render_template('materials.html', student=student)

@app.route('/gallery')
def gallery():
    # Later, replace this with database query
    # For now, we use placeholder image URLs or empty list
    gallery_images = [
        'images/gallery/photo1.jpg',
        'images/gallery/photo2.jpg',
        'images/gallery/photo3.jpg',
        'images/gallery/photo4.jpg',
        'images/gallery/photo5.jpg',
        'images/gallery/photo6.jpg'
    ]
    return render_template('gallery.html', gallery_images=gallery_images)


if __name__ == "__main__":
    # Detect production vs dev
    is_production = os.environ.get("FLASK_ENV") == "production"

    # On Render: use PORT env variable; locally: auto-pick a free port
    port = int(os.environ.get("PORT", 0)) if is_production else find_free_port()

    if not is_production and Server:
        # Development with LiveReload
        server = Server(app.wsgi_app)
        server.watch("templates/*.html")
        server.watch("static/css/*.css")
        print(f"Running with LiveReload at http://127.0.0.1:{port}")
        server.serve(host="0.0.0.0", port=port, liveport=None)
    else:
        # Production (Render): no LiveReload
        print(f"Running production Flask app on http://0.0.0.0:{port}")
        app.run(host="0.0.0.0", port=port)
