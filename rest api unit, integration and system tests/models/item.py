from db import db


class ItemModel(db.Model):  # ItemModel inherits from db.Model (SGLAlchemy database)
    __tablename__ = 'items'  # give a name to a newly created table
    #  define columns (id, name, price) we're gonna store on our table
    id = db.Column(db.Integer, primary_key=True)  # primary key of integer type
    name = db.Column(db.String(80))  # name of up to 80 char string
    price = db.Column(db.Float(precision=2))  # float with precision of 2 elements after the decimal point

    def __init__(self, name, price):  # this lets us give the method a name and price
        self.name = name
        self.price = price

    def json(self):  # returns a dictionary representing the item (only its name and price)
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):  # this class finds an item by name
        return cls.query.filter_by(name=name).first()  # here we use SQLAlchemy to query our database by name
        #  cls is just an ItemModel, so it's like ItemModel.query.filter_by
        #  we're passing in the name as a property so it's gonna find out an item by its column called 'name'
        #  .first() > it's going to give us the first item from this column, it returns an Item object as well

    def save_to_db(self):  # we can add things to our database
        db.session.add(self)  # here we're adding the Item
        db.session.commit(  # commit saves the session contents to the disk

    def delete_from_db(self):  # we can delete things from our database
        db.session.delete(self)
        db.session.commit()
