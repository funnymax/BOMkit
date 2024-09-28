class Item:
    # 某一物料的抽象，不包含数量信息

    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name

    def __str__(self):
        return f"Item({self.item_id}, {self.name})"


class Ingredient(Item):
    # 包含数量、单位信息的Item
    def __init__(
        self, item_id: str, name: str, quantity: float = 1, unit: str = "piece"
    ):
        super().__init__(item_id, name)
        self.quantity = quantity
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.item_id}-{self.name}: {self.quantity} {self.unit}"


class Repository:
    def __init__(self):
        self.items = {}

    def add(self, subject):
        if isinstance(subject, Item):
            self.items[subject.item_id] = subject
        elif isinstance(subject, str):
            pass  # 这里需要实现输入itemid增加
        elif isinstance(subject, Bom):
            self.items.update(subject.items)

    def remove_item(self, item_id: str):
        if item_id in self.items:
            del self.items[item_id]

    def update_item(self, item_id: str, new_item: Item):
        if item_id in self.items:
            self.items[item_id] = new_item

    def merge(self, other_bom):
        # 合并两个Bom，返回一个新的Bom
        return self.items.update(other_bom.items)

    def filter_by_name(self, name: str):
        return Bom([item for item in self.items.values() if name in item.name])

    def filter_by_id(self, item_id: str):
        return self.items[item_id]

    def __str__(self) -> str:
        return "\n".join([str(item) for item in self.items.values()])


class Bom(Repository):
    # 物料明细，既可以作为库存，也是Recipe的输入和输出
    def __init__(self):
        super().__init__()


class ProductionRecipe:
    # 描述物料之间的转换方式
    def __init__(self, recipe_id: str, output: Bom, input: Bom):
        self.recipe_id = recipe_id
        self.output = output
        self.input = input

    def reverse(self):
        return ProductionRecipe(self.recipe_id, self.input, self.output)

    def __str__(self):
        return f"Recipe({self.recipe_id}):\n{self.output}\n{self.input}"


class RecipeBook(Repository):
    # 这个类可存放若干Recipe，可以支持用特定的方法拆解物料
    def __init__(self):
        super().__init__()
