import os
import sys
import boto3

from file_name import get_file_path_1_3
from file_name import get_file_path_json

s3 = boto3.client('s3')

BUCKET_NAME = 'wyze-ai-repository'
FILE_PATH = 'WyzeCam/201905/'
FOLD_PATH_3 = 'ImageFromVideo/'
FOLD_PATH_JSON = 'ResultJsonFile/'
FOLD_INPUT = 'files/'

def download_file_from_s3(object_name,file_name):
	with open(file_name, 'wb') as f:
		s3.download_fileobj(BUCKET_NAME,object_name,f)

def get_file_path_by_file_object_name(file_name):
	file_path = file_name.replace(file_name.split('/')[-1],'')
	return file_path

def dir_path_is_exist(file_path):
	# file_path = get_file_path_by_file_object_name(file_name)
	if(os.path.exists(file_path) == False):
		os.makedirs(file_path)

def download_image_and_json_file(image_path):
	image_file_path,image_file_name = get_file_path_1_3(image_path)
	image_path_remote = FILE_PATH+FOLD_PATH_3+image_file_path+'/'+image_file_name
	image_path_local = FOLD_INPUT + image_file_path+'/'+image_file_name
	dir_path_is_exist(FOLD_INPUT + image_file_path)
	download_file_from_s3(image_path_remote,image_path_local)

	json_file_path,json_file_name = get_file_path_json(image_path)
	json_path_remote = FILE_PATH+FOLD_PATH_JSON+json_file_path+'/'+json_file_name
	json_path_local = FOLD_INPUT + image_file_path+'/'+json_file_name
	dir_path_is_exist(FOLD_INPUT + image_file_path)
	print(json_path_local)
	download_file_from_s3(json_path_remote,json_path_local)

if __name__ == '__main__':
	image_path = 'A4DA2230D83D/2019-05-10/A4DA2230D83D9b98ef1549f6438e_1557454218000_8_4/926473e4a6814c76b73d862b8bc621ce_f011.jpg'
	download_image_and_json_file(image_path)

