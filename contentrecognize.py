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

image = get_file_content('c:/1.png')
""" 调用网络图片文字识别, 图片参数为本地图片 """
client.webImage(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_language"] = "true"

""" 带参数调用网络图片文字识别, 图片参数为本地图片 """
result1 = client.webImage(image, options)
print(result1)
url = "https//www.x.com/sample.jpg"

""" 调用网络图片文字识别, 图片参数为远程url图片 """
client.webImageUrl(url);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["detect_language"] = "true"

""" 带参数调用网络图片文字识别, 图片参数为远程url图片 """
client.webImageUrl(url, options)

