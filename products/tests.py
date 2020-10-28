# Testing viewing the products
# as well as the adding, editing, and deleting that the superuser is able to do

from django.test import TestCase
from .models import Product
from .forms import ProductForm

# Create your tests here.


class ProductsViewsTest(TestCase):
    """
    Test main products view returns properly
    """
    def test_get_products_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    """
    Test one product view returns properly
    """
    def test_get_one_product_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/one_product.html')


class TestProductModel(TestCase):
    """
    Test the Product Model is working
    """

    def test_product_model(self):
        # create a product
        product = Product(category="12oz",
                          sku="111111",
                          name="test",
                          description="Test Description",
                          price="10.99",
                          image="img.jpg",)
        # save product
        product.save()
        # check to see that the product fields equal the saved products values
        self.assertEqual(product.category, "sale")
        self.assertEqual(product.sku, "111111")
        self.assertEqual(product.name, "test")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.price, "10.99")
        self.assertEqual(product.image, "img.jpg")


class TestProducts(TestCase):
    """
    Test to check add a product posts successfully and the form is valid
    """
    def test_can_add_product(self):
        response = self.client.post('add/', {'name': 'Test Added Product'})
        self.assertRedirects(response, '/')

    """
    Test to check whether a product deletes successfully
    """
    def test_can_delete_product(self):
        product = Product.objects.create(name='Test Delete Product')
        response = self.client.get('delete/<int:product_id>/')
        self.assertRedirects(response, '/')
        existing_items = Product.objects.filter(pk=product.id)
        self.assertEqual(len(existing_items), 0)

    """
    Test to check when edited that a product posts successfully
    """
    def test_can_edit_product(self):
        product = Product.objects.create(name='Test Edit Product', done=True)
        response = self.client.get('edit/<int:product_id>/')
        self.assertRedirects(response, '/')
        updated_product = Product.objects.get(pk=product.id)
        self.assertFalse(updated_product.done)


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
        self.assertTrue(form.is_valid())

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

