import cv2
import numpy as np

from Vector2 import Vector2

class PersonDetection:
    def __init__(self):
        # TODO: move to parameters
        self.confThreshold = 0.5
        self.nmsThreshold = 0.4
        self.inpWidth = 448
        self.inpHeight = 448
        classesFile = "coco.names"
        modelConfiguration = "yolov3.cfg"
        modelWeights = "yolov3.weights"

        with open(classesFile, 'rt') as f:
            self.classes = f.read().rstrip('\n').split('\n')

        self.net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        # Get the names of the output layers
        # Get the names of all the layers in the network
        layersNames = self.net.getLayerNames()
        # Get the names of the output layers, i.e. the layers with unconnected outputs
        self.outputNames = [layersNames[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

    def detectPersons(self, frame):
        # Returns the *relative* position of persons on an image.

        resultList = []

        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (self.inpWidth, self.inpHeight), [0, 0, 0], 1, crop=False)

        # Sets the input to the network
        self.net.setInput(blob)

        # Runs the forward pass to get output of the output layers
        outs = self.net.forward(self.outputNames)

        frameHeight = frame.shape[0]
        frameWidth = frame.shape[1]

        # Scan through all the bounding boxes output from the network and keep only the
        # ones with high confidence scores. Assign the box's class label as the class with the highest score.
        classIds = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    classIds.append(classId)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

        # Perform non maximum suppression to eliminate redundant overlapping boxes with
        # lower confidences.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confThreshold, self.nmsThreshold)
        for i in indices:
            # TODO: check if the detected objects are in fact persons...
            i = i[0]
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]

            center = Vector2(left + (width/2), top + (height/2))
            centerRelative = Vector2(center.x / self.inpWidth, center.y / self.inpHeight)
            resultList.append(centerRelative)
        return resultList
