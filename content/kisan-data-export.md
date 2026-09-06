---
title: "किसान समस्या डेटा — Excel / CSV डाउनलोड एवं प्रबंधन | CaneUp"
date: 2026-09-06T12:35:00+05:30
description: "CaneUp किसान सहायता फॉर्म के माध्यम से प्राप्त सभी किसानों के डेटा को Excel (.csv/.xlsx) में डाउनलोड करें।"
slug: kisan-data-export
robots: "noindex, nofollow"
ShowToc: false
author: "Aamir Raza"
---

<style>
.data-admin-wrap {
  max-width: 1100px;
  margin: 20px auto 40px;
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #d1fae5;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  padding: 28px 24px;
  font-family: 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, sans-serif;
}
.data-admin-hdr {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 18px;
  border-bottom: 2px solid #e5e7eb;
}
.data-admin-hdr h2 {
  font-size: 24px;
  font-weight: 800;
  color: #15803d;
  margin: 0;
}
.data-admin-hdr p {
  font-size: 13px;
  color: #6b7280;
  margin: 4px 0 0;
}
.data-admin-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.btn-export {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
  text-decoration: none;
}
.btn-export-excel {
  background: #15803d;
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(21,128,61,0.25);
}
.btn-export-excel:hover {
  background: #166534;
  transform: translateY(-1px);
}
.btn-export-copy {
  background: #0284c7;
  color: #ffffff;
}
.btn-export-copy:hover {
  background: #0369a1;
}
.btn-export-danger {
  background: #ef4444;
  color: #ffffff;
}
.btn-export-danger:hover {
  background: #dc2626;
}
.stat-summary-bar {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.stat-card-sm {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 10px;
  padding: 12px 18px;
  flex: 1;
  min-width: 160px;
}
.stat-card-sm span {
  font-size: 12px;
  color: #166534;
  font-weight: 600;
  display: block;
}
.stat-card-sm b {
  font-size: 24px;
  color: #15803d;
  font-weight: 800;
}
.table-responsive {
  width: 100%;
  overflow-x: auto;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
}
.kisan-data-tbl {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: left;
}
.kisan-data-tbl thead {
  background: #052e16;
  color: #ffffff;
}
.kisan-data-tbl th {
  padding: 12px 14px;
  font-weight: 700;
  white-space: nowrap;
}
.kisan-data-tbl td {
  padding: 10px 14px;
  border-bottom: 1px solid #f3f4f6;
  color: #374151;
  vertical-align: top;
}
.kisan-data-tbl tbody tr:hover {
  background: #f9fafb;
}
.badge-consent {
  background: #dcfce7;
  color: #15803d;
  font-size: 11px;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  display: inline-block;
}
.empty-data-msg {
  text-align: center;
  padding: 40px 20px;
  color: #9ca3af;
  font-size: 15px;
}
.sheets-setup-note {
  margin-top: 30px;
  background: #fffbeb;
  border: 1px solid #fde68a;
  border-radius: 12px;
  padding: 16px 20px;
  font-size: 13px;
  color: #92400e;
  line-height: 1.6;
}
.sheets-setup-note strong {
  color: #78350f;
}
</style>

<div class="data-admin-wrap">
  <div class="data-admin-hdr">
    <div>
      <h2>📊 किसान सहायता फॉर्म — Excel डेटा</h2>
      <p>वेबसाइट और होमपेज से किसानों द्वारा दर्ज की गई सभी समस्याओं की लाइव सूची।</p>
    </div>
    <div class="data-admin-actions">
      <button onclick="downloadExcelCSV()" class="btn-export btn-export-excel">
        📥 Download Excel (.xlsx / .csv)
      </button>
      <button onclick="copyTableData()" class="btn-export btn-export-copy">
        📋 Copy for Excel
      </button>
      <button onclick="clearAllData()" class="btn-export btn-export-danger">
        🗑️ Clear Data
      </button>
    </div>
  </div>

  <div class="stat-summary-bar">
    <div class="stat-card-sm">
      <span>कुल दर्ज समस्याएं:</span>
      <b id="totalLeadsCount">0</b>
    </div>
    <div class="stat-card-sm">
      <span>व्हाट्सएप सहमति प्राप्त:</span>
      <b id="consentLeadsCount">0</b>
    </div>
    <div class="stat-card-sm">
      <span>सक्रिय जिले:</span>
      <b id="activeDistrictsCount">0</b>
    </div>
  </div>

  <div class="table-responsive">
    <table class="kisan-data-tbl" id="kisanTable">
      <thead>
        <tr>
          <th>#</th>
          <th>दिनांक / समय</th>
          <th>किसान का नाम</th>
          <th>मोबाइल नंबर</th>
          <th>जिला</th>
          <th>चीनी मिल</th>
          <th>गांव</th>
          <th>समस्या / संदेश</th>
          <th>सहमति</th>
        </tr>
      </thead>
      <tbody id="kisanTableBody">
        <tr>
          <td colspan="9" class="empty-data-msg">डेटा लोड हो रहा है...</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="sheets-setup-note">
    💡 <strong>Google Sheets ऑटो-सिंक:</strong> यदि आप चाहते हैं कि हर किसान का डेटा सीधे आपकी ऑनलाइन Google Sheet में भी ऑटोमैटिकली जुड़ता रहे, तो हमने इसके लिए तैयार स्क्रिप्ट <code>scripts/google-sheets-apps-script.js</code> में उपलब्ध करा दी है। 
  </div>
</div>

<script>
// Load and display data from localStorage
document.addEventListener('DOMContentLoaded', function() {
  loadKisanData();
});

function loadKisanData() {
  var leads = JSON.parse(localStorage.getItem('caneup_kisan_leads') || '[]');
  var tbody = document.getElementById('kisanTableBody');
  var totalCount = document.getElementById('totalLeadsCount');
  var consentCount = document.getElementById('consentLeadsCount');
  var distCount = document.getElementById('activeDistrictsCount');

  totalCount.textContent = leads.length;
  consentCount.textContent = leads.filter(function(l) { return l.consent; }).length;

  var uniqueDistricts = {};
  leads.forEach(function(l) {
    if (l.district) uniqueDistricts[l.district] = true;
  });
  distCount.textContent = Object.keys(uniqueDistricts).length;

  if (leads.length === 0) {
    tbody.innerHTML = '<tr><td colspan="9" class="empty-data-msg">अभी तक कोई फॉर्म सबमिशन नहीं है। होमपेज या फॉर्म पेज से टेस्ट करें।</td></tr>';
    return;
  }

  tbody.innerHTML = '';
  // Show newest first
  leads.slice().reverse().forEach(function(item, index) {
    var tr = document.createElement('tr');
    tr.innerHTML = '<td>' + (index + 1) + '</td>' +
                   '<td><small>' + (item.date || '') + '</small></td>' +
                   '<td><strong>' + escapeHtml(item.name || '') + '</strong></td>' +
                   '<td><a href="tel:' + item.phone + '">' + escapeHtml(item.phone || '') + '</a></td>' +
                   '<td>' + escapeHtml(item.district || '') + '</td>' +
                   '<td>' + escapeHtml(item.mill || '') + '</td>' +
                   '<td>' + escapeHtml(item.village || '') + '</td>' +
                   '<td style="max-width:280px;">' + escapeHtml(item.message || '') + '</td>' +
                   '<td><span class="badge-consent">✅ ' + (item.consent || 'हाँ') + '</span></td>';
    tbody.appendChild(tr);
  });
}

function escapeHtml(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// 1-Click Download as CSV/Excel with UTF-8 BOM for perfect Hindi characters
function downloadExcelCSV() {
  var leads = JSON.parse(localStorage.getItem('caneup_kisan_leads') || '[]');
  if (leads.length === 0) {
    alert('डाउनलोड करने के लिए अभी कोई डेटा उपलब्ध नहीं है।');
    return;
  }

  var headers = ['क्रमांक', 'तारीख', 'किसान का नाम', 'मोबाइल नंबर', 'जिला', 'चीनी मिल', 'गांव का नाम', 'समस्या / सवाल', 'व्हाट्सएप सहमति'];
  
  var csvRows = [];
  csvRows.push(headers.join(','));

  leads.forEach(function(item, idx) {
    var row = [
      idx + 1,
      '"' + (item.date || '').replace(/"/g, '""') + '"',
      '"' + (item.name || '').replace(/"/g, '""') + '"',
      '"' + (item.phone || '').replace(/"/g, '""') + '"',
      '"' + (item.district || '').replace(/"/g, '""') + '"',
      '"' + (item.mill || '').replace(/"/g, '""') + '"',
      '"' + (item.village || '').replace(/"/g, '""') + '"',
      '"' + (item.message || '').replace(/"/g, '""').replace(/\n/g, ' ') + '"',
      '"' + (item.consent || 'हाँ') + '"'
    ];
    csvRows.push(row.join(','));
  });

  // \uFEFF is UTF-8 BOM so Excel opens Hindi characters properly
  var csvContent = '\uFEFF' + csvRows.join('\r\n');
  var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  var filename = 'CaneUp_Kisan_Data_' + new Date().toISOString().slice(0, 10) + '.csv';
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// Copy table to clipboard for pasting straight into Excel
function copyTableData() {
  var leads = JSON.parse(localStorage.getItem('caneup_kisan_leads') || '[]');
  if (leads.length === 0) {
    alert('कॉपी करने के लिए कोई डेटा नहीं है।');
    return;
  }

  var lines = ['तारीख\tकिसान का नाम\tमोबाइल\tजिला\tचीनी मिल\tगांव\tसमस्या\tसहमति'];
  leads.forEach(function(item) {
    lines.push([
      item.date || '',
      item.name || '',
      item.phone || '',
      item.district || '',
      item.mill || '',
      item.village || '',
      (item.message || '').replace(/\n/g, ' '),
      item.consent || 'हाँ'
    ].join('\t'));
  });

  navigator.clipboard.writeText(lines.join('\n')).then(function() {
    alert('✅ डेटा क्लिपबोर्ड पर कॉपी हो गया है! आप Excel या Google Sheets में सीधे Paste (Ctrl+V) कर सकते हैं।');
  });
}

function clearAllData() {
  if (confirm('क्या आप वाकई सभी सेव किया हुआ डेटा हटाना चाहते हैं? यह क्रिया वापस नहीं ली जा सकेगी।')) {
    localStorage.removeItem('caneup_kisan_leads');
    loadKisanData();
  }
}
</script>
