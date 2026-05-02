import unittest
from shipping import get_shipping_cost


class TestShippingCost(unittest.TestCase):

    def test_weight_0_boundary_outside(self):
        self.assertRaises(ValueError, get_shipping_cost, 0)

    def test_weight_0_01_boundary_inside(self):
        self.assertEqual(get_shipping_cost(0.01), 10)

    def test_weight_2_boundary(self):
        self.assertEqual(get_shipping_cost(2), 10)

    def test_weight_2_01_second_segment(self):
        self.assertEqual(get_shipping_cost(2.01), 20)

    def test_weight_10(self):
        self.assertEqual(get_shipping_cost(10), 20)

    def test_weight_10_01(self):
        self.assertEqual(get_shipping_cost(10.01), 35)

    def test_weight_30(self):
        self.assertEqual(get_shipping_cost(30), 35)

    def test_weight_30_01(self):
        self.assertEqual(get_shipping_cost(30.01), 50)

    def test_weight_50(self):
        self.assertEqual(get_shipping_cost(50), 50)

    def test_weight_50_01_outside(self):
        self.assertRaises(ValueError, get_shipping_cost, 50.01)