---
title: "किसान सहायता एवं समस्या निवारण — गन्ना पर्ची, सर्वे व भुगतान सहायता | CaneUp"
date: 2026-09-06T12:15:00+05:30
lastmod: 2026-09-06T12:15:00+05:30
description: "गन्ना किसान अपनी समस्या (पर्ची, सट्टा, सर्वे, ई-गन्ना ऐप, भुगतान) सीधे दर्ज करें। अपनी चीनी मिल चुनकर व्हाट्सएप पर दैनिक अपडेट्स पाएं।"
keywords: ["गन्ना किसान समस्या निवारण", "caneup kisan help form", "गन्ना पर्ची शिकायत", "गन्ना भुगतान समस्या", "चीनी मिल व्हाट्सएप अपडेट"]
slug: kisan-samasya-form
ShowToc: false
author: "Aamir Raza"
authors:
- "Aamir Raza"
author_name: "Aamir Raza"
author_image: "/images/authors/aamir-raza.webp"
---

<style>
.kisan-form-container {
  max-width: 820px;
  margin: 20px auto 40px;
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #d1fae5;
  box-shadow: 0 10px 30px rgba(21, 128, 61, 0.08);
  overflow: hidden;
  font-family: 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.kisan-form-header {
  background: linear-gradient(135deg, #052e16 0%, #15803d 100%);
  color: #ffffff;
  padding: 30px 24px;
  text-align: center;
}
.kisan-form-header h2 {
  font-size: 26px;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 8px;
  line-height: 1.3;
}
.kisan-form-header p {
  font-size: 14px;
  color: #dcfce7;
  margin: 0;
  line-height: 1.6;
}
.kisan-form-badge {
  display: inline-block;
  background: #f59e0b;
  color: #111827;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 50px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 12px;
}
.kisan-form-body {
  padding: 32px 24px;
}
.form-step-guide {
  display: flex;
  justify-content: space-around;
  margin-bottom: 28px;
  background: #f0fdf4;
  border: 1px dashed #86efac;
  border-radius: 12px;
  padding: 14px 10px;
  text-align: center;
}
.form-step-item {
  flex: 1;
}
.form-step-item .num {
  width: 28px;
  height: 28px;
  background: #15803d;
  color: #ffffff;
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
  font-weight: 700;
  margin-bottom: 4px;
}
.form-step-item .lbl {
  font-size: 12px;
  font-weight: 600;
  color: #166534;
  display: block;
}
.form-row {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}
.form-group {
  flex: 1;
  display: flex;
  flex-direction: column;
}
@media (max-width: 640px) {
  .form-row {
    flex-direction: column;
    gap: 16px;
  }
}
.form-label {
  font-size: 14px;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.form-label .req {
  color: #dc2626;
}
.form-control {
  width: 100%;
  padding: 12px 14px;
  font-size: 15px;
  border: 1.5px solid #d1d5db;
  border-radius: 10px;
  outline: none;
  transition: all 0.2s;
  background: #fafafa;
  color: #111827;
  font-family: inherit;
  box-sizing: border-box;
}
.form-control:focus {
  border-color: #15803d;
  background: #ffffff;
  box-shadow: 0 0 0 3px rgba(21, 128, 61, 0.15);
}
select.form-control {
  cursor: pointer;
}
textarea.form-control {
  min-height: 110px;
  resize: vertical;
}
.form-hint {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
}
.consent-box {
  background: #f0fdf4;
  border: 2px solid #86efac;
  border-radius: 12px;
  padding: 16px 18px;
  margin: 24px 0;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  cursor: pointer;
  transition: background 0.2s;
}
.consent-box:hover {
  background: #dcfce7;
}
.consent-box input[type="checkbox"] {
  width: 20px;
  height: 20px;
  accent-color: #15803d;
  cursor: pointer;
  margin-top: 2px;
  flex-shrink: 0;
}
.consent-text {
  font-size: 14px;
  line-height: 1.5;
  color: #14532d;
  font-weight: 600;
  user-select: none;
}
.btn-submit-kisan {
  width: 100%;
  padding: 16px 20px;
  background: linear-gradient(135deg, #15803d 0%, #166534 100%);
  color: #ffffff;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(21, 128, 61, 0.3);
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}
.btn-submit-kisan:hover {
  background: linear-gradient(135deg, #166534 0%, #14532d 100%);
  box-shadow: 0 6px 20px rgba(21, 128, 61, 0.4);
  transform: translateY(-1px);
}
.btn-submit-kisan:active {
  transform: translateY(1px);
}
.privacy-assurance {
  text-align: center;
  font-size: 12px;
  color: #6b7280;
  margin-top: 14px;
}
.success-card {
  display: none;
  background: #f0fdf4;
  border: 2px solid #22c55e;
  border-radius: 14px;
  padding: 24px;
  text-align: center;
  margin-top: 20px;
}
.success-card.active {
  display: block;
}
.success-card h3 {
  font-size: 22px;
  color: #15803d;
  margin: 0 0 10px;
}
.success-card p {
  font-size: 14px;
  color: #1f2937;
  margin-bottom: 16px;
  line-height: 1.6;
}
.btn-wa-direct {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #25d366;
  color: #ffffff;
  font-weight: 700;
  padding: 12px 24px;
  border-radius: 50px;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);
  transition: transform 0.2s;
}
.btn-wa-direct:hover {
  transform: scale(1.03);
  color: #ffffff;
}
</style>

<div class="kisan-form-container">
  <div class="kisan-form-header">
    <span class="kisan-form-badge">🌾 CaneUp किसान सहायता पोर्टल</span>
    <h2>अपनी समस्या या सवाल दर्ज करें</h2>
    <p>गन्ना पर्ची, सट्टा संशोधन, सर्वे, ई-गन्ना ऐप या भुगतान में कोई भी दिक्कत हो, नीचे अपनी जानकारी भरें। हमारी टीम समाधान में आपकी पूरी मदद करेगी।</p>
  </div>

  <div class="kisan-form-body">
    <div class="form-step-guide">
      <div class="form-step-item">
        <span class="num">1</span>
        <span class="lbl">जिला व मिल चुनें</span>
      </div>
      <div class="form-step-item">
        <span class="num">2</span>
        <span class="lbl">गांव व नाम डालें</span>
      </div>
      <div class="form-step-item">
        <span class="num">3</span>
        <span class="lbl">समस्या लिखकर भेजें</span>
      </div>
    </div>

    <form id="kisanGrievanceForm" onsubmit="handleKisanSubmit(event)">
      
      <!-- 1. District & Sugar Mill -->
      <div class="form-row">
        <div class="form-group">
          <label class="form-label" for="farmerDistrict">
            📍 1. अपना जिला चुनें <span class="req">*</span>
          </label>
          <select id="farmerDistrict" class="form-control" required onchange="onDistrictChange()">
            <option value="">-- कृपया जिला चुनें --</option>
          </select>
          <span class="form-hint">उत्तर प्रदेश का अपना जनपद चुनें</span>
        </div>

        <div class="form-group">
          <label class="form-label" for="farmerMill">
            🏭 2. अपनी चीनी मिल / फैक्ट्री चुनें <span class="req">*</span>
          </label>
          <select id="farmerMill" class="form-control" required>
            <option value="">-- पहले जिला चुनें --</option>
          </select>
          <span class="form-hint">आपके जिले से संबंधित चीनी मिलें</span>
        </div>
      </div>

      <!-- Custom Mill Name if 'Other' selected -->
      <div class="form-row" id="otherMillRow" style="display:none;">
        <div class="form-group">
          <label class="form-label" for="otherMillName">
            🏭 अपनी चीनी मिल का नाम लिखें <span class="req">*</span>
          </label>
          <input type="text" id="otherMillName" class="form-control" placeholder="उदा० चीनी मिल का नाम या क्रय केंद्र">
        </div>
      </div>

      <!-- 2. Village & Farmer Name -->
      <div class="form-row">
        <div class="form-group">
          <label class="form-label" for="farmerVillage">
            🏡 3. अपने गांव का नाम डालें <span class="req">*</span>
          </label>
          <input type="text" id="farmerVillage" class="form-control" placeholder="उदा० गांव का नाम (ग्राम पंचायत)" required>
        </div>

        <div class="form-group">
          <label class="form-label" for="farmerName">
            👤 4. किसान का नाम <span class="req">*</span>
          </label>
          <input type="text" id="farmerName" class="form-control" placeholder="उदा० रमेश कुमार / राकेश वर्मा" required>
        </div>
      </div>

      <!-- 3. Phone Number -->
      <div class="form-row">
        <div class="form-group">
          <label class="form-label" for="farmerPhone">
            📱 5. मोबाइल नंबर (व्हाट्सएप नंबर) <span class="req">*</span>
          </label>
          <input type="tel" id="farmerPhone" class="form-control" placeholder="10-अंकीय मोबाइल नंबर (उदा० 9876543210)" pattern="[6-9][0-9]{9}" maxlength="10" required>
          <span class="form-hint">इस नंबर पर आपको पर्ची और भुगतान के व्हाट्सएप अपडेट्स मिलेंगे</span>
        </div>
      </div>

      <!-- 4. Message / Problem Description -->
      <div class="form-row">
        <div class="form-group">
          <label class="form-label" for="farmerMessage">
            📝 6. अपनी समस्या या सवाल विस्तार से लिखें <span class="req">*</span>
          </label>
          <textarea id="farmerMessage" class="form-control" placeholder="अपनी समस्या लिखें — जैसे: पर्ची कब आएगी? सर्वे में रकबा कम चढ़ा है, ई-गन्ना ऐप में पासवर्ड नहीं बन रहा, या भुगतान कितने दिन में मिलेगा..." required></textarea>
          <span class="form-hint">जितना स्पष्ट लिखेंगे, उतनी जल्दी सटीक समाधान मिलेगा</span>
        </div>
      </div>

      <!-- 5. Consent Checkbox (Strictly Requested by User) -->
      <label class="consent-box" for="farmerConsent">
        <input type="checkbox" id="farmerConsent" required>
        <span class="consent-text">
          मैं अपनी चीनी मिल से जुड़े गन्ना पर्ची, सर्वे और भुगतान के दैनिक अपडेट्स व्हाट्सएप पर पाने के लिए caneup.xyz को अपनी सहमति देता हूँ। <span class="req">*</span>
        </span>
      </label>

      <!-- Submit Button -->
      <button type="submit" class="btn-submit-kisan" id="submitBtn">
        <span>📩 समस्या दर्ज करें एवं सहायता पाएं</span>
      </button>

      <p class="privacy-assurance">
        🔒 आपकी निजी जानकारी 100% सुरक्षित है। हम कोई स्पैम नहीं भेजते। केवल आपकी मिल से जुड़े आधिकारिक अपडेट्स शेयर किए जाते हैं।
      </p>
    </form>

    <!-- Success Receipt Box -->
    <div class="success-card" id="successBox">
      <h3>🎉 आपकी समस्या दर्ज हो गई है!</h3>
      <p id="successSummary"></p>
      <a href="#" id="waDirectBtn" target="_blank" class="btn-wa-direct">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.632.063-.996-.063-.591-.205-1.393-.574-2.434-1.503-1.309-1.168-2.031-2.493-2.18-2.738-.149-.245-.015-.378.107-.5.11-.11.244-.286.366-.429.123-.143.163-.245.244-.408.082-.163.041-.306-.02-.429-.061-.122-.55-1.327-.755-1.817-.199-.479-.403-.414-.55-.422h-.47c-.163 0-.428.061-.652.306s-.857.837-.857 2.041c0 1.204.877 2.367 1 2.53.122.163 1.724 2.632 4.177 3.689.583.251 1.038.401 1.393.514.586.186 1.12.16 1.543.097.472-.071 1.448-.592 1.653-1.163.204-.571.204-1.061.143-1.163-.061-.102-.224-.163-.469-.286zM12 2C6.477 2 2 6.477 2 12c0 1.891.524 3.662 1.436 5.179L2 22l4.981-1.308A9.957 9.957 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2zm0 18.2a8.163 8.163 0 01-4.218-1.174l-.302-.18-2.97.779.792-2.894-.197-.314A8.164 8.164 0 1112 20.2z"/></svg>
        <span>व्हाट्सएप पर सहायता मैसेज भेजें</span>
      </a>
    </div>

  </div>
</div>

<script>
// Comprehensive UP District to Sugar Mill Mapping
var districtMills = {
  "मुजफ्फरनगर": ["खतौली (त्रिवेणी)", "तितावी (उत्तम)", "मंसूरपुर (सर शादीलाल)", "मोरना (सहकारी)", "रोहाना कलां", "टिकौला शुगर मिल", "खाईखेड़ी शुगर मिल", "अन्य / लिस्ट में नहीं"],
  "शामली": ["अपर दोआब शामली", "थानाभवन (बजाज)", "ऊन (सुपीरियर)", "अन्य / लिस्ट में नहीं"],
  "मेरठ": ["मवाना (उषा)", "दौराला (डीसीएम श्रीराम)", "किनौनी (बजाज)", "मोहिउद्दीनपुर (निगम)", "सकौती टांडा", "अन्य / लिस्ट में नहीं"],
  "सहारनपुर": ["देवबंद (त्रिवेणी)", "सरसावा (सहकारी)", "गांगनौली (बजाज)", "नानौता (सहकारी)", "शेरमऊ (राणा)", "अन्य / लिस्ट में नहीं"],
  "बिजनौर": ["धामपुर शुगर मिल", "बरकातपुर (उत्तम)", "चांदपुर शुगर मिल", "स्योहारा (अवध)", "बिलाई (बजाज)", "बुंदकी शुगर मिल", "नजीबाबाद (सहकारी)", "बहादुरपुर", "अन्य / लिस्ट में नहीं"],
  "बागपत": ["बागपत (सहकारी)", "मलकपुर (राणा)", "रमाला (सहकारी)", "अन्य / लिस्ट में नहीं"],
  "बुलंदशहर": ["अनूपशहर (सहकारी)", "साबितगढ़ (वेव)", "जहांगीराबाद", "बुलंदशहर", "अन्य / लिस्ट में नहीं"],
  "हापुड़": ["सिंभावली शुगर मिल", "बृजनाथपुर शुगर मिल", "अन्य / लिस्ट में नहीं"],
  "अमरोहा": ["धनौरा (वेव)", "चंदनपुर (त्रिवेणी)", "हसनपुर (सहकारी)", "गजरौला शुगर मिल", "अन्य / लिस्ट में नहीं"],
  "संभल": ["असमौली (डीएसएम)", "राजा का सहसपुर (राणा)", "संभल", "अन्य / लिस्ट में नहीं"],
  "मुरादाबाद": ["बिलारी (गोविंद)", "रानी नांगल (त्रिवेणी)", "अगवानपुर (दीवान)", "अन्य / लिस्ट में नहीं"],
  "रामपुर": ["रुद्र-बिलास (सहकारी)", "मिलक नारायणपुर (त्रिवेणी)", "बिलासपुर शुगर मिल", "अन्य / लिस्ट में नहीं"],
  "बरेली": ["बहेड़ी (केसर)", "नवाबगंज (ओसवाल)", "फरीदपुर (द्वारिकेश)", "मीरगंज (द्वारिकेश)", "सेमीखेड़ा (सहकारी)", "अन्य / लिस्ट में नहीं"],
  "पीलीभीत": ["पीलीभीत (एलएच शुगर्स)", "बीसलपुर (सहकारी)", "पूरनपुर (सहकारी)", "बरखेड़ा (बजाज)", "अन्य / लिस्ट में नहीं"],
  "शाहजहांपुर": ["रोजा शुगर मिल", "पुवायां (सहकारी)", "तिलहर (सहकारी)", "मकसूदापुर (बजाज)", "निगोही (डालमिया)", "अन्य / लिस्ट में नहीं"],
  "बदायूं": ["बिल्सी (सहकारी)", "शेखूपुर (सहकारी)", "दातागंज", "अन्य / लिस्ट में नहीं"],
  "लखीमपुर खीरी": ["गोला गोकर्णनाथ (बजाज)", "पलिया कलां (बजाज)", "खंभारखेड़ा (बजाज)", "ऐरा (गोविंद)", "कुंभी (बलरामपुर)", "गुलरिया (बलरामपुर)", "बेलरायां (सहकारी)", "अन्य / लिस्ट में नहीं"],
  "सीतापुर": ["हरगांव (अवध)", "बिसवां (डालमिया)", "महोली (निगम)", "रामगढ़ (डालमिया)", "जवाहरपुर (डालमिया)", "अन्य / लिस्ट में नहीं"],
  "हरदोई": ["रूपापुर (डीएसएम)", "लोनी (डीएसएम)", "हरियावां (डीएसएम)", "अन्य / लिस्ट में नहीं"],
  "बहराइच": ["नानपारा (सहकारी)", "जरवल रोड (निगम)", "चिलवरिया (सिंभावली)", "अन्य / लिस्ट में नहीं"],
  "बलरामपुर": ["बलरामपुर चीनी मिल", "तुलसीपुर चीनी मिल", "इटई मैदा", "अन्य / लिस्ट में नहीं"],
  "गोंडा": ["मनकापुर (बलरामपुर)", "कुंदनपुर / बभनान", "मैजापुर (बजाज)", "अन्य / लिस्ट में नहीं"],
  "बस्ती": ["बभनान चीनी मिल", "रुधौली (बजाज)", "मुंडेरवा (निगम)", "अन्य / लिस्ट में नहीं"],
  "गोरखपुर": ["पिपराइच (निगम)", "धुरियापार", "अन्य / लिस्ट में नहीं"],
  "देवरिया": ["प्रतापपुर (बजाज)", "बैतालपुर", "भाटपार रानी", "अन्य / लिस्ट में नहीं"],
  "कुशीनगर": ["कप्तानगंज शुगर मिल", "रामकोला (त्रिवेणी)", "सेवरही शुगर मिल", "ढाढा (हटा)", "खड्डा (सहकारी)", "अन्य / लिस्ट में नहीं"],
  "अयोध्या": ["रौजागांव (डीएसएम)", "मसौधा (केएम शुगर्स)", "अन्य / लिस्ट में नहीं"],
  "बाराबंकी": ["हैदरगढ़ (बलरामपुर)", "रामनगर शुगर मिल", "अन्य / लिस्ट में नहीं"],
  "अन्य जिला / यूपी के बाहर": ["अन्य चीनी मिल / लिस्ट में नहीं"]
};

// Populate Districts on page load
document.addEventListener('DOMContentLoaded', function() {
  var distSelect = document.getElementById('farmerDistrict');
  for (var dist in districtMills) {
    var opt = document.createElement('option');
    opt.value = dist;
    opt.textContent = dist;
    distSelect.appendChild(opt);
  }
});

// Update Mills when District changes
function onDistrictChange() {
  var dist = document.getElementById('farmerDistrict').value;
  var millSelect = document.getElementById('farmerMill');
  var otherRow = document.getElementById('otherMillRow');
  
  millSelect.innerHTML = '<option value="">-- चीनी मिल चुनें --</option>';
  otherRow.style.display = 'none';

  if (dist && districtMills[dist]) {
    districtMills[dist].forEach(function(mill) {
      var opt = document.createElement('option');
      opt.value = mill;
      opt.textContent = mill;
      millSelect.appendChild(opt);
    });
  }
}

// Show manual text if 'Other' mill selected
document.getElementById('farmerMill').addEventListener('change', function() {
  var otherRow = document.getElementById('otherMillRow');
  if (this.value.indexOf('अन्य') !== -1) {
    otherRow.style.display = 'flex';
    document.getElementById('otherMillName').required = true;
  } else {
    otherRow.style.display = 'none';
    document.getElementById('otherMillName').required = false;
  }
});

// Form Submit Handler
function handleKisanSubmit(e) {
  e.preventDefault();

  var dist = document.getElementById('farmerDistrict').value;
  var mill = document.getElementById('farmerMill').value;
  if (mill.indexOf('अन्य') !== -1) {
    mill = document.getElementById('otherMillName').value.trim() || 'अन्य मिल';
  }
  var village = document.getElementById('farmerVillage').value.trim();
  var name = document.getElementById('farmerName').value.trim();
  var phone = document.getElementById('farmerPhone').value.trim();
  var message = document.getElementById('farmerMessage').value.trim();
  var consent = document.getElementById('farmerConsent').checked;

  if (!consent) {
    alert('कृपया व्हाट्सएप दैनिक अपडेट्स के लिए सहमति चेकबॉक्स पर टिक करें।');
    return;
  }

  // Format WhatsApp message
  var waText = "🌾 *गन्ना किसान समस्या / सहायता फॉर्म - CaneUp*\n" +
               "----------------------------------\n" +
               "👤 *किसान का नाम:* " + name + "\n" +
               "📱 *मोबाइल नंबर:* " + phone + "\n" +
               "📍 *जिला:* " + dist + "\n" +
               "🏭 *चीनी मिल:* " + mill + "\n" +
               "🏡 *गांव का नाम:* " + village + "\n" +
               "----------------------------------\n" +
               "📝 *समस्या / सवाल:*\n" + message + "\n" +
               "----------------------------------\n" +
               "✅ *सहमति:* मैं अपनी चीनी मिल से जुड़े दैनिक अपडेट्स व्हाट्सएप पर पाने के लिए सहमत हूँ।";

  var waUrl = "https://api.whatsapp.com/send?phone=917017208945&text=" + encodeURIComponent(waText);

  // Show Success Receipt Box
  var summaryText = "प्रिय <strong>" + name + "</strong> जी, आपकी समस्या (जिला: " + dist + ", मिल: " + mill + ") सफलतापूर्वक दर्ज कर ली गई है। <strong>" + phone + "</strong> पर हमारी टीम आपसे जल्द संपर्क करेगी। तुरंत सहायता के लिए नीचे दिए गए बटन पर टैप करें:";
  document.getElementById('successSummary').innerHTML = summaryText;
  document.getElementById('waDirectBtn').href = waUrl;
  document.getElementById('successBox').classList.add('active');

  // Smooth scroll to success card
  document.getElementById('successBox').scrollIntoView({ behavior: 'smooth' });

  // Automatically open WhatsApp in new tab after 1 second
  setTimeout(function() {
    window.open(waUrl, '_blank');
  }, 1000);
}
</script>
