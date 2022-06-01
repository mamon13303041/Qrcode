import pyqrcode as qr
import png
url='https://www.linkedin.com/in/md-mamonur-rashid-b57b4910a/'
my_qrcode=qr.create(url,error='l')
my_qrcode.png('linkding.png',scale=6, module_color=[0, 0, 0, 228], background=[0xff, 0xff, 0xcc])
my_qrcode.show()