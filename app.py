from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

# Path to media folder
MEDIA_FOLDER = os.path.join(app.static_folder, "media")


@app.route("/")
def index():
    # Get list of all media files in the media folder
    media_files = os.listdir(MEDIA_FOLDER)
    videos = [file for file in media_files if file.endswith(('.mp4', '.avi', '.mov'))]
    images = [file for file in media_files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    return render_template("index.html", videos=videos, images=images)


if __name__ == "__main__":
    app.run(debug=True)
