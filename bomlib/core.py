class Item:
    def __init__(self, item_id: str, name: str):
        self.item_id = item_id
        self.name = name

    def __str__(self):
        return f"Item({self.item_id}, {self.name})"


class Bom:
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

    def __str__(self):
        items_str = "\n".join([str(item) for item in self.items.values()])
        return f"Items:\n{items_str}"


class Ingredient:
    # 包含数量、单位信息的Item
    def __init__(self, item: Item, quantity: float, unit: str = "piece"):
        self.item = item
        self.quantity = quantity
        self.unit = unit

    def __str__(self) -> str:
        return f"{self.item.name}: {self.quantity} {self.unit}"


class ProductionRecipe:
    # 包含输入和输出的Ingredient列表
    def __init__(
        self, recipe_id: str, output: list[Ingredient], input: list[Ingredient]
    ):
        self.recipe_id = recipe_id
        self.output = output
        self.ingredients = input

    def __str__(self):
        return f"Recipe({self.recipe_id}):\n{self.output}\n{self.ingredients}"


class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.recipe_id] = recipe

    def remove_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]

    def update_recipe(self, recipe_id, new_recipe):
        if recipe_id in self.recipes:
            self.recipes[recipe_id] = new_recipe

    def __str__(self):
        recipes_str = "\n".join([str(recipe) for recipe in self.recipes.values()])
        return f"Recipes:\n{recipes_str}"
