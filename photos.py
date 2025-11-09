import requests
import os

characters = [
    "Son Goku", "Vegeta", "Son Gohan", "Piccolo", "Krillin", "Bulma",
    "Future Trunks", "Frieza", "Cell", "Majin Buu", "Android 18",
    "Android 17", "Android 16", "Yamcha", "Tien Shinhan", "Chiaotzu",
    "Master Roshi", "Chi-Chi", "Mr. Satan", "Dende", "Kami", "King Kai",
    "Supreme Kai", "Raditz", "Nappa", "Captain Ginyu", "Dr. Gero",
    "Bardock", "Videl", "Goten"
]

# Placeholder URLs - REPLACE THESE WITH ACTUAL DIRECT IMAGE URLs
# You will need to manually find direct PNG image links for each character.
# Example: "https://example.com/images/son-goku.png"
image_urls = {
    "Son Goku": "https://i.imgur.com/placeholder_goku.png",
    "Vegeta": "https://i.imgur.com/placeholder_vegeta.png",
    "Son Gohan": "https://i.imgur.com/placeholder_gohan.png",
    "Piccolo": "https://i.imgur.com/placeholder_piccolo.png",
    "Krillin": "https://i.imgur.com/placeholder_krillin.png",
    "Bulma": "https://i.imgur.com/placeholder_bulma.png",
    "Future Trunks": "https://i.imgur.com/placeholder_future_trunks.png",
    "Frieza": "https://i.imgur.com/placeholder_frieza.png",
    "Cell": "https://i.imgur.com/placeholder_cell.png",
    "Majin Buu": "https://i.imgur.com/placeholder_majin_buu.png",
    "Android 18": "https://i.imgur.com/placeholder_android_18.png",
    "Android 17": "https://i.imgur.com/placeholder_android_17.png",
    "Android 16": "https://i.imgur.com/placeholder_android_16.png",
    "Yamcha": "https://i.imgur.com/placeholder_yamcha.png",
    "Tien Shinhan": "https://i.imgur.com/placeholder_tien_shinhan.png",
    "Chiaotzu": "https://i.imgur.com/placeholder_chiaotzu.png",
    "Master Roshi": "https://i.imgur.com/placeholder_master_roshi.png",
    "Chi-Chi": "https://i.imgur.com/placeholder_chi_chi.png",
    "Mr. Satan": "https://i.imgur.com/placeholder_mr_satan.png",
    "Dende": "https://i.imgur.com/placeholder_dende.png",
    "Kami": "https://i.imgur.com/placeholder_kami.png",
    "King Kai": "https://i.imgur.com/placeholder_king_kai.png",
    "Supreme Kai": "https://i.imgur.com/placeholder_supreme_kai.png",
    "Raditz": "https://i.imgur.com/placeholder_raditz.png",
    "Nappa": "https://i.imgur.com/placeholder_nappa.png",
    "Captain Ginyu": "https://i.imgur.com/placeholder_captain_ginyu.png",
    "Dr. Gero": "https://i.imgur.com/placeholder_dr_gero.png",
    "Bardock": "https://i.imgur.com/placeholder_bardock.png",
    "Videl": "https://i.imgur.com/placeholder_videl.png",
    "Goten": "https://i.imgur.com/placeholder_goten.png"
}

image_dir = "images"
os.makedirs(image_dir, exist_ok=True)

print("Starting image download...")

for character_name in characters:
    # Format character name for filename (lowercase, replace spaces with hyphens)
    filename_name = character_name.lower().replace(" ", "-").replace("(", "").replace(")", "")
    image_filename = os.path.join(image_dir, f"{filename_name}.png")
    
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

print("\nIMPORTANT: The image URLs in photos.py are placeholders. You need to manually find direct PNG image links for each character and update the 'image_urls' dictionary in 'photos.py' before running the script to download actual images.")
