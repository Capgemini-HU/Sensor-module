from ImageRecorderDummy import ImageRecorderDummy
from PersonDetection import PersonDetection
from DataPointSenderDummy import DataPointSenderDummy

from CameraClient import CameraClient


if __name__ == '__main__':
    imageRecorder = ImageRecorderDummy("testImage.jpg")
    personDetection = PersonDetection()
    dataPointSender = DataPointSenderDummy("testImage.jpg")


    cameraClient = CameraClient(0, imageRecorder, personDetection, dataPointSender, 10)

    cameraClient.update()
