from qlhsapp.models import Khoahoc, Lop, Hocsinh, Monhoc, Baikt, Hocky, Loaikt
from qlhsapp import db
from sqlalchemy import update
import hashlib


def save_hs(ho, ten, gioitinh, ngaysinh,
            sdt, diachi, email, lop_id):

    h = Hocsinh(ho=ho, ten=ten, gioitinh=gioitinh,
                ngaysinh=ngaysinh, sdt=sdt, diachi=diachi,
                email=email, lop_id=lop_id)
    db.session.add(h)
    db.session.commit()


def save_diem(hocsinh_id, monhoc_id,
              diem, loaiKT_id, hocky_id):

    d = Baikt(hocsinh_id=hocsinh_id, monhoc_id=monhoc_id,
              diem=diem, loaiKT_id=loaiKT_id, hocky_id=hocky_id)
    db.session.add(d)
    db.session.commit()


def update_siso(lop_id):
    l = Lop.query.get(lop_id)
    l.siso = l.siso + 1
    db.session.add(l)
    db.session.commit()


def load_lops():
    return Lop.query.all()

def load_monhoc():
    return Monhoc.query.all()

def load_loaikt():
    return Loaikt.query.all()

def load_hocky():
    return Hocky.query.all()

def load_lop_by_id(lop_id):
    query = Hocsinh.query
    if lop_id:
        query = query.filter(Hocsinh.lop_id == lop_id)
    return query.all()

def load_hs_by_id(hs_id):
    return Hocsinh.query.get(hs_id)

def get_lop_by_id(lop_id):
    return Lop.query.get(lop_id)


def load_hs(lop_id=None, kw=None):
    query = Hocsinh.query
    if lop_id:
        query = query.filter(Hocsinh.lop_id == lop_id)

    if kw:
        query = query.filter(Hocsinh.ten.contains(kw))

    return query.all()


def check_loaikt(hs_id,loaikt_id,hk_id, mh_id):
    c = Baikt.query.filter(Baikt.hocsinh_id == hs_id,
                           Baikt.loaiKT_id == loaikt_id,
                           Baikt.hocky_id == hk_id,
                           Baikt.monhoc_id == mh_id).count()
    return c

def get_hs_by_id(hs_id):
    return Hocsinh.query.get(hs_id)