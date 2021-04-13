# Training-Centernet
Training Centernet with custom COCO datasets.

step 1. set up environmet.

step 2. making custom datasets via supervisely and coco_keypoint_datasets.py
1) making label with locations of box and keypoints.
- https://supervise.ly/
![Screenshot from 2021-04-13 15-54-52](https://user-images.githubusercontent.com/62841284/114509720-d2182500-9c70-11eb-8196-5459212f4a4c.png)
- use keypoints class and rectangle class.
- download annotation json file after dealing all images.

2) executing coco_keypoint_datasets.py for making COCO format json file.
- command: python coco_keypoint_datasets.py --path /your/root/path
- file directory should be
- root/
    - label/
    - image/

