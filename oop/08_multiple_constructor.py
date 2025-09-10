class Category:
  def __init__(self, *args):
    if len(args) == 1:
      self.category_name = args[0]
    elif len(args) == 2:
      self.category_name = args[0]
      self.subcategory_name = args[1]
    else:
      raise ValueError("Invalid number of arguments")
    
# @overload
# @classmethod