with open('test.txt', 'r') as file:
    data = file.read()
    entries = data.split('@')[1:]  # 忽略文件开头的内容
    print(f"Total number of references: {len(entries)}")
