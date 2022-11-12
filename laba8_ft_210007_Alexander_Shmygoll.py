import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        n = int(input('Введите число'))
        logging.info(f'Введено число {n}')
        break
    except ValueError:
        print(" Вводите число ! ")
        logging.error("ValueError", exc_info=True)

while True:
    p = list(range(1, n + 1))
    s_p = []

    for x in range(n):
        t = random.choice(p)
        logging.info(f'{x}-раз выпало число {t}')
        s_p.append(t)
        p.remove(t)

    print(s_p)

    while True:
        try:
            r = int(input('Продолжаем жеребьевку (Да - 1\Нет - 2) '))
            logging.info(f'Введено {r}')
            break
        except ValueError:
            print(' Если  Да -Введите 1  \ Нет -Введите -2 !')
            logging.error("ValueError", exc_info=True)
    if r == 1:
        ''
    else:
        break



































