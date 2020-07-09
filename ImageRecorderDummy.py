import cv2

class ImageRecorderDummy:
    def __init__(self, imageName):
        self.imageName = imageName

    def getImage(self):
        return cv2.imread(self.imageName, cv2.IMREAD_COLOR)
