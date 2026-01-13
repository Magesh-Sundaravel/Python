from pathlib import Path



def basics_func() -> None:
    print(f"Current working directory: {Path.cwd()}")
    print(f"Home directory : {Path.home()}")
    
def checks_path() -> None:
    path = Path("/Users")
    print(f"Whether the specified path exists or not: {path.exists()}")

    path = Path("/Users(maja)")
    print(f"Whether the specified path exists or not: {path.exists()}")

def iterate_repo() -> None:
    new_path = Path.cwd()

    files = [x.name  for x in new_path.iterdir() if new_path.is_dir()]
    print(f"Files in the repository: {files}")

    stems = [x.stem  for x in new_path.iterdir() if new_path.is_dir()]
    print(f"Stems in the repository: {stems}")

    suffixes = [x.suffix  for x in new_path.iterdir() if new_path.is_dir()]
    print(f"suffixes in the repository: {suffixes}")

def check_file_or_repo() -> None:
    path = Path("sample.txt")

    print(f"Check is it a file: {path.is_file()}")
    print(f"Check is it a Directory: {path.is_dir()}")


def resolve_path() -> None:
    path = Path("sample.txt") 
    print(f"Resloved the absolute path into relative path: {path.resolve()}")

def create_and_delete_file() -> None:
    new_file = Path.cwd() / "Sample_1.txt"
    new_file.touch()
    print(f"Sample text file is created: {new_file}")

    new_file.unlink()
    print(f"The same sample text file is deleted from directory: {Path.cwd()}")

def create_and_delete_dir() -> None:
    new_dir = Path.cwd() / "new_dir"
    new_dir.mkdir(exist_ok=True)
    print(f"New directory  is created: {new_dir} ")

    new_dir.rmdir()
    print(f"Same new directory  is deleted: {Path.cwd()}")





def main() :
    basics_func()
    checks_path()
    iterate_repo()
    check_file_or_repo()
    resolve_path()
    create_and_delete_file()
    create_and_delete_dir()
    print("This shows the basics of Pathlib Library from Python")


if __name__ == "__main__":
    main()
