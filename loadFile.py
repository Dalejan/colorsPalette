from js import document
from pyodide import create_proxy
import asyncio
import io
from pyodide.http import pyfetch
import numpy as np
from PIL import Image



class ImageClass():
    imageData = ""

localImage = ImageClass()

async def _upload_change_and_show(e):
    #Load image from url
    url_val=Element('image-url-input').value

    #Get bytes from image
    response = await pyfetch(url=url_val, method="GET")
    img = Image.open(io.BytesIO(await response.bytes()))

    #Bytes stored into an array
    img=np.array(img)
    localImage.imageData = img

    #Show the image in the page
    new_image = document.createElement('img')
    new_image.src = url_val
    if document.getElementById("img-rendered-container").hasChildNodes() :
        document.getElementById("img-rendered-container").removeChild(document.getElementById("img-rendered-container").children[0])
    document.getElementById("img-rendered-container").appendChild(new_image)


# Run image processing code above whenever file is uploaded    
upload_file_proxy = create_proxy(_upload_change_and_show)
document.getElementById("uploadBtn").addEventListener("click", upload_file_proxy)
