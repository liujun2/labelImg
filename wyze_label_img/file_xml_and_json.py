from xml.dom.minidom import parse
import xml.dom.minidom
import json

JSON_FILE_PATH = './json/categories.json'

def parse_xml_file_for_label(xml_file_path):
   label = []
   DOMTree = xml.dom.minidom.parse(xml_file_path)
   collection = DOMTree.documentElement
   movies = collection.getElementsByTagName("object")
   for movie in movies:
      name = movie.getElementsByTagName('name')[0]
      xmin = movie.getElementsByTagName('xmin')[0]
      ymin = movie.getElementsByTagName('ymin')[0]
      xmax = movie.getElementsByTagName('xmax')[0]
      ymax = movie.getElementsByTagName('ymax')[0]
      label.append({
         'category':name.childNodes[0].data,
         'xmin':xmin.childNodes[0].data,
         'ymin':ymin.childNodes[0].data,
         'xmax':xmax.childNodes[0].data,
         'ymax':ymax.childNodes[0].data
         })
   return label

def load_file_json(file_path):
   data = {}
   with open(file_path,"r") as f:
      data = json.loads(f.read())
      f.close()
   return data

def get_category_id_by_name(key_name,file_path = JSON_FILE_PATH):
   json_data = load_file_json(file_path)
   for x in json_data['categories']:
      if(key_name == x['name']):
         return x['id']

def get_image_id_by_file_name(file_name,file_path):
   json_data = load_file_json(file_path)
   for x in json_data['images']:
      if(file_name == x['file_name']):
         return x['id']

def save_file_json(json_content,file_path):
   with open(file_path,"w") as f:
      json_data = json.dumps(json_content,indent = 4)
      f.write(json_data)
      f.close

def get_label_from_xml_file(xml_file_path):
   label = parse_xml_file_for_label(xml_file_path)
   print(label)
   json_file_path = xml_file_path.replace('.xml','.json')
   json_data = load_file_json(json_file_path)
   print(json_data)
   print('image_file_name',xml_file_path)
   image_file_name = xml_file_path.split('files/')[1].replace('/','_').replace('.xml','.jpg')
   print('image_file_name 2 ',image_file_name)
   image_id = get_image_id_by_file_name(image_file_name,json_file_path)
   print('image_id',image_id)
   for l in label:
      print('l',l)
      category_id = get_category_id_by_name(l['category'])
      if(category_id):
         print('category_id',category_id)
         xmin = int(l['xmin'])
         xmax = int(l['xmax'])
         ymin = int(l['ymin'])
         ymax = int(l['ymax'])
         json_data['annotation'].append({
            "area":(xmax - xmin) * (ymax - ymin),
            "bbox":[
               xmin,
               ymin,
               xmax - xmin,
               ymax - ymin
            ],
            "category_id":category_id,
            "id":0,
            "image_id":image_id,
            "iscrowd":0
         })
   print(json_data)
   save_file_json(json_data,json_file_path)

if __name__ == '__main__':
   path = 'files/A4DA2230D83D/2019-05-10/A4DA2230D83D9b98ef1549f6438e_1557454218000_8_3/926473e4a6814c76b73d862b8bc621ce_f001.xml'
   get_label_from_xml_file(path)