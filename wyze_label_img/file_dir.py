import os
import shutil

folder_file_path = []

def clean_file_path():
	folder_file_path.clear()

def ergodic_folder(folder_path):
	list = os.listdir(folder_path)
	for l in list:
		path = folder_path + '/' + l
		if os.path.isfile(path):
			folder_file_path.append(path)
		if os.path.isdir(path):
			ergodic_folder(path)

def file_filter_contain(file_path, filter_str):
    file_path_new = []
    for fp in file_path:
        if filter_str in fp:
            file_path_new.append(fp)
    file_path_new.sort()
    return file_path_new

def get_file_in_dir_path(dir_path,filter_str=''):
	clean_file_path()
	ergodic_folder(dir_path)
	if len(filter_str) > 0:
		return file_filter_contain(folder_file_path,filter_str)
	else:
		return folder_file_path

def dir_path_is_exist(file_path):
	if(os.path.exists(file_path) == False):
		os.makedirs(file_path)

def delete_dir(dir_path):
	shutil.rmtree(dir_path)

def delete_file(file_path):
	if(os.path.exists(file_path)):
		os.remove(file_path)

def delete_files(files_path):
	for file in files_path:
		delete_file(file)