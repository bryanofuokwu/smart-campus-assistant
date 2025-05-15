from typing import Dict, List

class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[str]]):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for var in variables:
            self.constraints[var] = []

    def add_constraint(self, var1, var2, constraint_func):
        self.constraints[var1].append((var2, constraint_func))
        self.constraints[var2].append((var1, lambda x, y: constraint_func(y, x)))

    def is_consistent(self, var, assignment):
        for (other_var, constraint) in self.constraints[var]:
            if other_var in assignment and not constraint(assignment[var], assignment[other_var]):
                return False
        return True

    def backtrack(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        unassigned = [v for v in self.variables if v not in assignment][0]
        for value in self.domains[unassigned]:
            assignment[unassigned] = value
            if self.is_consistent(unassigned, assignment):
                result = self.backtrack(assignment)
                if result:
                    return result
            del assignment[unassigned]
        return None

if __name__ == "__main__":
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

    solution = scheduler.backtrack()
    print("Course Schedule:", solution)