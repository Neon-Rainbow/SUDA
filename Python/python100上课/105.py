import re


def spell_check():
    a = 'This     is    very   funny   and     cool.Indeed!'
    space = re.compile(' {2,}')
    sign = re.compile('\?|\.|,')
    a = re.sub(space, ' ', a)
    return a


print(spell_check())
