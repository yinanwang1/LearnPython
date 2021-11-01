
import qrcode

qr = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
url = "wyn123456"
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
print("123")
img.save("/Users/arthurwang/Desktop/test.jpg", 'jpeg')

# stream = StringIO.StringIO()
# img.save(stream)
# print(stream.getvalue())