import socket

class DatapointSenderWifi:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def addStringParam(self, string, param):
        return string + str(param) + ";"

    def sendDatapoint(self, dataPoint, systemID):
        # dataString format: x;y;timeYear;timeMonth;timeDay;timeHour;timeMinute;timeSecond;systemID;
        dataString = ""
        self.addStringParam(dataString, dataPoint.coordinate.x)
        self.addStringParam(dataString, dataPoint.coordinate.y)
        self.addStringParam(dataString, dataPoint.time.year)
        self.addStringParam(dataString, dataPoint.time.month)
        self.addStringParam(dataString, dataPoint.time.day)
        self.addStringParam(dataString, dataPoint.time.hour)
        self.addStringParam(dataString, dataPoint.time.minute)
        self.addStringParam(dataString, dataPoint.time.second)
        self.addStringParam(dataString, systemID)

        try:
            # Connect to server and send data
            self.sock.connect((self.host, self.port))
            self.sock.sendall(dataString.encode())
        finally:
            self.sock.close()
