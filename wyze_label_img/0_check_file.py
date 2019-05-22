from file_dir import get_file_in_dir_path

handle_image_number = 100

def main():
	jpg_file = get_file_in_dir_path('./files','.jpg')
	print('jpg number',len(jpg_file))
	json_file = get_file_in_dir_path('./files','.json')
	print('json number',len(json_file))
	if len(jpg_file) != len(json_file) :
		print('删掉从新来')
	else:
		print('需要补充的数',handle_image_number - len(jpg_file))

if __name__ == '__main__':
	main()