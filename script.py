from PIL import Image, ImageSequence

tiff = Image.open("arquivo_multipagina.tiff")
for i, page in enumerate(ImageSequence.Iterator(tiff)):
    page.save(f"pagina_{i+1}.png")
