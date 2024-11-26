import cv2
import numpy as np
class MahalSdk():
    @staticmethod
    def read(filePath):
        #存在硬碟裏的檔案，是經過壓縮過的, 需使用 imdecode解壓縮
        img=cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        return img