import qrcode
from flask import Flask, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    link = request.args.get('link')
    qr = qrcode.QRCode(version=1, box_size=5, border=3)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
