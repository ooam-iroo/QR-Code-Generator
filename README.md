# QR Code Generator

A simple and fast command-line QR Code Generator built with Python.

Generate QR codes from text, URLs, emails, phone numbers, Wi-Fi credentials, and more.

---

## ✨ Features

* Generate QR codes from any text
* Generate QR codes from URLs
* Save output as PNG
* Custom output file path
* Simple command-line interface
* Lightweight and easy to use

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/qr-code-generator.git
cd qr-code-generator
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Generate a QR Code from a URL:

```bash
python main.py --text "https://github.com/YourUsername"
```

Generate a QR Code from plain text:

```bash
python main.py --text "Hello World!"
```

Save to a custom location:

```bash
python main.py --text "Hello World!" --output hello.png
```

---

## 📁 Project Structure

```
qr-code-generator/
│
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Examples

### Website

```bash
python main.py --text "https://google.com"
```

### Email

```bash
python main.py --text "mailto:example@gmail.com"
```

### Phone Number

```bash
python main.py --text "tel:+1234567890"
```

### Wi-Fi

```bash
python main.py --text "WIFI:T:WPA;S:MyWifi;P:12345678;;"
```

---

## 🛠 Requirements

* Python 3.9+
* qrcode
* Pillow

---

## 📚 Dependencies

```text
qrcode[pil]
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
