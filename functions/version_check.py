########################################################################
# some fabulous comment
########################################################################

import os
import requests
from typing import NoReturn

def version_check(main_path: str) -> NoReturn:
    """check current version and github,
       print if new version available
       
       parameters
       ----------
       main_path : str
           path to main.py file"""
    test_path = os.path.join(main_path, "version")
    with open(test_path, "r") as file:
        version = int(file.read())
    test_verison = int(requests.get("https://raw.githubusercontent.com/Akrosha/grenka_console/main/version").text)
    if test_verison > version:
        print(f"new version available: {test_verison} (using {version})\ncheck out https://github.com/Akrosha/grenka_console")