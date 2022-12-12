from qlhsapp import admin, db
from qlhsapp.models import Khoahoc, Lop, Hocsinh, Monhoc, Baikt
from flask_admin.contrib.sqla import ModelView


class LopView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_labels = {
        'tenLop': 'Lớp',
        'siso': 'Sĩ số',
        'khoahoc': 'Khóa học'
    }


class HocsinhView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_labels = {
        'ten': 'Tên',
        'ho': 'Họ và tên lót',
        'ngaysinh': 'Ngày sinh',
        'gioitinh': 'Giới tính',
        'sdt': 'SĐT',
        'diachi': 'Địa chỉ',
        'email': 'Email',
        'lop': 'Lớp',
        'baikts': 'Bài kiểm tra'
    }


class KhoahocView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True
    column_labels = {
        'nam': 'Năm học',
        'khoiLop': 'Khối lớp'
    }


class MonhocView(ModelView):
    can_view_details = True
    create_modal = True
    # edit_modal = True
    details_modal = True
    column_labels = {
        'tenMH': 'Tên môn học',
        'baikts': 'Bài kiểm tra'
    }


class BaiktView(ModelView):
    can_view_details = True
    create_modal = True
    # edit_modal = True
    details_modal = True
    column_labels = {
        'diem': 'Điểm',
        'hocsinh': 'Học sinh',
        'monhoc': 'Môn học',
        'loaiKT': 'Loại kiểm tra',
        'hocky': 'Học kỳ'
    }


admin.add_view(KhoahocView(Khoahoc, db.session, name='Khóa học'))
admin.add_view(LopView(Lop, db.session, name='Lớp học'))
admin.add_view(HocsinhView(Hocsinh, db.session, name='Học sinh'))
admin.add_view(MonhocView(Monhoc, db.session, name='Môn học'))
admin.add_view(BaiktView(Baikt, db.session, name='Bài kiểm tra'))