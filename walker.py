import os


def get_files(path, files_per_dir=10):
    if not path.endswith('/'):
        path += '/'

    files = [s for s in os.listdir(path)
             if os.path.isfile(os.path.join(path, s))]

    files.sort(key=lambda s: os.path.getmtime(os.path.join(path, s)))

    # get the total number of files in the directory
    total_files = len(files)
    print(f'Total Files: {total_files}')

    # get the number of dirs to create
    num_of_dirs_to_create = (total_files - 1) // files_per_dir + 1
    print(f'Total Directories To Create: {num_of_dirs_to_create}')

    # move files using the files per dir into each newly created dir
    for i in range(num_of_dirs_to_create):
        print("creating dir: ", i)

        counter = 0
        # dir location in the same path
        location = path + f'folder_{i}'
        if not os.path.isdir(location):
            os.mkdir(location)

        if i == num_of_dirs_to_create - 1:
            # last dir, move the remaining files
            start_index = i * files_per_dir
            end_index = total_files
        else:
            start_index = i * files_per_dir
            end_index = (i + 1) * files_per_dir

        for j in range(start_index, end_index):
            old_file_location = f'{path}{files[j]}'
            if os.path.isfile(old_file_location):
                # file location in dir path
                new_file_location = location + f'/{files[j]}'

                print(f'Moving File: {files[j]} to {new_file_location}')
                os.rename(f'{path}{files[j]}', new_file_location)

                print(f'Moved File: {files[j]} to {new_file_location}')
                print('-------------------------------------------')
                counter += 1
            else:
                print(f'File: {files[j]} does not exist')
                print('-------------------------------------------')

        total_files -= counter

    print("done moving files")


if __name__ == '__main__':
    dir = input("Enter the path of the dir: ")
    num_of_files_per_dir = int(input("Enter the number of files per dir: "))
    get_files(dir, num_of_files_per_dir)