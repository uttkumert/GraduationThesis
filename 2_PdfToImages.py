from wand.image import Image as wi

PDFfile = wi(filename="test.pdf",resolution=400)
Images = PDFfile.convert('jpg')
ImageSequence = 0
Image_Seq2 = 0

for img in PDFfile.sequence:
    if ImageSequence == 0:
        Image_Seq2 += 1
    if Image_Seq2%10 == 0:
        Image_Seq2 += 1
    Image = wi(image = img)
    Image.save(filename=str(Image_Seq2)+str(ImageSequence)+".jpg")
    ImageSequence += 1
    ImageSequence = ImageSequence%10

# +str(ImageSequence)+