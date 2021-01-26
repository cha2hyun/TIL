import os
import json
from collections import OrderedDict

INPUT_DIR = "./input/"

FOLDER_NAME = ""
JSON_DIR = INPUT_DIR + FOLDER_NAME

def getNamesAndPaths(dir):
    names = os.listdir(dir)
    paths = [ (dir + i) for i in names ] 
    return names, paths

folder_names, folder_paths = getNamesAndPaths(INPUT_DIR)
json_names, json_paths = getNamesAndPaths(INPUT_DIR + folder_names[0])
print(folder_names[0],"  |  ", folder_paths[0],"  |  ", json_names[0],"  |  ", json_paths[0])



# 폴더 이름과 경로를 리턴
def findFolder(current_path):
    path = current_path + "/input/"
    folder_names = os.listdir(path)
    folder_paths = [ (path + i) for i in folder_names ] 
    return folder_names, folder_paths

# 폴더에 있는 json 이름과 경로를 리스트를 리턴
def findJsonName(folder_path):
    path = folder_path + "/"
    json_names = os.listdir(path)
    json_paths = [ (path + i) for i in json_names ] 
    return json_names, json_paths

# json 경로 리스트에 있는 json들을 하나로 병합
def mergeJson(json_paths):
    merged_json = {}
    for path in json_paths:
        with open(path, 'r') as f:
            json_data = json.load(f)
            # print(json_data)

def createJson(folder_name, folder_path, json_names, json_paths):
    video_name = folder_name
    direction = folder_name.split("_")[1][1:-1].lower()
    golfer_type = folder_name.split("_")[3][1:-1][:3].lower() + "_level" + folder_name.split("_")[3][1:-1][3:]

    # 엑셀파일이 아닌 pdf로 되어있어서 action을 불러올 수 없음 -> 보류
    address = ""
    toe_up = ""
    mid_backswing = ""
    top = ""
    mid_downswing = ""
    impact = ""
    mid_follow_through = ""
    finish = ""

    frames_dict = {}
    
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
            "address":address,
            "toe-up":toe_up,
            "mid_backswing":mid_backswing,
            "top":top,
            "mid_downswing":mid_downswing,
            "impact":impact,
            "mid_follow_through":mid_follow_through,
            "finish":finish
        }
    data["frames"] = {
        "frame_name" : "",
        "width" : "",
        "height" : "",
        "action" : "",
        "bbox" : "",
        "keypoint_body" : "",
        "keypoint_club" : ""
    }

    print(json.dumps(data, ensure_ascii=False, indent='\t'))
    

# current_path = os.getcwd()

# folder_names, folder_paths = findFolder(current_path)
# folder_name = folder_names[0]
# folder_path = folder_paths[0]

# json_names, json_paths = findJsonName(folder_path)

# createJson(folder_name, folder_path, json_names, json_paths)
# print(json_names[0], json_paths[0])

# merged_json = mergeJson(json_paths)
# return_json = makeJson(folder_path, mergeJson)