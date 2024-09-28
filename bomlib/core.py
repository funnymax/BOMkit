class Item:
    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name

    def __str__(self):
        return f"Item({self.item_id}, {self.name})"


class Ingredient(Item):
    # 包含数量、单位信息的Item
    def __init__(self, item_id: str, name: str, quantity: float, unit: str = "piece"):
        super().__init__(item_id, name)
        self.quantity = quantity
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.item_id}-{self.name}: {self.quantity} {self.unit}"

class Repository:
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.item_id] = item

    def remove_item(self, item_id: str):
        if item_id in self.items:
            del self.items[item_id]

    def update_item(self, item_id: str, new_item: Item):
        if item_id in self.items:
            self.items[item_id] = new_item

    def __str__(self) -> str:
        return "\n".join([str(item) for item in self.items.values()])


class Bom(Repository):
    # 这个类可存放若干Ingredient，作为Recipe的输入和输出
    def __init__(self):
        super().__init__()


class RecipeBook(Repository):
    # 这个类可存放若干Recipe
    def __init__(self):
        super().__init__()


class ProductionRecipe:
    # 包含输入和输出的Ingredient列表
    def __init__(
        self, recipe_id: str, output: Bom, input: Bom
    ):
        self.recipe_id = recipe_id
        self.output = output
        self.input = input
    
    def reverse(self):
        return ProductionRecipe(self.recipe_id, self.input, self.output)
    
    def __str__(self):
        return f"Recipe({self.recipe_id}):\n{self.output}\n{self.input}"

