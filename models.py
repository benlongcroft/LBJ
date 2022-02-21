from app import db


class Products(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    colour = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    s_stock = db.Column(db.Integer, nullable=True)
    m_stock = db.Column(db.Integer, nullable=True)
    l_stock = db.Column(db.Integer, nullable=True)
    xl_stock = db.Column(db.Integer, nullable=True)
    image_path = db.Column(db.String(150), nullable=True)

    # db.relationship('product_order')


class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(400), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)

    # db.relationship('product_order')


# class ProductOrder(db.Model):
#     __tablename__ = 'product_order'
#     order_id = db.Column(db.Integer, db.ForeignKey(Orders.order_id), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey(Products.product_id), nullable=False)
#
#     db.relationship('product')
#     db.relationship('orders')
