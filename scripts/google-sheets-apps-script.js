/**
 * CaneUp — Google Sheets Apps Script for Kisan Samasya Form
 * -----------------------------------------------------------
 * यह कोड आपके Google Sheet में सभी किसानों का डेटा (नाम, फोन, जिला, मिल, गांव, समस्या)
 * रियल-टाइम में ऑटोमैटिकली सेव करने के लिए है।
 * 
 * 📌 सेटअप कैसे करें (सिर्फ 2 मिनट):
 * 1. https://sheets.google.com पर जाएं और एक नई Google Sheet बनाएं।
 * 2. Sheet का नाम रखें: "CaneUp Kisan Samasya Leads"
 * 3. पहली Row (Header) में ये कॉलम लिखें:
 *    A1: तारीख (Timestamp)
 *    B1: किसान का नाम
 *    C1: मोबाइल नंबर
 *    D1: जिला
 *    E1: चीनी मिल
 *    F1: गांव का नाम
 *    G1: समस्या / सवाल
 *    H1: व्हाट्सएप सहमति
 * 4. ऊपर मेनू में जाएं: Extensions > Apps Script
 * 5. वहां पुराना कोड हटाकर नीचे दिया गया पूरा कोड पेस्ट करें।
 * 6. ऊपर Deploy > New deployment पर क्लिक करें।
 * 7. Select type में 'Web app' चुनें।
 *    - Description: "CaneUp Form Webhook"
 *    - Execute as: "Me"
 *    - Who has access: "Anyone" (ताकि वेबसाइट से डेटा बिना लॉगिन सेव हो सके)
 * 8. 'Deploy' दबाएं और 'Authorize access' पर क्लिक करके अपना गूगल अकाउंट सिलेक्ट करें।
 * 9. आपको एक "Web app URL" मिलेगा (जैसे: https://script.google.com/macros/s/.../exec)
 * 10. उस URL को hugo.toml में params.kisan_sheet_url में पेस्ट कर दें।
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    var rawData = e.postData.contents;
    var data = JSON.parse(rawData);

    // भारत का स्थानीय समय (IST)
    var timestamp = Utilities.formatDate(new Date(), "Asia/Kolkata", "dd/MM/yyyy HH:mm:ss");

    sheet.appendRow([
      timestamp,
      data.name || "",
      data.phone || "",
      data.district || "",
      data.mill || "",
      data.village || "",
      data.message || "",
      data.consent ? "हाँ (सहमति प्राप्त)" : "नहीं"
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

function doGet(e) {
  return ContentService
    .createTextOutput("CaneUp Google Sheets Webhook is active and running!")
    .setMimeType(ContentService.MimeType.TEXT);
}
