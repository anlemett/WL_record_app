import os

DEBUG = True
PORT = 8100
HOST = '127.0.0.1'


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

OUTPUT_DIR = os.path.join(BASE_DIR, os.path.join('data', 'output'))
