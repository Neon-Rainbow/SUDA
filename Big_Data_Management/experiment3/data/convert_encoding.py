import chardet

# 检查文件编码
with open('romeo_and_juliet.txt', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"File encoding: {encoding}")

# 转换为 utf-8 编码
if encoding.lower() != 'utf-8':
    with open('romeo_and_juliet.txt', 'r', encoding=encoding) as f:
        text = f.read()
    with open('romeo_and_juliet.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("File has been converted to utf-8 encoding")