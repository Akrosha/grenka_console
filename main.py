########################################################################
# some fabulous comment
########################################################################

import os

# main path needs to navigate (line 10)
main_path = os.getcwd()

# navigate like for this shit (line 7)
test_path = os.path.join(main_path, "functions")
if not os.path.exists(test_path):
    print(f"program is broken: not enough files [{test_path}]")
    exit()

test_path = os.path.join(main_path, "functions", "handler_cmd.py")
if os.path.exists(test_path):
    from functions.handler_cmd import Handler_cmd
    handler_cmd = Handler_cmd()
else:
    print(f"program is broken: not enough files [{test_path}]")
    exit()

test_path = os.path.join(main_path, "commands")
if not os.path.exists(test_path):
    os.mkdir(test_path)

test_path = os.path.join(main_path, "commands")
command_files = os.listdir(test_path)
for file in command_files:
    if ".py" in file:
        handler_cmd.add_command(file[:-3])

test_path = os.path.join(main_path, "database")
if not os.path.exists(test_path):
    os.mkdir(test_path)

test_path = os.path.join(main_path, "languages")
if not os.path.exists(test_path):
    os.mkdir(test_path)

handler_cmd.run_command("test")