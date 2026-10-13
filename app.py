<!-- Section 1: Form Input Nilai -->
<div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
  <div class="bg-slate-50 border-b border-slate-200 px-6 py-4">
    <h2 class="text-lg font-bold text-slate-700 flex items-center">
      <i class="fa-solid fa-pen-to-square text-indigo-600 me-2"></i> Form Input Nilai Siswa
    </h2>
  </div>

  <form action="{{ url_for('simpan_nilai') }}" method="POST" class="p-6 space-y-6">
    <!-- Informasi Identitas -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div>
        <label for="nama_siswa" class="block text-xs font-semibold text-slate-600 uppercase mb-1">Nama Siswa</label>
        <input type="text" id="nama_siswa" name="nama_siswa" required placeholder="Masukkan nama lengkap"
               class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
      </div>

      <div>
        <label for="kelas" class="block text-xs font-semibold text-slate-600 uppercase mb-1">Kelas</label>
        <select id="kelas" name="kelas" required
                class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
          <option value="" disabled selected>-- Pilih Kelas --</option>
          <option value="7A">Kelas 7A</option>
          <option value="7B">Kelas 7B</option>
          <option value="8A">Kelas 8A</option>
          <option value="8B">Kelas 8B</option>
          <option value="9A">Kelas 9A</option>
          <option value="9B">Kelas 9B</option>
        </select>
      </div>

      <div>
        <label for="mapel" class="block text-xs font-semibold text-slate-600 uppercase mb-1">Mata Pelajaran</label>
        <select id="mapel" name="mapel" required onchange="kalkulasiOtomatis()"
                class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
          <option value="" disabled selected>-- Pilih Mata Pelajaran --</option>
          <option value="Matematika">Matematika</option>
          <option value="Bahasa Indonesia">Bahasa Indonesia</option>
          <option value="IPA">IPA (Sains)</option>
          <option value="IPS">IPS</option>
          <option value="Seni Budaya">Seni Budaya</option>
          <option value="PJOK">PJOK</option>
          <option value="Prakarya">Prakarya</option>
        </select>
      </div>
    </div>

    <hr class="border-slate-100">

    <!-- Input Nilai Komponen -->
    <div>
      <h3 class="text-sm font-bold text-slate-600 mb-3 uppercase tracking-wider">Komponen Penilaian (0 - 100)</h3>
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <div>
          <label for="formatif" class="block text-xs font-medium text-slate-500 mb-1">Formatif</label>
          <input type="number" id="formatif" name="formatif" min="0" max="100" step="any" placeholder="0" oninput="kalkulasiOtomatis()"
                 class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>

        <div>
          <label for="sumatif" class="block text-xs font-medium text-slate-500 mb-1">Sumatif</label>
          <input type="number" id="sumatif" name="sumatif" min="0" max="100" step="any" placeholder="0" oninput="kalkulasiOtomatis()"
                 class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>

        <div>
          <label for="pts" class="block text-xs font-medium text-slate-500 mb-1">PTS</label>
          <input type="number" id="pts" name="pts" min="0" max="100" step="any" placeholder="0" oninput="kalkulasiOtomatis()"
                 class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>

        <div>
          <label for="pas" class="block text-xs font-medium text-slate-500 mb-1">PAS</label>
          <input type="number" id="pas" name="pas" min="0" max="100" step="any" placeholder="0" oninput="kalkulasiOtomatis()"
                 class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>

        <div>
          <label for="praktek" class="block text-xs font-medium text-slate-500 mb-1">Praktek <span class="text-xs text-slate-400">(Opsional)</span></label>
          <input type="number" id="praktek" name="praktek" min="0" max="100" step="any" placeholder="0" oninput="kalkulasiOtomatis()"
                 class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500">
        </div>
      </div>
    </div>

    <!-- Display Hasil Pembulatan & Tombol Simpan -->
    <div class="bg-indigo-50 rounded-xl p-4 border border-indigo-100 flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <div class="p-3 bg-indigo-600 text-white rounded-lg">
          <i class="fa-solid fa-calculator text-xl"></i>
        </div>
        <div>
          <span class="block text-xs font-medium text-indigo-700 uppercase">Estimasi Nilai Rapot (Otomatis Dibulatkan)</span>
          <span id="preview-nilai" class="text-3xl font-extrabold text-indigo-900">0</span>
        </div>
      </div>

      <button type="submit" class="w-full md:w-auto bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2.5 px-6 rounded-lg transition duration-200 shadow-md hover:shadow border border-transparent flex items-center justify-center">
        <i class="fa-solid fa-floppy-disk me-2"></i> Simpan Nilai
      </button>
    </div>
  </form>
</div>

<!-- Section 2: Tabel Daftar Nilai Siswa -->
<div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
  <div class="bg-slate-50 border-b border-slate-200 px-6 py-4 flex justify-between items-center">
    <h2 class="text-lg font-bold text-slate-700 flex items-center">
      <i class="fa-solid fa-table text-indigo-600 me-2"></i> Data Penilaian Saya
    </h2>
    <span class="text-xs text-slate-500">Hanya menampilkan data yang dimasukkan oleh Anda</span>
  </div>

  <div class="overflow-x-auto">
    <table class="w-full text-left border-collapse text-sm">
      <thead>
        <tr class="bg-slate-100 text-slate-600 uppercase text-xs border-b border-slate-200">
          <th class="py-3 px-4 font-semibold">No</th>
          <th class="py-3 px-4 font-semibold">Nama Siswa</th>
          <th class="py-3 px-4 font-semibold">Kelas</th>
          <th class="py-3 px-4 font-semibold">Mata Pelajaran</th>
          <th class="py-3 px-4 font-semibold text-center">Formatif</th>
          <th class="py-3 px-4 font-semibold text-center">Sumatif</th>
          <th class="py-3 px-4 font-semibold text-center">PTS</th>
          <th class="py-3 px-4 font-semibold text-center">PAS</th>
          <th class="py-3 px-4 font-semibold text-center">Praktek</th>
          <th class="py-3 px-4 font-semibold text-center bg-indigo-50 text-indigo-800">Nilai Rapot</th>
          <th class="py-3 px-4 font-semibold text-center">Aksi</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-slate-100">
        {% if data %}
          {% for row in data %}
          <tr class="hover:bg-slate-50 transition">
            <td class="py-3 px-4 font-medium text-slate-500">{{ loop.index }}</td>
            <td class="py-3 px-4 font-semibold text-slate-800">{{ row.nama_siswa }}</td>
            <td class="py-3 px-4 text-slate-600"><span class="bg-slate-100 border border-slate-200 text-slate-700 text-xs px-2 py-0.5 rounded">{{ row.kelas }}</span></td>
            <td class="py-3 px-4 text-slate-600">{{ row.mapel }}</td>
            <td class="py-3 px-4 text-center text-slate-600">{{ row.formatif }}</td>
            <td class="py-3 px-4 text-center text-slate-600">{{ row.sumatif }}</td>
            <td class="py-3 px-4 text-center text-slate-600">{{ row.pts }}</td>
            <td class="py-3 px-4 text-center text-slate-600">{{ row.pas }}</td>
            <td class="py-3 px-4 text-center text-slate-600">{{ row.praktek if row.praktek > 0 else '-' }}</td>
            <td class="py-3 px-4 text-center font-bold text-indigo-700 bg-indigo-50/50 text-base">{{ row.nilai_akhir }}</td>
            <td class="py-3 px-4 text-center">
              <a href="#" class="text-indigo-600 hover:text-indigo-900 text-xs font-semibold underline">Cetak Rapot</a>
            </td>
          </tr>
          {% endfor %}
        {% else %}
          <tr>
            <td colspan="11" class="py-8 text-center text-slate-400">
              <i class="fa-regular fa-folder-open text-3xl mb-2 block"></i>
              Belum ada data nilai yang dimasukkan. Gunakan form di atas untuk menambah data.
            </td>
          </tr>
        {% endif %}
      </tbody>
    </table>
  </div>
</div>
