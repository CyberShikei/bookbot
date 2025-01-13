from interface.cli import start_cli


def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    start_cli(file_contents)


if __name__ == "__main__":
    main()
