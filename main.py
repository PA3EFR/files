__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Opdracht 1
import os
import shutil


def clean_cache():
    dir_path = './cache'
    if os.path.isdir('./cache') == True:
        shutil.rmtree(dir_path)  # delete folder /cache
        os.mkdir(dir_path)  # create folder /cache
        print(f"successfully cleared folder {dir_path[1:]}")
    else:
        os.mkdir(dir_path)  # create folder /cache
        print(f"successfully created folder {dir_path[1:]}")
    return


# Opdracht 2
import time


def cache_zip(zip_file_path, cache_dir_path):
    clean_cache()
    wait(3)
    from zipfile import ZipFile
    ZipFile(zip_file_path).extractall(cache_dir_path)
    print("files unzipped - ready. Files include:")
    return


def wait(seconds):
    print(f"waiting {seconds} seconds for Windows to realize internal operations....")
    time.sleep(seconds)
    return


zip_file_path = os.path.abspath("data.zip")
cache_dir_path = os.path.join("cache")
cache_zip(zip_file_path, cache_dir_path)


# Opdracht 3
def cached_files():
    file_list = ""
    os.chdir('cache')
    for file in os.listdir():
        file_list = file_list + os.path.abspath(file) + " "
    return file_list


cached_files = cached_files()


# # Opdracht 4

def Convert(string):
    li = list(string.split(" "))
    return li


def find_password(cached_files):
    for i in cached_files:
        with open(i) as fp:
            line = fp.readline()
            while line:
                if "password" in line:
                    signal = line
                    file_number = i
                else:
                    pass
                line = fp.readline()
    return signal, file_number


cached_files = Convert(cached_files)  # Conversion from string tot list of cached files
print(cached_files.pop())
print(find_password(cached_files))
