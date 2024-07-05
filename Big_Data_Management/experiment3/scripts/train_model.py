import tensorflow as tf
import numpy as np
import pickle
import sys

def generate_skipgram_data(sequences, window_size, vocab_size):
    couples = []
    labels = []
    for i, word_id in enumerate(sequences):
        start = max(0, i - window_size)
        end = min(len(sequences), i + window_size + 1)
        for j in range(start, end):
            if i != j:
                couples.append([word_id, sequences[j]])
                labels.append(1)
    return np.array(couples), np.array(labels)

if __name__ == "__main__":
    input_file = sys.argv[1]
    model_file = sys.argv[2]
    vectors_file = sys.argv[3]

    with open(input_file, 'rb') as f:
        sequences, word_index, vocab_size = pickle.load(f)

    window_size = 2
    couples, labels = generate_skipgram_data(sequences, window_size, vocab_size)

    print(f"Number of training samples: {len(couples)}")
    print(f"First 5 couples: {couples[:5]}")

    if couples.size == 0:
        raise ValueError("No training data generated. Check your data and preprocessing steps.")

    embedding_dim = 100

    target_input = tf.keras.layers.Input(shape=(1,), dtype='int32')
    context_input = tf.keras.layers.Input(shape=(1,), dtype='int32')

    embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, name='embedding')
    target_embedding = embedding(target_input)
    context_embedding = embedding(context_input)

    dot_product = tf.keras.layers.Dot(axes=-1)([target_embedding, context_embedding])
    dot_product = tf.keras.layers.Reshape((1,))(dot_product)
    output = tf.keras.layers.Dense(1, activation='sigmoid')(dot_product)

    model = tf.keras.models.Model(inputs=[target_input, context_input], outputs=output)
    model.compile(loss='binary_crossentropy', optimizer='adam')

    model.fit([couples[:, 0], couples[:, 1]], labels, epochs=5, batch_size=64)

    model.save(model_file)
    np.save(vectors_file, model.get_layer('embedding').get_weights()[0])