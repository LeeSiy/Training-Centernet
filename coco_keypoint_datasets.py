import json
import os
import datetime
import argparse

#construction of directoryfile
# >> ./2012-04-09/
#                  >> label/
#                  >> image/

parser = argparse.ArgumentParser(description="test code")
parser.add_argument('--path',required=False, help="input path of root file")
args = parser.parse_args()

if args.path:
    base_path = args.path
else:
    base_path  = '/home/softonnet/temp/label' # default value of root path


suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
save_name = "_".join([suffix,"output.json"]) # output file name

#making json for saving------------------------------------------------------------------------------------------------------
coco_data = {}
coco_data['info'] = []
coco_data['info'].append({
		"description": "shellfish Dataset",
		"url": "",
		"version": "1.0",
		"year": 2021,
		"contributor": "",
		"date_created": "2021"
	})
coco_data['licenses'] = []
coco_data['licenses'].append({
		"url": "http://softonnet.com",
		"id": 1,
		"name": ""
	})
coco_data['images'] = []
coco_data['annotations'] = []
coco_data['categories'] = []
coco_data['categories'].append(
            {
		"supercategory": "oyster",
		"id": 1,
		"name": "oyster",
		"keypoints": ["right", "left", "bottom", "top"],
		"skeleton": [
			[3, 1],
			[3, 2],
			[4, 1],
			[4, 2]
		]
            })
coco_data['categories'].append({
                "supercategory": "scallop",
		"id": 2,
		"name": "scallop",
		"keypoints": ["right", "left", "bottom", "top"],
		"skeleton": [
			[3, 1],
			[3, 2],
			[4, 1],
			[4, 2]
                ]
            })

#for reading json annotation
count = 0
file_list = os.listdir(os.path.join(base_path))
for filename in file_list:
    file_path = os.path.join(base_path,filename)
    temp1 = file_list[0][:-5]
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)
        class_name = json_data['objects'][0]['classTitle']
        box=[json_data['objects'][1]['points']['exterior'][0][0],
             json_data['objects'][1]['points']['exterior'][0][1],
             json_data['objects'][1]['points']['exterior'][1][0]-json_data['objects'][1]['points']['exterior'][0][0],
             json_data['objects'][1]['points']['exterior'][1][1]-json_data['objects'][1]['points']['exterior'][0][1]]
        width=json_data['size']['width']
        height=json_data['size']['height']
        top_x=int(json_data['objects'][0]['nodes']['de6081dd-2c3e-4ca7-a952-e353fb419f66']['loc'][0])
        top_y=int(json_data['objects'][0]['nodes']['de6081dd-2c3e-4ca7-a952-e353fb419f66']['loc'][1])
        bottom_x=int(json_data['objects'][0]['nodes']['106e60ef-8762-4a17-aab1-1f806ea75480']['loc'][0])
        bottom_y=int(json_data['objects'][0]['nodes']['106e60ef-8762-4a17-aab1-1f806ea75480']['loc'][1])
        left_x=int(json_data['objects'][0]['nodes']['a1316931-6476-40ee-a1e0-308bd81a544b']['loc'][0])
        left_y=int(json_data['objects'][0]['nodes']['a1316931-6476-40ee-a1e0-308bd81a544b']['loc'][1])
        right_x=int(json_data['objects'][0]['nodes']['f9aea33a-3f72-4412-8d24-42a96df6a092']['loc'][0])
        right_y=int(json_data['objects'][0]['nodes']['f9aea33a-3f72-4412-8d24-42a96df6a092']['loc'][1])
        coco_data['images'].append( {
                        "license": 0,
                        "file_name": "",
                        "coco_url": "",
                        "height": 0,
                        "width": 0,
                        "date_captured": "",
                        "flickr_url": "",
                        "id": 0
                })

        coco_data['annotations'].append({"segmentation": [
                                []
                        ],
                        "num_keypoints": 0,
                        "area": 0.0,
                        "iscrowd": 0,
                        "keypoints": [],
                        "image_id": 0,
                        "bbox": [],
                        "category_id": 0,
                        "id": 0})
        coco_data['images'][count]["license"] = 1
        coco_data['images'][count]["file_name"] = file_list[0][:-5]
        coco_data['images'][count]["coco_url"] = ""
        coco_data['images'][count]["height"] = height
        coco_data['images'][count]["width"] = width

        coco_data['images'][count]["date_captured"] = "2021-04-01 12:00:00",
        coco_data['images'][count]["flickr_url"] = ""
        coco_data['images'][count]["id"] = count + 1

        coco_data['annotations'][count]["segmentation"] = [[]]
        coco_data['annotations'][count]["num_keypoints"] = 4
        coco_data['annotations'][count]["area"] = 0.0
        coco_data['annotations'][count]["iscrowd"] = 0
        coco_data['annotations'][count]["keypoints"] = [right_x,right_y,2,left_x,left_y,2,bottom_x,bottom_y,2,top_x,top_y,2]
        coco_data['annotations'][count]["image_id"] = count+1
        coco_data['annotations'][count]["bbox"] = box


        # classifing categories with classTitle
        if 'oyster' in class_name:
            coco_data['annotations'][count]["category_id"] = 1
        elif 'scallop' in class_name :
            coco_data['annotations'][count]["category_id"] = 2
        else:
            coco_data['annotations'][count]["category_id"] = 99

        coco_data['annotations'][count]["id"] = count +10001
        count+=1

#saving path of output json file
output_path = os.path.join(base_path,save_name)
print("saved ", save_name)
with open(output_path,'w') as outfile:
    json.dump(coco_data, outfile,indent="\t")

