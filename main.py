import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)

img.save("output/qrcode.png")

print("QR Code saved!")