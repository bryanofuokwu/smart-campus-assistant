states = ["low_energy", "focused", "tired"]
actions = ["study", "rest"]
rewards = {
    ("low_energy", "study"): -1,
    ("low_energy", "rest"): 1,
    ("focused", "study"): 2,
    ("focused", "rest"): 0,
    ("tired", "study"): -2,
    ("tired", "rest"): 1,
}
transitions = {
    ("low_energy", "study"): "tired",
    ("low_energy", "rest"): "focused",
    ("focused", "study"): "focused",
    ("focused", "rest"): "low_energy",
    ("tired", "study"): "tired",
    ("tired", "rest"): "low_energy",
}

def policy_evaluation(policy, gamma=0.9, theta=0.01):
    V = {s: 0 for s in states}
    while True:
        delta = 0
        for s in states:
            a = policy[s]
            next_s = transitions[(s, a)]
            r = rewards[(s, a)]
            v = V[s]
            V[s] = r + gamma * V[next_s]
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

def policy_iteration():
    policy = {s: "rest" for s in states}
    stable = False
    while not stable:
        V = policy_evaluation(policy)
        stable = True
        for s in states:
            best_a = max(actions, key=lambda a: rewards[(s, a)] + 0.9 * V[transitions[(s, a)]])
            if best_a != policy[s]:
                stable = False
                policy[s] = best_a
    return policy

if __name__ == "__main__":
    optimal_policy = policy_iteration()
    print("Optimal Study Policy:", optimal_policy)