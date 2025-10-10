import string
from collections import Counter
from itertools import count

blog_content = """
Python is an amazing programming language. Python is used in web development, data science, AI, and more.
"""
stopwords = [
    "a", "an", "the", "is", "in", "and", "to", "of", "for", "on", "with", "as", "by", "it", "from", "at", "be", "this", "that", "more", "used"
]
translator=str.maketrans('','',string.punctuation)
words=blog_content.translate(translator)
filtered_sentence=[word for word in words.lower().split() if word not in stopwords]
words_count=Counter(filtered_sentence)
most_common_word,freq=words_count.most_common(1)[0]
print(f"most common word is ={most_common_word} and its frequency is ={freq}")
