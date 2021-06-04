from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):

    def test_create_item(self):
        item = ItemModel('Test Name', 60.99)

        self.assertEqual('Test Name', item.name,
                         "Item name does not equal the constructor argument")
        # the error message is shown if the 2 things are not equal
        self.assertEqual(60.99, item.price,
                         "Item price does not equal the constructor argument")

    def test_item_json(self):
        item = ItemModel('Test Name', 60.99)
        expected = {
            'name': 'Test Name',
            'price': 60.99
        }

        self.assertDictEqual(item.json(), expected,
                             "Incorrect JSON export of the item. Received {}, expected {}".format(item.json(),
                                                                                                  expected)
        )
