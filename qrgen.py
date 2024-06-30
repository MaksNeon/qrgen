import qrcode
from PIL import Image

print("Enter the QRCode data: ")
data = input()
qr = qrcode.QRCode(version=1, box_size=50, border=5) # Here you can modify some parameters to best fit your needs.
qr.add_data(data)
qr.make(fit=True)

print("How do you want to render your QRCode ? \n1. Save it\n2. Show it")
img = qr.make_image(fill='black', back_color='white') # Here you can modify some parameters to best fit your needs as well.
choice = int(input())
if choice == 1:
    img.save("qrcode.png")
elif choice == 2:
    img.show()
else:
    print("Incorrect choice")