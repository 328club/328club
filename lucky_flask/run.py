from flask import Flask, render_template, request
from aip import AipFace

import random, time, sys, datetime

# 百度API配置
APP_ID = '24096837'
API_KEY = '4EkfjzDIVIdC47wrdkgcQwK8'
SECRET_KEY = 'e3mgFT9uROQ24UYOCUygGQmx1YRhfydK'

# 初始化client
client = AipFace(APP_ID, API_KEY, SECRET_KEY)
app = Flask(__name__)


# 单注模式
def create_lucky(seed):
    LUCKY_SEED = int(seed)
    redball = list(range(1, 36))
    blueball = list(range(1, 13))
    redball_left = 35
    blueball_left = 12
    lucky_ball = 0
    redball_pool = []
    blueball_pool = []
    random.shuffle(redball)
    random.shuffle(blueball)
    for i in range(5):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        redball_pool.append(lucky_ball)
        redball_left = redball_left - 1
    # print("BLUE BALL IS ROLLING")
    for i in range(2):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            # print(blueball)
            random.shuffle(blueball)
        # print(blueball)
        lucky_ball = blueball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        blueball_pool.append(lucky_ball)
        blueball_left = blueball_left - 1
    redball_pool.sort()
    blueball_pool.sort()
    # lottery=str(redball_pool+blueball_pool).replace('[','').replace(']','\n')
    redball_pool.extend(blueball_pool)
    return redball_pool


# 胆托模式
def create_dantuo(seed):
    LUCKY_SEED = int(seed)
    redball = list(range(1, 36))
    blueball = list(range(1, 13))
    redball_left = 35
    blueball_left = 12
    lucky_ball = 0
    redballdan_pool = []
    redballtuo_pool = []
    blueballdan_pool = []
    blueballtuo_pool = []
    random.shuffle(redball)
    random.shuffle(blueball)
    for i in range(4):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        redballdan_pool.append(lucky_ball)
        redball_left = redball_left - 1
    for i in range(7):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % redball_left):
            random.shuffle(redball)
        lucky_ball = redball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        redballtuo_pool.append(lucky_ball)
        redball_left = redball_left - 1
    # print("BLUE BALL IS ROLLING")
    for i in range(1):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            # print(blueball)
            random.shuffle(blueball)
        # print(blueball)
        lucky_ball = blueball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        blueballdan_pool.append(lucky_ball)
        blueball_left = blueball_left - 1
    for i in range(2):
        time.sleep(random.randint(1, LUCKY_SEED) / LUCKY_SEED)
        for j in range(random.randint(1, LUCKY_SEED) % blueball_left):
            # print(blueball)
            random.shuffle(blueball)
        # print(blueball)
        lucky_ball = blueball.pop()
        # print("LUCKY_BALL is %s" %(lucky_ball))
        blueballtuo_pool.append(lucky_ball)
        blueball_left = blueball_left - 1
    redballdan_pool.sort()
    redballtuo_pool.sort()
    blueballdan_pool.sort()
    blueballtuo_pool.sort()
    lottery = str(redballdan_pool) + '+' + str(redballtuo_pool) + '    ' + str(blueballdan_pool) + '+' + str(
        blueballtuo_pool)
    return lottery


# 解析请求数据并以json形式返回
def request_parse(req_data):
    data = None
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/8888/')
@app.route('/8888/<name>')
@app.route('/single/')
@app.route('/single/<name>')
def single(name=None):
    return render_template('hello.html', name=create_lucky(name))


@app.route('/8848/')
@app.route('/8848/<name>')
@app.route('/dantuo/')
@app.route('/dantuo/<name>')
def dantuo(name=None):
    return render_template('more.html', name=create_dantuo(name))


@app.route('/login/')
def login():
    return app.send_static_file('camera.html')


# 传入Base64格式的图片
@app.route('/api-face-login/', methods=["POST"])
def face_search():
    time_start = time.time()
    data = request_parse(request)
    if data is None:
        return "ERROR"

    image = data.get("image")

    print(image)

    if image is None or image == "":
        return None

    imageType = "BASE64"
    groupIdList = "328lucky"

    """ 如果有可选参数 """
    options = {
        "max_face_num": 1,  # 只检测一张人脸
        "match_threshold": 70,
        "quality_control": "NORMAL",
        "liveness_control": "HIGH",  # 活体检测级别
        "max_user_num": 1  # 只搜索一个结果
    }

    """ 带参数调用人脸搜索 """
    result = client.search(image, imageType, groupIdList, options)

    time_end = time.time()

    print(time_end - time_start)
    # TODO 添加登录逻辑

    return result
