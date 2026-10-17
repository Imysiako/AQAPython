import logging
import pytest
from controller import CarController

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("test_search.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class TestCarSearchAPI:

    @pytest.fixture(scope='class', autouse=True)
    @classmethod
    def controller(cls):
        client = CarController()
        auth_result = client.dz_auth()

        assert "access_token" in auth_result, f"Failed: {auth_result}"

        cls.client = client
        return client

    test_data = [
        ("price", 5),
        ("price", 10),
        ("year", 3),
        ("engine_volume", 4),
        ("brand", 6),
        (None, 8),
        ("price", None)
    ]

    @pytest.mark.parametrize("sort_by, limit", test_data)
    def test_search_cars(self, sort_by, limit):
        logger.info(f"First: sort_by={sort_by}, limit={limit}")

        response = self.client.get_cars(sort_by=sort_by, limit=limit)

        logger.info(f"Status code {response.status_code}")
        assert response.status_code == 200, f"Error: {response.text}"

        cars = response.json()
        logger.info(f"Lens: {len(cars)}")

        if limit is not None:
            assert len(cars) <= limit, f"Expected {limit}, received {len(cars)}"

        if sort_by and len(cars) > 1:
            values = [car[sort_by] for car in cars]
            sorted_values = sorted(values)
            assert values == sorted_values, f"Sorted {sort_by}. Value: {values}"
