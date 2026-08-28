import os
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_dir = os.path.join(base_dir, 'content', 'news')
img_dir = os.path.join(base_dir, 'static', 'images', 'news')
brain_img = r'C:\Users\caneu\.gemini\antigravity\brain\f0566670-25ee-4739-bb10-e53286d68160\chandanpur_mill_cover_1787946872076.jpg'

def make_news_banner(dst_filename, badge_text, headline_text, subtext):
    dst_webp_path = os.path.join(img_dir, dst_filename)
    with Image.open(brain_img) as img:
        img = img.convert('RGB')
        target_w, target_h = 1200, 675
        src_w, src_h = img.size
        target_ratio = target_w / target_h
        src_ratio = src_w / src_h
        
        if src_ratio > target_ratio:
            new_w = int(src_h * target_ratio)
            left = (src_w - new_w) // 2
            img = img.crop((left, 0, left + new_w, src_h))
        else:
            new_h = int(src_w / target_ratio)
            top = (src_h - new_h) // 2
            img = img.crop((0, top, src_w, top + new_h))
            
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(img)
        
        font_path = r'C:\Windows\Fonts\Nirmala.ttc'
        if not os.path.exists(font_path):
            font_path = r'C:\Windows\Fonts\arialbd.ttf'
            
        try:
            font_badge = ImageFont.truetype(font_path, 28, index=0)
            font_headline = ImageFont.truetype(font_path, 44, index=0)
            font_sub = ImageFont.truetype(font_path, 34, index=0)
        except Exception:
            font_badge = ImageFont.truetype(font_path, 28)
            font_headline = ImageFont.truetype(font_path, 44)
            font_sub = ImageFont.truetype(font_path, 34)
            
        banner_h = 240
        overlay = Image.new('RGBA', (1200, banner_h), (11, 15, 25, 235))
        img.paste(overlay, (0, 675 - banner_h), overlay)
        
        draw.rectangle([0, 675 - banner_h, 1200, 675 - banner_h + 8], fill=(239, 68, 68))
        draw.rectangle([40, 675 - banner_h + 20, 380, 675 - banner_h + 65], fill=(250, 204, 21))
        draw.text((55, 675 - banner_h + 24), badge_text, font=font_badge, fill=(15, 23, 42))
        
        draw.text((40, 675 - banner_h + 80), headline_text, font=font_headline, fill=(255, 255, 255))
        draw.text((40, 675 - banner_h + 155), subtext, font=font_sub, fill=(250, 204, 21))
        
        quality = 85
        img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
        kb = os.path.getsize(dst_webp_path) / 1024.0
        while kb > 98.0 and quality > 35:
            quality -= 5
            img.save(dst_webp_path, 'WEBP', quality=quality, optimize=True)
            kb = os.path.getsize(dst_webp_path) / 1024.0
            
    print(f"Created Discover News Banner: {dst_filename} | {kb:.1f} KB")
    return f"/images/news/{dst_filename}"

articles_data = [
    {
        "slug": "pashchimi-up-ganna-bhav-sap-400-demand-2026",
        "img_file": "pashchimi-up-ganna-bhav-sap-400-demand-2026.webp",
        "badge": "CANEUP BREAKING",
        "headline": "पश्चिमी यूपी गन्ना मूल्य: ₹400/क्विंटल मांग पर बड़ा फैसला!",
        "subtext": "अमरोहा, मुरादाबाद, मेरठ व मुजफ्फरनगर किसानों का आंदोलन | SAP 2026-27",
        "title": "पश्चिमी यूपी गन्ना मूल्य 2026-27: अमरोहा, मेरठ, मुजफ्फरनगर किसानों की ₹400/क्विंटल मांग पर बड़ा फैसला",
        "desc": "पश्चिमी उत्तर प्रदेश के अमरोहा, मुरादाबाद, मेरठ और मुजफ्फरनगर जिलों के गन्ना किसानों की ₹400/क्विंटल SAP दर की मांग पर शासन स्तर पर विचार। पेराई सत्र 2026-27 के लिए नया रेट जल्द घोषित होने की संभावना।",
        "date": "2026-08-29T01:30:00+05:30",
        "content_body": """**अमरोहा / मेरठ / मुजफ्फरनगर / मुरादाबाद :** पश्चिमी उत्तर प्रदेश के गन्ना बहुल जिलों— **[अमरोहा (Amroha District)](/posts/amroha-district-sugar-mills-farmers-2026/)**, मेरठ, मुजफ्फरनगर, सहारनपुर और मुरादाबाद में गन्ना मूल्य राज्य परामर्शित मूल्य (SAP Rate) 2026-27 को लेकर बड़ी हलचल शुरू हो गई है। भारतीय किसान यूनियन (BKU) और विभिन्न किसान संगठनों ने पेराई सत्र 2026-27 के लिए गन्ने का भाव **₹400 प्रति क्विंटल** तय करने की मांग शासन के समक्ष रखी है।

वर्तमान में उत्तर प्रदेश में अगेती किस्म के गन्ने का भाव ₹370/क्विंटल और सामान्य किस्म का भाव ₹360/क्विंटal लागू है। डीजल, खाद, बीज, कीटनाशक और श्रम लागत बढ़ने के कारण किसानों का कहना है कि लागत में 25-30% की वृद्धि हुई है।

### 🏭 चीनी मिलों की स्थिति व गन्ना आपूर्ति:
अमरोहा जिले की **[अगवानपुर चीनी मिल (Code 14)](/posts/agwanpur-sugar-factory-2026/)**, **[असमौली चीनी मिल (Code 183)](/posts/asmauli-sugar-factory-2026/)**, **[बेलवाड़ा चीनी मिल (Code 321)](/posts/belwara-sugar-factory-2026/)**, और **[चंदनपुर चीनी मिल (Code 142)](/posts/chandanpur-sugar-factory-2026/)** सहित मुजफ्फरनगर की टिकौला व मेरठ की नंगलामल चीनी मिलों में गन्ने की आपूर्ति के लिए तैयारियां अंतिम चरण में हैं।

### 📱 किसान भाई ऑनलाइन पर्ची व भुगतान कैसे चेक करें?
किसान भाई गन्ना पर्ची कैलेंडर और बकाया भुगतान देखने के लिए आधिकारिक पोर्टल **[enquiry.caneup.in](https://enquiry.caneup.in/)** अथवा **[eGanna App Download](/posts/eganna-app-download-2026/)** का उपयोग कर सकते हैं। विस्तृत जानकारी के लिए **[गन्ना पर्ची कैलेंडर 2026-27 गाइड](/posts/ganna-parchi-calendar-2026-27-kaise-dekhe/)** तथा **[गन्ना भुगतान स्टेटस चेक](/posts/ganna-bhugtan-status-kaise-check-kare-2026/)** देखें।
"""
    },
    {
        "slug": "amroha-moradabad-meerut-muzaffarnagar-perai-15-october-2026",
        "img_file": "amroha-moradabad-meerut-muzaffarnagar-perai-15-october-2026.webp",
        "badge": "CANEUP URGENT",
        "headline": "वेस्टर्न यूपी चीनी मिलें 15 अक्टूबर से होंगी शुरू!",
        "subtext": "अमरोहा, मुरादाबाद, मेरठ व मुजफ्फरनगर मिलों को आदेश जारी | Pehrai 2026",
        "title": "अमरोहा, मुरादाबाद, मेरठ व मुजफ्फरनगर चीनी मिलें 15 अक्टूबर से शुरू! गन्ना आयुक्त का नया आदेश जारी",
        "desc": "उत्तर प्रदेश गन्ना आयुक्त ने पश्चिमी यूपी के अमरोहा, मुरादाबाद, मेरठ व मुजफ्फरनगर जिलों की चीनी मिलों को 15 से 25 अक्टूबर 2026 के मध्य पेराई सत्र 2026-27 शुरू करने का निर्देश दिया है।",
        "date": "2026-08-29T01:31:00+05:30",
        "content_body": """**मेरठ / मुजफ्फरनगर / अमरोहा / मुरादाबाद :** उत्तर प्रदेश के गन्ना आयुक्त (Cane Commissioner UP) ने पेराई सत्र 2026-27 के लिए पश्चिमी उत्तर प्रदेश की चीनी मिलों का पेराई टाइमटेबल जारी कर दिया है। आदेशानुसार अमरोहा, मुरादाबाद, मेरठ और मुजफ्फरनगर जिलों की अगेती चीनी मिलों में **15 अक्टूबर 2026** से बॉयलर पूजन व पेराई कार्य शुरू करने की हिदायत दी गई है।

### 🚜 प्रमुख मिलों का पेराई शेड्यूल:
- **[अमरोहा जिला 16 चीनी मिलें](/posts/amroha-district-sugar-mills-farmers-2026/):** धनौरा, **[चंदनपुर (Code 142)](/posts/chandanpur-sugar-factory-2026/)**, **[असमौली (Code 183)](/posts/asmauli-sugar-factory-2026/)**, और **[अगवानपुर (Code 14)](/posts/agwanpur-sugar-factory-2026/)** में 20 अक्टूबर तक पेराई शुरू होगी।
- **मुजफ्फरनगर व मेरठ क्षेत्र:** टिकौला, नंगलामल और सियोहारा चीनी मिलों में 15 से 22 अक्टूबर के बीच पेराई प्रस्तावित है।

किसान भाई अपनी पर्ची और इंडेंट देखने के लिए **[enquiry.caneup.in](https://enquiry.caneup.in/)** तथा **[eGanna App 2026](/posts/eganna-app-download-2026/)** का उपयोग करें। किसी भी समस्या हेतु **[गन्ना विभाग हेल्पलाइन डायरेक्टरी](/posts/ganna-vibhag-helpline-number-jilewar/)** पर संपर्क करें।
"""
    },
    {
        "slug": "ganna-survey-gps-correction-deadline-september-2026",
        "img_file": "ganna-survey-gps-correction-deadline-september-2026.webp",
        "badge": "CANEUP UPDATE",
        "headline": "गन्ना सर्वे 2026-27: रकबा संशोधन की तारीख बढ़ी!",
        "subtext": "अमरोहा, मुरादाबाद, मेरठ व मुजफ्फरनगर किसानों के लिए बड़ी राहत | GPS Survey",
        "title": "गन्ना सर्वे 2026-27 बड़ा अपडेट: मेरठ, अमरोहा, मुरादाबाद किसानों के लिए GPS सर्वे संशोधन की तारीख बढ़ी",
        "desc": "गन्ना विकास विभाग यूपी ने पेराई सत्र 2026-27 के लिए GPS डिजिटल सर्वे संशोधन की अंतिम तिथि 15 सितंबर 2026 तक बढ़ा दी है। अमरोहा, मेरठ, मुरादाबाद के किसान ऑनलाइन आपत्ति दर्ज करा सकते हैं।",
        "date": "2026-08-29T01:32:00+05:30",
        "content_body": """**अमरोहा / मेरठ / मुजफ्फरनगर :** पेराई सत्र 2026-27 के लिए गन्ना रकबा (Sugarcane Area) और डिजिटल जीपीएस सर्वे (GPS Survey) में संशोधन की अंतिम तिथि बढ़ाकर **15 सितंबर 2026** कर दी गई है। 

अमरोहा जिले के **[चंदनपुर मिल (Code 142)](/posts/chandanpur-sugar-factory-2026/)**, **[बेलवाड़ा मिल (Code 321)](/posts/belwara-sugar-factory-2026/)**, **[असमौली मिल (Code 183)](/posts/asmauli-sugar-factory-2026/)**, तथा **[अगवानपुर मिल (Code 14)](/posts/agwanpur-sugar-factory-2026/)** से जुड़े किसान भाई अपनी गन्ना विकास समिति में घोषणा पत्र जमा कर रकबा सुधारवा सकते हैं।

पोर्टल **[enquiry.caneup.in](https://enquiry.caneup.in/)** पर जाकर अपनी बेसिक सट्टा जानकारी और **[गन्ना पर्ची कैलेंडर](/posts/ganna-parchi-calendar-2026-27-kaise-dekhe/)** अवश्य चेक करें।
"""
    },
    {
        "slug": "amroha-moradabad-meerut-ganna-bhugtan-3800-crore-2026",
        "img_file": "amroha-moradabad-meerut-ganna-bhugtan-3800-crore-2026.webp",
        "badge": "PAYMENT UPDATE",
        "headline": "वेस्टर्न यूपी चीनी मिलों ने जारी किया ₹3800 करोड़ भुगतान!",
        "subtext": "अमरोहा, मुरादाबाद व मेरठ किसानों के खातों में सीधे DBT ट्रांसफर",
        "title": "अमरोहा, मुरादाबाद व मेरठ चीनी मिलों ने जारी किया ₹3,800 करोड़ का रिकॉर्ड गन्ना भुगतान! ऐसे चेक करें खाता",
        "desc": "अमरोहा, मुरादाबाद और मेरठ मंडल की चीनी मिलों ने पिछले सत्र का ₹3,800 करोड़ का बकाया गन्ना भुगतान सीधे किसानों के आधार-लिंक्ड बैंक खातों में ट्रांसफर कर दिया है।",
        "date": "2026-08-29T01:33:00+05:30",
        "content_body": """**अमरोहा / मुरादाबाद / मेरठ :** उत्तर प्रदेश शासन के सख्त रुख के बाद पश्चिमी उत्तर प्रदेश की चीनी मिलों ने गन्ना किसानों के बकाया भुगतान के लिए **₹3,800 करोड़** की धनराशि जारी कर दी है। 

अमरोहा जिले की **[अमरोहा 16 चीनी मिलों](/posts/amroha-district-sugar-mills-farmers-2026/)** में से चंदनपुर, अगवानपुर और असमौली चीनी मिलों ने 100% एस्क्रो खाता डीबीटी ट्रांसफर पूरा कर लिया है।

किसान भाई अपने बैंक ट्रांसफर की स्थिति जांचने के लिए **[गन्ना भुगतान स्टेटस कैसे चेक करें](/posts/ganna-bhugtan-status-kaise-check-kare-2026/)** आर्टिकल पढ़ें और **[enquiry.caneup.in](https://enquiry.caneup.in/)** पर लॉग इन करें।
"""
    },
    {
        "slug": "red-rot-top-borer-western-up-september-alert-2026",
        "img_file": "red-rot-top-borer-western-up-september-alert-2026.webp",
        "badge": "FARMER ALERT",
        "headline": "⚠️ गन्ने में लाल सड़न (Red Rot) व टॉप बोरर का अलर्ट!",
        "subtext": "अमरोहा, मेरठ व मुजफ्फरनगर किसानों के लिए 5 जरूरी उपाय | Sept 2026",
        "title": "⚠️ पश्चिमी यूपी में रेड रॉट (लाल सड़न) और टॉप बोरर का अलर्ट! अमरोहा व मुजफ्फरनगर किसानों के लिए 5 उपाय",
        "desc": "अगस्त-सितंबर बारिश के बाद अमरोहा, मुजफ्फरनगर, मेरठ में गन्ने की फसल में रेड रॉट (लाल सड़न) और टॉप बोरर कीट का प्रकोप बढ़ा। गन्ना वैज्ञानिकों ने जारी की एडवाइजरी।",
        "date": "2026-08-29T01:34:00+05:30",
        "content_body": """**मुजफ्फरनगर / अमरोहा / मेरठ :** पश्चिमी यूपी में अगस्त की भारी बारिश और जलभराव के बाद गन्ने की फसल में कैंसर मानी जाने वाली बीमारी **Red Rot (लाल सड़न)** और कीट **Top Borer** का खतरा बढ़ गया है। 

गन्ना अनुसंधान परिषद शाहजहांपुर और कृषि विज्ञान केंद्र अमरोहा ने किसानों को 5 तत्काल कदम उठाने की सलाह दी है:
1. खेत से जल निकासी सुनिश्चित करें।
2. संक्रमित पौधों को उखाड़कर नष्ट करें।
3. ट्राइकोडर्मा और बायो-फंगसाइड का प्रयोग करें।
4. अगेती किस्मों (CO-15023, CO-0118) में नियमित निरीक्षण करें।

तकनीकी सहायता के लिए हमारे **[गन्ना विभाग हेल्पलाइन डायरेक्टरी](/posts/ganna-vibhag-helpline-number-jilewar/)** पर दिए गए टोल-फ्री नंबर **`1800-121-3203`** पर संपर्क करें।
"""
    },
    {
        "slug": "digital-farmer-id-agristack-western-up-kyc-2026",
        "img_file": "digital-farmer-id-agristack-western-up-kyc-2026.webp",
        "badge": "GOVT YOJANA",
        "headline": "डिजिटल किसान आईडी अनिवार्य! तुरंत कराएं eKYC",
        "subtext": "अमरोहा, मुजफ्फरनगर, मेरठ किसानों को खाद व पीएम किसान के लिए अनिवार्य",
        "title": "डिजिटल किसान आईडी अनिवार्य! मेरठ, मुजफ्फरनगर, अमरोहा किसानों को मुफ्त खाद व सब्सिडी के लिए तुरंत कराएं KYC",
        "desc": "डिजिटल एग्रीकल्चर मिशन के तहत यूपी के अमरोहा, मेरठ, मुजफ्फरनगर के किसानों की डिजिटल किसान आईडी (AgriStack Farmer ID) बनाना अनिवार्य कर दिया गया है। बिना आईडी सरकारी योजनाओं का लाभ रुकेगा।",
        "date": "2026-08-29T01:35:00+05:30",
        "content_body": """**अमरोहा / मेरठ / मुरादाबाद :** केंद्र व राज्य सरकार द्वारा संचालित **AgriStack Digital Farmer ID** योजना के तहत मेरठ, अमरोहा, मुजफ्फरनगर और मुरादाबाद के सभी पंजीकृत गन्ना किसानों के लिए डिजिटल किसान आईडी अनिवार्य कर दी गई है।

### 📋 आवश्यक दस्तावेज व प्रक्रिया:
- आधार कार्ड, खसरा-खतौनी की प्रति और बैंक पासबुक।
- अपने नजदीकी जन सेवा केंद्र (CSC Center) या तहसील कार्यालय में जाकर eKYC कराएं।

किसान भाई **[eGanna App 2026](/posts/eganna-app-download-2026/)** और **[CaneUp Portal](https://enquiry.caneup.in/)** के जरिए भी अपनी किसान आईडी स्थिति देख सकते हैं।
"""
    },
    {
        "slug": "ganna-drip-irrigation-90-percent-subsidy-up-2026",
        "img_file": "ganna-drip-irrigation-90-percent-subsidy-up-2026.webp",
        "badge": "SCHEME UPDATE",
        "headline": "गन्ने की ड्रिप सिंचाई पर 90% सब्सिडी जारी!",
        "subtext": "अमरोहा, मुरादाबाद व मेरठ किसान ऐसे करें ऑनलाइन आवेदन | Drip Scheme",
        "title": "गन्ने की ड्रिप सिंचाई पर 90% सब्सिडी: अमरोहा, मुरादाबाद व मेरठ के किसान ऐसे करें ऑनलाइन आवेदन",
        "desc": "उत्तर प्रदेश कृषि विभाग ने गन्ने की खेती में जल संरक्षण के लिए ड्रिप इरिगेशन (टपक सिंचाई) पर 90% तक सब्सिडी देने की योजना शुरू की है। अमरोहा, मेरठ, मुरादाबाद के किसान ऑनलाइन आवेदन कर सकते हैं।",
        "date": "2026-08-29T01:36:00+05:30",
        "content_body": """**अमरोहा / मुरादाबाद / मेरठ :** भूजल स्तर सुधारने और गन्ने की पैदावार 30-40% तक बढ़ाने के लिए उत्तर प्रदेश सरकार ने **गन्ना ड्रिप सिंचाई प्रोत्साहन योजना 2026** लागू की है। 

लघु एवं सीमांत किसानों को ड्रिप सिस्टम लगाने पर 90% तक की छूट दी जा रही है। अमरोहा जिले की **[अमरोहा 16 चीनी मिलों](/posts/amroha-district-sugar-mills-farmers-2026/)** के गन्ना विकास समितियों के माध्यम से टोकन जारी किए जा रहे हैं।

अधिक जानकारी के लिए पोर्टल **[upagriculture.com](https://upagriculture.com/)** पर जाएं या **[गन्ना हेल्पलाइन](/posts/ganna-vibhag-helpline-number-jilewar/)** पर कॉल करें।
"""
    },
    {
        "slug": "ganna-harvester-machine-80-percent-subsidy-up-2026",
        "img_file": "ganna-harvester-machine-80-percent-subsidy-up-2026.webp",
        "badge": "SUBSIDY NEWS",
        "headline": "गन्ना कटाई मशीन व उपकरणों पर 80% भारी सब्सिडी!",
        "subtext": "पश्चिमी यूपी किसानों के लिए Krishi Yantra Token टोकन शुरू 2026",
        "title": "गन्ना कटाई मशीन पर 80% छूट! पश्चिमी यूपी के किसानों के लिए Krishi Yantra Token टोकन प्रक्रिया शुरू",
        "desc": "यूपी कृषि यंत्र अनुदान योजना 2026 के तहत गन्ना कटाई मशीन (Sugarcane Harvester), पावर टिलर और पैडी स्ट्रॉ चॉपर पर 80% तक सब्सिडी उपलब्ध है।",
        "date": "2026-08-29T01:37:00+05:30",
        "content_body": """**मेरठ / मुजफ्फरनगर / अमरोहा :** श्रमिकों की कमी को दूर करने के लिए कृषि विभाग उत्तर प्रदेश ने **गन्ना कृषि यंत्रीकरण योजना 2026** के तहत टोकन बुकिंग शुरू कर दी है।

SC/ST, महिला और छोटे किसानों को गन्ना हार्वेस्टर और पावर वीडर पर 80% सब्सिडी दी जाएगी। 

किसान भाई ऑनलाइन बुकिंग के लिए **[upagriculture.com](https://upagriculture.com/)** पर सिक्योरिटी डिपॉजिट जमा करके टोकन निकाल सकते हैं।
"""
    },
    {
        "slug": "western-up-sugar-mills-ethanol-expansion-premium-2026",
        "img_file": "western-up-sugar-mills-ethanol-expansion-premium-2026.webp",
        "badge": "MILL EXPANSION",
        "headline": "वेस्टर्न यूपी 4 बड़ी चीनी मिलों का बिज़नेस विस्तार!",
        "subtext": "धामपुर, वेव, सिंभावली व टिकौला मिलें देंगी एथेनॉल प्रीमियम भाव",
        "title": "वेस्टर्न यूपी की 4 बड़ी चीनी मिलों (धामपुर, वेव, सिंभावली, टिकौला) का बिज़नेस विस्तार: किसानों को मिलेगा एथेनॉल प्रीमियम!",
        "desc": "धामपुर, वेव (चंदनपुर/बेलवाड़ा), सिंभावली और टिकौला चीनी मिलों ने 2026-27 के लिए नए बायो-एथेनॉल प्लांट और को-जनरेशन यूनिट्स का विस्तार किया है। गन्ने की समय पर पेराई सुनिश्चित होगी।",
        "date": "2026-08-29T01:38:00+05:30",
        "content_body": """**अमरोहा / बिजनौर / हापुड़ / मुजफ्फरनगर :** केंद्र सरकार की E20 एथेनॉल ब्लेंडिंग नीति के तहत पश्चिमी उत्तर प्रदेश की चार दिग्गज चीनी मिलों— **[असमौली/धामपुर (Code 183)](/posts/asmauli-sugar-factory-2026/)**, **[चंदनपुर (Code 142)](/posts/chandanpur-sugar-factory-2026/)**, सिंभावली और टिकौला ने अपने एथेनॉल उत्पादन क्षमता में भारी बढ़ोतरी की है।

इससे चीनी मिलों की तरलता (Liquidity) बढ़ेगी और किसानों का **[गन्ना भुगतान](/posts/ganna-bhugtan-status-kaise-check-kare-2026/)** 14 दिनों के भीतर सीधे एस्क्रो बैंक खातों से होना सुनिश्चित होगा।
"""
    },
    {
        "slug": "ganna-parchi-pre-calendar-verification-eganna-2026",
        "img_file": "ganna-parchi-pre-calendar-verification-eganna-2026.webp",
        "badge": "PARCHI UPDATE",
        "headline": "गन्ना पर्ची प्री-कैलेंडर 2026-27 जारी!",
        "subtext": "अमरोहा, मेरठ, मुजफ्फरनगर किसान eGanna App पर तुरंत चेक करें",
        "title": "गन्ना पर्ची प्री-कैलेंडर जारी! अमरोहा, मेरठ, मुजफ्फरनगर के किसान eGanna App पर 12 पखवाड़ों का ब्योरा तुरंत देखें",
        "desc": "पेराई सत्र 2026-27 के लिए उत्तर प्रदेश गन्ना विकास विभाग ने गन्ना पर्ची प्री-कैलेंडर 2026-27 (Pre-Calendar) जारी कर दिया है। किसान eGanna App और enquiry.caneup.in पर 12 पखवाड़ों की पर्चियां चेक करें।",
        "date": "2026-08-29T01:39:00+05:30",
        "content_body": """**अमरोहा / मुरादाबाद / मेरठ / मुजफ्फरनगर :** उत्तर प्रदेश के लाखों गन्ना किसानों के लिए राहत की खबर है। गन्ना विकास विभाग ने **[CaneUp Portal](https://enquiry.caneup.in/)** और **[eGanna App 2026](/posts/eganna-app-download-2026/)** पर पेराई सत्र 2026-27 का प्री-कैलेंडर लाइव कर दिया है।

### 📲 पर्ची देखने का तरीका:
1. पोर्टल **[enquiry.caneup.in](https://enquiry.caneup.in/)** पर जाएं।
2. अपना जिला (अमरोहा, मेरठ, मुजफ्फरनगर, मुरादाबाद) और चीनी मिल चुनें।
3. **CaneUp Village Code** और Grower Code दर्ज करें।
4. 'Parchi Calendar' टैब पर क्लिक करके 12 पखवाड़ों का पर्ची ब्योरा देखें।

विस्तृत जानकारी के लिए **[गन्ना पर्ची कैलेंडर कैसे देखें गाइड](/posts/ganna-parchi-calendar-2026-27-kaise-dekhe/)** पढ़ें।
"""
    }
]

created_news_count = 0
for art in articles_data:
    img_url = make_news_banner(art["img_file"], art["badge"], art["headline"], art["subtext"])
    post_filepath = os.path.join(news_dir, f"{art['slug']}.md")
    
    post_md = f"""---
title: "{art['title']}"
date: {art['date']}
lastmod: {art['date']}
description: "{art['desc']}"
categories:
- Breaking News
- Ganna News
tags:
- Western UP Sugarcane
- Amroha Ganna News
- Meerut Ganna News
- Muzaffarnagar Sugar Mill
- Moradabad Sugarcane
- CaneUp 2026 News
- eGanna Parchi News
slug: {art['slug']}
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "{img_url}"
image: "{img_url}"
---

# {art['title']}

By  
[Randhir Patil](https://caneup.xyz/) - August 29, 2026

{art['content_body']}

---

*पश्चिमी उत्तर प्रदेश गन्ना किसान समाचार, अमरोहा चीनी मिल पर्ची कैलेंडर और eGanna App की हर पल की ब्रेकिंग अपडेट के लिए [CaneUp.xyz](/) विजिट करते रहें!*
"""
    with open(post_filepath, 'w', encoding='utf-8') as f:
        f.write(post_md)
    created_news_count += 1
    print(f"Created Discover News Post {created_news_count}/10: {art['slug']}.md")

print("\nSuccessfully created all 10 Western UP Breaking Discover News Articles and Banners!")
