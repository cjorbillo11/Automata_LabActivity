# DFA 4 State Transition Logic & Minimization Verification

def run_original_dfa4(input_str):
    delta = {
        '1': {'0': '2', '1': '4'},
        '2': {'0': '3', '1': '4'},
        '3': {'0': '6', '1': '3'},
        '4': {'0': '5', '1': '1'},
        '5': {'0': '6', '1': '1'},
        '6': {'0': '3', '1': '6'}
    }
    state = '1'
    accepting_states = {'3', '6'}
    
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta[state][symbol]
        
    return state in accepting_states


def run_minimized_dfa4(input_str):
    delta_min = {
        'A': {'0': 'B', '1': 'A'},  # A = {1, 4}
        'B': {'0': 'C', '1': 'A'},  # B = {2, 5}
        'C': {'0': 'C', '1': 'C'}   # C = {3, 6} (Accepting)
    }
    state = 'A'
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta_min[state][symbol]
        
    return state == 'C'


if __name__ == '__main__':
    samples = ["0", "00", "101001", "101010101000"]
    print("\n--- DFA 4 Execution Results ---")
    for sample in samples:
        orig = run_original_dfa4(sample)
        mini = run_minimized_dfa4(sample)
        print(f"String: '{sample}' -> Original: {orig} | Minimized: {mini}")