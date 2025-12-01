# Genie CRM उपयोग निर्देश (हिंदी)

यह गाइड स्टेप-बाय-स्टेप बताती है कि ऐप को कैसे बिल्ड करें, साइन-इन/साइन-अप कैसे करें, यूज़र/एडमिन के रूप में लॉगिन कैसे करें, और रोल्स/परमिशन का उपयोग कैसे करें।

## आवश्यकताएँ
- `Python 3.12+`, `pip`
- वैकल्पिक: `Docker` और `Docker Compose`
- डेटाबेस: डेवलपमेंट के लिए `SQLite` (डिफ़ॉल्ट), प्रोडक्शन के लिए `PostgreSQL`

## बिल्ड और रन (लोकल)
- डिपेंडेंसी इंस्टॉल: `pip install -r requirements.txt`
- माइग्रेशन चलाएँ: `python manage.py migrate`
- सुपरयूज़र बनाएँ: `python manage.py createsuperuser`
- सर्वर स्टार्ट: `python manage.py runserver`
- ब्राउज़र खोलें: `http://localhost:8000`

सभी सेटिंग्स `genie/settings/base.py:21–47` में `.env` से नियंत्रित होती हैं।

## बिल्ड और रन (Docker)
- `.env` कॉन्फ़िगर करें: `cp .env.example .env`
- डेवलपमेंट: `docker-compose up --build`
- प्रोडक्शन: `docker-compose --profile production up --build -d`
- सुपरयूज़र: कंटेनर शेल में `python manage.py createsuperuser`
- एक्सेस: `http://localhost:8000` (dev), `http://localhost` (prod with nginx)

## साइन-इन (Login)
- लॉगिन पेज: `GET /login` → टेम्पलेट `templates/login.html`
- दो तरीके सपोर्टेड हैं (`genie_core/views.py:185–205`):
  - ईमेल + फोन नंबर
  - यूज़रनेम + पासवर्ड
- सफल लॉगिन पर रीडायरेक्ट: `DEFAULT_HOME_REDIRECT` (`genie/settings/base.py:347`)

## साइन-अप (पहली बार सेटअप)
जब डेटाबेस में कोई यूज़र नहीं होता, तो ऐप “Initialize Database” फ्लो दिखाता है:
- स्टेप 1: DB पासवर्ड पेज `GET /initialize-database` (`genie_core/urls.py:785–788`)
- स्टेप 2: साइन-अप पेज `GET /initialize-database-user` → टेम्पलेट `genie_core/templates/initialize_database/sign_up.html` (`genie_core/initialiaze_database.py:47–60`)
- स्टेप 3: कंपनी बनाना `GET /initialize-database-company` (`genie_core/initialiaze_database.py:84–94`)
- स्टेप 4: रोल सेटअप `GET /initialize-database-role`

DB पासवर्ड (`genie/settings/base.py:376–378`) डिफ़ॉल्ट: `DB_INIT_PASSWORD` — इसे `.env` में बदल सकते हैं।

साइन-अप सबमिट करने पर पहला यूज़र `is_superuser=True` और `is_staff=True` सेट होता है (`genie_core/initialiaze_database.py:121–138`)।

## एडमिन के रूप में लॉगिन
- अगर आपने `createsuperuser` चलाया है, उसी क्रेडेंशियल्स से `/login` पर लॉगिन करें।
- अगर “Initialize Database” फ्लो से साइन-अप किया है, वही यूज़र एडमिन होगा।

## सामान्य यूज़र लॉगिन
- एडमिन UI से नया यूज़र बनाएँ: `Users → Create` (`genie_core/urls.py:218–224`)
- या API से यूज़र क्रिएट करें (DRF): `POST /core/users/`
- यूज़र `/login` से अपने क्रेडेंशियल्स के साथ लॉगिन कर सकता है।

## रोल्स और परमिशन
- रोल मैनेजमेंट: `Roles` व्यू और संबंधित URLs (`genie_core/urls.py:261–297`)
- रोल में यूज़र जोड़ना/देखना: `AddUserToRole`, `UsersInRole`
- परमिशन स्क्रीन: `Groups and Permissions` सेक्शन (`genie_core/urls.py:637–783`)
- फील्ड-लेवल परमिशन भी उपलब्ध हैं।

## मल्टी-लैंग्वेज और रीजनल सेटिंग्स
- सपोर्टेड लैंग्वेज: `genie/settings/base.py:218–315`
- यूज़र/कंपनी के लिए भाषा/टाइम ज़ोन/करेंसी सेटिंग: `genie_core/models.py:823–876`, `94–166`
- भाषा कुकी और लोकेल पाथ: `genie/settings/base.py:323–333`

## पासवर्ड संबंधित फीचर्स
- “Forgot Password” UI: `GET /forgot-password` (`genie_core/urls.py:814`)
- पासवर्ड रीसेट लिंक्स: `GET /reset-password/<uidb64>/<token>/` (`genie_core/urls.py:816–819`)
- पासवर्ड बदलना: `GET /change-password-view` और `POST /change-password-form` (`genie_core/urls.py:821–829`)

## मीडिया/स्टैटिक एक्सेस नियम
- स्टैटिक: WhiteNoise (`genie/settings/base.py:357–365`)
- प्रोटेक्टेड मीडिया: `GET /media/<path>` एक्सेस नियम (`genie_core/views.py:75–115`)
- कुछ पब्लिक पेजों से मीडिया एक्सेस की अनुमति, अन्यथा लॉगिन आवश्यक।

## रियल-टाइम फीचर्स
- Channels/ASGI सक्षम हैं (`genie/settings/base.py:151–165`)
- डेवलपमेंट सर्वर: `Daphne` (`runserver` आउटपुट)
- प्रोडक्शन स्केलिंग के लिए `Redis` (`README.md:195–206`)

## API डॉक्युमेंटेशन
- Swagger/OpenAPI: DRF-YASG सक्षम (`genie/settings/base.py:72`, `genie/api_urls.py`)
- बेस पाथ: `GET /core/` (एप नाम `horilla_core_api`)

## टिप्स
- `ALLOWED_HOSTS` और `CSRF_TRUSTED_ORIGINS` `.env` में सेट करें (`genie/settings/base.py:31–46`)
- पहली कंपनी बनाते समय वही डिफ़ॉल्ट कंपनी बनती है और करेंसी सेटअप के साथ मल्टी-करेंसी नियम लागू होते हैं (`genie_core/models.py:211–257`)