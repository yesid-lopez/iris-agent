import os
from io import BytesIO

import requests
from dotenv import load_dotenv

load_dotenv()


class DirectusClient:
    def __init__(self):
        self.base_url = os.getenv("DIRECTUS_BASE_URL")
        self.token = os.getenv("DIRECTUS_TOKEN")

    def get_products(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
            f"{self.base_url}/items/products",
            headers=headers,
        )
        products = response.json()
        return products["data"]

    def create_order(self, order_json):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(
            f"{self.base_url}/items/orders",
            headers=headers,
            json=order_json,
        )

        if response.status_code != 200:
            raise Exception(f"Failed to create order: {
                            response.status_code} {response.text}")
        return response

    def get_image(self, image_id):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(
            f"{self.base_url}/assets/{image_id}",
            headers=headers,
            stream=True,
        )
        if response.status_code == 200:
            return BytesIO(response.content)
