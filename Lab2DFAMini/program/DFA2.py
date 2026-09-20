# DFA 2 State Transition Logic & Minimization Verification

def run_original_dfa2(input_str):
    delta = {
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q1', 'b': 'q3'},
        'q2': {'a': 'q1', 'b': 'q2'},
        'q3': {'a': 'q1', 'b': 'q4'},
        'q4': {'a': 'q1', 'b': 'q2'}
    }
    state = 'q0'
    accepting_states = {'q4'}
    
    for symbol in input_str:
        if symbol not in ('a', 'b'):
            return False
        state = delta[state][symbol]
        
    return state in accepting_states


def run_minimized_dfa2(input_str):
    delta_min = {
        'Group0': {'a': 'Group1', 'b': 'Group0'},  # {q0, q2}
        'Group1': {'a': 'Group1', 'b': 'Group2'},  # {q1, q3}
        'Group2': {'a': 'Group1', 'b': 'Group0'}   # {q4} (Accepting)
    }
    state = 'Group0'
    for symbol in input_str:
        if symbol not in ('a', 'b'):
            return False
        state = delta_min[state][symbol]
        
    return state == 'Group2'


if __name__ == '__main__':
    samples = ["b", "abb", "abbb", "ababb"]
    print("\n--- DFA 2 Execution Results ---")
    for sample in samples:
        orig = run_original_dfa2(sample)
        mini = run_minimized_dfa2(sample)
        print(f"String: '{sample}' -> Original: {orig} | Minimized: {mini}")