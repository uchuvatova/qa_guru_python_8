"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


BUY_COUNT = 5


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity)
        assert not product.check_quantity(product.quantity + 1)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(product.quantity)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_first_product(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        assert cart.products[product] == BUY_COUNT

    def test_cart_add_one_more_product(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.add_product(product, 1)
        assert cart.products[product] == BUY_COUNT + 1

    def test_cart_remove_none_product(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product)
        assert product not in cart.products

    def test_cart_remove_one_product(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product, 1)
        assert cart.products[product] == BUY_COUNT - 1

    def test_cart_remove_all_products(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product, BUY_COUNT)
        assert product not in cart.products

    def test_cart_remove_more_then_all_products(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.remove_product(product, (BUY_COUNT + 1))
        assert product not in cart.products

    def test_empty_cart_clear(self, cart, product):
        cart.clear()
        assert product not in cart.products

    def test_cart_clear(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.clear()
        assert product not in cart.products

    def test_cart_get_total_price(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.get_total_price()
        assert cart.get_total_price() == product.price * BUY_COUNT

    def test_cart_empty_get_total_price(self, cart, product):
        cart.get_total_price()
        assert cart.get_total_price() == 0.0

    def test_cart_buy_available_items(self, cart, product):
        cart.add_product(product, BUY_COUNT)
        cart.buy()
        assert product not in cart.products

    def test_cart_buy_more_than_available(self, cart, product):
        cart.add_product(product, (product.quantity + 1))
        with pytest.raises(ValueError):
            cart.buy()
