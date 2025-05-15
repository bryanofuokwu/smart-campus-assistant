from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample training data
training_data = [
    ("Where is the AI class?", "location_query"),
    ("What time is my ML exam?", "time_query"),
    ("Who teaches NLP?", "instructor_query"),
    ("I need help with registration", "help_request"),
    ("Where can I find the library?", "location_query"),
    ("Tell me who teaches CS5210", "instructor_query"),
    ("When is the midterm?", "time_query"),
    ("I can't log into Canvas", "help_request")
]

X_train, y_train = zip(*training_data)

model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

model.fit(X_train, y_train)

# Test queries
queries = [
    "Where is my class held?",
    "I need tech support",
    "Who teaches Artificial Intelligence?",
    "When does the class meet?"
]

for q in queries:
    intent = model.predict([q])[0]
    print(f"Query: '{q}' => Intent: {intent}")
