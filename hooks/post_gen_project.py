import os
import urllib.request

urllib.request.urlretrieve("https://www.gitignore.io/api/django,node", "../.gitignore")

for file_name in os.listdir("_root"):
    os.rename(f"_root/{file_name}", f"../{file_name}")
os.rmdir("_root")
