import sys
import os
from pathlib import Path
import shlex

def find_command(command):
    paths = os.environ.get('PATH') or ""
    for path in map(lambda s: f"{s}/{command}", paths.split(":")):
        if Path(path).exists():
            parts = path.split("/")
            return parts[-1]
    return None

def find_path(command):
    paths = os.environ.get('PATH') or ""
    for path in map(lambda s: f"{s}/{command}", paths.split(":")):
        if Path(path).exists():
            return path
    return None

def main():
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input

        line = input()
        try:
            command, args = line.split(maxsplit=1)
        except:
            command = line
        is_program = False

        if command[0] == "exit" and command[1] == "0": break
        elif command[0] == "echo":
            args = shlex.split(args)
            for i in range(len(args)):
                if (args[i].startswith("'") and args[i].endswith("'")) or (
                    args[i].startswith('"') and args[i].endswith('"')
                ):
                    args[i] = args[i][1:-1]
            print(" ".join(args))
        elif command[0] == "type":
            current_path = find_path(command[1])
            if command[1] == "type" or command[1] == "exit" or command[1] == "echo" or command[1] == "pwd":
                print(f"{command[1]} is a shell builtin")
            elif current_path:
                print(f"{command[1]} is {current_path}")
            else: print(f"{command[1]}: not found")
        elif command[0] == "pwd":
            sys.stdout.write(os.getcwd() + "\n")
        elif command[0] == "cd":
            path = Path(command[1])
            if command[1].startswith("~"):
                path = path.expanduser()

            if path.exists() and path.is_dir():
                is_program = True
                os.chdir(path)
            else:
                sys.stdout.write(f"{command[0]}: {command[1]}: No such file or directory\n")
        else:
            # Run external program
            program = find_command(command[0])
            if program:
                is_program = True
                os.system(" ".join([program, *command[1:]]))
            else:
                print(f"{command[0]}: command not found")
        sys.stdout.flush()
if __name__ == "__main__":
    main()
