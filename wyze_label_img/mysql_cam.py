import pymysql
from DBUtils.PooledDB import PooledDB

pool = PooledDB(
		creator=pymysql, 
		mincached=2, 
		maxcached=20, 
		host='wyze-ai-db-cluster.cluster-cedum2gcbyb7.us-west-2.rds.amazonaws.com', 
		user='root', 
		passwd='lc8aijr4DjF6', 
		db='wyze_ai_db_test', 
		port=3306
	)

def get_image_list_for_label(number_need):
	conn = pool.connection()
	cur=conn.cursor()
	SQL="SELECT * FROM wyze_cam_label WHERE (is_label = 2 or is_label = 3) ORDER BY image_id ASC limit %s;"
	cur.execute(SQL,[number_need])
	results=cur.fetchall()
	cur.close()
	conn.close()
	return results

def update_images_label_status(status,image_id_list):
	conn = pool.connection()
	cur=conn.cursor()
	SQL="UPDATE wyze_cam_label SET is_label = " + str(status) + " WHERE image_id IN (%s)" % ','.join(['%s'] * len(image_id_list))
	cur.execute(SQL,image_id_list)
	conn.commit()
	cur.close()
	conn.close()

if __name__ == '__main__':
	data = get_image_list_for_label()
	print(data)
	# update_images_label_status([0,1])