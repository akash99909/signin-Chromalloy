import fitz # PyMuPDF
import io
from PIL import Image

file = "IDC Digital Commerce.pdf"
# open the file
pdf_file = fitz.open(file)

for page_index in range(len(pdf_file)):
    # get the page itself
    page = pdf_file[page_index]
    # get image list
    image_list = page.get_images()
    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))
