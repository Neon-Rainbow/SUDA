
def copy_files(f1, f2):
    file_raw = open(f1)
    file_copy = open(f2, "w")
    text = file_raw.read()
    file_copy.write(text)


if __name__ == "__main__":
    copy_files(r"copy.txt", r"new.txt")