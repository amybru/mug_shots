# Testing viewing the products
# as well as the adding, editing, and deleting that the superuser is able to do

from django.test import TestCase
from .models import Product, Category
from .forms import ProductForm

# Create your tests here.

def create_test_prod():
    cat = Category(name="sale", friendly_name="sale")
    cat.save()
    product = Product(category=cat,
                          sku="111111",
                          name="test",
                          description="Test Description",
                          price="10.99",
                          image="img.jpg",)
        # save product
    product.save()
    return (product, cat)


class ProductsViewsTest(TestCase):
    """
    Test main products view returns properly
    """
    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    """
    Test one product view returns properly
    """
    def test_get_one_product_page(self):
        product, cat = create_test_prod()
        response = self.client.get('/products/' + str(product.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/one_product.html')


class TestProductModel(TestCase):
    """
    Test the Product Model is working
    """

    def test_product_model(self):
        # create a product
        product, cat = create_test_prod()
        # check to see that the product fields equal the saved products values
        self.assertEqual(product.category, cat)
        self.assertEqual(product.sku, "111111")
        self.assertEqual(product.name, "test")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, "10.99")
        self.assertEqual(product.image, "img.jpg")


class ProductFormTest(TestCase):
    """
    Check that validation works when a user doesn't fill in at
    least one field, all fields are required, tests forms.py
    """
    def test_product_form(self):
        form = ProductForm({
            'category': 'sale',
            'sku': '111111',
            'name': 'test',
            'description': 'Test Description',
            'price': '10',
        })
        self.assertFalse(form.is_valid())

    def test_product_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0],
                         'This field is required.')

    def test_product_description_is_required(self):
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_product_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0],
                         'This field is required.')

