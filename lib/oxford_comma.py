def oxford_comma(items):
    if len(items) == 1:  
        return items[0]
    elif len(items) == 2:
        return f'{items[0]} and {items[1]}'
    else:
        oxford_items = ', '.join(items[:-1]) + ', and ' + items[-1]
        return oxford_items 

print(oxford_comma(['Kiwi', 'Durian', 'Pear', 'Mango']))