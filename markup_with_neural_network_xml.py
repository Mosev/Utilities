from detectors.yolo_detector.inference.yolo_detector import ObjectDetection
import os
import cv2
import copy
import xml.etree.ElementTree as ET

path_to_images = r"F:\NOT_LABELED"
path_to_save_xml = r"F:\ANN"
master_body = ET.parse("body.xml")
# master_root = body.getroot()
# body.write("test.xml")
images = os.listdir(path_to_images)
FireDetector = ObjectDetection()
for image_name in images:
    body = ET.parse("body.xml")
    root = body.getroot()
    image_path = os.path.join(path_to_images, image_name)
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    for elem in root.iter('folder'):
        elem.text = path_to_images.split('\\')[-1]
    for elem in root.iter('filename'):
        elem.text = image_name
    for elem in root.iter('path'):
        elem.text = image_path
    for elem in root.iter('width'):
        elem.text = str(width)
    for elem in root.iter('height'):
        elem.text = str(height)
    output_objects_array, detected_objects_image_array, all_boxes = FireDetector.detect_from_image(image=image)
    if len(all_boxes) != 0:
        for object in all_boxes:
            name = object['name']
            xmin, ymin, xmax, ymax = object['box_points']
            object = ET.SubElement(root, 'object')
            object_name = ET.SubElement(object, 'name')
            bndbox = ET.SubElement(object, 'bndbox')
            xmin_xml = ET.SubElement(bndbox, 'xmin')
            ymin_xml = ET.SubElement(bndbox, 'ymin')
            xmax_xml = ET.SubElement(bndbox, 'xmax')
            ymax_xml = ET.SubElement(bndbox, 'ymax')

            object_name.text = name
            xmin_xml.text = str(xmin)
            ymin_xml.text = str(ymin)
            xmax_xml.text = str(xmax)
            ymax_xml.text = str(ymax)


    else:
        pass
    xml_name = os.path.join(path_to_save_xml,image_name.split('.')[0]+'.xml')
    if os.path.isfile(xml_name):
        pass
    else:
        body.write(xml_name)
    # cv2.imshow("frame", drawn_image)
    # cv2.waitKey(1)
# cv2.destroyAllWindows()




