from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship, backref, query, join, joinedload, outerjoin, session
from qlhsapp import db, app


class Khoahoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nam = Column(Integer, nullable=False)
    khoiLop = Column(Integer, nullable=False)

    lops = relationship('Lop', backref='khoahoc', lazy=True)

    def __str__(self):
        return str(self.nam)


class Lop(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenLop = Column(String(50), nullable=False)
    siso = Column(Integer(), default=0, nullable=False)

    khoahoc_id = Column(Integer, ForeignKey(Khoahoc.id), nullable=False)

    hocsinhs = relationship('Hocsinh', backref='lop', lazy=True)

    def __str__(self):
        return str(self.khoahoc.khoiLop) + self.tenLop


class Baikt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    hocsinh_id = Column(Integer, ForeignKey('hocsinh.id'), nullable=False)
    monhoc_id = Column(Integer, ForeignKey('monhoc.id'), nullable=False)
    diem = Column(Float, default=0, nullable=False)

    loaiKT_id = Column(Integer, ForeignKey('loaikt.id'), nullable=False)
    hocky_id = Column(Integer, ForeignKey('hocky.id'), nullable=False)

    def __str__(self):
        return self.diem


class Hocky(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    baikts = relationship('Baikt', backref='hocky', lazy=True)

    def __str__(self):
        return self.name


class Loaikt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    baikts = relationship('Baikt', backref='loaiKT', lazy=True)

    def __str__(self):
        return self.name


class Hocsinh(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    ho = Column(String(50), nullable=False)
    ten = Column(String(50), nullable=False)
    ngaysinh = Column(Date, nullable=False)
    gioitinh = Column(String(10), nullable=False)
    sdt = Column(String(20), nullable=False)
    diachi = Column(String(255), nullable=False)
    email = Column(String(255))

    lop_id = Column(Integer, ForeignKey(Lop.id), nullable=False)

    baikts = relationship('Baikt', backref='hocsinh', lazy=True)

    def __str__(self):
        return self.ho + ' ' + self.ten


class Monhoc(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenMH = Column(String(50), nullable=False, unique=True)

    baikts = relationship('Baikt', backref='monhoc', lazy=False)

    def __str__(self):
        return self.tenMH


if __name__ == '__main__':
    with app.app_context():
        # h = Hocsinh(name="Nhat hao")
        # db.session.add(h)
        # h = Lop(tenLop='').query.filter(Lop.tenLop.contains('a1')).all()
        # p = h[0].hocsinh.ten
        # h.name = "Nha hao"

        # h = Hocsinh.query.filter_by(id=3).first()
        # h.lop.tenLop

        # print(p)

        d = Hocsinh.query.filter_by(id=1).first()
        p = d.ngaysinh.month
        print(p, type(p))

        # db.drop_all()
        # db.create_all()
