import unittest
from unittest.mock import patch
from src.action.buzzer import app

class TestBuzzerAPI(unittest.TestCase):
    @patch('src.action.buzzer.GPIO')
    def test_activate_buzzer(self, mock_gpio):
        client = app.test_client()
        response = client.get('/buzzer/activate')
        self.assertEqual(response.status_code, 200)
        mock_gpio.output.assert_called_with(18, mock_gpio.HIGH)

    @patch('src.action.buzzer.GPIO')
    def test_deactivate_buzzer(self, mock_gpio):
        client = app.test_client()
        response = client.get('/buzzer/deactivate')
        self.assertEqual(response.status_code, 200)
        mock_gpio.output.assert_called_with(18, mock_gpio.LOW)

if __name__ == "__main__":
    unittest.main()
