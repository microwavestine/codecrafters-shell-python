import sys


def main():
    # Uncomment this block to pass the first stage

    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        print(f"{command}: command not found\n")
        input()



if __name__ == "__main__":
    main()
