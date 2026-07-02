import argparse
import os

import qrcode


def generate_qr(text: str, output: str):
    img = qrcode.make(text)

    os.makedirs(os.path.dirname(output), exist_ok=True)

    img.save(output)

    print(f"✅ QR Code saved to: {output}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate QR Codes from text or URLs."
    )

    parser.add_argument(
        "--text",
        required=True,
        help="Text or URL to encode"
    )

    parser.add_argument(
        "--output",
        default="output/qrcode.png",
        help="Output file path"
    )

    args = parser.parse_args()

    generate_qr(args.text, args.output)


if __name__ == "__main__":
    main()