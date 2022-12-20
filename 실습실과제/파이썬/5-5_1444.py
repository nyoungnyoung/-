words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}


result = []
for el in words_dict:
    if el[0] in 'bmp':
        result.append(f'im{el}')
    elif el[0] == 'l':
        result.append(f'il{el}')
    elif el[0] == 'r':
        result.append(f'ir{el}')
    else:
        result.append(f'in{el}')
print(sorted(result))