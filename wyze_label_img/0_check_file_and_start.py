from file_dir import get_file_in_dir_path
from file_dir import dir_path_is_exist
from file_dir import delete_dir
from file_dir import delete_files
from file_xml_and_json import get_label_from_xml_file
from get_image_from_rds import get_image_list_and_update_status_from_rds
from s3_file import download_image_and_json_file
from s3_file import upload_json_file_2_s3

handle_image_number = 100
FILE_PATH = './files'
FILTER_JPG = '.jpg'
FILTER_JSON = '.json'
FILTER_XML = '.xml'

def get_xml_file():
	dir_path_is_exist(FILE_PATH)
	xml_file = get_file_in_dir_path(FILE_PATH,FILTER_XML)
	return xml_file

def check_xml_file(xml_file,jpg_file,json_file):
	if(len(xml_file) > 0):
		print('合成xml和json')
		for index in range(0,len(xml_file)):
			print(xml_file[index])
			get_label_from_xml_file(xml_file[index])
			upload_json_file_2_s3(xml_file[index])
			delete_files([xml_file[index],jpg_file[index],json_file[index]])
	else:
		print('不合成')

def get_jpg_and_json():
	dir_path_is_exist(FILE_PATH)
	jpg_file = get_file_in_dir_path(FILE_PATH,FILTER_JPG)
	print('jpg number',len(jpg_file))
	json_file = get_file_in_dir_path(FILE_PATH,FILTER_JSON)
	print('json number',len(json_file))
	return jpg_file,json_file

def check_jpg_and_json_file(jpg_file,json_file):
	if len(jpg_file) != len(json_file) :
		print('删掉从新来')
		delete_dir(FILE_PATH)
		list_img = get_image_list_and_update_status_from_rds(handle_image_number)
		for img in list_img:
			print(img)
			download_image_and_json_file(img)
	elif(handle_image_number > len(jpg_file)):
		number_image_need = handle_image_number - len(jpg_file)
		print('需要补充的数',number_image_need)
		list_img = get_image_list_and_update_status_from_rds(number_image_need)
		for img in list_img:
			print(img)
			download_image_and_json_file(img)
	else:
		print('不用动')

def main():
	xml_file = get_xml_file()
	jpg_file,json_file = get_jpg_and_json()
	check_xml_file(xml_file,jpg_file,json_file)
	jpg_file,json_file = get_jpg_and_json()
	check_jpg_and_json_file(jpg_file,json_file)

if __name__ == '__main__':
	main()