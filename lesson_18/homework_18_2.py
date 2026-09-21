import requests

with open('mars_photo1.jpg', 'rb') as file_to_upload:
    files = {"image": file_to_upload}
    response_upload = requests.post('http://127.0.0.1:8080/upload', files=files)

print("Status Code:", response_upload.status_code)
print("Response JSON:", response_upload.json())

image_url = f"http://127.0.0.1:8080/image/mars_photo1.jpg"

response_get_url = requests.get(image_url, headers={"Content-Type": "text"})
print("Status Code:", response_get_url.status_code)
print("Response JSON:", response_get_url.json())


response_get_file = requests.get(image_url, headers={"Content-Type": "image"})
print("Status Code:", response_get_file.status_code)

with open(f"downloaded_mars_photo1.jpg", "wb") as f:
    f.write(response_get_file.content)


delete_url = f"http://127.0.0.1:8080/delete/mars_photo1.jpg"

response_delete = requests.delete(delete_url)
print("Status Code:", response_delete.status_code)
print("Response JSON:", response_delete.json())


response_verify = requests.get(image_url, headers={"Content-Type": "text"})
print("Status Code:", response_verify.status_code)
print("Response JSON:", response_verify.json())