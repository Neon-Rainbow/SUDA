import re

a = input(f'Confirm？(Y[es] or N[o])\n')
stra = re.compile('Y|Yes|y|YES')
strb = re.compile('N|No|NO')
if re.search(stra,a) is not None:
    print('Comfirmed')
elif re.search(strb,a) is not None:
    print("Not Confirmed")
else:
    print('输入错误')