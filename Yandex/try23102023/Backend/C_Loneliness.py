# def add():
#     import matplotlib as mpl
#     import matplotlib.pyplot as plt
#     % matplotlib
#     inline
#
#     mpl.rc('font', family='Verdana', size=16)
#
#     w = numpy.linalg.solve(M6, v6)  # запишем найденные коэффициенты в переменную
#
#     def f(x):
#         return w[0] * x ** 2 + w[1] * x + w[2]  # уравнение параболы
#
#     fig, ax = plt.subplots(figsize=(10, 5))
#
#     x = numpy.linspace(-2, 2, 200)
#     ax.axis([-2., 2., 0., 2.])
#     ax.grid()
#     ax.plot(x, f(x), label='Парабола')
#     ax.plot(x, x, label='Биссектриса 1й\nкоординатной четверти')
#     ax.set_xlabel(u'x', {'fontname': 'Arial', 'size': 24})
#     ax.set_ylabel(u'f(x)', {'fontname': 'Arial', 'size': 24})
#     plt.plot([-1, 1], [1, 1], 'ro', label='Точки для\nпостроения графика')
#     ax.annotate('Точка\nкасания', xy=(1., 1.), xytext=(1.5, 0.5),
#                 arrowprops=dict(facecolor='black', shrink=0.05),
#                 )
#
#     ax.legend(bbox_to_anchor=(1.6, 1.))
#
#     plt.show()

def solve_with_numpy(a: list[list[float]], b: list[float]):
    import numpy  # импортируем библиотеку

    m = numpy.array(a)  # Матрица (левая часть системы)
    v = numpy.array(b)  # Вектор (правая часть системы)

    return numpy.linalg.solve(m, v)

def main() -> None:
    count_coordinates = int(input())
    A, B = [], []
    for _ in range(count_coordinates):
        x, y, z, d = map(float, input().split())
        A.append([x, y, z])
        B.append(d)
    # A = [
    #     [1.7, 2.8, 1.9],
    #     [2.1, 3.4, 1.8],
    #     [4.2, -1.7, 1.3]]
    # B = [0.7, 1.1, 2.8]

    print('Solution:', solve_with_numpy(A, B))  # Display solution output


if __name__ == '__main__':
    main()

'''
3
-5.0 -1.0 9.0 20.4694894905
4.0 -1.0 9.0 16.3095064303
-7.0 6.0 7.0 19.9499373433

Answer:
8.0 4.0 -6.0

'''