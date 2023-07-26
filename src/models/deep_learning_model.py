```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class DeepLearningModel:
    def __init__(self, vocab_size, embedding_dim, max_length, trunc_type='post', padding_type='post', oov_tok="<OOV>", training_portion=.8):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.max_length = max_length
        self.trunc_type = trunc_type
        self.padding_type = padding_type
        self.oov_tok = oov_tok
        self.training_portion = training_portion
        self.model = None
        self.tokenizer = None

    def tokenize(self, sentences):
        self.tokenizer = Tokenizer(num_words = self.vocab_size, oov_token=self.oov_tok)
        self.tokenizer.fit_on_texts(sentences)
        total_words = len(self.tokenizer.word_index)+1

        input_sequences = []
        for line in sentences:
            token_list = self.tokenizer.texts_to_sequences([line])[0]
            for i in range(1, len(token_list)):
                n_gram_sequence = token_list[:i+1]
                input_sequences.append(n_gram_sequence)

        return input_sequences, total_words

    def pad_sequences(self, input_sequences):
        input_sequences = pad_sequences(input_sequences, maxlen=self.max_length, padding=self.padding_type, truncating=self.trunc_type)
        predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
        label = tf.keras.utils.to_categorical(label, num_classes=self.total_words)
        return predictors, label

    def create_model(self, total_words):
        self.model = Sequential()
        self.model.add(Embedding(total_words, self.embedding_dim, input_length=self.max_length-1))
        self.model.add(LSTM(150, return_sequences = True))
        self.model.add(LSTM(100))
        self.model.add(Dense(total_words, activation='softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return self.model

    def train_model(self, predictors, label, epochs=100):
        history = self.model.fit(predictors, label, epochs=epochs, verbose=1)
        return history

    def generate_text(self, seed_text, next_words, max_sequence_len):
        for _ in range(next_words):
            token_list = self.tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
            predicted = self.model.predict_classes(token_list, verbose=0)
            
            output_word = ""
            for word, index in self.tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed_text += " " + output_word
        return seed_text
```