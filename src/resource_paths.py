import sys, os

def resource_path(relative_path):
    """For pyinstaller to get the path to the company logo"""
    try:
        base_path = sys._MIEPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

logo_path = resource_path(r"configs\Etezazi_logo.jpg")