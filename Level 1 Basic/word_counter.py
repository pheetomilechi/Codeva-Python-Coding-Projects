import os

if __name__ == "__main__":
    path_to_txt = os.path.abspath(os.path.join("./", "TextFile.txt"))
    
    text = ""
    with open(path_to_txt, "r") as stream:
        text = stream.read()
        
        
        words = text.split()
        print('Words: ', words)
        print('Word count: ', len(words))