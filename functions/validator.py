########################################################################
# some fabulous comment
########################################################################

import os
from typing import NoReturn

def validator(main_path: str) -> NoReturn:
    """validate for existing important files (else close program)
       and create not very important
       
       parameters
       ----------
       main_path : str
           path to main.py file"""
    test_broken = ["functions{sep}handler_cmd.py",
                   "functions{sep}randoms.py",
                   "functions{sep}database.py",
                   "functions{sep}version_check.py",
                   "resources",
                   "resources{sep}resources.sqlite3"]
    test_enough = ["commands",
                   "database",
                   "languages"]
    for path in test_broken:
        test_path = os.path.join(main_path, path.format(sep = os.sep))
        if not os.path.exists(test_path):
            print(f"program is broken: not enough files [{test_path}]")
            exit()
    for path in test_enough:
        test_path = os.path.join(main_path, path.format(sep = os.sep))
        if not os.path.exists(test_path):
            os.mkdir(test_path)
    