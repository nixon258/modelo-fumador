import os

def ruta_absoluta(rel_path):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel_path)
