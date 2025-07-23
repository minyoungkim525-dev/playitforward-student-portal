# from flask import Flask, render_template
# from livereload import Server
# import json

# app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True  # Force template reload
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable static file caching

# def load_mock_data():
#     with open('mock_data/neon_student.json') as f:
#         return json.load(f)

# @app.route('/')
# def dashboard():
#     student = load_mock_data()
#     return render_template('dashboard.html', student=student)

# @app.route('/grades')
# def grades():
#     student = load_mock_data()
#     return render_template('grades.html', student=student)

# @app.route('/assignments')
# def assignments():
#     student = load_mock_data()
#     return render_template('assignments.html', student=student)

# @app.route('/calendar')
# def calendar():
#     student = load_mock_data()
#     return render_template('calendar.html', student=student)

# @app.route('/profile')
# def profile():
#     student = load_mock_data()
#     return render_template('profile.html', student=student)

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)

# if __name__ == "__main__":
#     app.config['TEMPLATES_AUTO_RELOAD'] = True
#     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # No static cache

#     server = Server(app.wsgi_app)
#     # Watch all template and CSS files for changes
#     server.watch("templates/*.html")
#     server.watch("static/css/*.css")
#     # Start server with LiveReload WebSocket
#     server.serve(port=5000, host="127.0.0.1", liveport=35729)

from flask import Flask, render_template
import json
import os

# Try to use livereload locally, but don't fail if not present (for Render)
try:
    from livereload import Server
except ImportError:
    Server = None

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable static file caching

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


if __name__ == "__main__":
    # Use the port Render expects, or default to 5000 for local dev
    port = int(os.environ.get("PORT", 5000))

    # Run with LiveReload only in development (not production)
    if Server and os.environ.get("FLASK_ENV") != "production":
        server = Server(app.wsgi_app)
        server.watch("templates/*.html")
        server.watch("static/css/*.css")
        print(f"Running with LiveReload on http://127.0.0.1:{port}")
        server.serve(host="0.0.0.0", port=port, liveport=None)  # disable WebSocket for simplicity
    else:
        # Production mode (for Render) — no LiveReload
        print(f"Running production Flask app on 0.0.0.0:{port}")
        app.run(host="0.0.0.0", port=port)
