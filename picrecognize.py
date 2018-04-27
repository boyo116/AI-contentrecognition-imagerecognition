from aip import AipImageCensor

""" 你的 APPID AK SK """
APP_ID = '11156578'
API_KEY = '3K73kH6H4aGoZbUrE1N0oTO5'
SECRET_KEY = 'YoL5g6BCnWG4mQvEo0TjyDPozlySdDRp'

client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""" 调用色情识别接口 """
result = client.imageCensorUserDefined(get_file_content('c:/code/11.jpg'))
result2 = client.imageCensorUserDefined(get_file_content('c:/code/22.jpg'))
print(result)
print(result2)
""" 如果图片是url调用如下 """
result3 = client.imageCensorUserDefined('http://www.example.com/image.jpg')
