from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

app = FastAPI()
#app.mount("/imgs", StaticFiles(directory="imgs"), name='images')


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
    app.mount("/imgs", StaticFiles(directory="imgs"), name='images')
    img_src = "imgs/g.png"
    result_html = f"<h2>Generated Image:</h2><img src='{img_src}'><br><br>"
    return HTMLResponse(content=html_template % result_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

