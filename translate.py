from googletrans import Translator
import argparse

parser = argparse.ArgumentParser(description='translate a text in french with googletrans api')
parser.add_argument('--textfile', type=str,
                    help='a .txt file to translate')
                    
                    

file = parser.parse_args().textfile


def __main__():
    translator = Translator()
    with open(file) as f:
        list_of_lines = f.read().splitlines()
        for i, line in enumerate(list_of_lines):
            if line.endswith('-'):
                list_of_lines[i] = line[:-1]
        text = ' '.join(list_of_lines)
        translated = translator.translate(text, dest='fr')
        open('translated_%s'%file, 'w').write(translated.text)
    
if __name__=='__main__':
    __main__()
