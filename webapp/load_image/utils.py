import cv2
from datetime import datetime
import numpy as np
import pickle
from werkzeug.utils import secure_filename

from webapp.db import db
from webapp.load_image.models import Photo


def create_filename():
    new_filename = f"{str(datetime.now()).replace('.', '_')}.jpg"
    filename = secure_filename(new_filename)
    return filename


def save_upload_info(picture_title, path_to_dir, upload_time):
    upload_info = Photo(picture_title=picture_title, path_to_dir=path_to_dir,
                        upload_time=upload_time)
    db.session.add(upload_info)
    db.session.commit()


def match_templates(image):
    # read test image for finding templates and drawing them
    test_img = cv2.imread(f"downloads/{image}", 0)
    test_img_for_draw = cv2.imread(f"downloads/{image}", 0)

    with open("webapp/dict_of_templates.pkl", "rb") as f:
        dict_of_templates = pickle.load(f)

    # dictionary, where key = y, value = list of x
    dict_line = {}
    # dictionary, where key = coordinates and value = character
    coordinates_and_letters = {}

    for key, value in dict_of_templates.items():
        template = value
        w, h = template.shape[::-1]

        result = cv2.matchTemplate(test_img, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.75
        loc = np.where(result >= threshold)

        # draw boxes and letters on image
        for pt in zip(*loc[::-1]):
            cv2.rectangle(test_img_for_draw, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
            org = (pt[0] + w - 20, pt[1] + h + 30)
            cv2.putText(test_img_for_draw, key, org, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)
            coordinates_and_letters[org] = key
            x, y = org
            if y not in dict_line:
                dict_line[y] = [x]
            else:
                dict_line[y].append(x)

    # create dictionary with lines' length 3 or more characters, and x coordinates ascending
    new_dict_line = {}

    for y, x in dict_line.items():
        if len(x) >= 4:
            new_dict_line[y] = sorted(x)

    # delete repeated xs in lines:
    last_dict_line = {}

    for y, xs in new_dict_line.items():
        new_xs = []
        true_x = 0
        for x in xs:
            if x > (true_x + 5):
                true_x = x
                new_xs.append(true_x)
        last_dict_line[y] = new_xs

    # y coordinates ascending
    last_dict_line = dict(sorted(last_dict_line.items()))

    # create list of all coordinates ascending
    coordinates = []
    for y, xs in last_dict_line.items():
        for x in xs:
            coordinates.append((x, y))

    # find by ascending coordinates all letters from left to right and from top to bottom
    text = ""
    for coord in coordinates:
        text += coordinates_and_letters.get(coord)

    # create images whit boxes and characters on it
    cv2.imwrite(f'downloads/result_{image}', test_img_for_draw)
    return text, f'result_{image}'
