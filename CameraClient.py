from datetime import datetime, timedelta

from Datapoint import Datapoint

# TODO: 3d map from multiple camera's functionality
class CameraClient:
    def __init__(self, systemID, imageRecorder, personDetection, datapointSender, minTimeInterval):
        self.lastPictureTime = datetime.min()
        self.systemID = systemID
        self.imageRecorder = imageRecorder
        self.personDetection = personDetection
        self.datapointSender = datapointSender
        self.minTimeInterval = minTimeInterval

    def update(self):
        # check time
        if((datetime.now() - self.lastPictureTime).total_seconds() < self.minTimeInterval):
            return

        # take picture
        image = self.imageRecorder.getImage()
        self.lastPictureTime = datetime.now()

        # detect persons
        personList = self.personDetection.detectPersons(image)
        # TODO: convert to 3d map

        # send data
        for personPos in personList:
            self.datapointSender.sendDatapoint(Datapoint(personPos, self.lastPictureTime), self.systemID)
