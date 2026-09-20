# DFA 3 State Transition Logic & Minimization Verification

def run_original_dfa3(input_str):
    delta = {
        '1': {'0': '4', '1': '2'},
        '2': {'0': '3', '1': '5'},
        '3': {'0': '4', '1': '5'},
        '4': {'0': '1', '1': '5'},
        '5': {'0': '6', '1': '2'},
        '6': {'0': '1', '1': '2'}
    }
    state = '1'
    accepting_states = {'3', '6'}
    
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta[state][symbol]
        
    return state in accepting_states


def run_minimized_dfa3(input_str):
    delta_min = {
        'S0': {'0': 'S0', '1': 'S1'},  # S0 = {1, 4}
        'S1': {'0': 'S2', '1': 'S1'},  # S1 = {2, 5}
        'S2': {'0': 'S0', '1': 'S1'}   # S2 = {3, 6} (Accepting)
    }
    state = 'S0'
    for symbol in input_str:
        if symbol not in ('0', '1'):
            return False
        state = delta_min[state][symbol]
        
    return state == 'S2'


if __name__ == '__main__':
    samples = ["0", "10", "10110", "1111111110"]
    print("\n--- DFA 3 Execution Results ---")
    for sample in samples:
        orig = run_original_dfa3(sample)
        mini = run_minimized_dfa3(sample)
        print(f"String: '{sample}' -> Original: {orig} | Minimized: {mini}")