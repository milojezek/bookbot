def main():
  path_to_file = "books/frankenstein.txt"
  with open(path_to_file) as f:
    file_contents = f.read()
  print(countWords(file_contents))

def countWords(text):
  words = text.split()
  return len(words)

if __name__ == "__main__":
  main()
