from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11156578'
API_KEY = '3K73kH6H4aGoZbUrE1N0oTO5'
SECRET_KEY = 'YoL5g6BCnWG4mQvEo0TjyDPozlySdDRp'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('c:/code/3.jpg')
idCardSide = "back"

""" 调用身份证识别 """
client.idcard(image, idCardSide);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_risk"] = "false"

""" 带参数调用身份证识别 """
result = client.idcard(image, idCardSide, options)

print(result)