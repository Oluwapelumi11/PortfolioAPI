import qrcode
import qrcode.image.svg

def generateQR(url="some data",size=10,border=4,fill="black",back="white"):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True) # uncomment this line
    img = qr.make_image(fill_color=fill, back_color=back)
    response = Response(content_type="image/png")
    img.save(response, format="PNG")
    return response

generateQR()
