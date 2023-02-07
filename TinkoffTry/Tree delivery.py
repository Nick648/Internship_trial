class Tree:
    main_town = None

    def __init__(self, name: int, parent=None):
        self.name = name
        self.kids = []
        self.parent = parent
        self.product = 0
        if not parent:
            Tree.main_town = self

    def set_kids(self, kid):
        self.kids.append(kid)

    def set_product(self, product):
        self.product = product

    def get_name(self) -> int:
        return self.name

    def get_kids(self) -> list:
        return self.kids

    def get_parent(self):
        return self.parent

    def get_product(self) -> int:
        return self.product

    def delivery(self, level, package) -> None:
        self.product += package
        if level > 0:
            level -= 1
            for kid in self.get_kids():
                kid.delivery(level, package)

    def display_town(self, indent: str) -> None:
        print(f"{indent}{self.get_name()}")
        indent += "\t"
        for kid in self.get_kids():
            kid.display_town(indent)

    @classmethod
    def display_tree(cls) -> None:
        print("Current Tree:\n")
        cur_town = Tree.main_town
        print(f"{cur_town.get_name()}")
        for kid in cur_town.get_kids():
            kid.display_town("\t")
        print()


def main() -> None:
    count_town = int(input("Введите количество городов(узлов): "))
    tree_town = [i + 1 for i in range(count_town)]
    tree_town[0] = Tree(1)
    print("\nНадо ввести дороги между городами в виде цифр; Example: 1 2")
    print(f"P.S. Count of roads = {count_town - 1}\n")
    for _ in range(count_town - 1):
        t_1, t_2 = map(int, input("Дорога между городами: ").strip().split())
        if isinstance(tree_town[t_1 - 1], Tree) and not isinstance(tree_town[t_2 - 1], Tree):
            tree_town[t_2 - 1] = Tree(t_2, tree_town[t_1 - 1])
            tree_town[t_1 - 1].set_kids(tree_town[t_2 - 1])
        elif isinstance(tree_town[t_2 - 1], Tree) and not isinstance(tree_town[t_1 - 1], Tree):
            tree_town[t_1 - 1] = Tree(t_1, tree_town[t_2 - 1])
            tree_town[t_2 - 1].set_kids(tree_town[t_1 - 1])
        else:
            print("\nError! Один из городов уже должен быть создан другой ещё не создан!")
            print("P.S. Город под номером 1 был создан с самого начала\n")
    # print(f"{tree=}")
    Tree.display_tree()
    transportation = int(input("Количество поставок: "))
    for _ in range(transportation):
        num_town, level, package = map(int, input("Номер города, На сколько спускаемся, Размер посылки: ").split())
        tree_town[num_town - 1].delivery(level, package)

    for town in tree_town:
        if isinstance(town, Tree):
            print(f"{town.get_product()}", end=" ")
    print()


if __name__ == '__main__':
    main()
