#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// NFA simulation function for C-style comments over alphabet {a, *, /}
bool simulate_nfa(const char *input) {
    bool current_states[5] = {false};
    current_states[0] = true; // Start state q0

    for (int i = 0; input[i] != '\0'; i++) {
        char ch = input[i];
        bool next_states[5] = {false};

        if (ch != 'a' && ch != '*' && ch != '/') {
            return false;
        }

        if (current_states[0]) {
            if (ch == '/') next_states[1] = true;
        }

        if (current_states[1]) {
            if (ch == '*') next_states[2] = true;
        }

        if (current_states[2]) {
            if (ch == 'a' || ch == '/') next_states[2] = true;
            if (ch == '*') {
                next_states[2] = true;
                next_states[3] = true;
            }
        }

        if (current_states[3]) {
            if (ch == 'a') next_states[2] = true;
            if (ch == '*') next_states[3] = true;
            if (ch == '/') next_states[4] = true;
        }

        for (int k = 0; k < 5; k++) {
            current_states[k] = next_states[k];
        }
    }

    return current_states[4];
}

void run_test_row(const char *test_str, bool expected_result) {
    bool actual_result = simulate_nfa(test_str);
    const char *actual_text = actual_result ? "ACCEPTED" : "REJECTED";
    const char *expected_text = expected_result ? "Accepted" : "Rejected";

    printf("%-20s | %-10s | Expected: %s\n", test_str, actual_text, expected_text);
}

int main() {
    printf("=====================================================\n");
    printf("   C-STYLE COMMENT RECOGNIZER (NFA AUTOMATON)\n");
    printf("=====================================================\n\n");

    printf("%-20s | %-10s | %s\n", "Input String", "Result", "Evaluation");
    printf("-----------------------------------------------------\n");

    // Accepted Test Cases
    run_test_row("/*a*/", true);
    run_test_row("/**/", true);
    run_test_row("/***/", true);
    run_test_row("/*aaa*aaa*/", true);
    run_test_row("/*a/a*/", true);

    // Rejected Test Cases
    run_test_row("/**", false);
    run_test_row("/*a/*aa*/", false);
    run_test_row("aaa/**/a", false);
    run_test_row("/*/", false);
    run_test_row("/**a/", false);
    run_test_row("//aaaa", false);

    printf("=====================================================\n\n");

    // Interactive custom user input
    char user_input[256];
    printf("Enter your own string to test: ");
    if (scanf("%255s", user_input) == 1) {
        bool res = simulate_nfa(user_input);
        printf("Input: \"%s\" -> Status: %s\n", user_input, res ? "ACCEPTED" : "REJECTED");
    }

    return 0;
}