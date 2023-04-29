import language_tool_python

tool = language_tool_python.LanguageTool('de')
def start():
    with open("transcript.txt", "r", encoding="iso-8859-1") as file:
        text = file.read()
    corrected = tool.correct(text)

    print(corrected)

if __name__ == "__main__":
    start()
