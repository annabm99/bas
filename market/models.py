from market import db # Import the db

class User(db.Model): # User object inherits from Model
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    # Passport are encripted
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # Relating User to Items through the owned_user backreference (so relationship is 1:N)
    items = db.relationship("Item", backref="owned_user", lazy=True) # Lazy is to grab all items in one shot (important)
    def __repr__(self):
            return f'User {self.username}' 

# Not working
# SQLAlchemy class. The classes we create will later be converted to database tables (modules with items)
class Item(db.Model): # Class item imports from the db.Model class
    # PRIMARY KEY (mandatory)
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True) # Create a column, parameters
                                                # String = string type character
                                                # Length = cannot be longer than 30 characters
                                                # Nullable = does it allow null fields?
                                                # Unique = make each item have a unique name (avoids confusion)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey("user.id")) # important to write user.id in lowercase

    # Make the input name be the name for the variable when created in the database
    def __repr__(self):
        return f'Item {self.name}' # Item will also be written in the name
    # Relting Item to User through a foreign key referring to the user id