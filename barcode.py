import os

from zxing import BarCodeReader

def generate_qr_code(text, output_file):
    reader = BarCodeReader()
    barcode = reader.qrcode(text, output=output_file, module_size=4, version=1, eclevel='M')
    print(barcode.filename)

if __name__ == '__main__':
    generate_qr_code("Hello, World!", "qr_code.png")
