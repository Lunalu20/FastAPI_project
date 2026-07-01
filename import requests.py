import requests
import xml.etree.ElementTree as ET

main_url = '127.0.0.1'
url = 'http://127.0.0.1:8000/send_xml'
port = 8000

xui = requests.get(url=url)

file_path = "/Users/admin/IT/projects/books_store/response.xml"
with open(file_path, "wb") as file:
    file.write(xui.content)

# print(xui.text)





