from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = FastAPI()

# HTML template for the user interface
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title> String to Image Generator</title>
</head>
<body>
    <h1>String to Image Generator</h1>
    <form action="/generate_image" method="post">
        <label for="input_string">Input String:</label><br>
        <input type="text" id="input_string" name="input_string"><br><br>
        <button type="submit">Generate Image</button>
    </form>
    %s
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def root():
    return html_template % ""

@app.post("/generate_image")
async def generate_image(input_string: str = Form(...)):
    # Generate the image
    image = Image.new("RGB", (400, 200), color="white")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 10), input_string, fill="black", font=font)

    # Convert the image to bytes
    img_byte_array = BytesIO()
    image.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)

    # Display the image in HTML
    image_data = img_byte_array.getvalue()
    img_src = f"data:image/png;base64,{image_data.decode('utf-8')}"
    result_html = f"<h2>Generated Image:</h2><img src='{img_src}'><br><br>"
    return HTMLResponse(content=html_template % result_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)