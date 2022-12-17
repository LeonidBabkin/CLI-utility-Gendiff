def turn_value(value):
    if value == '[complex value]':
        return '[complex value]'
    elif value == 'True' or value == "False":
        return str(value).lower()
    elif value == "None":
        return 'null'
    else:
        return f'\'{value}\''


def make_plainish(dct):
    finale = []
    for key, value in dct.items():
        if len(value) == 2:
            if value[1] == '+':
                finale.append(f'Property \'{key}\''
                              f' was added with value: {turn_value(value[0])}')
            elif value[1] == '-':
                finale.append(f'Property \'{key}\' was removed')
        elif len(value) > 2:
            if value[3] == '+':
                finale.append(f'Property \'{key}\' was updated.'
                              f' From {turn_value(value[0])}'
                              f' to {turn_value(value[2])}')
    return '\n'.join(finale)


def make_dict(datum):
    dct = {}
    for i in datum:
        i = i.split('.')
        key = '.'.join(i[: -2])
        if key in dct:
            if '{' and '}' in i[-2:][0]:
                dct[key].extend(['[complex value]', i[-2:][1]])
                dct.update({key: dct[key]})
            else:
                dct[key].extend(i[-2:])
                dct.update({key: dct[key]})
        else:
            if '{' and '}' in i[-2:][0]:
                dct.update({key: ['[complex value]', i[-2:][1]]})
            else:
                dct.update({key: i[-2:]})
    return dct


def make_list(datum):
    lst = []
    for i in datum:
        if '[' and ']' in i:
            one, two = i.index('[') + 1, i.index(']')
            string = i[one:two]
            string = string.split(',')
            for j in string:
                j = j.strip()
                j = j.strip('\'')
                i = i[:one - 1] + f'{j}'
                lst.append(i)
        else:
            lst.append(i)
    return lst


def desc_ts(data):
    lst = []
    string = ''
    for i in data:
        if isinstance(i['descendants'], list):
            for j in i['descendants']:
                if j['descendants'] == '':
                    string += f'{i["key"]}.{j["key"]}.{j["value"]}.{j["state"]}'
                    lst.append(string)
                    string = ''
                else:
                    string += f'{i["key"]}.{j["key"]}.{desc_ts(j["descendants"])}'
                    lst.append(string)
                    string = ''
        else:
            string += f'{i["key"]}.{i["value"]}.{i["state"]}'
            lst.append(string)
            string = ''
    return lst


def build_plain(data):
    lst = []
    string = ''
    for i in data:
        if isinstance(i['descendants'], list):
            for j in i['descendants']:
                if j['descendants'] == '':
                    string += f'{i["key"]}.{j["key"]}.{j["value"]}.{j["state"]}'
                    lst.append(string)
                    string = ''
                else:
                    string += f'{i["key"]}.{j["key"]}.{desc_ts(j["descendants"])}'
                    lst.append(string)
                    string = ''
        else:
            string += f'{i["key"]}.{i["value"]}.{i["state"]}'
            lst.append(string)
            string = ''
    list_ = make_list(lst)
    dict_ = make_dict(list_)
    plain = make_plainish(dict_)
    return plain.strip()
