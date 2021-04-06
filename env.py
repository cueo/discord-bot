import os


def load(file='.env'):
    if os.path.exists(file):
        with open(file, 'r') as f:
            for line in f.readlines():
                key, value = line.split('=')
                os.environ[key.strip()] = value.strip()
