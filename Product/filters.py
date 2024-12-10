from dj_rql.filter_cls import AutoRQLFilterClass
from Product.models import Product, Brand, Category


class ProductFilterClass(AutoRQLFilterClass):
    MODEL = Product
    # Filtros Personalizados
    FILTERS = [
        {
            'filter': 'brand',
            'source': 'brand__name'
        },
        {
            'filter': 'category',
            'source': 'category__name'
        }
    ]
        # com essa personalização do filtro o usuário pode filtrar diretamente pelo nome da marca e categoria,
        # e não pelo id da marca/categoria que é uma ForeignKey na tabela de produtos

class BrandFilterClass(AutoRQLFilterClass):
    MODEL = Brand


class CategoryFilterClass(AutoRQLFilterClass):
    MODEL = Category
