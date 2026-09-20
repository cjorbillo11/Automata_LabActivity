# DFA 1 State Transition Logic & Minimization Verification

def run_original_dfa1(input_str):
    delta = {
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'B', '1': 'C'},
        'D': {'0': 'B', '1': 'E'},
        'E': {'0': 'B', '1': 'C'}
    }
    state = 'A'
    accepting_states = {'E'}
    
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta[state][symbol]
        
    return state in accepting_states


def run_minimized_dfa1(input_str):
    delta_min = {
        'S0': {'0': 'S0', '1': 'S1'},  # S0 = {A, C}
        'S1': {'0': 'S0', '1': 'S2'},  # S1 = {B, D}
        'S2': {'0': 'S0', '1': 'S1'}   # S2 = {E} (Accepting)
    }
    state = 'S0'
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta_min[state][symbol]
        
    return state == 'S2'


if __name__ == '__main__':
    samples = ["0", "111", "1011", "11011"]
    print("\n--- DFA 1 Execution Results ---")
    for sample in samples:
        orig = run_original_dfa1(sample)
        mini = run_minimized_dfa1(sample)
        print(f"String: '{sample}' -> Original: {orig} | Minimized: {mini}")