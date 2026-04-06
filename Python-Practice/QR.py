#create QR code.
import qrcode
qr = qrcode.make("https://www.linkedin.com/in/jiya-kumari-1a2a51282")
qr.save("linkedin_qr.png")