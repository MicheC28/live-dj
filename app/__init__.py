from flask import Flask

app = Flask(__name__)

from app import views
# avoid circular imports. how to import files from package.
# b/c there is an __init__.py file, treats this directory as a package