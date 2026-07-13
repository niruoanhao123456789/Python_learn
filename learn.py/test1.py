import qrcode

img = qrcode.make('I am cool') # 此处可填一个网站网址
img.save('test.png')
# 生成二维码