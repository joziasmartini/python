# Run pip install qrcode
import qrcode
 
# User inputs
data = input("Insert text: ")
name = input("Save with file name: ")

# Configurations
qr = qrcode.QRCode(version = 1, box_size = 50, border = 5)

# Add data
qr.add_data(data)

# Automatically detect the size
qr.make(fit = True)

# Create image with the data
img = qr.make_image()

# Save image
img.save(name)