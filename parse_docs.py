import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_code = False
        self.current_code = []

    def handle_starttag(self, tag, attrs):
        if tag == 'code':
            self.in_code = True
        if tag in ['h1', 'h2', 'h3', 'p', 'li']:
            self.text.append('\n')

    def handle_endtag(self, tag):
        if tag == 'code':
            self.in_code = False
            self.text.append('`' + ''.join(self.current_code) + '`')
            self.current_code = []
        if tag in ['h1', 'h2', 'h3', 'p', 'li']:
            self.text.append('\n')

    def handle_data(self, data):
        if self.in_code:
            self.current_code.append(data)
        else:
            self.text.append(data.strip())

    def get_text(self):
        return ' '.join(self.text)

def parse_file(filename):
    with open(filename, 'r') as f:
        html = f.read()
    parser = TextExtractor()
    parser.feed(html)
    print(f"--- {filename} ---")
    print(parser.get_text())
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        parse_file(arg)
