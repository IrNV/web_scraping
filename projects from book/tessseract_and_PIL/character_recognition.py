from PIL import Image
import subprocess


def clean_file(file_path, new_file_path):
    image = Image.open(file_path)
    # Задаем пороговое значение для данного изображения и сохраняем
    image = image.point(lambda x: 0 if x < 143 else 255)
    image.save(new_file_path)
    # Вызываем tesseract, чтобы выполнить OCR вновь созданного изображения
    subprocess.call(["tesseract", new_file_path, "output"])
    # Открываем и читаем полученный в результате файл данных
    output_file = open("output.txt", 'r')
    print(output_file.read())
    output_file.close()

clean_file("t.png", "t_2_clean.png")
