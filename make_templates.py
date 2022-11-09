import cv2
import json
import os
import pickle

# create list of training files
list_dir = os.listdir(path="./train2")

# create list of all json files
json_list = []
for i in list_dir:
    if ".json" in i:
        json_list.append(i)


# cut out character for template
def get_frame(image, points):
    image = cv2.imread(image, 0)
    char = image[
        int(points[0][1]) - 5:int(points[1][1]) + 5,
        int(points[0][0]) - 5:int(points[1][0]) + 5
    ]
    return char


# create dictionary of templates where key is label and value is list of templates
dict_of_templates = {}
for f_json in json_list:
    with open(os.path.join("train2", f_json)) as f:
        data = json.load(f)
        image_name = os.path.join("train2", data.get("imagePath"))
        for item in data.get("shapes"):
            img = get_frame(image_name, item.get("points"))
            key = item.get("label")
            dict_of_templates[key] = img
            # if key not in dict_of_templates:
            #     dict_of_templates[key] = [img]
            # else:
            #     dict_of_templates[key].append(img)

with open("dict_of_templates.pkl", "wb") as f:
    pickle.dump(dict_of_templates, f)
