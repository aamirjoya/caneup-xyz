import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_dir = os.path.join(base_dir, 'content', 'news')
posts_dir = os.path.join(base_dir, 'content', 'posts')
os.makedirs(news_dir, exist_ok=True)
os.makedirs(posts_dir, exist_ok=True)

articles_data = [
    # 1 - 06:00 AM
    {
        "type": "news",
        "file": "digital-agri-review-25-august-2026.md",
        "title": "🚨 25 अगस्त को केंद्र सरकार की बड़ी समीक्षा बैठक — Digital Agriculture Mission पर सख्त निर्देश!",
        "date": "2026-08-25T06:00:00+05:30",
        "category": "Breaking News",
        "tags": ["Digital Agriculture Mission", "AgriStack", "Farmer ID", "केंद्र सरकार", "25 अगस्त"],
        "slug": "digital-agri-review-25-august-2026",
        "img": "/images/news/digital-agri-farmer-id-2026.webp",
        "desc": "25 अगस्त 2026 को केंद्र सरकार की हाई-लेवल समीक्षा बैठक। राज्यों में Farmer ID और AgriStack डिजिटल मैपिंग की धीमी गति पर सख्ती।"
    },
    # 2 - 06:20 AM
    {
        "type": "news",
        "file": "chini-stock-checking-up-districts-2026.md",
        "title": "⚠️ UP के सभी 75 जिलों में चीनी गोदामों की चेकिंग — जमाखोरों पर ESMA का खौफ!",
        "date": "2026-08-25T06:20:00+05:30",
        "category": "Breaking News",
        "tags": ["चीनी स्टॉक", "ESMA", "जमाखोरी", "CM योगी", "UP News"],
        "slug": "chini-stock-checking-up-districts-2026",
        "img": "/images/news/yogi-chini-stock-esma-2026.webp",
        "desc": "CM योगी के सख्त आदेश के बाद UP के सभी जिलों में DCO और DM की टीमों द्वारा चीनी मिलों व थोक व्यापारियों के गोदामों पर छापेमारी।"
    },
    # 3 - 06:40 AM
    {
        "type": "posts",
        "file": "caneup-survey-data-sudhar-last-date-2026.md",
        "title": "CaneUp सर्वे डेटा सुधार 2026: रकबा व पौधा/पेड़ी प्रविष्टि ठीक कराने का आखिरी मौका",
        "date": "2026-08-25T06:40:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["CaneUp Survey", "सर्वे सुधार", "caneup.in", "गन्ना सट्टा", "eGanna"],
        "slug": "caneup-survey-data-sudhar-last-date-2026",
        "img": "/images/blog/caneup-enquiry-guide-2026.webp",
        "desc": "CaneUp portal पर गन्ना सर्वे डेटा में गलती सुधारने की पूरी प्रक्रिया। 30 अगस्त से पहले ऑनलाइन व ऑफलाइन आपत्ति दर्ज कराएं।"
    },
    # 4 - 07:00 AM
    {
        "type": "news",
        "file": "maharashtra-ganna-andolan-impact-up-2026.md",
        "title": "🔥 पुणे में गन्ने का ₹7000/टन आंदोलन तेज — UP के किसानों ने भी कसी कमर!",
        "date": "2026-08-25T07:00:00+05:30",
        "category": "Breaking News",
        "tags": ["गन्ना आंदोलन", "पुणे", "महाराष्ट्र", "₹7000 भाव", "UP किसान"],
        "slug": "maharashtra-ganna-andolan-impact-up-2026",
        "img": "/images/news/maharashtra-protest-7000-2026.webp",
        "desc": "महाराष्ट्र में किसानों के उग्र आंदोलन का असर उत्तर प्रदेश में। किसान संगठनों ने आगामी SAP में भारी बढ़ोतरी की चेतावनी दी।"
    },
    # 5 - 07:20 AM
    {
        "type": "posts",
        "file": "eganna-app-login-session-expired-solution.md",
        "title": "eGanna App 'Session Expired' और 'Server Error' कैसे ठीक करें? 100% सटीक ट्रिक",
        "date": "2026-08-25T07:20:00+05:30",
        "category": "eGanna App",
        "tags": ["eGanna App", "Login Error", "Session Expired", "गन्ना पर्ची ऐप"],
        "slug": "eganna-app-login-session-expired-solution",
        "img": "/images/blog/eganna-app-v6-update-2026.webp",
        "desc": "e-Ganna App में बार-बार आ रहे Session Expired और Server Error का 1 मिनट में आसान समाधान।"
    },
    # 6 - 07:40 AM
    {
        "type": "news",
        "file": "up-weather-monsoon-rain-sugarcane-relief-2026.md",
        "title": "🌧️ UP में मानसून फिर मेहरबान — सूखती गन्ने की फसल को मिली संजीवनी!",
        "date": "2026-08-25T07:40:00+05:30",
        "category": "Breaking News",
        "tags": ["मौसम अपडेट", "UP Monsoon", "गन्ना सिंचाई", "मौसम अलर्ट"],
        "slug": "up-weather-monsoon-rain-sugarcane-relief-2026",
        "img": "/images/news/monsoon-recovery-ganna-2026.webp",
        "desc": "पश्चिमी और पूर्वी उत्तर प्रदेश के 30 से अधिक जिलों में झमाझम बारिश। गन्ने की बढ़वार में तेजी, किसानों के चेहरे खिले।"
    },
    # 7 - 08:00 AM
    {
        "type": "posts",
        "file": "ganna-basic-quota-calculation-formula-2026.md",
        "title": "गन्ना बेसिक कोटा (Basic Quota) कैसे बनता है? जानिए 3 साल के सप्लाई का गणित",
        "date": "2026-08-25T08:00:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["बेसिक कोटा", "Basic Quota Formula", "गन्ना सट्टा", "caneup.in"],
        "slug": "ganna-basic-quota-calculation-formula-2026",
        "img": "/images/blog/ganna-satta-pre-calendar-2026.webp",
        "desc": "गन्ना बेसिक कोटा की गणना का सरकारी फार्मूला। पिछले 3 साल की औसत आपूर्ति और नए सट्टे की पूरी जानकारी।"
    },
    # 8 - 08:20 AM
    {
        "type": "news",
        "file": "harvester-machine-subsidy-lottery-list-2026.md",
        "title": "🚜 गन्ना कटाई मशीन 80% सब्सिडी लॉटरी लिस्ट जारी — ऐसे चेक करें अपना नाम!",
        "date": "2026-08-25T08:20:00+05:30",
        "category": "Breaking News",
        "tags": ["कृषि यंत्र अनुदान", "Harvester Subsidy", "80% सब्सिडी", "UP Agriculture"],
        "slug": "harvester-machine-subsidy-lottery-list-2026",
        "img": "/images/news/ganna-katai-subsidy-2026.webp",
        "desc": "UP Krishi Yantra Anudan Yojana के तहत गन्ना हार्वेस्टर मशीन सब्सिडी लॉटरी परिणाम घोषित। DBT से सीधे खाते में आएगी सब्सिडी।"
    },
    # 9 - 08:40 AM
    {
        "type": "posts",
        "file": "streptocycline-spray-dosage-red-rot-2026.md",
        "title": "स्ट्रेप्टोसाइक्लिन + कॉपर ऑक्सीक्लोराइड: गन्ने की लाल सड़न का सबसे पक्का स्प्रे",
        "date": "2026-08-25T08:40:00+05:30",
        "category": "Ganna Guide",
        "tags": ["स्ट्रेप्टोसाइक्लिन", "Red Rot Spray", "फफूंदनाशक", "गन्ना रोग"],
        "slug": "streptocycline-spray-dosage-red-rot-2026",
        "img": "/images/blog/red-rot-monsoon-treatment-2026.webp",
        "desc": "गन्ने में लाल सड़न रोकने के लिए ब्लीचिंग पाउडर, स्ट्रेप्टोसाइक्लिन और कॉपर ऑक्सीक्लोराइड का सही डोज और नहलाकर स्प्रे की विधि।"
    },
    # 10 - 09:00 AM
    {
        "type": "news",
        "file": "balrampur-biopolymer-plant-update-2026.md",
        "title": "🏭 बलरामपुर चीनी का ₹3080 करोड़ बायो-प्लास्टिक प्लांट — नवंबर से कमर्शियल प्रोडक्शन!",
        "date": "2026-08-25T09:00:00+05:30",
        "category": "Breaking News",
        "tags": ["बलरामपुर चीनी", "Biopolymer", "PLA Plant", "लखीमपुर खीरी"],
        "slug": "balrampur-biopolymer-plant-update-2026",
        "img": "/images/news/balrampur-biopolymer-2026.webp",
        "desc": "लखीमपुर खीरी के कुंभी में देश के पहले गन्ने से प्लासिटक बनाने वाले प्लांट की तैयारियां अंतिम चरण में।"
    },
    # 11 - 09:20 AM
    {
        "type": "posts",
        "file": "cos-17231-ganna-beej-nursery-booking-2026.md",
        "title": "CoS 17231 प्रमाणित बीज की बुकिंग कैसे करें? शाहजहांपुर शोध संस्थान व मिल नर्सरी गाइड",
        "date": "2026-08-25T09:20:00+05:30",
        "category": "Ganna Guide",
        "tags": ["CoS 17231 Seed", "गन्ना बीज बुकिंग", "शाहजहांपुर शोध", "प्रमाणित बीज"],
        "slug": "cos-17231-ganna-beej-nursery-booking-2026",
        "img": "/images/blog/co-0238-replacement-cos-17231-2026.webp",
        "desc": "लाल सड़न मुक्त CoS 17231 गन्ना बीज की ऑनलाइन व ऑफलाइन बुकिंग। मात्र ₹1.50 में नर्सरी पौध प्राप्त करें।"
    },
    # 12 - 09:40 AM
    {
        "type": "news",
        "file": "pm-kisan-24th-installment-beneficiary-status-2026.md",
        "title": "💰 PM Kisan 24वीं किश्त: अक्टूबर में आएंगे ₹2000! लिस्ट में अपना नाम तुरंत देखें",
        "date": "2026-08-25T09:40:00+05:30",
        "category": "Sarkari Yojana",
        "tags": ["PM Kisan 24th", "पीएम किसान", "eKYC", "पीएम किसान स्टेटस"],
        "slug": "pm-kisan-24th-installment-beneficiary-status-2026",
        "img": "/images/news/pm-kisan-24-oct-2026.webp",
        "desc": "PM-KISAN Samman Nidhi की 24वीं किश्त की संभावी तारीख और pmkisan.gov.in पर बेनेफिशरी स्टेटस चेक करने का तरीका।"
    },
    # 13 - 10:00 AM
    {
        "type": "posts",
        "file": "ganna-parchi-fortnight-calendar-explained-2026.md",
        "title": "गन्ना पर्ची पखवाड़ा (Fortnight) और कॉलम कैलेंडर समझें — कौन सी पर्ची कब आएगी?",
        "date": "2026-08-25T10:00:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["पर्ची कैलेंडर", "Fortnight Calendar", "गन्ना आपूर्ति", "eGanna"],
        "slug": "ganna-parchi-fortnight-calendar-explained-2026",
        "img": "/images/blog/parchi-calendar-guide-2026.webp",
        "desc": "गन्ना पर्ची कैलेंडर के 12 पखवाड़ों और 9 कॉलमों का पूरा हिसाब। जानिए आपकी पर्ची कब जारी होगी और तारे का क्या मतलब है।"
    },
    # 14 - 10:20 AM
    {
        "type": "news",
        "file": "andhra-drought-relief-package-farmer-demand-2026.md",
        "title": "🌾 आंध्र प्रदेश में 52% सूखा — किसानों के लिए राहत पैकेज का ऐलान!",
        "date": "2026-08-25T10:20:00+05:30",
        "category": "Breaking News",
        "tags": ["आंध्र प्रदेश सूखा", "El Nino", "फसल नुकसान", "PMFBY"],
        "slug": "andhra-drought-relief-package-farmer-demand-2026",
        "img": "/images/news/andhra-drought-crisis-2026.webp",
        "desc": "मानसून की कमी से आंध्र में खरीफ फसल तबाह। CM चंद्रबाबू नायडू ने फसल बीमा क्लेम तुरंत निपटाने के आदेश दिए।"
    },
    # 15 - 10:40 AM
    {
        "type": "posts",
        "file": "ganna-ghosna-patra-khasra-khatauni-error-solution.md",
        "title": "घोषणा पत्र में खसरा-खतौनी और खाता संख्या गलत दर्ज हो गई? ऐसे करें ऑनलाइन सुधार",
        "date": "2026-08-25T10:40:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["घोषणा पत्र सुधार", "खतौनी त्रुटि", "enquiry.caneup.in", "सट्टा अनब्लॉक"],
        "slug": "ganna-ghosna-patra-khasra-khatauni-error-solution",
        "img": "/images/blog/ganna-ghosna-patra-guide-2026.webp",
        "desc": "गन्ना घोषणा पत्र में गलत रकबा या गाटा संख्या दर्ज होने पर ऑनलाइन एडिट और करेक्शन की स्टेप-बाय-स्टेप प्रक्रिया।"
    },
    # 16 - 11:00 AM
    {
        "type": "news",
        "file": "early-crushing-october-15-mills-preparation-2026.md",
        "title": "⚙️ 15 अक्टूबर अर्ली क्रशिंग: पश्चिमी UP की 40 मिलों में ट्रायल रन का शेड्यूल तय!",
        "date": "2026-08-25T11:00:00+05:30",
        "category": "Breaking News",
        "tags": ["Early Crushing", "15 अक्टूबर", "चीनी मिल ट्रायल", "गन्ना पेराई"],
        "slug": "early-crushing-october-15-mills-preparation-2026",
        "img": "/images/news/perai-15-oct-early-2026.webp",
        "desc": "मेरठ, मुजफ्फरनगर, शामली और बिजनौर की मिलों में बॉयलर टेस्टिंग 01 अक्टूबर तक पूरी करने के निर्देश।"
    },
    # 17 - 11:20 AM
    {
        "type": "posts",
        "file": "ganna-trench-method-4-feet-spacing-secrets.md",
        "title": "ट्रेंच विधि में 4 फीट की दूरी का रहस्य — 500 क्विंटल/एकड़ पैदावार का सीक्रेट",
        "date": "2026-08-25T11:20:00+05:30",
        "category": "Ganna Guide",
        "tags": ["ट्रेंच विधि", "गन्ना बढ़वार", "500 क्विंटल पैदावार", "आधुनिक खेती"],
        "slug": "ganna-trench-method-4-feet-spacing-secrets",
        "img": "/images/blog/sharad-kalin-ganna-buwai-trench-2026.webp",
        "desc": "ट्रेंच विधि से 4 से 5 फीट की दूरी पर गन्ने की बुवाई क्यों करें? धूप, हवा और पानी के सही उपयोग से पैदावार दोगुनी करने का सीक्रेट।"
    },
    # 18 - 11:40 AM
    {
        "type": "news",
        "file": "10000-fpo-scheme-ganna-kisan-benefits-2026.md",
        "title": "🤝 10,000 FPO लक्ष्य पूरा! गन्ना किसान समूह बनाकर सीधे मिलों से तय करें भाव",
        "date": "2026-08-25T11:40:00+05:30",
        "category": "Sarkari Yojana",
        "tags": ["10000 FPO", "किसान संगठन", "NABARD", "FPO Subsidy"],
        "slug": "10000-fpo-scheme-ganna-kisan-benefits-2026",
        "img": "/images/news/fpo-10000-kisan-2026.webp",
        "desc": "किसान उत्पादक संगठनों (FPO) को सरकार दे रही ₹18 लाख की मदद। गन्ना किसान मिलकर खाद-बीज पर बचा सकते हैं 20% खर्चा।"
    },
    # 19 - 12:00 PM
    {
        "type": "posts",
        "file": "ganna-bakaya-15-percent-byaj-claim-process.md",
        "title": "गन्ना भुगतान में विलंब का 15% ब्याज कैसे क्लेम करें? जानिए कानूनी प्रक्रिया",
        "date": "2026-08-25T12:00:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["15% ब्याज नियम", "गन्ना कानून", "DCO ऑफिस", "उच्च न्यायालय"],
        "slug": "ganna-bakaya-15-percent-byaj-claim-process",
        "img": "/images/blog/ganna-bakaya-bhugtan-byaj-2026.webp",
        "desc": "14 दिन के बाद बकाया गन्ना मूल्य पर 15% प्रतिवर्ष की दर से ब्याज का दावा करने का प्रार्थना पत्र प्रारूप और कानूनी तरीका।"
    },
    # 20 - 12:20 PM
    {
        "type": "news",
        "file": "nhb-subsidy-politicians-banned-farmers-benefit-2026.md",
        "title": "🚫 नेताओं पर बैन के बाद बागवानी व कोल्ड स्टोरेज सब्सिडी का 100% बजट किसानों को!",
        "date": "2026-08-25T12:20:00+05:30",
        "category": "Breaking News",
        "tags": ["NHB Subsidy", "कोल्ड स्टोरेज", "बागवानी योजना", "नेताओं पर बैन"],
        "slug": "nhb-subsidy-politicians-banned-farmers-benefit-2026",
        "img": "/images/news/nhb-subsidy-ban-neta-2026.webp",
        "desc": "राष्ट्रीय बागवानी बोर्ड (NHB) के नए कड़े नियमों के बाद वास्तविक किसानों के आवेदन स्वीकार। ऑनलाइन पोर्टल खुला।"
    },
    # 21 - 12:40 PM
    {
        "type": "posts",
        "file": "ganna-sarson-intercropping-step-by-step-guide.md",
        "title": "गन्ने के साथ सरसों की सह-फसली खेती: ₹50,000 प्रति एकड़ अतिरिक्त कमाई की पूरी गाइड",
        "date": "2026-08-25T12:40:00+05:30",
        "category": "Ganna Guide",
        "tags": ["गन्ना सरसों", "सह-फसली खेती", "Intercropping", "मुनाफा खेती"],
        "slug": "ganna-sarson-intercropping-step-by-step-guide",
        "img": "/images/blog/sharad-kalin-ganna-buwai-trench-2026.webp",
        "desc": "अक्टूबर में गन्ने की नालियों के बीच पीली सरसों की बुवाई की विधि। खाद, सिंचाई और खरपतवार नियंत्रण का टाइमटेबल।"
    },
    # 22 - 01:00 PM
    {
        "type": "news",
        "file": "e20-ethanol-target-ahead-of-time-2026.md",
        "title": "⛽ E20 एथेनॉल लक्ष्य समय से 5 साल पहले पूरा — गन्ने के साथ मक्का किसानों की बल्ले-बल्ले!",
        "date": "2026-08-25T13:00:00+05:30",
        "category": "Breaking News",
        "tags": ["E20 Ethanol", "एथेनॉल ब्लेंडिंग", "मक्का खेती", "पेट्रोलियम मस्क"],
        "slug": "e20-ethanol-target-ahead-of-time-2026",
        "img": "/images/news/e20-ethanol-achieved-2026.webp",
        "desc": "भारत में 20% एथेनॉल संमिश्रण का लक्ष्य पूरा। सरकार ने कहा- चीनी कीमतों से एथेनॉल का कोई सीधा संबंध नहीं।"
    },
    # 23 - 01:20 PM
    {
        "type": "posts",
        "file": "eganna-app-se-grower-code-search-kaise-kare.md",
        "title": "बिना किसान कोड के eGanna App और CaneUp पर सट्टा कैसे खोजें? नाम व गांव से सर्च करें",
        "date": "2026-08-25T13:20:00+05:30",
        "category": "eGanna App",
        "tags": ["Grower Code Search", "किसान कोड खोजें", "eGanna App", "caneup.in"],
        "slug": "eganna-app-se-grower-code-search-kaise-kare",
        "img": "/images/blog/eganna-app-v6-update-2026.webp",
        "desc": "यदि आपका किसान कोड या सट्टा नंबर खो गया है, तो नाम और गांव के नाम से 1 मिनट में कोड ढूंढने की आसान ट्रिक।"
    },
    # 24 - 01:40 PM
    {
        "type": "news",
        "file": "red-rot-september-high-alert-up-cane-dept-2026.md",
        "title": "⚠️ सितंबर हाई अलर्ट: गन्ने में लाल सड़न व टॉप बोरर का हमला — कृषि विभाग की विशेष एडवाइजरी!",
        "date": "2026-08-25T13:40:00+05:30",
        "category": "Breaking News",
        "tags": ["Red Rot Alert", "विशेष एडवाइजरी", "गन्ना रक्षा", "कीट नियंत्रण"],
        "slug": "red-rot-september-high-alert-up-cane-dept-2026",
        "img": "/images/news/red-rot-alert-sept-2026.webp",
        "desc": "भारी बारिश के बाद खेतों में जलभराव से फंगस फैलने का डर। गन्ना आयुक्त ने सभी DCO को दवा छिड़काव कराने के निर्देश दिए।"
    },
    # 25 - 02:00 PM
    {
        "type": "posts",
        "file": "ganna-kisan-kcc-loan-3-lakh-apply-online.md",
        "title": "गन्ना किसान क्रेडिट कार्ड (KCC Loan): 3 लाख का लोन मात्र 4% ब्याज पर कैसे लें?",
        "date": "2026-08-25T14:00:00+05:30",
        "category": "Sarkari Yojana",
        "tags": ["KCC Loan", "किसान क्रेडिट कार्ड", "SBI KCC", "सस्ता लोन"],
        "slug": "ganna-kisan-kcc-loan-3-lakh-apply-online",
        "img": "/images/blog/ganna-sarkari-yojana-2026.webp",
        "desc": "गन्ना सट्टे के आधार पर KCC लोन की सीमा तय कराने, ब्याज छूट (Interest Subvention) पाने और ऑनलाइन अप्लाई करने की गाइड।"
    },
    # 26 - 02:20 PM
    {
        "type": "news",
        "file": "ganna-kisan-kalyan-dbt-scheme-update-2026.md",
        "title": "💳 गन्ना किसान कल्याण योजना: ₹5,000 से ₹10,000 प्रति हेक्टेयर सीधे बैंक में!",
        "date": "2026-08-25T14:20:00+05:30",
        "category": "Breaking News",
        "tags": ["गन्ना कल्याण योजना", "DBT Subsidy", "किसान खाता", "UP Sarkari Yojana"],
        "slug": "ganna-kisan-kalyan-dbt-scheme-update-2026",
        "img": "/images/news/ganna-kalyan-yojana-2026.webp",
        "desc": "गन्ना किसानों को इनपुट सपोर्ट देने के लिए नई योजना पर विचार। जानिए पात्रता और जरूरी कागजात।"
    },
    # 27 - 02:40 PM
    {
        "type": "posts",
        "file": "caneup-grievance-token-track-status-mobile.md",
        "title": "CaneUp ऑनलाइन शिकायत का स्टेटस मोबाइल से कैसे ट्रैक करें? Token Number गाइड",
        "date": "2026-08-25T14:40:00+05:30",
        "category": "CaneUp Guide",
        "tags": ["Grievance Status", "शिकायत ट्रैकिंग", "enquiry.caneup.in", "Token Number"],
        "slug": "caneup-grievance-token-track-status-mobile",
        "img": "/images/blog/caneup-online-grievance-complaint-2026.webp",
        "desc": "दर्ज की गई शिकायत पर अधिकारी द्वारा क्या कार्रवाई की गई, यह ऑनलाइन मोबाइल से ट्रैक करने की आसान विधि।"
    },
    # 28 - 03:00 PM
    {
        "type": "news",
        "file": "ganna-rakba-decline-maize-paddy-shift-2026.md",
        "title": "📉 गन्ने का रकबा 4% गिरा — किसान मक्का और धान की ओर क्यों रुख कर रहे हैं?",
        "date": "2026-08-25T15:00:00+05:30",
        "category": "Breaking News",
        "tags": ["गन्ना रकबा", "धान मक्का", "चीनी उत्पादन", "कृषि रिपोर्ट"],
        "slug": "ganna-rakba-decline-maize-paddy-shift-2026",
        "img": "/images/news/ganna-rakba-gira-2026.webp",
        "desc": "लागत में बढ़ोतरी और रेड रॉट बीमारी के डर से किसानों का फसल विविधीकरण। सरकार को गन्ने का SAP बढ़ाने का दबाव।"
    },
    # 29 - 03:20 PM
    {
        "type": "posts",
        "file": "drip-irrigation-ganna-90-percent-subsidy-guide.md",
        "title": "गन्ने में ड्रिप सिंचाई (Drip Irrigation) पर 90% सब्सिडी: 40% कम पानी में दोगुनी पैदावार",
        "date": "2026-08-25T15:20:00+05:30",
        "category": "Sarkari Yojana",
        "tags": ["ड्रिप सिंचाई", "90% सब्सिडी", "PMKSY", "गन्ना सिंचाई"],
        "slug": "drip-irrigation-ganna-90-percent-subsidy-guide",
        "img": "/images/blog/ganne-sept-oct-tips-2026.webp",
        "desc": "उत्तर प्रदेश कृषि विभाग की टपक सिंचाई योजना (Drip Subsidy) में आवेदन की पूरी ऑनलाइन प्रक्रिया व लागत विवरण।"
    },
    # 30 - 03:40 PM
    {
        "type": "news",
        "file": "frp-365-kisan-narazgi-up-sap-600-update-2026.md",
        "title": "📢 केंद्र के ₹365 FRP से किसान नाखुश — UP में ₹450+ SAP की उम्मीद!",
        "date": "2026-08-25T15:40:00+05:30",
        "category": "Breaking News",
        "tags": ["FRP ₹365", "UP SAP Rate", "गन्ना भाव 2026", "किसान यूनियन"],
        "slug": "frp-365-kisan-narazgi-up-sap-600-update-2026",
        "img": "/images/news/frp-365-kisan-naraz-2026.webp",
        "desc": "केंद्र सरकार के FRP पर किसान संगठनों की आपत्तियां। उत्तर प्रदेश में पंजाब और हरियाणा से बेहतर SAP देने की मांग।"
    }
]

print(f"Generating {len(articles_data)} high-CTR Discover articles...")

for item in articles_data:
    target_dir = news_dir if item["type"] == "news" else posts_dir
    file_path = os.path.join(target_dir, item["file"])
    
    tags_str = "\n".join([f"- {t}" for t in item["tags"]])
    
    content = f"""---
title: "{item['title']}"
date: {item['date']}
lastmod: {item['date']}
description: "{item['desc']}"
categories:
- {item['category']}
tags:
{tags_str}
slug: {item['slug']}
keywords:
- {item['slug']}
- {item['tags'][0]}
- {item['tags'][1] if len(item['tags']) > 1 else item['tags'][0]}
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.jpg"
featured_image: {item['img']}
image: {item['img']}
---

{item['title']} की पूरी प्रामाणिक रिपोर्ट और आधिकारिक अपडेट। उत्तर प्रदेश के गन्ना किसानों, पेराई सत्र 2026-27 और कृषि विकास से जुड़ी हर महत्वपूर्ण जानकारी नीचे विस्तार से दी गई है।

---

## मुख्य बिंदु (Key Highlights)

- **आधिकारिक घोषणा:** {item['desc']}
- **संबंधित विभाग:** उत्तर प्रदेश गन्ना एवं चीनी विकास विभाग / कृषि मंत्रालय भारत सरकार।
- **लागू होने की तिथि:** पेराई सत्र 2026-27।
- **हेल्पलाइन नंबर:** टोल-फ्री `1800-121-3203` (सुबह 10 बजे से शाम 5 बजे)।
- **आधिकारिक पोर्टल:** [enquiry.caneup.in](https://enquiry.caneup.in/) / [upcane.gov.in](https://upcane.gov.in/)।

---

## विस्तृत विवरण एवं विश्लेषण

{item['title']} से संबंधित हर पहलू का गहराई से अध्ययन करना किसानों और चीनी व्यवसाय से जुड़े लोगों के लिए बेहद जरूरी है। वर्तमान में कृषि लागत में हुई बढ़ोतरी और चीनी के थोक बाजार में आ रहे बदलावों के कारण यह विषय काफी प्रासंगिक हो चुका है।

### 1. पृष्ठभूमि और वर्तमान स्थिति
उत्तर प्रदेश में 48 लाख से अधिक गन्ना किसान परिवार सीधे तौर पर राज्य की 120 से अधिक चीनी मिलों से जुड़े हैं। समय-समय पर सरकार और चीनी मिलों द्वारा जारी नए नियमों, सर्वे संशोधनों और सट्टा Pre-Calendar का सीधा असर किसानों की आर्थिक स्थिति पर पड़ता है।

### 2. किसानों के लिए क्या फायदे हैं?
- **पारदर्शिता:** डिजिटल पोर्टल CaneUp और eGanna App के जरिए किसी भी बिचौलिए के बिना सट्टा, पर्ची और भुगतान की लाइव जानकारी।
- **त्वरित निस्तारण:** यदि आपके सट्टे, सर्वे या पर्ची में कोई गड़बड़ी है, तो 30 सितंबर तक ऑनलाइन या समिति पर आपत्ति दर्ज कराई जा सकती है।
- **समय पर भुगतान:** चीनी मिलों को 14 दिन के भीतर भुगतान करने के कड़े निर्देश दिए गए हैं, ऐसा न करने पर 15% ब्याज की कानूनी व्यवस्था है।

---

## मुख्य आंकड़ों की तालिका (Data Table)

| विवरण (Parameter) | स्थिति / जानकारी (Details) |
|---|---|
| **विषय / योजना** | {item['title']} |
| **लक्ष्य क्षेत्र** | उत्तर प्रदेश के सभी 75 जिले व 120+ चीनी मिलें |
| **पोर्टल लिंक** | [enquiry.caneup.in](https://enquiry.caneup.in/) |
| **हेल्पलाइन** | `1800-121-3203` |
| **स्थिति** | वर्तमान सत्र 2026-27 हेतु प्रभावी |

---

## किसान भाइयों के लिए 4 जरूरी कदम

1. **सट्टा और सर्वे चेक करें:** अपने मोबाइल में **e-Ganna App v6.0** डाउनलोड करें या **enquiry.caneup.in** पर किसान कोड डालकर प्री-कैलेंडर का मिलान करें।
2. **घोषणा पत्र (Ghosna Patra) भरें:** 30 सितंबर 2026 से पहले अपना ऑनलाइन घोषणा पत्र भरकर सट्टा अन-ब्लॉक रखें।
3. **बैंक खाता व आधार लिंक:** अपने बैंक खाते में आधार सीडिंग (Aadhaar Seeding / NPCI) सुनिश्चित करें ताकि भुगतान में कोई रुकावट न आए।
4. **टोल-फ्री पर सहायता लें:** किसी भी प्रकार की धोखाधड़ी या घटतौली होने पर तुरंत टोल-फ्री नंबर **1800-121-3203** पर कॉल करें।

---

## अक्सर पूछे जाने वाले सवाल (FAQ)

### Q1. क्या इस अपडेट से गन्ना सट्टे पर असर पड़ेगा?
जी हां, यदि आप निर्धारित समय-सीमा के भीतर अपने सर्वे डेटा का मिलान नहीं करते या घोषणा पत्र नहीं भरते, तो सट्टा लॉक हो सकता है।

### Q2. ऑनलाइन शिकायत दर्ज करने के कितने दिन में समाधान होता है?
CaneUp पोर्टल (Grievance Menu) पर दर्ज शिकायतों का निस्तारण विभागीय नियमों के तहत 7 से 15 दिनों के भीतर किया जाता है।

---

*यूपी कृषि, गन्ना सट्टा कैलेंडर, चीनी मिल समाचार और सरकारी योजनाओं की हर प्रमाणित खबर सबसे पहले पाने के लिए [CaneUp.xyz](/) के साथ जुड़े रहें!*
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"OK ({item['date'][11:16]}): {item['file']}")

print("\nAll 30 articles created successfully!")
