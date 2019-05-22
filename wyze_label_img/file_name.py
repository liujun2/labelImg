import os

def get_file_path_1_3(image_path):
	dir_path = os.path.split(image_path)[0]
	source_image_path = dir_path.rsplit('_', 1)[0] + '_3'
	image_name = os.path.split(image_path)[1]
	return source_image_path,image_name

def get_file_path_json(image_path):
	dir_path = os.path.split(image_path)[0].rsplit('_', 2)[0] + '_json'
	file_name = os.path.split(image_path)[1].rsplit('.', 1)[0] + '.json'
	return dir_path,file_name

if __name__ == '__main__':
	on = 'A4DA2230D83D/2019-05-10/A4DA2230D83D9b98ef1549f6438e_1557454218000_8_4/926473e4a6814c76b73d862b8bc621ce_f001.jpg'
	path,name = get_file_path_1_3(on)
	