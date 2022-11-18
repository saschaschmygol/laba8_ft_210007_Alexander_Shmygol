import random
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:                                                      # проверка правильности ввода n
    try:
        n = int(input('Введите число'))
        logging.info(f'Введено число {n}')
        break
    except ValueError:
        print(" Вводите число ! ")
        logging.error("ValueError", exc_info=True)

while True:
    p = list(range(1, n + 1))

    while True:
        b = int(input('показать число - 1 :'))
        if b == 1:
            if len(p) != 0:
                t = random.choice(p)
                logging.info(f'выпало число {t}')
                p.remove(t)
                print(t)
            else:
                print('Боченки закончились =(')
                logging.info(f'Боченки закончились')
                break
        else:
            ''

    while True:                                                        # проверка условия , жеребьевка продолжается или нет
        try:
            r = int(input('Начать жеребьевку заново (Да - 1\Нет - 2) '))
            logging.info(f'Введено {r}')
            break
        except ValueError:
            print(' Если  Да -Введите 1  \ Нет -Введите -2 !')
            logging.error("ValueError", exc_info=True)
    if r == 1:
        ''
    else:
        break






























