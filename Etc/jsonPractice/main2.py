# -*- coding: UTF-8 -*-
import os
import json
from openpyxl import load_workbook

try:
    configFile = r"./config.json"
    with open(configFile, 'rt', encoding='utf-8') as f:
        config = json.load(f)
finally:
    f.close()

before_image_path = config['BEFORE_IMAGE_PATH']
after_image_path = config['AFTER_IMAGE_PATH']

def start():
    e = load_workbook('./SKT_골프_동작정의문서.xlsx', data_only=True)
    excel_file = e['Sheet1']
    total_value = {}
    action_list = []
    row_count = 0

    for row in excel_file.rows:
        row_value = []
        for cell in row:
            row_value.append(cell.value)

        if row_count != 0:
            for i in range(len(row_value)):
                if i == 0:
                    total_value[row_value[i]] = []
                else:
                    total_value[row_value[0]].append(row_value[i])
        else:
            for i in range(len(row_value)):
                if i == 0:
                    pass
                else:
                    action_list.append(row_value[i])
        row_count += 1

    for (path, dir, files) in os.walk(before_image_path):
        real_file_name = ''
        real_folder_name = ''
        res_json = {}
        res_dict = {}
        res_dict['frames'] = []
        for fileName in files:
            if fileName.endswith('.json'):
                try:
                    with open(os.path.join(path, fileName), encoding='utf-8') as json_file:
                        real_file_name = fileName.split('.json')[0]
                        real_folder_name = real_file_name.split(' ')[0]
                        real_file_num = real_file_name.split(' ')[1]

                        json_data = json.load(json_file)
                        json_data['frames'] = json_data.pop('images')

                        for i in range(len(json_data['frames'])):
                            json_data['frames'][i]['frame_name'] = json_data['frames'][i].pop('filename')
                            json_data['frames'][i]['width'] = json_data['frames'][i].pop('width')
                            json_data['frames'][i]['height'] = json_data['frames'][i].pop('height')

                            for key, value in total_value.items():
                                if real_folder_name == key:
                                    none_count = 0
                                    for j in range(len(value)):
                                        if value[j] is None:
                                            none_count += 1
                                            pass
                                        elif real_file_num == value[j]:
                                            json_data['frames'][i]['action'] = (j + 1) * 10
                                            break
                                        else:
                                            if real_file_num < value[j]:
                                                json_data['frames'][i]['action'] = (j + 1 - none_count) * 10
                                                break

                            json_data['frames'][i]['bbox'] = []
                            json_data['frames'][i]['keypoint_body'] = []
                            json_data['frames'][i]['keypoint_club'] = []

                            for j in range(len(json_data['annotations'])):
                                if 'box' in json_data['annotations'][j]:
                                    json_data['annotations'][j]['box'].append(int(json_data['annotations'][j]['class']))
                                    json_data['frames'][i]['bbox'].append(json_data['annotations'][j]['box'])
                                elif 'points' in json_data['annotations'][j]:
                                    point_count = 0
                                    point_list = []
                                    if json_data['annotations'][j]['class'] != 'keypoint_club':
                                        for k in range(len(json_data['annotations'][j]['points'])):
                                            point_count += 1
                                            point_list.append(json_data['annotations'][j]['points'][k])
                                            if point_count == 3:
                                                json_data['frames'][i]['keypoint_body'].append(point_list)
                                                point_count = 0
                                                point_list = []
                                    else:
                                        for k in range(len(json_data['annotations'][j]['points'])):
                                            point_count += 1
                                            point_list.append(json_data['annotations'][j]['points'][k])
                                            if point_count == 3:
                                                json_data['frames'][i]['keypoint_club'].append(point_list)
                                                point_count = 0
                                                point_list = []

                            res_dict['frames'].append(json_data['frames'][i])
                finally:
                    json_file.close()

        if real_file_name != '':
            res_json['label_info'] = {}

            res_json['label_info']['video_info_format'] = {}
            res_json['label_info']['video_info_format']['direction'] = 'front/side'
            res_json['label_info']['video_info_format']['golfer_type'] = 'pro/ama_level0/ama_level1/ama_level2'

            res_json['label_info']['bbox'] = {}
            res_json['label_info']['bbox']['class'] = {}
            res_json['label_info']['bbox']['class']['person'] = 0
            res_json['label_info']['bbox']['class']['head'] = 1
            res_json['label_info']['bbox']['class']['hand'] = 2
            res_json['label_info']['bbox']['class']['foot'] = 3
            res_json['label_info']['bbox']['class']['cap'] = 4
            res_json['label_info']['bbox']['class']['golf_ball'] = 5
            res_json['label_info']['bbox']['class']['golf_club_head'] = 6
            res_json['label_info']['bbox']['format'] = '[x1,y1,x2,y2,class_number]/0<=x1<x2<width/0<=y1<y2<height'
 
            keypoint_body_joint_order_list = [
                "nose", "right_eye", "left_eye", "right_ear", "left_ear",
                "neck", "right_shoulder", "left_shoulder", "right_elbow", "left_elbow",
                "right_wrist", "left_wrist", "pelvis", "right_hip", "left_hip",
                "right_knee", "left_knee", "right_ankle", "left_ankle", "right_big_toe",
                "left_big_toe", "right_small_toe", "left_small_toe", "right_heel", "left_heel"
            ]

            res_json['label_info']['keypoint_body'] = {}
            res_json['label_info']['keypoint_body']['joint_order'] = keypoint_body_joint_order_list
            res_json['label_info']['keypoint_body'][
                'joint_format'] = '[x,y,v]/v:0(out_of_frame)/1(estimated)/2(visible)'

            res_json['label_info']['keypoint_club'] = {}
            res_json['label_info']['keypoint_club']['joint_order'] = ['grip_cap', 'club_head_toe', 'club_head_heel']
            res_json['label_info']['keypoint_club'][
                'joint_format'] = '[x,y,v]/v:0(out_of_frame)/1(estimated)/2(visible)'

            res_json['video_name'] = real_folder_name

            info_direction = real_folder_name.split('_')[1].replace('[', '').replace(']', '').lower()
            first_info_golfer_type = real_folder_name.split('_')[-1].replace('[', '').replace(']', '').lower()[:-2]
            last_info_golfer_type = real_folder_name.split('_')[-1].replace('[', '').replace(']', '').lower()[-2:]
            info_golfer_type = first_info_golfer_type + '_level' + last_info_golfer_type
            res_json['video_info'] = {}
            res_json['video_info']['direction'] = info_direction
            res_json['video_info']['golfer_type'] = info_golfer_type

            res_json['action'] = {}
            res_json['action']['address'] = 10
            res_json['action']['toe'] = 20
            res_json['action']['mid_backswing'] = 30
            res_json['action']['top'] = 40
            res_json['action']['mid_downswing'] = 50
            res_json['action']['impact'] = 60
            res_json['action']['mid_follow_through'] = 70
            res_json['action']['finish'] = 80

            res_json['frames'] = res_dict['frames']

            after_image_folder_path = os.path.join(after_image_path, real_folder_name)

            if not os.path.exists(after_image_folder_path):
                os.mkdir(after_image_folder_path)

            with open(os.path.join(after_image_folder_path, real_folder_name + '.json'), 'w', encoding='utf-8') as json_change:
                json.dump(res_json, json_change, indent='\t')


if __name__ == '__main__':
    start()