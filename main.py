from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo3.cfg", "load": "bin/yolo3.weights", "threshold": 0.1}

tfnet = TFNet(options)

imgcv = cv2.imread("./data/mountain.jpg")
result = tfnet.return_predict(imgcv)
print(result)
