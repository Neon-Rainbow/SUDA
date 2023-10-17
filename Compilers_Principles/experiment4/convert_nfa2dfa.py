#! /usr/bin/env python
# coding=utf-8
from convert_re2nfa import re2nfa


def p_closure(p, nfa_state):
    T = []
    T1 = [p]

    while len(T) != len(T1):
        T = [q for q in T1]

        for q in T:
            for t0, sym, t1 in nfa_state:
                if t0 == q and sym == 'eps' and t1 not in T1:
                    T1.append(t1)
    T1.sort()
    return T1


def move(NFA_state_T, input_symbol, NTran) -> list:
    states_sets_reached_through_inputsymbol = []
    for state in NFA_state_T:
        for tran in NTran:
            if state == tran[0] and input_symbol == tran[1]:
                states_sets_reached_through_inputsymbol.append(tran[2])
    return states_sets_reached_through_inputsymbol


def fun(p_closure_list: list, NFA_state) -> list:
    U = []
    for i in p_closure_list:
        temp_list = p_closure(i, NFA_state)
        for j in temp_list:
            if j not in U:
                U.append(j)
    return U


def isExist(DFA_states, current_state):
    for i in range(len(DFA_states)):
        if DFA_states[i][0] == current_state:
            if DFA_states[i][1]:
                return i
            else:
                return -i
    return -0.5


def nfa2dfa(Ntran):
    closure_table = {}
    NFA_final_state = 0
    for i in Ntran:
        if i[2] > NFA_final_state:
            NFA_final_state = i[2]
    for i in range(NFA_final_state + 1):
        closure_table[i] = p_closure(i, Ntran)
    DFA_states = [[p_closure(0, Ntran), False]]
    DFA_tran = []
    DFA_final_states = []
    length: int = len(DFA_states)  # length为当前DFA_states的长度,length会变化
    index: int = 0
    while index < length:
        if not DFA_states[index][1]:
            DFA_states[index][1] = True
            temp_state_a = fun(move(DFA_states[index][0], "a", Ntran), Ntran)
            temp_state_b = fun(move(DFA_states[index][0], "b", Ntran), Ntran)
            if (isExist(DFA_states, temp_state_a)) != -0.5 and (isExist(DFA_states, temp_state_b)) != -0.5 and (
            isExist(DFA_states, temp_state_a)) != index and (isExist(DFA_states, temp_state_b)) != index:
                DFA_final_states.append(chr(65 + index))
            if (isExist(DFA_states, temp_state_a)) == -0.5:
                DFA_states.append([temp_state_a, False])
            DFA_tran.append([chr(65 + index), "a", chr(65 + abs(isExist(DFA_states, temp_state_a)))])
            if (isExist(DFA_states, temp_state_b)) == -0.5:
                DFA_states.append([temp_state_b, False])
            DFA_tran.append([chr(65 + index), "b", chr(65 + abs(isExist(DFA_states, temp_state_b)))])
        if length == len(DFA_states) == index:
            break
        length = len(DFA_states)
        index += 1
    return DFA_tran, DFA_final_states


if __name__ == "__main__":
    Ntran = re2nfa("(a|b)*ab")
    DFA_tran, DFA_final_states = nfa2dfa(Ntran)
    for i in DFA_tran:
        print(f"{i[0]} to {i[2]}   by {i[1]}")
    print(f"final states are {DFA_final_states}")
