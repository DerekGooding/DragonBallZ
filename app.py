from flask import Flask, render_template, send_from_directory
import os
import webbrowser
from threading import Timer
from character_mapping import character_mapping

app = Flask(__name__)

# List of characters (should match the names in characters.md and used for filenames)
characters = [
    "Son Goku", "Vegeta", "Son Gohan", "Piccolo", "Krillin", "Bulma",
    "Future Trunks", "Frieza", "Cell", "Majin Buu", "Android 18",
    "Android 17", "Android 16", "Yamcha", "Tien Shinhan", "Chiaotzu",
    "Master Roshi", "Chi-Chi", "Mr. Satan", "Dende", "Kami", "King Kai",
    "Supreme Kai", "Raditz", "Nappa", "Captain Ginyu", "Dr. Gero",
    "Bardock", "Videl", "Goten"
]

@app.route('/')
def index():
    character_data = []
    for char_name in characters:
        # Format name for file paths
        filename_base = character_mapping.get(char_name, char_name.lower().replace(' ', '-'))
        image_path = f'{filename_base}.webp'
        bio_path = os.path.join('bio', f'{filename_base}.md')
        
        bio_content = "Bio not found."
        if os.path.exists(bio_path):
            with open(bio_path, 'r', encoding='utf-8') as f:
                bio_content = f.read()
        
        character_data.append({
            'name': char_name,
            'image': image_path,
            'bio': bio_content
        })
    return render_template('index.html', characters=character_data)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)
