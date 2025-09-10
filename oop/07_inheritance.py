class Category:
    def __init__(self, category_name):
        self.category_name = category_name

    def get_info(self):
        return f"Category: {self.category_name}"


class SubCategory(Category):
    def __init__(self, category_name, subcategory_name):
        super().__init__(category_name)
        self.subcategory_name = subcategory_name

    def get_info(self):
        return f"{super().get_info()}, Subcategory: {self.subcategory_name}"


subcat = SubCategory("Clothing", "Shirts")
print(subcat.category_name)
print(subcat.subcategory_name)
print(subcat.get_info())
