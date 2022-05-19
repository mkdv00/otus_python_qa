import requests

response = requests.get("http://ya.ru")
assert response.status_code == 200, f"Got unexpected status code: {response.status_code}"

### TEXT ###
print("TEXT")
ch = "_"
print(response.text, f"\n{ch*100}")

### Content (Ex. - Videos, music) ###
print("Content")
print(response.content)
print(f"{ch*100}")

### Headers ###
print("HEADERS: ")
for key, value in response.headers.items():
    print(key, "=>", value)
print(f"{ch*100}")

### Cookies ###
print("COOKIES: ")
for key, value in response.cookies.items():
    print(key, "=>", value)
print(f"{ch*100}")

### JSON ###
# print("JSON")
# print(response.json())
# print(f"{ch*100}")
