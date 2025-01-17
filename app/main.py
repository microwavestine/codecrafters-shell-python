import sys
import os

def main():
    PATH = os.environ.get("PATH")
    while(True):
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        arr = command.split(" ")
        if arr[0] == "exit" and arr[1] == "0": break
        elif arr[0] == "echo":
            print(" ".join(arr[1:]))
        elif arr[0] == "type":
            paths = PATH.split(":")
            current_path = None
            for path in paths:
                if os.path.isfile(f"{path}/{arr[1]}"):
                    current_path = f"{path}/{arr[1]}"
            if arr[1] == "type" or arr[1] == "exit" or arr[1] == "echo":
                print(f"{arr[1]} is a shell builtin\n")
            elif current_path:
                print(f"{arr[1]} is {current_path}\n")
            else: print(f"{arr[1]}: not found\n") 
        else: print(f"{arr[0]}: command not found\n")



if __name__ == "__main__":
    main()
