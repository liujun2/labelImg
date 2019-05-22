from get_image_from_rds import get_image_list_and_update_status_from_rds
from download_file_from_s3 import download_image_and_json_file

def main():
	list_img = get_image_list_and_update_status_from_rds()
	for img in list_img:
		print(img)
		download_image_and_json_file(img)

if __name__ == '__main__':
	main()