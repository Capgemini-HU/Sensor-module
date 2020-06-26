# Capgemini-094 Sensor module
Deze repository is voor het ontwikkelen van de software voor op de sensor module.

Op de sensor worden foto's gemaakt, mensenvormen herkend en posities hiervan verstuurd naar de server module.

Mensenvormen herkennen wordt gedaan door middel van OpenCV en YoloV3.

# Gebruik

Om mensenvormen te herkennen in een foto kan het volgende commando gebruikt worden.


```
python3 yoloV3.py --image=street.jpg
```

Dit genereert een bestand genaamt "street_yolo_out_py.jpg".

Om een foto te maken.

```
python3 take_pic.py
```

Deze code gebruikt "fswebcam" op de Raspberry Pi. Dit is een ubuntu package en werkt dus niet op windows.
Dit genereert een jpg in dezelfde folder.
