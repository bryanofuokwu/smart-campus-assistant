# Smart Campus Assistant: Full AI Integration Project

## 🎓 Overview
This project showcases a complete end-to-end AI system built for a university campus assistant. It brings together **all major topics** taught in UPenn’s **CIS 5210 Artificial Intelligence** course. Each module demonstrates a foundational AI concept — from search and planning to machine learning, reasoning, and natural language understanding.

The project is interactive and modular — run each part independently via CLI and see how individual AI topics translate into real applications.

---

## 📦 Modules & Explanations

### 🔍 1. Search Algorithms – `search/a_star.py`
**Concept:** A* Search is a graph traversal algorithm that finds the shortest path from a start node to a goal node by combining path cost (g) and heuristic estimates (h).

**How it works:**
- The graph consists of named nodes (e.g., "Library") with costs to neighboring nodes.
- A* maintains a priority queue where nodes are ranked based on f(n) = g(n) + h(n).
- In our example, we use a **uniform cost search** by setting the heuristic function `h(n)` to zero.
- The system returns the shortest path between any two locations on campus.

Use case: Finding the shortest walking route from Library to Lecture Hall.

---

### 📚 2. Constraint Satisfaction – `csp/course_scheduler.py`
**Concept:** CSPs model problems where variables must be assigned values under constraints.

**How it works:**
- Variables: Courses (e.g., "AI", "ML", "NLP")
- Domains: Available time slots (e.g., Mon 9am, Wed 11am)
- Constraints: No overlapping time slots
- The solver uses **backtracking search** to assign a valid time to each course while obeying all constraints.

Use case: Schedule classes for a student with no conflicts.

---

### 🎯 3. MDP (Markov Decision Process) – `mdp/study_planner.py`
**Concept:** MDPs are used for planning under uncertainty. The agent transitions between states based on probabilistic actions.

**How it works:**
- States: "low_energy", "focused", "tired"
- Actions: "study", "rest"
- Transition model: Deterministic mappings
- Rewards: +2 for studying when focused, -2 when tired, etc.
- Uses **policy iteration** to compute the best strategy for maximizing long-term rewards.

Use case: Recommend whether a student should rest or study based on their energy.

---

### 🔁 4. Reinforcement Learning – `rl/study_policy_qlearn.py`
**Concept:** RL learns from trial and error using rewards. Q-learning estimates action values without requiring a model.

**How it works:**
- Same state/action setup as MDP
- Learns Q-values over multiple episodes using the Q-learning update rule
- After training, picks actions that maximize learned rewards

Use case: Learn a study routine personalized for long-term success.

---

### 🧠 5. Machine Learning Classifier – `ml/course_classifier.py`
**Concept:** Supervised learning is used to predict labels based on features.

**How it works:**
- Features: GPA, study hours, preference for theory
- Label: "CS" or "Math"
- Model: Decision Tree Classifier
- Evaluated using train/test split and accuracy

Use case: Suggest whether a student might prefer a CS or Math major.

---

### ⚠️ 6. Neural Network – `nn/cheat_detector.py`
**Concept:** Neural networks model complex relationships through layers of interconnected neurons.

**How it works:**
- Input: Browser switch count, idle time, history of past strikes
- Architecture: 3 input features → 5 hidden units → sigmoid output
- Output: Probability of cheating
- Framework: PyTorch

Use case: Flag suspicious test behavior during online exams.

---

### 🗣️ 7. NLP (Intent Classification) – `nlp/intent_classifier.py`
**Concept:** Natural Language Processing classifies text into categories based on content.

**How it works:**
- Input: Student questions like "Where is the library?"
- Labels: location_query, time_query, instructor_query, help_request
- Uses scikit-learn’s CountVectorizer + Naive Bayes for intent classification

Use case: Understand what kind of help a student is asking for.

---

### 🧾 8. Knowledge Representation – `kb/faq_knowledge_base.py`
**Concept:** AI systems represent facts and rules to support logical reasoning.

**How it works:**
- Stores known facts (e.g., "CS5210_requires_python")
- Applies forward-chaining inference rules
- Automatically deduces new facts like "student_should_review_python"

Use case: Guide students on what background knowledge they need.

---

### 📊 9. Probabilistic Reasoning – `bayes/topic_inference.py`
**Concept:** Naive Bayes is a probabilistic model for classification based on Bayes’ Theorem.

**How it works:**
- Training data: keywords labeled with topics (e.g., "bayes" → Probabilistic Reasoning)
- Predicts the most likely topic from new text by combining word likelihoods

Use case: Detect what AI topic a student is discussing in a question.

---

## ✅ Summary of Topics Covered
| Module | Topic | Technique |
|--------|-------|-----------|
| Search | A* Search | Graph traversal with heuristics |
| CSP | Constraint Satisfaction | Backtracking search |
| MDP | Planning | Policy iteration |
| RL | Learning by interaction | Q-learning |
| ML | Classification | Decision Tree |
| NN | Deep Learning | Feedforward Neural Net |
| NLP | Language Understanding | Intent classification (Naive Bayes) |
| KB | Logic & Reasoning | Forward chaining inference |
| Bayes | Probabilistic Reasoning | Naive Bayes classifier |

---

## 💡 Why This Project Matters
This assistant demonstrates how a cohesive AI system can be built using foundational tools. It goes beyond toy examples to simulate real-world applications — decision making, dialogue handling, behavioral prediction, and planning — in a single, unified codebase.

---

## ⚙️ Run This Project
```bash
pip install -r requirements.txt
python main.py search     # Try pathfinding
python main.py csp        # Try course scheduling
python main.py ml         # Predict course fit
... and so on
```

---

Built for education, built from scratch. Push it to GitHub and show the world what AI can do.