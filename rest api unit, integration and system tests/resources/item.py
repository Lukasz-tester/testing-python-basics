from flask_restful import Resource, reqparse
from models.item import ItemModel


class Item(Resource):  # using 'flask_restful > Resource' means we can define some methods in the Item
    parser = reqparse.RequestParser()  # create a RequestParser where we can define some arguments eg. 'price'
    parser.add_argument('price',
                        type=float,  # we define the 'price' type
                        required=True,  # whether it's required
                        help="This field cannot be left blank!")  # and what happens if it's not included

    def get(self, name):
        # when a client such as a browser makes a 'get request' to our end-point
        # eg. get request for /item/piano [/item/<string:name>] will run the method get(piano)
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        # searches db for the given post, if it's not there - it creates a new post with the name
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()  # we create a new post with a parser
        #  when running parse_args() it looks at the request and extracts all the arguments we've put there (like 'price'), then it gives us the args in a dictionary
        #  the parser is going to extract some values from the json payload of the request, put it into the 'data' and let us create an ItemModel
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]}
