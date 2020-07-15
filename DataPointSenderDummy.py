import cv2

class DataPointSenderDummy:
    def __init__(self, backgroundImagePath):
        self.backgroundImagePath = backgroundImagePath

    def sendDatapoints(self, dataPoints, systemID):
        image = cv2.imread(self.backgroundImagePath, cv2.IMREAD_COLOR)
        for dataPoint in dataPoints:
            pointX = int(round(dataPoint.coordinate.x))
            pointY = int(round(dataPoint.coordinate.y))
            cv2.line(image,
                     (pointX - 1, pointY - 1),
                     (pointX, pointY),
                     color=(0,0,255),
                     thickness=5)
        cv2.imshow("dataPoints", image)
        cv2.waitKey(0)
