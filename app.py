from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kunci-rahasia-sekolah-smp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# --- MODEL DATABASE ---
class Guru(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nama_guru = db.Column(db.String(100), nullable=False)

class NilaiSiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guru_id = db.Column(db.Integer, db.ForeignKey('guru.id'), nullable=False) # Kunci data isolasi guru
    nama_siswa = db.Column(db.String(100), nullable=False)
    kelas = db.Column(db.String(10), nullable=False)
    mapel = db.Column(db.String(50), nullable=False)
    formatif = db.Column(db.Float, default=0)
    sumatif = db.Column(db.Float, default=0)
    pts = db.Column(db.Float, default=0)
    pas = db.Column(db.Float, default=0)
    praktek = db.Column(db.Float, default=0)
    nilai_akhir = db.Column(db.Integer, nullable=False) # Angka bulat

@login_manager.user_loader
def load_user(user_id):
    return Guru.query.get(int(user_id))

# --- ROUTE / HALAMAN ---
@app.route('/')
@login_required
def dashboard():
    # Mengambil HANYA data milik guru yang sedang login
    data_nilai = NilaiSiswa.query.filter_by(guru_id=current_user.id).all()
    return render_template('dashboard.html', data=data_nilai, nama=current_user.nama_guru)

@app.route('/simpan', methods=['POST'])
@login_required
def simpan_nilai():
    nama_siswa = request.form.get('nama_siswa')
    kelas = request.form.get('kelas')
    mapel = request.form.get('mapel')
    f = float(request.form.get('formatif') or 0)
    s = float(request.form.get('sumatif') or 0)
    pts = float(request.form.get('pts') or 0)
    pas = float(request.form.get('pas') or 0)
    pr = float(request.form.get('praktek') or 0)

    # Logika Perhitungan & Pembulatan Otomatis
    if pr > 0:
        total = (f * 0.20) + (s * 0.25) + (pts * 0.20) + (pas * 0.20) + (pr * 0.15)
    else:
        total = (f * 0.25) + (s * 0.35) + (pts * 0.20) + (pas * 0.20)

    # Pembulatan otomatis (contoh: 84.5 menjadi 85)
    nilai_bulat = math.floor(total + 0.5)

    baris_baru = NilaiSiswa(
        guru_id=current_user.id, # Data dikunci ke ID guru aktif
        nama_siswa=nama_siswa,
        kelas=kelas,
        mapel=mapel,
        formatif=f,
        sumatif=s,
        pts=pts,
        pas=pas,
        praktek=pr,
        nilai_akhir=nilai_bulat
    )
    db.session.add(baris_baru)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Buat tabel database jika belum ada
    app.run(debug=True)