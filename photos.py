import requests
import os
from character_mapping import character_mapping

characters = [
    "Son Goku", "Vegeta", "Son Gohan", "Piccolo", "Krillin", "Bulma",
    "Future Trunks", "Frieza", "Cell", "Majin Buu", "Android 18",
    "Android 17", "Android 16", "Yamcha", "Tien Shinhan", "Chiaotzu",
    "Master Roshi", "Chi-Chi", "Mr. Satan", "Dende", "Kami", "King Kai",
    "Supreme Kai", "Raditz", "Nappa", "Captain Ginyu", "Dr. Gero",
    "Bardock", "Videl", "Goten"
]

image_urls = {
    "Son Goku": "https://dragonball-api.com/characters/goku_normal.webp",
    "Vegeta": "https://dragonball-api.com/characters/vegeta_normal.webp",
    "Son Gohan": "https://dragonball-api.com/characters/gohan.webp",
    "Piccolo": "https://dragonball-api.com/characters/picolo_normal.webp",
    "Krillin": "https://dragonball-api.com/characters/Krilin_Universo7.webp",
    "Bulma": "https://dragonball-api.com/characters/bulma.webp",
    "Future Trunks": "https://dragonball-api.com/characters/Trunks_Buu_Artwork.webp",
    "Frieza": "https://dragonball-api.com/characters/Freezer.webp",
    "Cell": "https://dragonball-api.com/characters/celula.webp",
    "Majin Buu": "https://dragonball-api.com/characters/BuuGordo_Universo7.webp",
    "Android 18": "https://dragonball-api.com/characters/Androide_18_Artwork.webp",
    "Android 17": "https://dragonball-api.com/characters/17_Artwork.webp",
    "Android 16": "https://dragonball-api.com/characters/Androide_16.webp",
    "Yamcha": "https://dragonball-api.com/characters/Final_Yamcha.webp",
    "Tien Shinhan": "https://dragonball-api.com/characters/Tenshinhan_Universo7.webp",
    "Chiaotzu": "",
    "Master Roshi": "https://dragonball-api.com/characters/roshi.webp",
    "Chi-Chi": "https://dragonball-api.com/characters/ChiChi_DBS.webp",
    "Mr. Satan": "https://dragonball-api.com/characters/Mr_Satan_DBSuper.webp",
    "Dende": "https://dragonball-api.com/characters/Dende_Artwork.webp",
    "Kami": "",
    "King Kai": "https://dragonball-api.com/characters/Kaio_del_Norte.webp",
    "Supreme Kai": "https://dragonball-api.com/characters/Kaio-shin_del_este_Artwork.webp",
    "Raditz": "https://dragonball-api.com/characters/Raditz_artwork_Dokkan.webp",
    "Nappa": "",
    "Captain Ginyu": "https://dragonball-api.com/characters/ginyu.webp",
    "Dr. Gero": "https://dragonball-api.com/characters/Dr._Gero nadroide 20.webp",
    "Bardock": "https://dragonball-api.com/characters/Bardock_Artwork.webp",
    "Videl": "",
    "Goten": ""
}

image_dir = "images"
os.makedirs(image_dir, exist_ok=True)

print("Starting image download...")

for character_name in characters:
    image_filename = os.path.join(image_dir, f"{character_mapping.get(character_name, character_name.lower().replace(' ', '-'))}.webp")
    
    image_url = image_urls.get(character_name)

    if not image_url or "placeholder" in image_url:
        print(f"Skipping {character_name}: No valid image URL provided or it's a placeholder.")
        continue

    try:
        print(f"Downloading {character_name} from {image_url}...")
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        with open(image_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded {character_name} to {image_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {character_name} from {image_url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for {character_name}: {e}")

print("Image download process completed.")


