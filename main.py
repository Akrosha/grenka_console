########################################################################
# some fabulous comment
########################################################################

import os

# main path need to navigate (line 10)
main_path = os.getcwd()

# navigate like for this shit (line 7)
# validate program for program validator
test_broken = ["functions", "functions{sep}validator.py"]
for path in test_broken:
    test_path = os.path.join(main_path, path.format(sep = os.sep))
    if not os.path.exists(test_path):
        print(f"program is broken: not enough files [{test_path}]")
        exit()

# validate program for other files
from functions.validator import validator
validator(main_path)

# version check
from functions.version_check import version_check
version_check(main_path)

# load and init the command handler
from functions.handler_cmd import Handler_cmd
handler_cmd = Handler_cmd(main_path)

# init all commands in handler that will find in main_path/commands/
test_path = os.path.join(main_path, "commands")

for root, dirs, files in os.walk(test_path):
    for file in files:
        if file.endswith(".py"):
            path = os.path.relpath(root, os.path.basename(main_path)).split("/")[1:]
            if "debug" in path:
                handler_cmd.add_debug(file[:-3], path)
            else:
                handler_cmd.add_command(file[:-3], path)

if __name__ == "__main__":
    # run
    enter = ""
    while True:
        enter = input("> ")
        if enter == "exit":
            break
        print(handler_cmd.run_command(enter))
    
    print("bye bye")
else:
    print("loaded from debug")
    def run(enter = ""):
        print(handler_cmd.run_command(str(enter)))