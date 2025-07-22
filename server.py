from flask import Flask, render_template
from livereload import Server
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Force template reload
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

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # No static cache

    server = Server(app.wsgi_app)
    # Watch all template and CSS files for changes
    server.watch("templates/*.html")
    server.watch("static/css/*.css")
    # Start server with LiveReload WebSocket
    server.serve(port=5000, host="127.0.0.1", liveport=35729)

