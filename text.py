from aip import AipImageCensor

""" 你的 APPID AK SK """
APP_ID = '11156578'
API_KEY = '3K73kH6H4aGoZbUrE1N0oTO5'
SECRET_KEY = 'YoL5g6BCnWG4mQvEo0TjyDPozlySdDRp'
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)
result = client.antiSpam('民警提醒说，此类骗局中，通常骗子要求汇款的理由包括“发红包”、“买礼物”、“生病就医”、“凑路费”、“生意需要资金”、“见面需要彩礼”等各种理由。因此，微信交友遇到这样情形要小心防骗')

print(result)