import os


def get_cwd():
    print(os.getcwd())

def change_dir() :
    os.chdir("/Users/mageshlookalike/Documents/Personal/AI/Python/src/modules")


def main():
    get_cwd()
    change_dir()
    get_cwd()


if __name__ == "__main__":
    main()