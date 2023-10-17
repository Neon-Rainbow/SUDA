def append_file(f1, f2):
    file_1 = open(f1, "a")
    file_2 = open(f2)
    text = file_2.read()
    file_1.write(text)
    file_1.close()
    file_2.close()


if __name__ == "__main__":
    append_file(r"cat1.txt", r"cat2.txt")