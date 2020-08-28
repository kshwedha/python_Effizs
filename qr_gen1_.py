import qrcode

qr = qrcode.QRCode(
    version=12,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=8
)
qr.add_data('https://docs.google.com/document/d/1eFqNeksiOPU_OBfsPXZBt_EfH-yPrLWGDS7o2wK6IiA/edit')
qr.make()
img = qr.make_image(fill_color="black", back_color="#23dda0")
img.save('maath1_.png')
