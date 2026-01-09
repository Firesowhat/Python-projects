import qrcode
from PIL import Image

# 1. Define the data and logo path
data = 'https://bit.ly/4qJvgmJ' # The data/URL for your QR code
logo_path = 'Whatsapp_logo.jpg'    # Path to your logo image file (must be square for best results)

# 2. Configure the QR code with high error correction (ERROR_CORRECT_H)
# This allows up to 30% of the QR code to be obscured, making room for the logo
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 3. Add data to the QR code and generate it
qr.add_data(data)
qr.make(fit=True)

# 4. Create the QR code image using the make_image method
# Use convert('RGB') for general compatibility or 'RGBA' if your logo has transparency
qr_img = qr.make_image(fill_color="navy", back_color="white").convert('RGB')

# 5. Open and resize the logo image
logo = Image.open(logo_path)
# Calculate a suitable logo size (e.g., about 1/4 of the QR code size)
logo_size = qr_img.size[0] // 4
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# 6. Calculate the position to paste the logo in the center
# The position is the top-left corner of where the logo will be placed
pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

# 7. Paste the logo onto the QR code image
# The third argument (logo) ensures transparency is maintained if the logo has an alpha channel
qr_img.paste(logo, pos, logo if logo.mode == 'RGBA' else None)

# 8. Save the final image
output_path = 'qr_with_whatsapplogo.png'
qr_img.save(output_path)

print(f"QR code with logo generated and saved as {output_path}!")
