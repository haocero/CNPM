from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, update
from sqlalchemy.orm import relationship, backref, query
from qlhsapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    cat_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():


        p = Product.query.filter(Product.cat_id==1,
                                 Product.name=='test').count()
        print(p)

        db.session.add(p)
        db.session.commit()

        # # db.drop_all()
        # db.create_all()
