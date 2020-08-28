import pyqrcode
from pyqrcode import QRCode

s="https://docs.google.com/document/d/1eFqNeksiOPU_OBfsPXZBt_EfH-yPrLWGDS7o2wK6IiA/edit"

url=pyqrcode.create(s)
url.svg("maath.svg",scale=8)
