import re

a = input('输入电话号码')
mobile_phone_number = re.compile('1([0-9]{10})')
fixed_phone_number = re.compile('(0[0-9]{2,3}[1-9])(-?)([0-9]{6,7})')
special_phone_number = re.compile('119|120|110')
if re.match(mobile_phone_number, a) is not None:
    print('是电话号码')
elif re.match(fixed_phone_number, a) is not None:
    print('是固定电话')
elif re.match(special_phone_number, a) is not None:
    print('是特殊电话')
else:
    print('无法识别')