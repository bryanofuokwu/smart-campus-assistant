from collections import defaultdict
import math

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = defaultdict(float)
        self.word_probs = defaultdict(lambda: defaultdict(float))
        self.vocab = set()
        self.class_counts = defaultdict(int)
        self.word_counts = defaultdict(lambda: defaultdict(int))

    def train(self, data):
        total = len(data)
        for text, label in data:
            self.class_counts[label] += 1
            for word in text.split():
                self.word_counts[label][word] += 1
                self.vocab.add(word)

        for label in self.class_counts:
            self.class_probs[label] = self.class_counts[label] / total
            total_words = sum(self.word_counts[label].values())
            for word in self.vocab:
                self.word_probs[label][word] = (self.word_counts[label][word] + 1) / (total_words + len(self.vocab))

    def predict(self, text):
        scores = {}
        for label in self.class_probs:
            score = math.log(self.class_probs[label])
            for word in text.split():
                if word in self.vocab:
                    score += math.log(self.word_probs[label][word])
            scores[label] = score
        return max(scores, key=scores.get)

if __name__ == "__main__":
    training_data = [
        ("AI planning search graph", "AI"),
        ("probability inference bayes", "Probabilistic Reasoning"),
        ("neural network deep learning", "Neural Networks"),
        ("token parsing question answer", "NLP"),
        ("value function markov decision", "MDP")
    ]

    classifier = NaiveBayesClassifier()
    classifier.train(training_data)

    test_text = "bayesian inference"
    print(f"Topic for '{test_text}':", classifier.predict(test_text))