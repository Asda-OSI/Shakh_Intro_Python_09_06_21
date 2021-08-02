import os

# current_dir = os.getcwd()
# print(current_dir)
#
# list_dir = os.listdir('../homeworks')
# print(list_dir)
#
# tmp_path = os.path.join('homeworks', 'tmp', 'test_2')
# print(tmp_path)


def get_files_from_dir(base_dir: str, full_path=True) -> list:
    list_dir = os.listdir(base_dir)
    files = []
    for file_object in list_dir:
        path_object = os.path.join(base_dir, file_object)
        if os.path.isfile(path_object):
            files.append(f'{path_object if full_path else f"{path_object}:{file_object}"}')
    print(files)
    return files


# alphabet_files = get_files_from_dir('../alphabet')
# homeworks_files = get_files_from_dir('../homeworks', full_path=False)

# def create_dir(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass

# os.makedirs('test_3_dir/test_4_dir', exist_ok=True)

# FINISH