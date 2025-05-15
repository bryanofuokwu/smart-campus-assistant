import random

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

def q_learning(episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.2):
    Q = {(s, a): 0 for s in states for a in actions}
    for _ in range(episodes):
        state = random.choice(states)
        for _ in range(5):  # simulate 5 steps per episode
            if random.random() < epsilon:
                action = random.choice(actions)
            else:
                action = max(actions, key=lambda a: Q[(state, a)])

            reward = rewards[(state, action)]
            next_state = transitions[(state, action)]
            max_q_next = max(Q[(next_state, a)] for a in actions)
            Q[(state, action)] += alpha * (reward + gamma * max_q_next - Q[(state, action)])
            state = next_state
    policy = {s: max(actions, key=lambda a: Q[(s, a)]) for s in states}
    return policy

if __name__ == "__main__":
    learned_policy = q_learning()
    print("Learned Q-Learning Policy:", learned_policy)