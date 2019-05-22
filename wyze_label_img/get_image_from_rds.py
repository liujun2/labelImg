from mysql_cam import get_image_list_for_label
from mysql_cam import update_images_label_status

def get_image_list_and_update_status_from_rds():
	image_catalog = []
	list_image = get_image_list_for_label()
	if(list_image and len(list_image) > 0):
		list_image_id = []
		for img in list_image:
			image_catalog.append(img[2])
			list_image_id.append(img[1])
		print(list_image_id)
		update_images_label_status(list_image_id)
	print(image_catalog)
	return image_catalog 

def main():
	get_image_list_and_update_status_from_rds()

if __name__ == '__main__':
	main()