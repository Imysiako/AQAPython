import requests

BASE_URL = "https://images-api.nasa.gov"

# 1. Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

print("Searching")
response = requests.get(search_url, params=search_params)
response.raise_for_status()

data = response.json()
items = data.get("collection", {}).get("items", [])

nasa_ids = []
for item in items:
    data_list = item.get("data", [])
    if data_list and "nasa_id" in data_list[0]:
        nasa_ids.append(data_list[0]["nasa_id"])
    if len(nasa_ids) == 2:
        break

print(f"NASA IDs: {nasa_ids}")

for index, nasa_id in enumerate(nasa_ids, start=1):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()

    asset_items = asset_response.json().get("collection", {}).get("items", [])

    image_url = None
    for asset in asset_items:
        href = asset.get("href", "")
        if href.lower().endswith(".jpg"):
            image_url = href
            break

    if image_url:
        img_response = requests.get(image_url)
        img_response.raise_for_status()

        filename = f"mars_photo{index}.jpg"
        with open(filename, "wb") as file:
            file.write(img_response.content)
        print(f"Saved as {filename}")
    else:
        print(f"File not found")