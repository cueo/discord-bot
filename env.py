import os


def load(file='.env'):
    with open(file, 'r') as f:
        for line in f.readlines():
            key, value = line.split('=')
            os.environ[key.strip()] = value.strip()
