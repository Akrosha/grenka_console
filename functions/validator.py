########################################################################
# some fabulous comment
########################################################################

import os

def validator(main_path):
    test_broken = ["functions{sep}handler_cmd.py", "functions{sep}randoms.py", "functions{sep}database.py"]
    test_enough = ["commands", "database", "languages"]
    for path in test_broken:
        test_path = os.path.join(main_path, path.format(sep = os.sep))
        if not os.path.exists(test_path):
            print(f"program is broken: not enough files [{test_path}]")
            exit()
    for path in test_enough:
        test_path = os.path.join(main_path, path.format(sep = os.sep))
        if not os.path.exists(test_path):
            os.mkdir(test_path)
    