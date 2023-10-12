
import requests


url ="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02.jpg/550px-Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02.jpg"

response = requests.get(url)

# if 200 meant request was successfull
print(response)
# response.text for website but for image response. content

print(response.content)
# use the same if file or zip on the internet
with open("image.jpg", "wb") as file:
    file.write(response.content)