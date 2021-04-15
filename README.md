# Training-Centernet
Training Centernet with custom COCO datasets.

## step 1. set up environmet.
- python == 3.8.5
- tensorflow == 2.3.1
- CUDA Toolkit == 10.1
- numpy == 1.18.5
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md
    - When you install object detection API, do pip install tf-models-official==2.3.0 before installing object detection API
- If an error "~expected "required", "optional", or "repeated"." occurs, do following steps
    - home/user$ mkdir protoc_3.3
    - cd protoc_3.3
    - home/user/protoc_3.3$ wget wget https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip
    - home/user/protoc_3.3$ unzip protoc-3.3.0-linux-x86_64.zip
    - home/user/protoc_3.3$ cd ../models/
    - home/user/protoc_3.3$ /home/user/protoc_3.3/bin/protoc object_detection/protos/*.proto --python_out=.

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
- change the parsing and making up json code upto your purpose.

## step 2-2. making TFrecord datasets with coco datasets
- use "models/research/object_detection/dataset_tools/python create_coco_tf_record.py" for making TFrecord
- example usage is bellow
- python create_coco_tf_record.py --logtostderr \
      --train_image_dir="${TRAIN_IMAGE_DIR}" \
      --val_image_dir="${VAL_IMAGE_DIR}" \
      --test_image_dir="${TEST_IMAGE_DIR}" \
      --train_annotations_file="${TRAIN_ANNOTATIONS_FILE}" \
      --val_annotations_file="${VAL_ANNOTATIONS_FILE}" \
      --testdev_annotations_file="${TESTDEV_ANNOTATIONS_FILE}" \
      --output_dir="${OUTPUT_DIR}" 
      
## step 3 modify your pipeline config file 
- files are located on "models/research/object_detection/configs/tf2"
- modify your pipeline upto model
    - ex) feature_extractor, keypoints, number of keypoints, image size, label_map .....
    - ![Screenshot from 2021-04-15 09-02-12](https://user-images.githubusercontent.com/62841284/114795666-13701800-9dca-11eb-847e-6861f1a46c9e.png)

 
