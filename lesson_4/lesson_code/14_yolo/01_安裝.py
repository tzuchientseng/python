# pip install ultralytics // lytics 公司名稱
# yolov7 還需下載 原始檔，yolov8直接 pip install 即可
# yolov4 : darknet
# yolov6 : pytorch : 大陸接手
# yolov7 : pytorch : 中研究/俄羅斯 - 應該是大陸研發，2022
# yolov8 : pytorch : ultralytics - 2023

import torch as tc
print(tc.cuda.is_available()) # False (會非常久)
# 如果是 coco 資料集 , GPU 約 2天，CPU可能超過 2 個月

# 需手動安裝 pytorch : pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio===2.0.2+cu118 -f https://download.pytorch.org/whl/cu118/torch_stable.html
# 安裝 ultralytics 時，就是自動安裝無法使用 GPU 的 Pytorch 版本。
# 當後面手動安裝有 cuda 的 pytorch 時，會先移除無 cuda 的 pytorch, 再重新安裝有 cuda 的 pytorch

# **建議安裝步驟如下**
# 1. pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 torchaudio===2.0.2+cu118 -f https://download.pytorch.org/whl/cu118/torch_stable.html
# 2. pip install ultralytics

# 安裝 torch 時，若有出現 MemoryError, 請在 最後加上 --no-chahe-dir

