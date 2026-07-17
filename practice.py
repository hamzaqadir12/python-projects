def main():
    file = input("File Name: ").strip().lower()
    type = file_type(file)
    print(type)


def file_type(file):
    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

main()