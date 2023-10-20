import unittest
import requests
import json

base_url = "http://localhost:5000/api"
EXAMPLE_ID = ""


class TestSkinAPI(unittest.TestCase):

    def test_available_skins(self):
        url = f"{base_url}/skins/available"
        response = requests.get(url)
        data = response.json()
        data = json.loads(data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_buy_skin(self):
        global EXAMPLE_ID
        url = f"{base_url}/skins/buy"
        data = {
            "name": "SkinName",
            "type": "SkinType",
            "price": 9.99,
            "color": "Red"
        }
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        EXAMPLE_ID = json.loads(data)["_id"]["$oid"]
        self.assertIsInstance(json.loads(data), dict)

    def test_my_skins(self):
        url = f"{base_url}/skins/myskins"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        data = json.loads(data)
        self.assertIsInstance(data, list)

    def test_change_skin_color(self):
        global EXAMPLE_ID
        url = f"{base_url}/skins/color"
        data = {
            "id": EXAMPLE_ID,
            "color": "Blue"
        }
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(json.loads(data), dict)

    def test_delete_skin(self):
        global EXAMPLE_ID
        url = f"{base_url}/skins/delete/{EXAMPLE_ID}"
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Comprueba que los datos sean un diccionario
        self.assertIsInstance(data, dict)

    def test_get_skin(self):
        global EXAMPLE_ID
        url = f"{base_url}/skins/getskin/{EXAMPLE_ID}"
        response = requests.get(url)
        # Comprueba que el status code sea 500 ya que el skin ya fue eliminado
        self.assertEqual(response.status_code, 500)


if __name__ == "__main__":
    print("-" * 50)
    print("Running tests...")
    print("-" * 50 + "\n")
    result = unittest.main(verbosity=2, exit=False)
    if result.result.wasSuccessful():
        print("\n" + "-" * 50)
        print("All tests passed!")
        print("-" * 50)
    else:
        print("\n" + "-" * 50)
        print("Some tests failed!")
        print("-" * 50)
