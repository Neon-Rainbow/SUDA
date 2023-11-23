v_table = {}  # variable table


def update_v_table(name, value):
    v_table[name] = value


def trans(node):
    for c in node.get_children():
        trans(c)

    # Translation

    # Assignment
    if node.get_data() == '[ASSIGNMENT]':
        ''' statement : VARIABLE '=' NUMBER'''
        value = node.get_child(2).get_value()
        node.get_child(0).set_value(value)
        # update v_table
        update_v_table(node.get_child(0).get_data(), value)


    # Operation
    elif node.get_data() == '[OPERATION]':
        '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                     | VARIABLE '=' VARIABLE '-' VARIABLE'''
        arg0 = v_table[node.get_child(2).get_data()]
        if node.get_child(4).get_data() != "1":
            arg1 = v_table[node.get_child(4).get_data()]
        else:
            arg1 = 1.0
        op = node.get_child(3).get_data()

        if op == '+':
            value = arg0 + arg1
        elif op == "-":
            value = arg0 - arg1
        elif op == "*":
            value = arg0 * arg1
        elif op == "/":
            value = arg0 / arg1

        if len(node.get_children()) == 7:
            value = 3

        node.get_child(0).set_value(value)
        # update v_table
        update_v_table(node.get_child(0).get_data(), value)

    # Print
    elif node.get_data() == '[PRINT]':
        '''print : PRINT '(' VARIABLE ')' '''
        arg0 = v_table[node.get_child(0).get_data()]
    # print(arg0)
