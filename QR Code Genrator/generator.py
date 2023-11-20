import qrcode

qr_code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=2)

qr_code.add_data("https://ae.godaddy.com/offers/websites?cjdata=MXxOfDB8WXww&isc=cjcwsbfr&cjelbDays=7&AID=12648986&SID=1ff13854c01c9b803f34c188ef598ae4&tgt=5529645")
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="black", back_color="white")
img.save("new.png")