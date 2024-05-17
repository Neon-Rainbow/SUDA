import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import sys

if __name__ == "__main__":
    input_file = sys.argv[1]
    vectors_file = sys.argv[2]

    with open(input_file, 'rb') as f:
        sequences, word_index, vocab_size = pickle.load(f)

    word_vectors = np.load(vectors_file)

    def find_similar_words(target_word, word_index, word_vectors, top_n=5):
        target_index = word_index.get(target_word)
        if not target_index:
            return []

        target_vector = word_vectors[target_index].reshape(1, -1)
        similarities = cosine_similarity(target_vector, word_vectors)[0]

        similar_indices = similarities.argsort()[-top_n-1:-1][::-1]
        similar_words = [(word, similarities[index]) for word, index in word_index.items() if index in similar_indices]

        return similar_words

    similar_words = find_similar_words('romeo', word_index, word_vectors)

    for word, similarity in similar_words:
        print(f"Word: {word}, Similarity: {similarity}, Vector: {word_vectors[word_index[word]]}")