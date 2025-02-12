from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.form.get("url")
    if data:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        img_io = BytesIO()
        img.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png")
    
    return "Error: No data provided", 400

if __name__ == "__main__":
    app.run(debug=True)
