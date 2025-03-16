import os
import argparse
import cv2
import webbrowser
import validators

from pyzbar import pyzbar

def open_url(url, allow_unsafe):
    if not validators.url(url):
        print(f"[ERR] Not a valid URL: {url}")
        return
    if allow_unsafe or url.startswith("https://"):
        try:
            print(f"[INFO] Opening QR Code URL: {url}")
            if not webbrowser.open(url, new=2):
                try:
                    os.system(f"explorer.exe {url}")
                except:
                    print(f"[ERR] Unable to open URL. Set $DISPLAY if Linux distro is headless")
        except Exception as e:
            print(f"[ERR] Could not open URL: {url} - {str(e)}")
    else:
        print(f"[WARN] url found but might be unsafe {url}. Pass the --unsafe flag to open it")

def parse_barcode(image, barcode, allow_unsafe=False):
    (x, y, w, h) = barcode.rect
    cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
    
    barcode_data = barcode.data.decode('utf-8')
    barcode_type = barcode.type

    text = f"{barcode_data} ({barcode_type})"
    cv2.putText(img=image, text=text, org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255), thickness=2)
    print(f"[INFO] Found [{barcode_type}] barcode: {barcode_data}")

    if barcode_type == 'QRCODE':
        open_url(barcode_data, allow_unsafe)
    

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=True, help='Path to input image')
    parser.add_argument('-u', '--unsafe', action='store_true', default=False, help='Allow to open http QR codes in browser')
    return vars(parser.parse_args())

if __name__ == '__main__':
    args = parse_args()

    image_path = args['image']
    allow_unsafe = args['unsafe']

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File {image_path} not found")
    
    image = cv2.imread(filename=image_path)
    barcodes = pyzbar.decode(image=image)

    for barcode in barcodes:
        parse_barcode(image, barcode, allow_unsafe)
    cv2.imshow("Image", image)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()