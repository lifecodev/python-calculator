import re


def calculator():
    # eval() не будет рассматриваться из-за нарушения безопасности.
    math_text = input('Math example: ')
    first_parts = re.findall(r"\((.*?)\)", math_text)
    if first_parts:
        for part in first_parts:
            math_text = math_text.replace(f'({part})', _calc(part), 1)
    math_text = _calc(math_text)
    print(float(math_text))


def _calc(text: str):
    math_text = text
    #  Деление и умножение
    while re.search(r"(-|)\d+(\.\d+|)([/*])\d+(\.\d+|)", math_text) is not None:
        div_op = re.search(r"(-|)\d+(\.\d+|)([/*])\d+(\.\d+|)", math_text).group()
        if div_op.count('/') == 1:
            val_arr = [float(x) for x in div_op.split('/')]
            total = val_arr[0] / val_arr[1]
            math_text = math_text.replace(div_op, str(total), 1)
        else:
            val_arr = [float(x) for x in div_op.split('*')]
            total = val_arr[0] * val_arr[1]
            math_text = math_text.replace(div_op, str(total), 1)

    #  Сложение и вычитание
    part_1 = math_text[0:1]
    part_2 = math_text[1:]
    math_text = part_1 + part_2.replace('-', '+-')
    while re.search(r"(-|)\d+(\.\d+|)\+(-|)\d+(\.\d+|)", math_text) is not None:
        sum_op = re.search(r"(-|)\d+(\.\d+|)\+(-|)\d+(\.\d+|)", math_text).group()
        val_sum = sum([float(x) for x in sum_op.split('+')])
        math_text = math_text.replace(sum_op, str(val_sum))
    return math_text


if __name__ == '__main__':
    calculator()
