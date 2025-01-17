import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    # Wait for user input
    command = input()
    print(f"{command}: command not found\n")
    input()

    main()



if __name__ == "__main__":
    main()
