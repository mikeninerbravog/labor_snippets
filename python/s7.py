# pip install rembg
# Remove image Background

from rembg import remove
from PIL import Image

input_path = 'lara2.png'
output_path = 'lara2_edit.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)