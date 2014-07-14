from sales.models import Orders, Categories, Suppliers, Products, OrderDetail
from autofixture import generators, register, AutoFixture

class CategoriesFixture(AutoFixture):
	field_values = {
		'name' : generators.FirstNameGenerator(),
		'description' : generators.LoremGenerator(),
		#'picture' : generators.ImageGenerator()
	}

register(Categories, CategoriesFixture)