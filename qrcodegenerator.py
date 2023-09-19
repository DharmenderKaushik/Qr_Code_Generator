import qrcode
qr = qrcode.QRCode(
    version = 15,   #version of qr higher the number, bigger the image 
    box_size = 10,  #size of the box where qr code will be displayed
    border = 5,     #border of the image
)

data = "https://github.com/DharmenderKaushik"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "white", back_color = "white")
img.save("qr_code.png")
