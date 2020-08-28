import qrcode

qr = qrcode.QRCode()
qr.add_data('test text')
qr.make()
img = qr.make_image()
img.save('qrcode_test2.png')
