########################################################################
# some fabulous comment
########################################################################

import os

# main path need to navigate (line 10)
main_path = os.getcwd()

# navigate like for this shit (line 7)
test_broken = ["functions", "functions{sep}validator.py"]
for path in test_broken:
    test_path = os.path.join(main_path, path.format(sep = os.sep))
    if not os.path.exists(test_path):
        print(f"program is broken: not enough files [{test_path}]")
        exit()

# validate program, code in 10-16 do it too
from functions.validator import validator
validator(main_path)

# load and init the command handler
from functions.handler_cmd import Handler_cmd
handler_cmd = Handler_cmd()

# init all commands in handler that will find in main_path/commands/
test_path = os.path.join(main_path, "commands")
command_files = os.listdir(test_path)
for file in command_files:
    if ".py" in file:
        handler_cmd.add_command(file[:-3])

# run
enter = ""
while True:
    enter = input("> ")
    if enter == "exit":
        break
    print(handler_cmd.run_command(enter))

print("bye bye")