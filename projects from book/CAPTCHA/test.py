import subprocess

p = subprocess.Popen(["tesseract", "4MmC3.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
