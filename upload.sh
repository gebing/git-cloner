#/bin/sh
rm -fr dist
python3 setup.py sdist
python3 -m twine upload dist/*