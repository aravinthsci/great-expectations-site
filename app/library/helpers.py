import os.path
import markdown


def openfile(filename):
    filepath = os.path.join("/validations/", filename)
    with open(filename, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return html