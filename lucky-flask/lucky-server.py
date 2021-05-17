from aip import AipFace

# configure
APP_ID = '24096837'
API_KEY = '4EkfjzDIVIdC47wrdkgcQwK8'
SECRET_KEY = 'e3mgFT9uROQ24UYOCUygGQmx1YRhfydK'

# 初始化client
client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# 传入Base64格式的图片
def face_detect(image):
    imageType = "BASE64"

    """ 如果有可选参数 """
    options = {
        # "face_field": "age",
        "max_face_num": 1,
        "face_type": "LIVE",
        "liveness_control": "LOW"
    }

    """ 带参数调用人脸检测 """
    client.detect(image, imageType, options)


# 传入Base64格式的图片
def face_search(image):
    imageType = "BASE64"
    groupIdList = "3,2"

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
