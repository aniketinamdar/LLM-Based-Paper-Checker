import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()

images = [
    keras_ocr.tools.read(img) for img in ['images/test2.png']
]

prediction_groups = pipeline.recognize(images)

predicted_image = prediction_groups[0]
for text, box in predicted_image:
    print(text, end = " ") 