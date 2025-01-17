import sys


def main():
    while(True):
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        if command.split(" ")[0] == "exit" and command.split(" ")[1] == "0": exit()
        if command.split(" ")[0] == "echo":
            arr = command.split(" ")
            print(" ".join(arr[1:]))
        else: print(f"{command}: command not found")



if __name__ == "__main__":
    main()
