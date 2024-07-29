from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Coffee(db.Model):
    Production_id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer(50), nullable=False)
    Bean_type= db.String(db.Integer(50), nullable=False)
    roasting_level = db.String(db.Integer(50), nullable=False)   
    Grinding_level= db.String(db.Integer(50), nullable=False)
    additive_used= db.String(db.Integer(50), nullable=False)
   
class Potatoes(db.Model):
    Production_id = db.Column(db.Integer, primary_key=True)
    Batch_id = db.Column(db.String(50), nullable=False)
    Potatoes_type = db.Column(db.Integer, nullable=False)
    Processing_method = db.String(db.Integer(50), nullable=False)
    Preservatives= db.String(db.Integer(50), nullable=False)
    flavor_enhancers= db.String(db.Integer(50), nullable=False)
    texturizer_and_stabilizers= db.String(db.Integer(50), nullable=False)
    Color_additives= db.String(db.Integer(50), nullable=False)
    Antioxidant= db.String(db.Integer(50), nullable=False)
    Anti_caking_agent= db.String(db.Integer(50), nullable=False)
    Emulsifiers= db.String(db.Integer(50), nullable=False)
    Acidity_regulators= db.String(db.Integer(50), nullable=False)


class Banana(db.Model):
    Production_id = db.Column(db.Integer, primary_key=True)
    Batch_id = db.Column(db.String(50), nullable=False)
    Banana_type = db.Column(db.Integer, nullable=False)
    Processing_method = db.String(db.Integer(50), nullable=False)
    Preservatives= db.String(db.Integer(50), nullable=False)
    flavor= db.String(db.Integer(50), nullable=False)
    texturizer_and_stabilizers= db.String(db.Integer(50), nullable=False)
    Sweeteners= db.String(db.Integer(50), nullable=False)
    Antioxidant= db.String(db.Integer(50), nullable=False)
    Acidic_regulator= db.String(db.Integer(50), nullable=False)
    packaging_additives= db.String(db.Integer(50), nullable=False)
    fortification= db.String(db.Integer(50), nullable=False)


class Milk(db.Model):
    Production_id = db.Column(db.Integer, primary_key=True)
    Batch_id = db.Column(db.String(50), nullable=False)
    Milk_allocation = db.Column(db.Integer, nullable=False)
    Additives_used= db.String(db.Integer(50), nullable=False)
    Temperature= db.String(db.Integer(50), nullable=False)


class BatchFormation(db.Model):
    Batch_id = db.Column(db.Integer, primary_key=True)
    Product_id = db.Column(db.Integer, nullable=False)
    Batch_code = db.Column(db.Integer, nullable=False)
    Production_date = db.Column(db.Integer, nullable=False)
    Expiry_date = db.Column(db.Integer, nullable=False)
    Quantity_produced = db.Column(db.String(50), nullable=False    )

class Additives(db.Model):
    Additive_id = db.Column(db.Integer, primary_key=True)
    additive_name = db.Column(db.String(50), nullable=False)
    Additive_type = db.Column(db.String(50), nullable=False)
    Discription = db.Column(db.String(50), nullable=False)

class Packaging(db.Model):
    Packaging_id = db.Column(db.Integer, primary_key=True)
    Product_id = db.Column(db.Integer, nullable=False)
    Packaging_type = db.Column(db.String(50), nullable=False)
    Packaging_size = db.Column(db.String(50), nullable=False)
    Quantity_per_package = db.Column(db.String(50), nullable=False)
    Packaging_date = db.Column(db.Integer, nullable=False)

class Distribution(db.Model):
   Distribution_id = db.Column(db.Integer, primary_key=True)
   Batch_id = db.Column(db.Integer, nullable=False)
   Outlet_id = db.Column(db.Integer, nullable=False)
   Distribution_Date = db.Column(db.Integer, nullable=False)
   Quantity_distributed = db.Column(db.String(50), nullable=False)
   Packaging_id = db.Column(db.Integer, nullable=False)
class SaleTracking(db.Model):
    Sales_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    Outlet_id = db.Column(db.Integer, nullable=False)
    Sale_date = db.Column(db.Integer, nullable=False)
    Quantrity_sold = db.Column(db.String(50), nullable=False)
    Unit_price = db.Column(db.String(50), nullable=False)
    Total_omount = db.Column(db.Integer, nullable=False)
    Distribution_id = db.Column(db.Integer, nullable=False)

class client(db.Model):
    Customer_id = db.Column(db.Integer, primary_key=True)
    Customer_name = db.Column(db.String(50), nullable=False)
    Customer_Address = db.Column(db.Integer, nullable=False)
    Payment_method = db.Column(db.String(50), nullable=False)

class Suppliers(db.Model):
   Suppliers_id = db.Column(db.Integer, primary_key=True)
   Suppliers_name = db.Column(db.String(50), nullable=False)
   Contact_information = db.Column(db.String(50), nullable=False)
   Address = db.Column(db.Integer, nullable=False)

class Outlet(db.Model):
   Outlet_id = db.Column(db.Integer, primary_key=True)
   Outlet_name = db.Column(db.String(50), nullable=False)
   Contact_information = db.Column(db.String(50), nullable=False)
   Address = db.Column(db.Integer, nullable=False)

class RawMaterial(db.Model):
    Material_id = db.Column(db.Integer, primary_key=True)
    Material_name = db.Column(db.String(50), nullable=False)
    Material_type  = db.Column(db.String(50), nullable=False)
    Suppliers_id  = db.Column(db.Integer, nullable=False)
    Stock_quantity  = db.Column(db.String(50), nullable=False)
    Unit_of_price  = db.Column(db.String(50), nullable=False)

class Product(db.Model):
    Product_id = db.Column(db.Integer, primary_key=True)
    Product_name = db.Column(db.String(50), nullable=False)
    Product_type  = db.Column(db.String(50), nullable=False)
    Discription  = db.Column(db.String(50), nullable=False)

class ReturnDamage(db.Model):
    Returns_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    Batch_id = db.Column(db.Integer, nullable=False)
    Returns_date = db.Column(db.Integer, nullable=False)
    Quantity_returned = db.Column(db.String(50), nullable=False)
    Reason_for_return = db.Column(db.String(50), nullable=False)


class LedgerReport(db.Model):
    Ledger_id = db.Coblumn(db.Integer, primary_key=True)
    transaction_date = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.String(50), nullable=False)
    Sales_id = db.Column(db.Integer, nullable=False)


@app.route('/')
def index():
    coffee = Coffee.query.all()
    potatoes = Potatoes.query.all()
    banana = Banana.query.all()
    milk = Milk.query.all()
    batch_formation = BatchFormation.query.all()
    additives = Additives.query.all()
    packaging = Packaging.query.all()
    distribution = Distribution.query.all()
    sale_tracking = SaleTracking.query.all()
    clients = clients.query.all()
    Suppliers = Suppliers.query.all()
    ledger_report = LedgerReport.query.all()
    ReturnDamage = ReturnDamage.query.all()
    Product = Product.query.all()
    Outlet = Outlet.query.all()
    ledger_report = LedgerReport.query.all()

    return render_template('index.html', coffee=coffee, potatoes=potatoes, banana=banana, milk=milk,
                           batch_formation=batch_formation, additives=additives, packaging=packaging,
                           distribution=distribution, sale_tracking=sale_tracking, clients=clients,
                           Suppliers=Suppliers, ledger_report=ledger_report)

if __name__ == '__main__':
    app.run(debug=True)
