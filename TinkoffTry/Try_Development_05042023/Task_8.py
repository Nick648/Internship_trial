class Tree:
    main_top = None

    def __init__(self, name: int, parent=None):
        self.name = name
        self.kids = []
        self.parent = parent
        self.value = 0
        if not parent:
            Tree.main_top = self
        else:
            parent.set_kids(self)

    def set_kids(self, kid) -> None:
        self.kids.append(kid)

    def set_value(self, value: int) -> None:
        self.value = value

    def get_name(self) -> int:
        return self.name

    def get_kids(self) -> list:
        return self.kids

    def get_parent(self):
        return self.parent

    def get_value(self) -> int:
        return self.value

    def check_name_kid(self, name: int):
        if self.get_name() == name:
            return self
        else:
            for kid in self.get_kids():
                feedback = kid.check_name_kid(name)
                if feedback is not None:
                    return feedback
            return None

    @classmethod
    def get_parent_by_name(cls, name: int):
        cur_top = Tree.main_top
        if cur_top.get_name() == name:
            return cur_top
        else:
            for kid in cur_top.get_kids():
                feedback = kid.check_name_kid(name)
                if feedback is not None:
                    return feedback
            return None

    def display_top(self, indent: str) -> None:
        print(f"{indent}{self.get_name()}, value={self.get_value()}")
        indent += "\t"
        for kid in self.get_kids():
            kid.display_top(indent)

    @classmethod
    def display_tree(cls) -> None:
        cur_top = Tree.main_top
        print(f"{cur_top.get_name()}, value={cur_top.get_value()}")
        for kid in cur_top.get_kids():
            kid.display_top("\t")


def main() -> None:
    count_top = int(input())
    tops = list(map(int, input().split()))
    tree = [Tree(name=1)]
    name = 2
    for parent in tops:
        p = Tree.get_parent_by_name(parent)
        tree.append(Tree(name=name, parent=p))
        name += 1
    values_x = list(map(int, input().split()))
    for value, top in zip(values_x, tree):
        top.set_value(value)
    Tree.display_tree()


if __name__ == '__main__':
    main()
