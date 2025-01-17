import sys


def main():
    while(True):
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        arr = command.split(" ")
        if arr[0] == "exit" and arr[1] == "0": exit()
        if arr[0] == "echo":
            print(" ".join(arr[1:]))
        if arr[0] == "type":
            if arr[1] == "type" or arr[1] == "exit" or arr[1] == "echo":
                print(f"{arr[1]} is a shell builtin")
            else: print(f"{arr[1]}: not found") 
        else: print(f"{command}: command not found")



if __name__ == "__main__":
    main()
