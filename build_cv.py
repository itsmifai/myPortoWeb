import base64
import os

with open("Mifthahul-Amri.jpeg", "rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Curriculum Vitae — Miftahul Amri</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;450;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1e293b;
    background: #ffffff;
    width: 210mm;
    height: 297mm;
    margin: 0 auto;
    font-size: 9.2pt;
    line-height: 1.45;
  }}
  .page {{
    width: 210mm;
    height: 297mm;
    display: flex;
    overflow: hidden;
  }}
  .sidebar {{
    width: 72mm;
    background: #f8fafc;
    border-right: 1px solid #e2e8f0;
    padding: 16mm 14mm 16mm 16mm;
    display: flex;
    flex-direction: column;
    gap: 15px;
  }}
  .main {{
    width: 138mm;
    padding: 16mm 18mm 16mm 17mm;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}

  /* Photo & Identity */
  .photo-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }}
  .photo {{
    width: 82px;
    height: 82px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #ffffff;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.12);
    margin-bottom: 8px;
  }}

  .header-name {{
    font-size: 20pt;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #0f172a;
    line-height: 1.1;
  }}
  .header-title {{
    font-size: 10pt;
    font-weight: 600;
    color: #0284c7;
    margin-top: 3px;
    letter-spacing: -0.01em;
  }}
  .summary-text {{
    font-size: 8.7pt;
    color: #475569;
    line-height: 1.5;
    margin-top: 6px;
    text-align: justify;
  }}

  /* Section Styling */
  .section-title {{
    font-size: 8.2pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #0f172a;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 3.5px;
    margin-bottom: 7px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  /* Contact List */
  .contact-list {{
    display: flex;
    flex-direction: column;
    gap: 5.5px;
  }}
  .contact-item {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 7.9pt;
    color: #334155;
    text-decoration: none;
    word-break: break-all;
  }}
  .contact-item svg {{
    width: 12px;
    height: 12px;
    color: #0284c7;
    flex-shrink: 0;
  }}

  /* Sidebar blocks */
  .side-block {{
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}
  .side-item-title {{
    font-size: 8.4pt;
    font-weight: 600;
    color: #0f172a;
    line-height: 1.3;
  }}
  .side-item-sub {{
    font-size: 7.7pt;
    color: #64748b;
    line-height: 1.35;
  }}

  /* Skill Badges */
  .skill-group {{
    margin-bottom: 6px;
  }}
  .skill-group:last-child {{
    margin-bottom: 0;
  }}
  .skill-group-title {{
    font-size: 7.4pt;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    letter-spacing: 0.04em;
    margin-bottom: 3px;
  }}
  .skill-tags {{
    display: flex;
    flex-wrap: wrap;
    gap: 3.5px;
  }}
  .skill-tag {{
    font-size: 7.1pt;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    color: #334155;
    padding: 1.5px 5.5px;
    border-radius: 4px;
    font-weight: 500;
  }}

  /* Timeline & Work Experience */
  .exp-item {{
    display: flex;
    flex-direction: column;
    gap: 2px;
    margin-bottom: 9px;
  }}
  .exp-item:last-child {{
    margin-bottom: 0;
  }}
  .exp-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .exp-role {{
    font-size: 9.3pt;
    font-weight: 700;
    color: #0f172a;
  }}
  .exp-date {{
    font-size: 7.4pt;
    font-family: 'JetBrains Mono', monospace;
    color: #64748b;
    font-weight: 500;
  }}
  .exp-org {{
    font-size: 8.2pt;
    font-weight: 600;
    color: #0284c7;
    margin-bottom: 1.5px;
  }}
  .exp-desc {{
    font-size: 8.1pt;
    color: #475569;
    line-height: 1.42;
  }}

  /* Projects */
  .proj-grid {{
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .proj-item {{
    display: flex;
    flex-direction: column;
    gap: 1.5px;
  }}
  .proj-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .proj-name {{
    font-size: 8.8pt;
    font-weight: 700;
    color: #0f172a;
  }}
  .proj-category {{
    font-size: 7.4pt;
    color: #0284c7;
    font-weight: 600;
  }}
  .proj-desc {{
    font-size: 8.1pt;
    color: #475569;
    line-height: 1.4;
  }}

  .mono {{
    font-family: 'JetBrains Mono', monospace;
  }}
</style>
</head>
<body>

<div class="page">
  <!-- SIDEBAR (Left Column: Photo, Contact, Skills, Education, Certs) -->
  <aside class="sidebar">
    <!-- Formal Photo -->
    <div class="photo-container">
      <img src="data:image/jpeg;base64,{photo_b64}" alt="Miftahul Amri" class="photo">
    </div>

    <!-- Contact Info -->
    <div>
      <div class="section-title">Kontak & Media</div>
      <div class="contact-list">
        <div class="contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>mifthahulamri@gmail.com</span>
        </div>
        <div class="contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>+62 857-1682-3315</span>
        </div>
        <div class="contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>Surakarta, Indonesia</span>
        </div>
        <div class="contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
          <span>github.com/itsmifai</span>
        </div>
        <div class="contact-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          <span>instagram.com/itsmifai</span>
        </div>
      </div>
    </div>

    <!-- Education -->
    <div>
      <div class="section-title">Pendidikan</div>
      <div class="side-block">
        <div class="side-item-title">Universitas Muhammadiyah Surakarta</div>
        <div class="side-item-sub">S1 Pendidikan Teknik Informatika</div>
        <div class="side-item-sub mono" style="font-size:7.4pt;color:#0284c7;font-weight:600;">2023 – Sekarang</div>
      </div>
    </div>

    <!-- Skills -->
    <div>
      <div class="section-title">Keahlian Teknis</div>
      
      <div class="skill-group">
        <div class="skill-group-title">Frontend & Web</div>
        <div class="skill-tags">
          <span class="skill-tag">Next.js</span>
          <span class="skill-tag">React.js</span>
          <span class="skill-tag">TypeScript</span>
          <span class="skill-tag">Tailwind CSS</span>
          <span class="skill-tag">JavaScript</span>
          <span class="skill-tag">HTML5 / CSS3</span>
        </div>
      </div>

      <div class="skill-group">
        <div class="skill-group-title">Backend & Database</div>
        <div class="skill-tags">
          <span class="skill-tag">PostgreSQL</span>
          <span class="skill-tag">Supabase</span>
          <span class="skill-tag">Prisma ORM</span>
          <span class="skill-tag">MySQL</span>
          <span class="skill-tag">RESTful API</span>
        </div>
      </div>

      <div class="skill-group">
        <div class="skill-group-title">AI & Tools</div>
        <div class="skill-tags">
          <span class="skill-tag">AI Model Integration</span>
          <span class="skill-tag">Prompt Engineering</span>
          <span class="skill-tag">Git / GitHub</span>
          <span class="skill-tag">Vercel</span>
          <span class="skill-tag">Linux CLI</span>
          <span class="skill-tag">Docker</span>
        </div>
      </div>
    </div>

    <!-- Certifications -->
    <div>
      <div class="section-title">Sertifikasi Resmi</div>
      <div class="side-block" style="gap:5px;">
        <div>
          <div class="side-item-title" style="font-size:8.2pt;">AWS Cloud Web App Builder</div>
          <div class="side-item-sub">AWS Academy Graduate · 2026</div>
        </div>
        <div>
          <div class="side-item-title" style="font-size:8.2pt;">Dasar Pemrograman Web</div>
          <div class="side-item-sub">Dicoding Indonesia · 2024</div>
        </div>
        <div>
          <div class="side-item-title" style="font-size:8.2pt;">Intro to JavaScript for Beginner</div>
          <div class="side-item-sub">Harisenin.com · 2023</div>
        </div>
      </div>
    </div>

    <!-- Languages -->
    <div>
      <div class="section-title">Bahasa</div>
      <div style="font-size: 8pt; color: #334155; line-height: 1.5;">
        <div><strong>Bahasa Indonesia</strong> — Penutur Asli (Native)</div>
        <div><strong>English</strong> — Kemampuan Kerja (Working)</div>
      </div>
    </div>
  </aside>

  <!-- MAIN COLUMN (Right Column: Header, Summary, Experience, Projects) -->
  <main class="main">
    <!-- Header -->
    <section>
      <h1 class="header-name">Miftahul Amri</h1>
      <div class="header-title">Web Developer &bull; AI Enthusiast &bull; Coding Educator</div>
      <p class="summary-text">
        Mahasiswa Pendidikan Teknik Informatika UMS dan Software Developer yang berfokus pada perancangan aplikasi web modern serta integrasi model Artificial Intelligence. Berpengalaman membangun portal web nyata instansi, aktif membimbing praktikum pemrograman kampus, serta berdedikasi mengedukasi generasi muda dalam computational thinking dan logika pemrograman.
      </p>
    </section>

    <!-- Experience -->
    <section>
      <div class="section-title">Pengalaman Kerja & Mengajar</div>

      <div class="exp-item">
        <div class="exp-head">
          <span class="exp-role">Pengajar Ruangguru Coding</span>
          <span class="exp-date">2026 – Sekarang</span>
        </div>
        <div class="exp-org">Ruangguru &bull; Penempatan Kab. Sragen</div>
        <p class="exp-desc">
          Mengajar kurikulum computational thinking, fondasi logika pemrograman, dan creative coding (Scratch, game logic) untuk siswa sekolah mitra sesuai jenjang pembelajaran.
        </p>
      </div>

      <div class="exp-item">
        <div class="exp-head">
          <span class="exp-role">Guru Coding Ekstrakurikuler</span>
          <span class="exp-date">2026 – Sekarang</span>
        </div>
        <div class="exp-org">SMP Al Azhar IIBS Karanganyar</div>
        <p class="exp-desc">
          Melaksanakan bimbingan dan pengajaran materi dasar-dasar web development serta mendampingi perancangan proyek digital kreatif bagi siswa kelas 7–9.
        </p>
      </div>

      <div class="exp-item">
        <div class="exp-head">
          <span class="exp-role">Asisten Laboratorium PTI</span>
          <span class="exp-date">2025 – Sekarang</span>
        </div>
        <div class="exp-org">Pendidikan Teknik Informatika &bull; Universitas Muhammadiyah Surakarta</div>
        <p class="exp-desc">
          Membimbing praktikum mahasiswa S1 untuk mata kuliah <strong>Pemrograman Web</strong>, <strong>Basis Data</strong> (perancangan skema relasional, normalisasi ERD, query SQL), dan <strong>Sistem Operasi</strong> (manajemen proses dan otomasi scripting).
        </p>
      </div>

      <div class="exp-item">
        <div class="exp-head">
          <span class="exp-role">IT Helpdesk Staff (Intern)</span>
          <span class="exp-date">2023 – 2026</span>
        </div>
        <div class="exp-org">DSTI Universitas Muhammadiyah Surakarta</div>
        <p class="exp-desc">
          Menangani pemecahan masalah akun Single Sign-On (SSO) login civitas akademika, administrasi hak akses database mahasiswa, serta pendampingan teknis infrastruktur jaringan kampus.
        </p>
      </div>
    </section>

    <!-- Selected Projects -->
    <section>
      <div class="section-title">Proyek Unggulan Terpilih</div>
      <div class="proj-grid">
        <div class="proj-item">
          <div class="proj-head">
            <span class="proj-name">Website IMM SIMUN</span>
            <span class="proj-category">Portal Organisasi & Arsip Digital</span>
          </div>
          <p class="proj-desc">
            Portal resmi organisasi kemahasiswaan: memfasilitasi penerbitan naskah digital, direktori pengurus, repositori dokumen, dan arsip kaderisasi terpadu.
          </p>
        </div>

        <div class="proj-item">
          <div class="proj-head">
            <span class="proj-name">VibeCal AI (Google Vibe Hackathon)</span>
            <span class="proj-category">Kalender Cerdas & Ekstraksi AI</span>
          </div>
          <p class="proj-desc">
            Aplikasi produktivitas kalender pintar yang memproses percakapan dan catatan bahasa alami secara otomatis menjadi agenda kegiatan terstruktur.
          </p>
        </div>

        <div class="proj-item">
          <div class="proj-head">
            <span class="proj-name">Website MIM Gambiranom & CMS</span>
            <span class="proj-category">Profil Sekolah & CMS Mandiri</span>
          </div>
          <p class="proj-desc">
            Website profil resmi madrasah ibtidaiyah dasar dan Content Management System (CMS) mandiri untuk mempermudah guru mempublikasikan berita, galeri, dan transparansi sekolah.
          </p>
        </div>

        <div class="proj-item">
          <div class="proj-head">
            <span class="proj-name">LayakBisnis AI & Setara Special Ed</span>
            <span class="proj-category">Finansial UMKM & Asisten Edukasi</span>
          </div>
          <p class="proj-desc">
            Platform kalkulator kelayakan finansial UMKM terpadu dengan konsultasi strategi bisnis AI, serta platform asisten cerdas penyusun draf Program Pembelajaran Individual (PPI).
          </p>
        </div>
      </div>
    </section>
  </main>
</div>

</body>
</html>
"""

with open("cv.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("cv.html updated with generalized descriptions.")
