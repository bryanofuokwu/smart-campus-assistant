import argparse
from search.a_star import Graph
from csp.course_scheduler import CSP
from mdp.study_planner import policy_iteration
from rl.study_policy_qlearn import q_learning
from ml.course_classifier import clf
from nn.cheat_detector import model
from nlp.intent_classifier import model as nlp_model
from kb.faq_knowledge_base import KnowledgeBase
from bayes.topic_inference import NaiveBayesClassifier


def demo_pathfinding():
    g = Graph()
    g.add_node("Library", {"Cafeteria": 1, "Lab": 4})
    g.add_node("Cafeteria", {"Library": 1, "Gym": 2})
    g.add_node("Lab", {"Library": 4, "Gym": 3})
    g.add_node("Gym", {"Cafeteria": 2, "Lab": 3, "LectureHall": 5})
    g.add_node("LectureHall", {"Gym": 5})
    path = g.a_star("Library", "LectureHall")
    print("Shortest Path:", path)


def demo_course_scheduler():
    variables = ["AI", "ML", "NLP"]
    domains = {
        "AI": ["Mon 9am", "Tue 10am"],
        "ML": ["Mon 9am", "Wed 11am"],
        "NLP": ["Tue 10am", "Wed 11am"]
    }
    scheduler = CSP(variables, domains)
    scheduler.add_constraint("AI", "ML", lambda t1, t2: t1 != t2)
    scheduler.add_constraint("AI", "NLP", lambda t1, t2: t1 != t2)
    scheduler.add_constraint("ML", "NLP", lambda t1, t2: t1 != t2)
    print("Course Schedule:", scheduler.backtrack())


def demo_study_policy():
    print("Policy Iteration:", policy_iteration())
    print("Q-Learning Policy:", q_learning())


def demo_course_prediction():
    print("Prediction for [3.6, 14, 1]:", clf.predict([[3.6, 14, 1]])[0])


def demo_intent_classification():
    q = "Where is the library?"
    print(f"Intent for '{q}':", nlp_model.predict([q])[0])


def demo_knowledge_base():
    kb = KnowledgeBase()
    kb.tell("CS5210_requires_python")
    kb.add_rule("CS5210_requires_python", "student_needs_python")
    kb.add_rule("student_needs_python", "student_should_review_python")
    print("Should review Python?", kb.ask("student_should_review_python"))


def demo_topic_inference():
    clf = NaiveBayesClassifier()
    clf.train([
        ("AI planning search graph", "AI"),
        ("probability inference bayes", "Probabilistic Reasoning"),
        ("neural network deep learning", "Neural Networks"),
        ("token parsing question answer", "NLP"),
        ("value function markov decision", "MDP")
    ])
    print("Topic Inference:", clf.predict("bayesian inference"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="Module to run", choices=[
        "search", "csp", "mdp", "rl", "ml", "nlp", "kb", "bayes"
    ])
    args = parser.parse_args()

    if args.module == "search":
        demo_pathfinding()
    elif args.module == "csp":
        demo_course_scheduler()
    elif args.module == "mdp" or args.module == "rl":
        demo_study_policy()
    elif args.module == "ml":
        demo_course_prediction()
    elif args.module == "nlp":
        demo_intent_classification()
    elif args.module == "kb":
        demo_knowledge_base()
    elif args.module == "bayes":
        demo_topic_inference()

if __name__ == '__main__':
    main()