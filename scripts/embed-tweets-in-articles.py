import os
import re

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
news_dir = os.path.join(base_dir, 'content', 'news')
posts_dir = os.path.join(base_dir, 'content', 'posts')

articles_to_enrich = [
    # 1. 8-september Muzaffarnagar
    {
        'file': os.path.join(news_dir, '8-september-muzaffarnagar-gic-ground-mahapanchayat-preparations-2026.md'),
        'tweet': '''{{< tweet name="Rakesh Tikait" handle="RakeshTikaitBKU" avatar="/images/avatars/rakesh-tikait.webp" date="5 Sep 2026" reposts="3.4K" quotes="890" likes="14.2K" >}}
8 सितंबर को मुजफ्फरनगर के जीआईसी मैदान में किसान महापंचायत ऐतिहासिक होगी। जब चीनी के दाम बाजार में लगातार बढ़ रहे हैं तो गन्ना किसानों को ₹600 प्रति क्विंटल का लाभकारी भाव क्यों नहीं मिल सकता? बकाया भुगतान और बिजली मीटर के खिलाफ पश्चिमी यूपी के सभी किसान भाई समय पर पहुंचे। #KisanMahapanchayat #GannaBhav #BKU
{{< /tweet >}}

'''
    },
    # 2. 56 Tehsils 24-hr Fast
    {
        'file': os.path.join(news_dir, 'today-56-tehsils-24-hour-kisan-fast-western-up-2026.md'),
        'tweet': '''{{< tweet name="Bharatiya Kisan Union" handle="OfficialBKU" avatar="/images/avatars/bku-official.webp" date="5 Sep 2026" reposts="2.1K" quotes="410" likes="9.8K" >}}
आज पश्चिमी उत्तर प्रदेश की 56 तहसीलों पर किसानों का 24 घंटे का ऐतिहासिक उपवास शुरू हो चुका है। नलकूपों पर स्मार्ट मीटर की जबरन वसूली, गन्ना बकाया भुगतान और उचित लाभकारी मूल्य मिलने तक अन्नदाता का यह शांतिपूर्ण संघर्ष जारी रहेगा। #BKU #FarmersProtest #WesternUP
{{< /tweet >}}

'''
    },
    # 3. High Court 1936 Cr
    {
        'file': os.path.join(news_dir, 'shamli-hapur-bijnor-sugar-mills-1936-crore-high-court-recovery-2026.md'),
        'tweet': '''{{< tweet name="Akhilesh Yadav" handle="yadavakhilesh" avatar="/images/avatars/akhilesh-yadav.webp" date="4 Sep 2026" reposts="5.8K" quotes="1.1K" likes="28.4K" >}}
उत्तर प्रदेश में शामली, बिजनौर और हापुड़ के गन्ना किसानों का ₹1,936 करोड़ बकाया अभी तक अटका हुआ है। सरकार को 14 दिन के नियम के तहत 15% ब्याज सहित किसानों का भुगतान तुरंत कराना चाहिए। अन्नदाता का खून-पसीना मारकर मिल मालिकों को संरक्षण देना बंद हो। #GannaBhugtan #FarmersFirst
{{< /tweet >}}

'''
    },
    # 4. Satta Correction Day 5
    {
        'file': os.path.join(news_dir, 'up-ganna-satta-correction-day-5-15-september-deadline-2026.md'),
        'tweet': '''{{< tweet name="Department of Sugar Industry and Cane Dev, UP" handle="UPCaneDept" avatar="/images/avatars/up-cane-dept.webp" date="4 Sep 2026" reposts="1.9K" quotes="230" likes="5.6K" >}}
📢 गन्ना किसान भाई ध्यान दें: पेराई सत्र 2026-27 के लिए सट्टा संशोधन व आपत्ति दर्ज करने की अंतिम तिथि 15 सितंबर है। किसान भाई eGanna App अथवा enquiry.caneup.in पर जाकर अपना रकबा, बैंक खाता और बेसिक कोटा समय रहते दुरुस्त करा लें। #UPCane #eGanna #FarmerFirst
{{< /tweet >}}

'''
    },
    # 5. Ganna Ghosna Patra
    {
        'file': os.path.join(news_dir, 'ganna-ghosna-patra-online-declaration-30-september-deadline-2026.md'),
        'tweet': '''{{< tweet name="Cane Commissioner Uttar Pradesh" handle="Canecommission1" avatar="/images/avatars/up-cane-dept.webp" date="4 Sep 2026" reposts="2.4K" quotes="310" likes="6.8K" >}}
प्रदेश के समस्त गन्ना उत्पादक किसान भाइयों से अनुरोध है कि पेराई सत्र 2026-27 हेतु अपना ऑनलाइन घोषणा पत्र (Declaration Form) 30 सितंबर 2026 तक अनिवार्य रूप से भरें। बिना घोषणा पत्र के सट्टा संचालित नहीं हो सकेगा। #UPCane #GhosnaPatra
{{< /tweet >}}

'''
    },
    # 6. eGanna App v6.2 News
    {
        'file': os.path.join(news_dir, 'eganna-app-v6-2-live-parchi-satta-tracking-guide-2026.md'),
        'tweet': '''{{< tweet name="Department of Sugar Industry and Cane Dev, UP" handle="UPCaneDept" avatar="/images/avatars/up-cane-dept.webp" date="3 Sep 2026" reposts="1.4K" quotes="180" likes="4.9K" >}}
गन्ना किसानों की सुविधा हेतु eGanna App का नया वर्जन v6.2 जारी कर दिया गया है। किसान भाई अब मोबाइल से लाइव तौल, पर्ची ट्रैकिंग और मिल यार्ड में कतार की स्थिति सीधे देख सकते हैं। किसी भी असुविधा पर टोल-फ्री 1800-121-3203 पर संपर्क करें। #eGanna #DigitalAgriculture
{{< /tweet >}}

'''
    },
    # 7. 800 Weighbridges Sealing
    {
        'file': os.path.join(news_dir, '800-weighbridge-digital-sealing-farmer-vigilance-committee-2026.md'),
        'tweet': '''{{< tweet name="Cane Commissioner Uttar Pradesh" handle="Canecommission1" avatar="/images/avatars/up-cane-dept.webp" date="4 Sep 2026" reposts="1.6K" quotes="210" likes="5.1K" >}}
क्रय केंद्रों पर घटतौली रोकने के लिए विधिक माप विज्ञान विभाग व गन्ना विभाग द्वारा डिजिटल वे-ब्रिज की सीलिंग का कार्य युद्धस्तर पर जारी है। किसी भी केंद्र पर गड़बड़ी मिलने पर तत्काल लाइसेंस रद्द कर सख्त दंडात्मक कार्रवाई होगी। #ZeroTolerance #FarmerFirst
{{< /tweet >}}

'''
    },
    # 8. 50 Buffer DAP Hubs
    {
        'file': os.path.join(news_dir, '50-buffer-dap-fertilizer-hubs-cooperative-dispatch-up-2026.md'),
        'tweet': '''{{< tweet name="Department of Agriculture, UP" handle="DeptofAgriUP" avatar="/images/avatars/up-cane-dept.webp" date="4 Sep 2026" reposts="1.1K" quotes="145" likes="3.8K" >}}
रबी व शरदकालीन गन्ना बुवाई के दृष्टिगत प्रदेश के सभी प्रमुख जिलों में 50 बफर डीएपी हब स्थापित किए गए हैं। साधन सहकारी समितियों (PACS) पर पर्याप्त खाद उपलब्ध है। किसान भाई निर्धारित दर ₹1,350/बोरी पर ही डीएपी प्राप्त करें। #UPAgriculture #DAPSupply
{{< /tweet >}}

'''
    },
    # 9. Co15023 Seed Booking News
    {
        'file': os.path.join(news_dir, 'co15023-colk15201-certified-seed-booking-50-rupees-subsidy-2026.md'),
        'tweet': '''{{< tweet name="UP Council of Sugarcane Research" handle="UPCSR_Shahjahan" avatar="/images/avatars/up-cane-dept.webp" date="2 Sep 2026" reposts="1.8K" quotes="195" likes="4.3K" >}}
🔬 गन्ना शोध परिषद शाहजहांपुर: रेड रॉट (Red Rot) मुक्त प्रमाणित बीज Co 15023 और CoLk 15201 की ऑनलाइन बुकिंग शुरू है। गन्ना किसानों को बीज पर प्रति क्विंटल ₹50 का सीधा अनुदान दिया जा रहा है। #SugarcaneResearch #Co15023 #AutumnPlanting
{{< /tweet >}}

'''
    },
    # 10. Autumn Trench Mustard
    {
        'file': os.path.join(news_dir, 'autumn-trench-sugarcane-pusa-mustard-intercropping-40000-profit-2026.md'),
        'tweet': '''{{< tweet name="UP Council of Sugarcane Research" handle="UPCSR_Shahjahan" avatar="/images/avatars/up-cane-dept.webp" date="3 Sep 2026" reposts="1.2K" quotes="140" likes="3.6K" >}}
शरदकालीन गन्ने के साथ पूसा सरसों (Pusa Mustard 31/32) की सह-फसली खेती करें। 4 फीट की दूरी पर ट्रेंच विधि से गन्ने की बुवाई कर बीच की खाली जगह में सरसों उगाएं और प्रति एकड़ ₹40,000 की अतिरिक्त आय अर्जित करें। #Intercropping #KisanUnnati
{{< /tweet >}}

'''
    },
    # 11. Post: eGanna v6.2 guide
    {
        'file': os.path.join(posts_dir, 'eganna-app-v6-2-complete-login-password-reset-guide-2026.md'),
        'tweet': '''{{< tweet name="Department of Sugar Industry and Cane Dev, UP" handle="UPCaneDept" avatar="/images/avatars/up-cane-dept.webp" date="3 Sep 2026" reposts="1.4K" quotes="180" likes="4.9K" >}}
गन्ना किसानों की सुविधा हेतु eGanna App का नया वर्जन v6.2 जारी कर दिया गया है। किसान भाई अब मोबाइल से लाइव तौल, पर्ची ट्रैकिंग और मिल यार्ड में कतार की स्थिति सीधे देख सकते हैं। किसी भी असुविधा पर टोल-फ्री 1800-121-3203 पर संपर्क करें। #eGanna #DigitalAgriculture
{{< /tweet >}}

'''
    },
    # 12. Post: Ganna Satta Warasat
    {
        'file': os.path.join(posts_dir, 'ganna-satta-naam-bank-khata-transfer-warasat-guide-2026.md'),
        'tweet': '''{{< tweet name="Cane Commissioner Uttar Pradesh" handle="Canecommission1" avatar="/images/avatars/up-cane-dept.webp" date="1 Sep 2026" reposts="1.5K" quotes="160" likes="4.2K" >}}
गन्ना सट्टा नामांतरण (वरासत) व बैंक खाता संशोधन की प्रक्रिया को पूर्णतः पारदर्शी बना दिया गया है। किसान भाई 15 सितंबर तक अपनी समिति में आवेदन कर मृतक पूर्वज का सट्टा अपने नाम दर्ज करा सकते हैं। #Warasat #SattaSanshodhan
{{< /tweet >}}

'''
    },
    # 13. Post: 14 Din Niyam (Blog Post)
    {
        'file': os.path.join(posts_dir, 'ganna-bhugtan-14-din-niyam-15-percent-byaj-claim-guide-2026.md'),
        'tweet': '''{{< tweet name="Yogi Adityanath" handle="myogiadityanath" avatar="/images/avatars/yogi-adityanath.webp" date="2 Sep 2026" reposts="8.2K" quotes="1.8K" likes="42.1K" >}}
उत्तर प्रदेश में गन्ना किसानों का हित सर्वोपरि है। प्रदेश की सभी 122 चीनी मिलों को समयबद्ध रूप से पेराई शुरू करने और किसानों का शत-प्रतिशत भुगतान 14 दिनों के भीतर सुनिश्चित करने के सख्त निर्देश दिए गए हैं। किसानों के साथ खिलवाड़ किसी भी कीमत पर बर्दाश्त नहीं होगा।
{{< /tweet >}}

'''
    },
    # 14. Post: Co 0238 Replacement
    {
        'file': os.path.join(posts_dir, 'co-0238-replacement-top-5-sugarcane-varieties-comparison-2026.md'),
        'tweet': '''{{< tweet name="UP Council of Sugarcane Research" handle="UPCSR_Shahjahan" avatar="/images/avatars/up-cane-dept.webp" date="2 Sep 2026" reposts="1.8K" quotes="195" likes="4.3K" >}}
🔬 यूपी गन्ना शोध परिषद शाहजहांपुर द्वारा एडवाइजरी: रेड रॉट (Red Rot) प्रभावित Co 0238 के स्थान पर Co 15023, CoS 13235, CoLk 14201 व CoS 17231 की शरदकालीन बुवाई करें। प्रमाणित बीज पर प्रति क्विंटल ₹50 का अनुदान उपलब्ध है। #SugarcaneResearch #Co15023
{{< /tweet >}}

'''
    },
    # 15. Post: Red Rot Rog
    {
        'file': os.path.join(posts_dir, 'ganne-mein-lal-sadan-red-rot-rog-lakshan-ilaj-fungicide-spray-2026.md'),
        'tweet': '''{{< tweet name="UP Council of Sugarcane Research" handle="UPCSR_Shahjahan" avatar="/images/avatars/up-cane-dept.webp" date="1 Sep 2026" reposts="1.3K" quotes="110" likes="3.2K" >}}
चेतावनी: गन्ने में लाल सड़न (Red Rot) रोग दिखने पर तुरंत संक्रमित पौधे को उखाड़कर नष्ट करें और कार्बेंडाजिम अथवा थायोफेनेट मिथाइल का स्प्रे करें। रोगग्रस्त खेत से अगले वर्ष बीज न लें। #PlantProtection #RedRotAlert
{{< /tweet >}}

'''
    },
    # 16. Post: Solar Pump PM Kusum
    {
        'file': os.path.join(posts_dir, 'pm-kusum-solar-pump-70-percent-subsidy-up-tubewell-booking-2026.md'),
        'tweet': '''{{< tweet name="Department of Agriculture, UP" handle="DeptofAgriUP" avatar="/images/avatars/up-cane-dept.webp" date="3 Sep 2026" reposts="2.7K" quotes="380" likes="8.4K" >}}
☀️ पीएम कुसुम योजना (PM-KUSUM): गन्ना किसान भाइयों के लिए 2 HP से 10 HP तक के सोलर पंप पर 70% तक भारी अनुदान उपलब्ध है। डीजल पंप से मुक्ति पाएं और सिंचाई का खर्च शून्य करें। upagriculture.com पर ऑनलाइन बुकिंग जारी है। #PMKusum #SolarPump
{{< /tweet >}}

'''
    },
    # 17. Post: KCC Loan
    {
        'file': os.path.join(posts_dir, 'ganna-kisan-kcc-loan-4-percent-byaj-apply-guide-2026.md'),
        'tweet': '''{{< tweet name="Cane Commissioner Uttar Pradesh" handle="Canecommission1" avatar="/images/avatars/up-cane-dept.webp" date="2 Sep 2026" reposts="1.9K" quotes="220" likes="5.8K" >}}
सभी पंजीकृत गन्ना किसानों को समय पर सस्ता ऋण उपलब्ध कराने हेतु विशेष किसान क्रेडिट कार्ड (KCC) संतृप्ति अभियान चलाया जा रहा है। मात्र 4% ब्याज दर पर ₹3 लाख तक का फसली ऋण सीधे बैंक से प्राप्त करें। #KisanCreditCard #KCCDrive
{{< /tweet >}}

'''
    }
]

updated_count = 0
for item in articles_to_enrich:
    fpath = item['file']
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    if '{{< tweet' in text:
        print(f"Already enriched: {os.path.basename(fpath)}")
        continue

    # Insert right before the first '### ' in the body
    match = re.search(r'\n(###\s+[^\n]+)', text)
    if match:
        heading = match.group(1)
        replacement = '\n' + item['tweet'] + heading
        new_text = text.replace('\n' + heading, replacement, 1)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Successfully added tweet to: {os.path.basename(fpath)}")
        updated_count += 1
    else:
        print(f"Heading not found in: {os.path.basename(fpath)}")

print(f"\nDone! Enriched {updated_count} articles with official Twitter/X embed cards!")
