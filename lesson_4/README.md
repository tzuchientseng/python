# tensorflow 為一台強大的計算機，將指令送入 cudnn, 再送cuda ，再交由 GPU 計算

Cuda 是 Python 與顯卡溝通的橋樑，可以看成是顯卡的驅動程式，啟動顯卡的快速計算功能
Tensorflow : 一台強大的計算機(神經網路框架framework)
Python => tensorflow => cudnn => CUDA => 顯卡
看見的神經網路框架 : Tensorflow, pyTorch。Tensorflow由 Google開發。但今年的 yolo/yolact 由原本的 darknet 改成 pyTorch
先移除舊版本11.8
安裝cuda前，必需把華碩 tweak或msi  調變功率的程式關掉
`https://developer.nvidia.com/cudnn`
Download cudnn/然後要註冊再登入(記得收 mail Verify)
Cudnn for cuda 12.x/Windows(zip)
解開後，將bin, include, lib等目錄 copy 到 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.1之下
Pycharm記得先關掉，再重新進入

	TensorFlow: 2.10.1
	CUDA: 11.8
	cuDNN: 8.6 (檔案去覆蓋	CUDA: 11.8)
	GPU: NVIDIA GeForce RTX 3050
	Python: 3.8 的虛擬環境

# 每次開新專案時，Pycharm 的 download-pre build，千萬別下載，否則會變成簡體中文
# New Project ... 新項目，是大陸用語
# CUDA ：11.8 最穩定。
# CUDA ：12.1 版本，cusolver64_12.dll，但 tensorflow 最新版還是去找 cusolver64_11.dll。
# tensorflow : 2.10.1，pip install tensorflow==2.10.1
`.\venv\Scripts\python -m pip install tensorflow==2.10.1`
# CUDA Toolkit: 11.2
# cuDNN: 8.1
	
`py --list`
`nvidia-smi` (顯卡檢測)

創建一個基於 Python 3.8 的虛擬環境：
`py -3.8 -m venv venv`
激活虛擬環境：
`.\venv\Scripts\activate`
驗證版本：
python --version
`此時應顯示 Python 3.8`。
退出虛擬環境：
`deactivate`

// `pip install tensorflow==2.10.1` (這樣會用系統版本去裝)
// `python3.8 -m pip install tensorflow==2.10.1`(全域安中 python 3.8)
`.\venv\Scripts\python -m pip install tensorflow==2.10.1`
`.\venv\Scripts\python -m pip install matplotlib`
`python -m pip install <package>` (在虛擬環境安裝)

`pip list`
`.\venv\Scripts\python -m pip list`

// `py -3.8 XXX.py` (原本寫法)
`.\venv\Scripts\python test.py`

`python -m pip install --upgrade pip`
`pip install opencv-python`

`C:/Users/GOOD-PC/AppData/Local/Microsoft/WindowsApps/python3.12.exe -m pip install XXX`
