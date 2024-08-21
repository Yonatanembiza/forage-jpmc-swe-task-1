import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quot in quotes:
      self.assertEqual(getDataPoint(quot), (quot['stcok'], quot['top_bid']['price'], quot['top_ask']['price'], (quot['top_bid']['price'] + quot['top_ask']['price']) / 2)) 

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 120.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), (quotes[0]['stock'], quotes[0]['top_bid']['price'], quotes[0]['top_ask']['price'], (quotes[0]['top_bid']['price'] + quotes[0]['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_zeroDivisionError(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.00, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.00, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_prices = {
       'ABC': (120.48 + 119.2) / 2,
       'DEF': (0.00 + 0.00) / 2
    }
    self.assertIsNone(getRatio(expected_prices['ABC'], expected_prices['DEF']))

  def test_getRatio(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_prices = {
       'ABC': (120.48 + 119.2) / 2,
       'DEF': (117.87 + 121.68) / 2
    }
    ratio = expected_prices['ABC'] / expected_prices['DEF']
    self.assertEqual(getRatio(expected_prices['ABC'], expected_prices['DEF']), ratio)


if __name__ == '__main__':
    unittest.main()
