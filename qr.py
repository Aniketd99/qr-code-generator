import pyqrcode
from pyqrcode import QRCode

#String which represent the QR code
s = "https://academia.srmist.edu.in/"

#Generate QR code
url = pyqrcode.create(s)

#Create and save the png file naming "myqr.png"
url.svg("myacademia.svg", scale = 8)
