
from decimal import Decimal

from django.test import TestCase

from .models import Product, ShippingBox
from .services import recommend_box


class RecommendBoxTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Toy Car",
            length=Decimal("10"),
            width=Decimal("8"),
            height=Decimal("5"),
            weight=Decimal("1"),
        )

        ShippingBox.objects.create(
            name="Small Box",
            length=Decimal("12"),
            width=Decimal("10"),
            height=Decimal("7"),
            max_weight=Decimal("5"),
            cost=Decimal("20"),
        )

        ShippingBox.objects.create(
            name="Medium Box",
            length=Decimal("20"),
            width=Decimal("15"),
            height=Decimal("10"),
            max_weight=Decimal("10"),
            cost=Decimal("35"),
        )

    def test_recommends_cheapest_suitable_box(self):
        box = recommend_box([self.product])

        self.assertEqual(box.name, "Small Box")

    def test_returns_none_when_weight_exceeds_capacity(self):
        ShippingBox.objects.all().update(
            max_weight=Decimal("0.5")
        )

        box = recommend_box([self.product])

        self.assertIsNone(box)

    def test_returns_none_when_dimensions_do_not_fit(self):
        ShippingBox.objects.all().update(
            length=Decimal("5"),
            width=Decimal("4"),
            height=Decimal("3"),
        )

        box = recommend_box([self.product])

        self.assertIsNone(box)

    def test_empty_order_raises_error(self):
        with self.assertRaises(ValueError):
            recommend_box([])

    def test_two_products_cannot_fit_in_one_product_sized_box(self):
        product_a = Product.objects.create(
            name="Product A",
            length=Decimal("10"),
            width=Decimal("10"),
            height=Decimal("10"),
            weight=Decimal("1"),
        )

        product_b = Product.objects.create(
            name="Product B",
            length=Decimal("10"),
            width=Decimal("10"),
            height=Decimal("10"),
            weight=Decimal("1"),
        )

        ShippingBox.objects.all().delete()

        ShippingBox.objects.create(
            name="Too Small Box",
            length=Decimal("10"),
            width=Decimal("10"),
            height=Decimal("10"),
            max_weight=Decimal("5"),
            cost=Decimal("10"),
        )

        box = recommend_box([product_a, product_b])

        self.assertIsNone(box)
