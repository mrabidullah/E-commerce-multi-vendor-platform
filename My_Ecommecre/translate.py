import os

# Create directories
locales = ['en', 'ur', 'ar']
for lang in locales:
    os.makedirs(f'locale/{lang}/LC_MESSAGES', exist_ok=True)

# English translations
en_po = """msgid ""
msgstr ""
"Language: en\\n"

msgid "New Arrival"
msgstr "New Arrival"

msgid "The Artisan Collection"
msgstr "The Artisan Collection"

msgid "Welcome"
msgstr "Welcome"

msgid "Reviews"
msgstr "Reviews"

msgid "Order Now"
msgstr "Order Now"

msgid "Free Express Shipping"
msgstr "Free Express Shipping"

msgid "Sustainable Materials"
msgstr "Sustainable Materials"

msgid "Authentic Guarantee"
msgstr "Authentic Guarantee"

msgid "Artisanal Craft"
msgstr "Artisanal Craft"

msgid "Each pair is hand-assembled by master shoemakers in our Florence workshop."
msgstr "Each pair is hand-assembled by master shoemakers in our Florence workshop."

msgid "Cloud Cushioning"
msgstr "Cloud Cushioning"

msgid "Proprietary foam technology provides 12-hour comfort without sacrificing style."
msgstr "Proprietary foam technology provides 12-hour comfort without sacrificing style."

msgid "Heritage Design"
msgstr "Heritage Design"

msgid "Inspired by 1970s track spikes, reimagined for the contemporary explorer."
msgstr "Inspired by 1970s track spikes, reimagined for the contemporary explorer."

msgid "The Curator's Voice"
msgstr "The Curator's Voice"

msgid "What our community thinks about this product."
msgstr "What our community thinks about this product."

msgid "Write a Review"
msgstr "Write a Review"

msgid "ago"
msgstr "ago"

msgid "No reviews yet. Be the first to write one!"
msgstr "No reviews yet. Be the first to write one!"

msgid "View All Reviews"
msgstr "View All Reviews"

msgid "Complete the Look"
msgstr "Complete the Look"

msgid "In Stock"
msgstr "In Stock"

msgid "Out of Stock"
msgstr "Out of Stock"

msgid "Stock"
msgstr "Stock"

msgid "Quick Shop"
msgstr "Quick Shop"

msgid "No products found"
msgstr "No products found"

msgid "Try adjusting your filters or check back later"
msgstr "Try adjusting your filters or check back later"

msgid "Select Size (EU)"
msgstr "Select Size (EU)"
"""

# Urdu translations
ur_po = """msgid ""
msgstr ""
"Language: ur\\n"

msgid "New Arrival"
msgstr "نئی آمد"

msgid "The Artisan Collection"
msgstr "کارٹیجین کلیکشن"

msgid "Welcome"
msgid "Reviews"
msgstr "جائزے"

msgid "Order Now"
msgstr "ابھی آرڈر کریں"

msgid "Free Express Shipping"
msgstr "مفت ایکسپریس شپنگ"

msgid "Sustainable Materials"
msgstr "پائیدار مواد"

msgid "Authentic Guarantee"
msgstr "مستند ضمانت"

msgid "Artisanal Craft"
msgstr "دستکاری"

msgid "Each pair is hand-assembled by master shoemakers in our Florence workshop."
msgstr "ہر جوڑا ہمارے فلورنس ورکشاپ میں ماسٹر جوتا سازوں کے ذریعہ ہاتھ سے تیار کیا جاتا ہے۔"

msgid "Cloud Cushioning"
msgstr "کلاؤڈ کشننگ"

msgid "Proprietary foam technology provides 12-hour comfort without sacrificing style."
msgstr "ملکیتی جھاگ ٹیکنالوجی انداز کی قربانی کے بغیر 12 گھنٹے کا آرام فراہم کرتی ہے۔"

msgid "Heritage Design"
msgstr "ورثے کا ڈیزائن"

msgid "Inspired by 1970s track spikes, reimagined for the contemporary explorer."
msgstr "1970 کی دہائی کے ٹریک اسپائکس سے متاثر، عصری متلاشی کے لیے دوبارہ تصور کیا گیا۔"

msgid "The Curator's Voice"
msgstr "کیوریٹر کی آواز"

msgid "What our community thinks about this product."
msgstr "ہماری کمیونٹی اس پروڈکٹ کے بارے میں کیا سوچتی ہے۔"

msgid "Write a Review"
msgstr "جائزہ لکھیں"

msgid "ago"
msgstr "پہلے"

msgid "No reviews yet. Be the first to write one!"
msgstr "ابھی تک کوئی جائزہ نہیں۔ سب سے پہلے لکھنے والے بنیں!"

msgid "View All Reviews"
msgstr "تمام جائزے دیکھیں"

msgid "Complete the Look"
msgstr "ظاہری شکل مکمل کریں"

msgid "In Stock"
msgstr "اسٹاک میں ہے"

msgid "Out of Stock"
msgstr "اسٹاک ختم"

msgid "Stock"
msgstr "اسٹاک"

msgid "Quick Shop"
msgstr "فوری خریداری"

msgid "No products found"
msgstr "کوئی پروڈکٹ نہیں ملی"

msgid "Try adjusting your filters or check back later"
msgstr "اپنے فلٹرز کو ایڈجسٹ کرنے کی کوشش کریں یا بعد میں دوبارہ چیک کریں"

msgid "Select Size (EU)"
msgstr "سائز منتخب کریں (EU)"
"""

# Arabic translations
ar_po = """msgid ""
msgstr ""
"Language: ar\\n"

msgid "New Arrival"
msgstr "وصل حديث"

msgid "The Artisan Collection"
msgstr "مجموعة الحرفيين"

msgid "Welcome"
msgstr "مرحباً"

msgid "Reviews"
msgstr "التقييمات"

msgid "Order Now"
msgstr "اطلب الآن"

msgid "Free Express Shipping"
msgstr "شحن سريع مجاني"

msgid "Sustainable Materials"
msgstr "مواد مستدامة"

msgid "Authentic Guarantee"
msgstr "ضمان أصلي"

msgid "Artisanal Craft"
msgstr "حرفة يدوية"

msgid "Each pair is hand-assembled by master shoemakers in our Florence workshop."
msgstr "يتم تجميع كل زوج يدويًا بواسطة أساتذة صناعة الأحذية في ورشة عملنا في فلورنسا."

msgid "Cloud Cushioning"
msgstr "توسيد سحابي"

msgid "Proprietary foam technology provides 12-hour comfort without sacrificing style."
msgstr "توفر تقنية الرغوة الخاصة راحة لمدة 12 ساعة دون التضحية بالأناقة."

msgid "Heritage Design"
msgstr "تصميم تراثي"

msgid "Inspired by 1970s track spikes, reimagined for the contemporary explorer."
msgstr "مستوحى من مسامير المضمار في سبعينيات القرن الماضي، أعيد تصوره للمستكشف المعاصر."

msgid "The Curator's Voice"
msgstr "صوت المنسق"

msgid "What our community thinks about this product."
msgstr "ما يفكر فيه مجتمعنا حول هذا المنتج."

msgid "Write a Review"
msgstr "اكتب تقييماً"

msgid "ago"
msgstr "منذ"

msgid "No reviews yet. Be the first to write one!"
msgstr "لا توجد تقييمات بعد. كن أول من يكتب تقييماً!"

msgid "View All Reviews"
msgstr "عرض جميع التقييمات"

msgid "Complete the Look"
msgstr "أكمل المظهر"

msgid "In Stock"
msgstr "متوفر"

msgid "Out of Stock"
msgstr "غير متوفر"

msgid "Stock"
msgstr "المخزون"

msgid "Quick Shop"
msgstr "تسوق سريع"

msgid "No products found"
msgstr "لم يتم العثور على منتجات"

msgid "Try adjusting your filters or check back later"
msgstr "حاول تعديل عوامل التصفية أو تحقق لاحقاً"

msgid "Select Size (EU)"
msgstr "اختر المقاس (EU)"
"""

# Write the files
with open('locale/en/LC_MESSAGES/django.po', 'w', encoding='utf-8') as f:
    f.write(en_po)

with open('locale/ur/LC_MESSAGES/django.po', 'w', encoding='utf-8') as f:
    f.write(ur_po)

with open('locale/ar/LC_MESSAGES/django.po', 'w', encoding='utf-8') as f:
    f.write(ar_po)

print("Translation files created successfully!")
print("Now run: python manage.py compilemessages")