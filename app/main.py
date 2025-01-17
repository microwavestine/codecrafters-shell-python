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
            valid_path = False
            for path in paths:
                if os.path.isfile(f"{path}/{arr[1]}"):
                    valid_path = True
            if arr[1] == "type" or arr[1] == "exit" or arr[1] == "echo":
                print(f"{arr[1]} is a shell builtin")
            elif valid_path:
                print(f"{arr[1]} is {path}/{arr[1]}")
            else: print(f"{arr[1]}: not found") 
        else: print(f"{arr[0]}: command not found")



if __name__ == "__main__":
    main()
