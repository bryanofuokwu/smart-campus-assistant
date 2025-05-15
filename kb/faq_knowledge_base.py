class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def tell(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def ask(self, query):
        inferred = set(self.facts)
        added = True
        while added:
            added = False
            for premise, conclusion in self.rules:
                if premise in inferred and conclusion not in inferred:
                    inferred.add(conclusion)
                    added = True
        return query in inferred

if __name__ == "__main__":
    kb = KnowledgeBase()
    kb.tell("CS5210_requires_python")
    kb.add_rule("CS5210_requires_python", "student_needs_python")
    kb.add_rule("student_needs_python", "student_should_review_python")

    print("Does the student need to review Python?",
          kb.ask("student_should_review_python"))