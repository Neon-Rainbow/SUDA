import re
import string
from collections import Counter
from tensorflow.keras.preprocessing.text import Tokenizer
import sys
import pickle


def preprocess_text(file_path: str) -> tuple[list, dict, int]:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    words = text.split()

    word_counts = Counter(words)
    words = [word for word in words if word_counts[word] > 1]

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([words])
    sequences = tokenizer.texts_to_sequences([words])[0]  # 确保生成正确的序列
    word_index = tokenizer.word_index

    vocab_size = len(word_index) + 1

    return sequences, word_index, vocab_size


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sequences, word_index, vocab_size = preprocess_text(input_file)

    with open(output_file, 'wb') as f:
        pickle.dump((sequences, word_index, vocab_size), f)
