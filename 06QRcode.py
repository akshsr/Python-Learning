import qrcode as qr


user_input = input('What url you want to make QR of?: ')
img = qr.make(user_input)
img.save("your_QRcode.png")