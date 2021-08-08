def create_name(path):
    with open(path, 'r') as txt_file:
        path = txt_file.readlines()
    return [line.split()[1] for line in path]


new_list = create_name("names.txt")
print(new_list)