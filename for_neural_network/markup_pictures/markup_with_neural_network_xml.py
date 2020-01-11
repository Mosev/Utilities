# from detectors.yolo_detector.inference.yolo_detector import ObjectDetection
import xml.etree.ElementTree as ET
import os
import cv2

path_to_images = r"F:\NOT_LABELED"
path_to_save_xml = r"F:\ANN"
FireDetector = ObjectDetection()

class MarkupPicturesXml(path_to_images, path_to_save_xml, detector body="body.xml"):
    def __init__(self):
        self.path_to_images = path_to_images
        self.path_to_save_xml = path_to_save_xml
        self.body = body
        self.images = os.listdir(path_to_images)
        self.detector = detector

    def set_sub_elements_for_parent(self, parent, *args):
        childs = set()
        for child in args:
            child = ET.SubElement(parent, child)
            childs.append(child)
        return childs

    def text_in_tag(self, parent, child_tag_name, text):
        etree.SubElement(parent, child_tag_name).text = text

    def get_all_boxes(self):
        _, _, all_boxes = detector.detect_from_image(image=image)
        return all_boxes
      
    def __getitem__(self):
        return self.images
    
if __name__ == "__main__":
    test = MarkupPicturesXml(path_to_images, path_to_save_xml, FireDetector)
    for image_name in test:
        body = ET.parse("body.xml")
        root = body.getroot()
        image_path = os.path.join(path_to_images, image_name)
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        test.text_in_tag(root, "folder", image_name)
        test.text_in_tag(root, "path", image_path)
        test.text_in_tag(root, "width", str(width))
        test.text_in_tag(root, "height", str(height))
        all_boxes = text.get_all_boxes(image)
        if len(all_boxes) != 0:
            for detected_object_list in all_boxes:
                name = detected_list['name']
                xmin, ymin, xmax, ymax = detected_object_list['box_points']
                detected_object = test.set_sub_elements_for_parent(root, 'object')
                object_name, xmin, ymin, xmax, ymax = test.set_sub_elements_for_parent(detected_object, 'name', 'bndbox', 'xmin', 'ymin', 'xmax', 'ymax)
                test.text_in_tag(
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




