#/bin/sh
python3 setup.py sdist
python3 -m twine upload --repository git-cloner dist/*