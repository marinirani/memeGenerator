from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/generate", methods=["POST"])
def generate():
    file = request.files["image"]
    img = Image.open(file)

    top = request.form["top_text"]
    bottom = request.form["bottom_text"]

    
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    w, h = img.size



    draw.text((w/2, 10), top, fill="white", anchor="mm", font=font)
    draw.text((w/2, h-20), bottom, fill="white", anchor="mm", font=font)

    img.save("static/meme.jpg")

    return render_template("result.html", image="meme.jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
