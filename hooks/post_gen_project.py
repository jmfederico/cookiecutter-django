import glob
import urllib.request
from pathlib import Path

urllib.request.urlretrieve("https://www.gitignore.io/api/django,node", "../.gitignore")

# Move root files.
_root = Path("_root")
project_root = Path("..")
for child in _root.iterdir():
    child.rename(project_root / child.name)
_root.rmdir()

for path in glob.glob('../**/.cookiecutter-keep', recursive=True):
    Path(path).unlink()
