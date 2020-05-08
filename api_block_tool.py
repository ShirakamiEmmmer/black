# -*- coding: utf-8 -*
import me
import json
import time
import requests


def pull_block_list(room_id, csrf):
    time.sleep(0.5)
    block_list = "http://api.live.bilibili.com/liveact/ajaxGetBlockList" + f"?roomid={room_id}" + "&page=1" + f"&csrf={csrf}" + f"&csrf_token={csrf}"
    get_list = requests.get(block_list, cookies=cookies)
    re_message = json.loads(get_list.text)
    return re_message["data"]


def set_block_user(room_id, csrf, user_uid):
    time.sleep(0.5)
    block_url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"roomid={room_id}&block_uid={user_uid}&hour=720&csrf_token={csrf}&csrf={csrf}&visit_id="
    block_it = requests.post(block_url, data=data, cookies=cookies, headers=headers)
    w
    return json.loads(block_it.text)


def del_block_user(course_id, room_id, csrf):
    time.sleep(0.5)
    del_url = "https://api.live.bilibili.com/banned_service/v1/Silent/del_room_block_user"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"id={course_id}&roomid={room_id}&csrf_token={csrf}&csrf={csrf}&visit_id="
    del_it = requests.post(del_url, data=data, cookies=cookies, headers=headers)
    print(del_it)


# 客制化参数在这里调整
room = 763869
my_csrf = me.user['CSRF']
cookies = me.cookie
##########################

man_list = pull_block_list(room, my_csrf)
for man in man_list:
    if set_block_user(room, my_csrf, man['uid'])['code'] == -400:
        del_block_user(man['id'], room, my_csrf)
        set_block_user(room, my_csrf, man['uid'])

black_list = open("black.txt", "r")
for line in black_list:
    line = line.split()[0]
    if set_block_user(room, my_csrf, line)['code'] == -400:
        continue
    # 下 次 一 定
black_list.close()
