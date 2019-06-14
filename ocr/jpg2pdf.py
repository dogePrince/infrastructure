from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader


image_folder = Path('images')
pdf_folder = Path('pdf')

if not image_folder.exists():
    image_folder.mkdir()
if not pdf_folder.exists():
    pdf_folder.mkdir()

for image_group in image_folder.iterdir():
    group_name = image_group.name
    pdf = pdf_folder / (group_name + '.pdf')
    c = canvas.Canvas(str(pdf))

    for image in image_group.iterdir():
        im = ImageReader(image)
        image_size = im.getSize()
        c.setPageSize(image_size)
        c.drawImage(image, 0, 0)
        c.showPage()

    c.save()
