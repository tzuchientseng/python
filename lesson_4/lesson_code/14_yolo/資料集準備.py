# http://images.cocodataset.org/zips/train2017.zip
# http://images.cocodataset.org/zips/val2017.zip
# http://images.cocodataset.org/zips/test2017.zip
# https://github.com/WongKinYiu/yolov7/releases/download/v0.1/coco2017labels-segments.zip
'''
資料集 (datasets) 製作
1. coco2017labels-segments.zip解壓縮至此
2. train2017.zip 此解縮至此，將 train2017目錄改成 images, 移到 coco/train 之下
3. val2017.zip 此解縮至此，將 val2017目錄改成 images, 移到 coco/valid 之下
4. test2017.zip 此解縮至此，將 test2017目錄改成 images, 移到 coco/test 之下
5. coco/labels/train2017 改成 labels, 移到 coco/train 之下
6. coco/labels/val2017 改成 labels, 移到 coco/valid 之下
7. 在 coco 下新增 data.yaml 檔，內容如下
請記得更改 train/val/test 三個目錄
train: e:/python_ai/yolov8_coco/coco/train/images
val: e:/python_ai/yolov8_coco/coco/valid/images
test: e:/python_ai/yolov8_coco/coco/test/images
# number of classes
nc: 80

# class names
names: [ 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
         'hair drier', 'toothbrush' ]

8. 下載 yolov8n.pt : https://github.com/ultralytics/ultralytics
9. 新增 02_coco模型訓練.py
'''
