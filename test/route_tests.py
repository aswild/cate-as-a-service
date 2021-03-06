from unittest import TestCase, main
from app import app

class RouteTests(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_can_get_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Should redirect
        self.assertNotEqual(response.data, '')

    def test_can_post_index(self):
        response = self.app.post('/', data=dict(text='test'))
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')

    def test_can_get_cate(self):
        response = self.app.get('/cate?text=meow')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')

    def test_can_get_cate_extended_route(self):
        response = self.app.get('/cate/meow')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')

    def test_missing_params_on_get_returns_400(self):
        response = self.app.get('/cate')
        self.assertEqual(response.status_code, 400)

    def test_missing_params_on_post_returns_400(self):
        response = self.app.post('/', data=dict())
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    main()

