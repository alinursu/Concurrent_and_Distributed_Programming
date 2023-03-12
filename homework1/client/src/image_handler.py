import os


def discover_images(start_path=".") -> list:
    images = []

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)

            size = os.path.getsize(fp)
            images.append({"size": size, "path": fp})

    return images


def read_image_as_bytearray(path: str) -> bytearray:
    with open(path, "rb") as image:
        f = image.read()
    b = bytearray(f)
    return b
