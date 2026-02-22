import nltk
from collections import defaultdict, Counter
from nltk.corpus import stopwords
from string import punctuation

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))
PUNCTUATION = set(punctuation)

def extract_proper_terms(file_path, max_terms=35):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)

    freq = Counter()
    scores = defaultdict(float)

    i = 0
    while i < len(pos_tags):
        word, tag = pos_tags[i]

        if tag not in ("NNP", "NNPS"):
            i += 1
            continue

        name_tokens = []

        while i < len(pos_tags) and pos_tags[i][1] in ("NNP", "NNPS"):
            name_word = pos_tags[i][0].strip("".join(PUNCTUATION))
            if name_word and name_word.isalpha():
                name_tokens.append(name_word)
            i += 1

        for name in name_tokens:
            name_lower = name.lower()
            if name_lower not in STOPWORDS:
                freq[name_lower] += 1
                scores[name_lower] += 3.0

    for word, tag in pos_tags:
        clean = word.strip("".join(PUNCTUATION))
        if clean and clean.isalpha() and clean.lower() not in STOPWORDS:
            if clean[0].isupper() and tag not in ("NNP", "NNPS"):
                name_lower = clean.lower()
                freq[name_lower] += 1
                scores[name_lower] += 1.5

    final_scores = {
        word: freq[word] * scores[word] for word in freq
    }

    sorted_terms = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)
    return [term for term, _ in sorted_terms[:max_terms]]

if __name__ == "__main__":
    top_terms = extract_proper_terms("Employee Profile.txt", max_terms=35)
    print(top_terms)
