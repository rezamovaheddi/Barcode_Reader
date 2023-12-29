# importing library
import cv2
from pyzabr.pyzabr import decode

# Make a method to decode the Barcode
def Barcode_Reader(image):
	img = cv2.imread(image)

	detectedBarcods = decode(img)

	if not detectedBarcods:
		print("Barcod is Not Detceted or Barcod is Blank")

	else:

		for Barcode in detectedBarcods:

			(x, y, w, h) = Barcode.rect

			cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)

		if Barcode.data!="":

			print(Barcode.data)
			print(Barcode.type)
	# Display the image
	cv2.imshow("Image", img)
	cv2.waitKey(0)
	cv2.destoryAllWindow()


	if __name__ == "__main__":
		image = "Img.jpg"
		print(image)