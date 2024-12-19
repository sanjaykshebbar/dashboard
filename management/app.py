# app.py
from flask import Flask, request, jsonify, render_template
import os
import shutil

app = Flask(__name__)
MEDIA_FOLDER = os.path.join(os.getcwd(), 'static', 'media')
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)

@app.route('/')
def index():
    media_files = os.listdir(MEDIA_FOLDER)
    media_files = [file for file in media_files if file.endswith(('jpg', 'png', 'mp4', 'webm'))]
    media_thumbnails = [f'/static/media/{file}' for file in media_files]
    return render_template('index.html', media_files=media_thumbnails)

@app.route('/upload', methods=['POST'])
def upload():
    if 'media' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['media']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(MEDIA_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully', 'file': file.filename}), 200

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    file_name = data.get('file_name')

    if not file_name:
        return jsonify({'error': 'No file specified'}), 400
    
    file_path = os.path.join(MEDIA_FOLDER, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': f'{file_name} deleted successfully'}), 200
    else:
        return jsonify({'error': f'{file_name} not found'}), 404

@app.route('/count', methods=['GET'])
def count():
    media_files = os.listdir(MEDIA_FOLDER)
    media_files = [file for file in media_files if file.endswith(('jpg', 'png', 'mp4', 'webm'))]
    return jsonify({'media_count': len(media_files)}), 200

if __name__ == '__main__':
    app.run(port=4000)
