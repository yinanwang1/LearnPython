
import os


def findAllFile(path):
    for root, ds, fs in os.walk(path):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


def replaceGitPath(path):
    with open(path, mode="r") as file:
        contents = file.read()
        contents = contents.replace("git@code.dbike.co", "git@code.youxu.cc")

    with open(path, mode="w") as file:
        file.write(contents)


def main():
    path = "/Users/arthurwang/Git"
    for i in findAllFile(path):
        if i.endswith(".git/config"):
            replaceGitPath(i)


if __name__ == "__main__":
    main()
    # replaceGitPath("/Users/arthurwang/Desktop/test.txt")



