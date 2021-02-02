import os
import json
import csv
from collections import OrderedDict
import pandas as pd 

def createFakeDB():
    fake_db = []
    folder_names = os.listdir(input_path)
    for folder_name in folder_names:
        json_names = os.listdir(input_path + folder_name)
        fake_db.append([folder_name, json_names])
    return fake_db

def createFakeCsv():
    file_path = "./SKT_골프_동작정의문서"
    xlsx = pd.read_excel(file_path + ".xlsx", sheet_name = "Sheet1")
    xlsx.to_csv(file_path + ".csv")
    with open(file_path + ".csv", 'r') as f:
        reader = csv.reader(f)
        fake_csv = list(reader)
    return fake_csv

def createAction(folder_name, img_num):
    action_score = [10,20,30,40,50,60,70,80]
    for csv_data in fake_csv:
        if csv_data[1] == folder_name:
            scores = csv_data[2:]
            action_idx = 0
            for idx, score in enumerate(scores):
                if score == "":
                    score = 0
                if float(img_num) > float(score) and score != 0:
                    action_idx = idx
                if (float(img_num) < float(score)) and score != 0:
                    return action_score[action_idx]
            return action_score[action_idx]
            
def createFrame(folder_name, json_name):
    path = input_path + folder_name + "/" + json_name
    with open(path, 'r') as f:
        json_data = json.load(f)
    
    images = json_data["images"][0]
    frame_name = images["filename"]
    width = images["width"]
    height = images["height"]

    img_num = frame_name[-7:-4]
    action = createAction(folder_name, img_num)

    bbox = []
    keypoint_body = []
    keypoint_club = []
    for annotate in json_data["annotations"]:
        # bbox
        box_and_class = []
        try:            
            for box in annotate["box"]:
                box_and_class.append(box)
            box_and_class.append(int(annotate["class"]))
            bbox.append(box_and_class)
        except:
            try:
                #keypoint_club
                if annotate["class"] == "keypoint_club":
                    points = annotate["points"]
                    temp = []
                    for idx, point in enumerate(points):
                        temp.append(point)
                        if (idx % 3 == 2) and (idx != 0):
                            keypoint_club.append(temp)
                            temp = []  
                #keypoint_body
                else:
                    points = annotate["points"]
                    temp = []
                    for idx, point in enumerate(points):
                        temp.append(point)
                        if (idx % 3 == 2) and (idx != 0):
                            keypoint_body.append(temp)
                            temp = []  
            except:
                pass

    frame = {
        "frame_name" : frame_name,
        "width" : width,
        "height" : height,
        "action" : action,
        "bbox" : bbox,
        "keypoint_body" : keypoint_body,
        "keypoint_club" : keypoint_club
    }
    
    return frame

def saveJson(folder_name, data):
    PATH = "./output/"
    if not(os.path.exists(PATH)):        
        os.mkdir(PATH)
    with open(PATH + folder_name + '.json', 'w', encoding="utf-8") as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")
    print("saved :",folder_name)

def createJson(folder_name, json_names):
    video_name = folder_name
    direction = folder_name.split("_")[1][1:-1].lower()
    golfer_type = folder_name.split("_")[3][1:-1][:3].lower() + "_level" + folder_name.split("_")[3][1:-1][3:]
    frames = []
    for json_name in json_names:
        frame = createFrame(folder_name, json_name)
        frames.append(frame)
        
    data = OrderedDict()
    data["label-info"] =  {
        "video_info_format": {
            "direction": "front/side",
            "golfer_type": "pro/ama_level0/ama_level1/ama_level2"
        },
        "bbox": {
            "class": {
                "person": 0,
                "head": 1,
                "hand": 2,
                "foot": 3,
                "cap": 4,
                "golf_ball": 5,
                "golf_club_head": 6
            },
            "format": "[x1,y1,x2,y2,class_number]/0<=x1<x2<width/0<=y1<y2<height"
        },
        "keypoint_body": {
            "joint_order": [
                "nose",
                "right_eye",
                "left_eye",
                "right_ear",
                "left_ear",
                "neck",
                "right_shoulder",
                "left_shoulder",
                "right_elbow",
                "left_elbow",
                "right_wrist",
                "left_wrist",
                "pelvis",
                "right_hip",
                "left_hip",
                "right_knee",
                "left_knee",
                "right_ankle",
                "left_ankle",
                "right_big_toe",
                "left_big_toe",
                "right_small_toe",
                "left_small_toe",
                "right_heel",
                "left_heel"
            ],
            "joint_format": "[x,y,v]/v:0(out_of_frame)/1(estimated)/2(visible)"
        },
        "keypoint_club": {
            "joint_order": [
                "grip_cap",
                "club_head_toe",
                "club_head_heel"
            ],
            "joint_format": "[x,y,v]/v:0(out_of_frame)/1(estimated)/2(visible)"
        }
    }

    data["video_name"] = video_name 
    data["video_info_format"] = {
            "direction": direction,
            "golfer_type": golfer_type
        }
    data["action"] = {         
        "address": 10,
        "toe-up": 20,
        "mid_backswing": 30,
        "top": 40,
        "mid_downswing": 50,
        "impact": 60,
        "mid_follow_through": 70,
        "finish": 80
    }
    data["frames"] = frames
    saveJson(folder_name, data)

input_path = "./input/"
fake_csv = createFakeCsv()
fake_db = createFakeDB()
for folder_name, json_names in fake_db:
    createJson(folder_name, json_names)
