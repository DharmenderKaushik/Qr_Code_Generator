
# QR Code Generator Using Python

Creating a QR Code Generator for my Github profile using Python.




## What is Qr code ?

A Quick Response code is a two-dimensional pictographic code used for its fast readability and comparatively large storage capacity. The code consists of black modules arranged in a square pattern on a white background. The information encoded can be made up of any kind of data (e.g., binary, alphanumeric, or Kanji symbols).


## Installation

I am using qrcode module in this project

```bash
  pip install qrcode
```
## Usage
Here is a sample code to use qrcode module
```javascript
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

```

## Screenshots
Output will come as a Qr code
![App Screenshot](https://github.com/DharmenderKaushik/Qr_Code_Generator/blob/main/qr_code.png)
    
