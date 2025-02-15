

import xml.etree.ElementTree as ET

def convert_xml_to_txt_with_class_id(xml_file, txt_file):
    # Class mapping
    class_mapping = {"two_wheelers": "0", "auto": "1"}

    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(txt_file, "w", encoding="utf-8") as txt:
        for obj in root.findall("object"):
            name = obj.find("name").text
            class_id = class_mapping.get(name, "-1")  # Default to -1 if unknown class

            bndbox = obj.find("bndbox")
            xmin = bndbox.find("xmin").text
            ymin = bndbox.find("ymin").text
            xmax = bndbox.find("xmax").text
            ymax = bndbox.find("ymax").text
            
            txt.write(f"{class_id} {xmin}, {ymin}, {xmax}, {ymax}\n")

# Example usage
xml_file = "input.xml"  # Replace with your actual XML file path
txt_file = "output.txt"  # Replace with your desired TXT file path
convert_xml_to_txt_with_class_id(xml_file, txt_file)
