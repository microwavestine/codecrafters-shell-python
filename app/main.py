import sys
import os
import subprocess

def main():
    PATH = os.environ.get("PATH", "")
    paths = PATH.split(":")
    while(True):
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        arr = command.split(" ")
        if arr[0] == "exit" and arr[1] == "0": break
        elif arr[0] == "echo":
            print(" ".join(arr[1:]))
        elif arr[0] == "type":
            current_path = None
            for path in paths:
                if os.path.isfile(f"{path}/{arr[1]}"):
                    current_path = f"{path}/{arr[1]}"
            if arr[1] == "type" or arr[1] == "exit" or arr[1] == "echo":
                print(f"{arr[1]} is a shell builtin")
            elif current_path:
                print(f"{arr[1]} is {current_path}")
            else: print(f"{arr[1]}: not found")
        else:
            # Run external program
            current_path = None
            for path in paths:
                file_path = os.path.join(path, command)
                if os.path.isfile(file_path):
                    subprocess.run([arr[0], arr[1]])
            else:
                print(f"{arr[0]}: command not found")

if __name__ == "__main__":
    main()
