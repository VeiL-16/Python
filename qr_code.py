import qrcode
url=input("enter your url").strip()
myqr=qrcode.make(url)
myqr.save("qrfinal.png")

