import sys
import os
from pathlib import Path
import shlex
import subprocess

def findExecutable(command):
    paths = os.getenv("PATH", "").split(os.pathsep)
    for path in paths:
        executablePath = os.path.join(path, command)
        if os.path.isfile(executablePath):
            return executablePath
    return None

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
        command = line.split()

        if command[0] == "exit" and command[1] == "0": break
        elif command[0] == "echo":
            print(" ".join(shlex.split(line)[1:]))
        elif command[0] == "type":
            current_path = find_path(command[1])
            if command[1] == "type" or command[1] == "exit" or command[1] == "echo" or command[1] == "pwd":
                print(f"{command[1]} is a shell builtin")
            elif current_path:
                print(f"{command[1]} is {current_path}")
            else: print(f"{command[1]}: not found")
        elif command[0] == "pwd":
            sys.stdout.write(os.getcwd() + "\n")
        elif line.startswith('"') or line.startswith("'"):
                command_list = shlex.split(line, posix=True)
                file_path = command_list[1]
                file = open(file_path, "r")
                sys.stdout.write(f"{file.read()}")
                file.close()
        elif command[0] == "cd":
            path = Path(command[1])
            if command[1].startswith("~"):
                path = path.expanduser()

            if path.exists() and path.is_dir():
                os.chdir(path)
            else:
                sys.stdout.write(f"{command[0]}: {command[1]}: No such file or directory\n")
        else:
            # Run external program
            program = find_command(command[0])
            if program:
                args = shlex.split(line)
                executablePath = findExecutable(args[0])
                if executablePath:
                    result = subprocess.run(args, capture_output=True, text=True)
                    print(result.stdout, end="")
            else:
                print(f"{command[0]}: command not found")
        sys.stdout.flush()
if __name__ == "__main__":
    main()
