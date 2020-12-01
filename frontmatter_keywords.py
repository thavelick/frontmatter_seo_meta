from rake_nltk import Rake
r = Rake()

text = ""
with open('samples/enchiridion.md') as input_file:
    text = input_file.read()

r.extract_keywords_from_text(text)
print(r.get_ranked_phrases())