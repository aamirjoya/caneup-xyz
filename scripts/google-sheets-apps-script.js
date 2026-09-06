/**
 * CaneUp — Bulletproof Google Sheets Apps Script for Kisan Samasya Form
 * ----------------------------------------------------------------------
 * यह स्क्रिप्ट POST और GET दोनों तरह के अनुरोधों से डेटा को सीधे Google Sheet में जोड़ती है।
 */

function doPost(e) {
  return handleData(e);
}

function doGet(e) {
  // अगर GET रिक्वेस्ट में डेटा आया है, तो भी Sheet में जोड़ें
  if (e && e.parameter && (e.parameter.name || e.parameter.phone)) {
    return handleData(e);
  }
  return ContentService
    .createTextOutput("CaneUp Google Sheets Webhook is active and running!")
    .setMimeType(ContentService.MimeType.TEXT);
}

function handleData(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var data = {};

    // 1. JSON बॉडी से डेटा निकालें
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    // 2. भारत का स्थानीय समय (IST)
    var timestamp = Utilities.formatDate(new Date(), "Asia/Kolkata", "dd/MM/yyyy HH:mm:ss");

    // 3. Google Sheet में नई पंक्ति (Row) जोड़ें
    sheet.appendRow([
      timestamp,
      data.name || "",
      data.phone || "",
      data.district || "",
      data.mill || "",
      data.village || "",
      data.message || "",
      data.consent || "हाँ (सहमति प्राप्त)"
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ "status": "success", "message": "डेटा सफलतापूर्वक सेव हुआ" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ "status": "error", "error": err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}
