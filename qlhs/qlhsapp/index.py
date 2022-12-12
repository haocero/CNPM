from flask import render_template, request, redirect
from qlhsapp import app, dao
from datetime import  datetime
from qlhsapp.models import Lop
import os
from qlhsapp.admin import *

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/add-hs", methods=['get', 'post'])
def add_hs():
    err_msg = ''
    if request.method == 'POST':
        ngaysinh = datetime.strptime(request.form['ngaysinh'], "%Y-%m-%d")
        t = datetime.now().year - ngaysinh.year
        if (t >= 15 and t <= 20):
            try:
                dao.save_hs(ho=request.form['ho'],
                            ten=request.form['ten'],
                            gioitinh=request.form['gioitinh'],
                            ngaysinh=request.form['ngaysinh'],
                            diachi=request.form['diachi'],
                            sdt=request.form['sdt'],
                            email=request.form['email'],
                            lop_id=request.form['lop_id'])
                dao.update_siso(lop_id=request.form['lop_id'])
                err_msg = "Thêm thành công"
            except:
                err_msg = "Đã có lỗi xảy ra! Vui lòng thử lại sau!"
        else:
            err_msg = "Độ tuổi không đúng yêu cầu!!"
            # return redirect('/add-hs')
    return render_template('addhs.html', err_msg=err_msg)


@app.route('/chitiet-lop/<int:lop_id>')
def chitiet_lop(lop_id):
    kw = request.args.get('keyword')
    hsid = dao.load_lop_by_id(lop_id)
    hocsinh = dao.load_hs(lop_id=lop_id, kw=kw)
    l = dao.get_lop_by_id(lop_id)

    return render_template('chitietlop.html', hocsinh=hocsinh,
                           lop=l,hsid=hsid)


@app.route('/chitiet-hs/<int:hs_id>')
def chitiet_hs(hs_id):
    hs = dao.get_hs_by_id(hs_id)
    return render_template('chitieths.html', hocsinh=hs)


@app.route('/nhap-diem/hs-<int:hs_id>', methods=['get', 'post'])
def nhap_diem(hs_id):
    msg = ''

    hocsinh_id = dao.load_hs_by_id(hs_id)
    monhocs = dao.load_monhoc()
    loaikt = dao.load_loaikt()
    hocky = dao.load_hocky()

    if request.method == 'POST':
        loaikt_id = request.form['loaiKT_id']
        l = int(loaikt_id)
        c = dao.check_loaikt(hs_id=request.form['hocsinh_id'],
                             loaikt_id=request.form['loaiKT_id'],
                             hk_id=request.form['hocky_id'],
                             mh_id=request.form['monhoc_id'])
        if (l == 1 and c < 5):
            try:
                dao.save_diem(hocsinh_id=hs_id,
                              monhoc_id=request.form['monhoc_id'],
                              diem=request.form['diem'],
                              loaiKT_id=request.form['loaiKT_id'],
                              hocky_id=request.form['hocky_id'], )
                msg = 'Thêm thành công'
            except:
                msg = 'Đã có lỗi xảy ra!!!'
        else:
            if (l == 2 and c < 3):
                try:
                    dao.save_diem(hocsinh_id=request.form['hocsinh_id'],
                                  monhoc_id=request.form['monhoc_id'],
                                  diem=request.form['diem'],
                                  loaiKT_id=request.form['loaiKT_id'],
                                  hocky_id=request.form['hocky_id'], )
                    msg = 'Thêm thành công'
                except:
                    msg = 'Đã có lỗi xảy ra!!!'
            else:
                if (l == 3 and c < 1):
                    try:
                        dao.save_diem(hocsinh_id=request.form['hocsinh_id'],
                                      monhoc_id=request.form['monhoc_id'],
                                      diem=request.form['diem'],
                                      loaiKT_id=request.form['loaiKT_id'],
                                      hocky_id=request.form['hocky_id'], )
                        msg = 'Thêm thành công'
                    except:
                        msg = 'Đã có lỗi xảy ra!!!'
                else:
                    msg = 'Số bài kiểm tra trong học kỳ đã đạt tối đa!!!'

    return render_template('nhapdiem.html', monhocs=monhocs, loaikt=loaikt, hocky=hocky, hocsinh=hocsinh_id, msg=msg)


@app.context_processor
def common_data():
    lops = dao.load_lops()

    return {
        'lops': lops
    }


if __name__ == "__main__":
    app.run(debug=True)