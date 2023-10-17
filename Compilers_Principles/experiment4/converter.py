from convert_nfa2dfa import nfa2dfa
from convert_re2nfa import re2nfa


def re_mathing_by_dfa(string: str, DFA_tran: list, DFA_final_states: list) -> bool:
    current_state = "A"
    for current_char in string:
        for i in DFA_tran:
            if [current_state, current_char] == i[0:2]:
                current_state = i[2]
                break
    return current_state in DFA_final_states


def character_input():
    print(f"Please enter the string to be matched: (Default = abab)")
    string = input()
    print(f"Please enter the regular expression: (Default = (a|b)*ab)")
    regular_expression = input()
    if len(string) == 0:
        string = "abab"
    if len(regular_expression) == 0:
        regular_expression = "(a|b)*ab"
    return string, regular_expression


if __name__ == "__main__":
    string, regular_expression = character_input()
    Ntran = re2nfa(regular_expression)
    DFA_tran, DFA_final_states = nfa2dfa(Ntran)
    isMatch = re_mathing_by_dfa(string, DFA_tran, DFA_final_states)
    print(
        f"string is \t\"{string}\"\n"
        f"regular_expression is \t\"{regular_expression}\"\n"
        f"Do the string and re match? \t{isMatch}"
    )
