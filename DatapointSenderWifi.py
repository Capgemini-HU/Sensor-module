import requests

class DatapointSenderWifi:
    def __init__(self, destinationAdress):
        self.destinationAdress = destinationAdress

    def sendDatapoints(self, dataPoints, systemID):
        # TODO: send systemID
        data = {"datapoints":[]}
        for dataPoint in dataPoints:
            data["datapoints"].append(
                {"X": dataPoint.coordinate.x,
                 "Y": dataPoint.coordinate.y,
                 "Time": "{0}:{1}:{2}".format(dataPoint.time.hour, dataPoint.time.minute, dataPoint.time.second),
                 "Date": "{0}-{1}-{2}".format(dataPoint.time.day, dataPoint.time.month, dataPoint.time.year)})

        requests.post(self.destinationAdress, json=data)
