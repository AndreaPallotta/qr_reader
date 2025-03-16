# QR Code and Barcode Scanner

This project allows you to scan QR codes and barcodes from an image. If the barcode is a QR code containing an `https` URL, the program will automatically open the link in your default web browser.

## Setup and Installation

### Conda - From packed environment:
Download the qr_reader.tar.gz archive

Extract the archive:
```bash
mkdir -p qr_reader
tar -xvzf qr_reader.tar.gz -C qr_reader
```

Repackage the environment and activate it:
```bash
./qr_reader/bin/conda-unpack
source qr_reader/bin/activate # Linux
qr_reader\Scripts\activate # Windows
```


### Conda - From scratch:
Create and activate your environment:
```bash
conda create --name qr_reader python=3.8
conda activate qr_reader
```

Install dependencies:
```bash
conda install -c conda-forge opencv pyzbar validators
```

### If using Pip:
Install the dependencies:
```bash
pip install opencv-python-headless pyzbar validators
```

## Usage

To scan QR codes and barcodes from an image, use the following command:

```bash
python qr_scanner.py -i <path_to_image> [-u]
```

### Parameters

- `-i`, `--image`: **Required**. The path to the input image that contains the barcode(s) or QR code(s).
  
- `-u`, `--unsafe`: **Optional**. If specified, it allows opening HTTP links (i.e., links starting with `http://`) in the browser. By default, only `https://` URLs are opened.

### Example

To scan a QR code in an image:

```bash
python qr_scanner.py -i /path/to/your/image.png
```

To allow opening `http` URLs in the browser (unsafe option):

```bash
python qr_scanner.py -i /path/to/your/image.png -u
```

### Notes
- If the image contains a QR code with an `https` link, the URL will be opened in your default web browser automatically.
- Barcodes are detected and logged to the console with their type and data.
- Press `q` to close the window displaying the image.
