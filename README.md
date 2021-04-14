# Training-Centernet
Training Centernet with custom COCO datasets.

## step 1. set up environmet.
- python == 3.8.5
- tensorflow == 2.3.1
- CUDA Toolkit == 10.1
- numpy == 1.18.5
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md
    - When you install object detection API, do pip install tf-models-official==2.3.0 before installing object detection API

## step 2-1. making custom datasets via supervisely and coco_keypoint_datasets.py
1) making label with locations of box and keypoints.
- https://supervise.ly/
![Screenshot from 2021-04-13 15-54-52](https://user-images.githubusercontent.com/62841284/114509720-d2182500-9c70-11eb-8196-5459212f4a4c.png)
- use keypoints class and rectangle class.
- download annotation json file after dealing with all images.

2) executing coco_keypoint_datasets.py for making COCO format json file.
- command: python coco_keypoint_datasets.py --path /your/root/path
- file directory should be
- root/
    - label/
    - image/

## step 2-2. making TFrecord datasets with coco datasets
