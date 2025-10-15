from flask import Flask, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')

@app.route('/')
def index():
    media_files = []
    for file in os.listdir(UPLOAD_FOLDER):
        ext = file.lower().split('.')[-1]
        if ext in ['png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm']:
            media_files.append(file)
    media_files.sort(reverse=True)
    return render_template('index.html', media_files=media_files)

if __name__ == '__main__':
    app.run(debug=True)
