from PIL import Image
import os


folderImages = os.path.dirname(os.path.realpath(__file__)) #Get the actual Folder
picturesFolder = f"{folderImages}test/"

if __name__ == "__main__":
    for filename in os.listdir(folderImages):
        name, extension = os.path.splitext(folderImages + filename)
        print(filename)
        if extension in [".jpg", "jpeg", ".png",".gif"]:
            image = Image.open(folderImages+filename)
            image.save(picturesFolder+filename,optimize=True,quality=70)
            os.remove(folderImages+filename)