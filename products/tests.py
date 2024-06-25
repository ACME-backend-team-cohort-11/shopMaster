from rest_framework.test import APITestCase  
from rest_framework import status  
from django.core.files.uploadedfile import SimpleUploadedFile  
from django.urls import reverse 
from .models import Product  
from .serializers import ProductSerializer  
import tempfile  
from PIL import Image  
import io  
from decimal import Decimal  

class ProductAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample product in the database
        self.product = Product.objects.create(
            name='Test Product',
            category='Test Category',
            price=Decimal('9.99'),
            description='Test Description',
            stars=5
        )
        # Create a sample image to use in tests
        self.image = self.create_test_image()

    def create_test_image(self):
        # Create a new RGB image with dimensions 100x100
        image = Image.new('RGB', (100, 100))
        # Save the image to a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temp_file)
        temp_file.seek(0)  # Go to the beginning of the file
        return temp_file

    def test_list_products(self):
        # Generate the URL for the product list view
        url = reverse('product-list')
        # Send a GET request to the URL
        response = self.client.get(url)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if one product is returned in the response
        self.assertEqual(len(response.data), 1)
        # Verify the name of the returned product
        self.assertEqual(response.data[0]['name'], 'Test Product')

    def test_retrieve_product(self):
        # Generate the URL for retrieving a single product
        url = reverse('product-detail', args=[self.product.id])
        # Send a GET request to the URL
        response = self.client.get(url)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify the name of the returned product
        self.assertEqual(response.data['name'], 'Test Product')

    def test_create_product(self):
        # Generate the URL for creating a new product
        url = reverse('product-list')
        # Define the data for the new product
        data = {
            'name': 'New Product',
            'category': 'New Category',
            'price': '19.99',
            'description': 'New Description',
            'stars': 4,
            'image': self.image  # Include the sample image
        }
        # Send a POST request to create the product
        response = self.client.post(url, data, format='multipart')
        # Check if the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Verify the total count of products in the database
        self.assertEqual(Product.objects.count(), 2)
        # Check the name of the newly created product
        self.assertEqual(Product.objects.get(id=response.data['id']).name, 'New Product')

    def test_update_product(self):
        # Generate the URL for updating an existing product
        url = reverse('product-detail', args=[self.product.id])
        # Define the updated data for the product
        data = {
            'name': 'Updated Product',
            'category': 'Updated Category',
            'price': '29.99',
            'description': 'Updated Description',
            'stars': 3,
            'image': self.image  # Include the sample image
        }
        # Send a PUT request to update the product
        response = self.client.put(url, data, format='multipart')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh the product instance from the database
        self.product.refresh_from_db()
        # Verify the updated product name
        self.assertEqual(self.product.name, 'Updated Product')

    def test_partial_update_product(self):
        # Generate the URL for partially updating a product
        url = reverse('product-detail', args=[self.product.id])
        # Define the data to partially update the product
        data = {
            'price': '49.99'  # Only updating the price
        }
        # Send a PATCH request to partially update the product
        response = self.client.patch(url, data, format='multipart')
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Refresh the product instance from the database
        self.product.refresh_from_db()
        # Verify the updated product price
        self.assertEqual(self.product.price, Decimal('49.99'))

    def test_delete_product(self):
        # Generate the URL for deleting a product
        url = reverse('product-detail', args=[self.product.id])
        # Send a DELETE request to the URL
        response = self.client.delete(url)
        # Check if the response status code is 204 No Content
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify that the product is deleted from the database
        self.assertEqual(Product.objects.count(), 0)

    def test_invalid_image_format(self):
        # Generate the URL for creating a new product
        url = reverse('product-list')
        # Create an invalid image file
        invalid_image = SimpleUploadedFile("image.txt", b"file_content", content_type="text/plain")
        # Define the data for the new product with an invalid image
        data = {
            'name': 'Invalid Image Product',
            'category': 'Invalid Category',
            'price': '9.99',
            'description': 'Invalid Description',
            'stars': 1,
            'image': invalid_image  # Include the invalid image
        }
        # Send a POST request to create the product
        response = self.client.post(url, data, format='multipart')
        # Check if the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Verify the error message for the invalid image
        self.assertIn('image', response.data)
        self.assertIn('Upload a valid image', response.data['image'][0].__str__())
