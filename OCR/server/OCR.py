import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext('smile.jpg')

for (bbox,text,prob) in result:
  print(text)