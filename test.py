# import module
from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
images = convert_from_path('pdf/sample.pdf', poppler_path='C:\\Users\\yM-A459009876M\\Downloads\\poppler-24.02.0\\Library\\bin')
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('images/page'+ str(i) +'.jpg', 'JPEG')
