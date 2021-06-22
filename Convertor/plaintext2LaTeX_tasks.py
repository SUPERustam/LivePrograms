from pprint import pprint
import os


def main():
    dct = {}
    for file in os.listdir("tests_plainfiles"):
        with open(f'tests_plainfiles/{file}', 'rb') as f:
            text = f.read()
        try:
            text = text.decode('utf8')
        except UnicodeDecodeError:
            text = text.decode('utf16')
        dct = convertor(text, dct)
    dct = dict(sorted(dct.items(), key=lambda x: (x[0], x[1])))

    with open('plaintext2LaTeX_tasks.json', 'w', encoding='utf-8') as f:
        


def convertor(text: str, dct: dict) -> dict:
    lst = list(map(lambda x: x.strip(), text.split('\n')))
    tasks = list(filter(lambda x: lst.index(x) % 2 != 0, lst))
    points = list(filter(lambda x: lst.index(x) % 2 == 0, lst))

    for i, point in enumerate(points):
        # point = int(point)
        if point in dct:
            dct[point].append(tasks[i])
        else:
            dct[point] = [tasks[i]]
    return dct


if __name__ == '__main__':
    main()
