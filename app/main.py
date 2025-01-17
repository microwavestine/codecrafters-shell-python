import sys


def main():
    while(True):
        sys.stdout.write("$ ")
        # Wait for user input
        command = input()
        if command == "exit 0": break
        if command.split(" ")[0] == "echo":
            print(command.split(" ")[1])
        print(f"{command}: command not found")
        # main()



if __name__ == "__main__":
    main()
