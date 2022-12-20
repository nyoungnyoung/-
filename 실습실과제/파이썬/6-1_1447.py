def de_identify(id):
    if '-' in id:
        return f'{id[:-8]}*******'
    else:
        return f'{id[:-7]}*******'


print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))
