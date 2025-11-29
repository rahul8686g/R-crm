# Genie CRM Tech Stack | Genie CRM टेक स्टैक

This document summarizes the application’s backend and frontend technologies in English and Hindi. For each item, Hindi explains how it is used in the app.

## Backend / बैकएंड

- Django 5.2
  - English: Primary web framework (ORM, auth, templates, admin).
  - Hindi: मुख्य वेब फ़्रेमवर्क; ORM, ऑथ, टेम्पलेट्स और एडमिन प्रदान करता है।
  - Reference: `horilla/settings/base.py:50`

- Django REST Framework (DRF)
  - English: Builds REST APIs with serializers, views, and pagination.
  - Hindi: REST API बनाने के लिए सीरियलाइज़र, व्यूज़ और पेजिनेशन का प्रयोग करता है।
  - Reference: `horilla/settings/base.py:70,87–96`

- Simple JWT
  - English: Token-based authentication for APIs.
  - Hindi: API के लिए टोकन आधारित प्रमाणीकरण करता है।
  - Reference: `horilla/settings/base.py:98–101`

- Django Channels + ASGI
  - English: Real-time features over WebSockets.
  - Hindi: रीयल-टाइम WebSocket फीचर्स सक्षम करता है।
  - Reference: `horilla/settings/base.py:62,151,157–165`

- Daphne (dev ASGI server)
  - English: Development ASGI server to run Channels.
  - Hindi: डेवलपमेंट में ASGI सर्वर के रूप में ऐप चलाने के लिए।
  - Reference: `horilla/settings/base.py:58,151`

- Gunicorn (prod WSGI server)
  - English: Production WSGI server for the app.
  - Hindi: प्रोडक्शन में ऐप चलाने के लिए WSGI सर्वर।
  - Reference: `debian/genie-crm.service:17–26`

- Celery + Redis
  - English: Background task processing and results backend.
  - Hindi: बैकग्राउंड टास्क चलाने और रिज़ल्ट स्टोर करने के लिए।
  - Reference: `horilla/settings/base.py:349–355`

- APScheduler
  - English: Scheduled jobs (e.g., mail scheduler).
  - Hindi: निर्धारित समय पर जॉब्स चलाने के लिए (जैसे मेल शेड्यूलर)।
  - Reference: `horilla_mail/scheduler.py` (imported via app config)

- WhiteNoise
  - English: Serves static files efficiently in production.
  - Hindi: प्रोडक्शन में स्टैटिक फाइलें तेज़ी से सर्व करता है।
  - Reference: `horilla/settings/base.py:108,360`

- Django Auditlog
  - English: Tracks model changes for auditing.
  - Hindi: मॉडल में हुए बदलावों का ऑडिट लॉग रखता है।
  - Reference: `horilla/settings/base.py:69,368–373`

- Login History
  - English: Records user login events.
  - Hindi: यूज़र लॉगिन घटनाओं का रिकॉर्ड रखता है।
  - Reference: `horilla/settings/base.py:68`

- django-money
  - English: Money and currency fields for models.
  - Hindi: रुपया/करेंसी फ़ील्ड्स को मॉडल्स में जोड़ता है।
  - Reference: `horilla/settings/base.py:65`

- django-filter
  - English: Declarative filtering for queryset and REST APIs.
  - Hindi: क्वेरीसेट और REST API में फ़िल्टरिंग के लिए।
  - Reference: `horilla/settings/base.py:66`

- django-summernote
  - English: Rich text editor integration.
  - Hindi: रिच टेक्स्ट एडिटर एकीकरण (WYSIWYG)।
  - Reference: `horilla/settings/base.py:67`, `horilla/urls.py:29`

- django-multiselectfield
  - English: Multi-select model field.
  - Hindi: एक फ़ील्ड में बहु-चयन (मल्टी-सेलेक्ट) की सुविधा देता है।
  - Reference: `horilla_core/models.py`

- colorfield
  - English: Color picker field for models.
  - Hindi: रंग चुनने वाले फ़ील्ड्स को मॉडल्स में जोड़ता है।
  - Reference: `horilla/settings/base.py:64`

- django-countries
  - English: Country fields and utilities.
  - Hindi: देश/कंट्री से जुड़े फ़ील्ड्स और यूटिलिटी।
  - Reference: `horilla/settings/base.py`

- django-environ
  - English: Environment variable management.
  - Hindi: `.env` के माध्यम से कॉन्फ़िगरेशन वेरिएबल मैनेज करता है।
  - Reference: `horilla/settings/base.py:16,27–46`

- DRF-YASG (Swagger/OpenAPI)
  - English: Auto-generated API docs and schema.
  - Hindi: API डॉक्यूमेंटेशन और स्कीमा स्वचालित रूप से बनाता है।
  - Reference: `horilla/settings/base.py:72`, `horilla/api_urls.py`

### Database / डेटाबेस

- SQLite (default dev)
  - English: Default development database.
  - Hindi: डेवलपमेंट में डिफ़ॉल्ट डेटाबेस।
  - Reference: `horilla/settings/base.py:178–189`

- PostgreSQL (via `DATABASE_URL`)
  - English: Production-ready DB configuration via environment.
  - Hindi: प्रोडक्शन के लिए वातावरण वेरिएबल के माध्यम से कॉन्फ़िगरेशन।
  - Reference: `horilla/settings/base.py:172–176`

- Connection Persistence
  - English: Long-lived DB connections for performance.
  - Hindi: बेहतर प्रदर्शन के लिए लंबे समय तक जीवित कनेक्शन।
  - Reference: `horilla/settings/base.py:191–193`

## Frontend / फ्रंटएंड

- Django Templates
  - English: Server-side rendered HTML templates.
  - Hindi: सर्वर-साइड HTML टेम्पलेट्स से UI बनता है।
  - Reference: `horilla/settings/base.py:129–148`

- TailwindCSS
  - English: Utility-first CSS framework.
  - Hindi: यूटिलिटी क्लास आधारित CSS फ्रेमवर्क।
  - Reference: `templates/index.html:7`

- HTMX
  - English: Progressive enhancement with AJAX via attributes.
  - Hindi: एट्रिब्यूट्स के ज़रिए AJAX/partial updates देता है।
  - Reference: `templates/index.html:9`

- Flowbite
  - English: Components built on Tailwind.
  - Hindi: टेलविंड पर बने UI कम्पोनेंट्स।
  - Reference: `templates/index.html:10–11`

- Font Awesome
  - English: Icon library.
  - Hindi: आइकन लाइब्रेरी।
  - Reference: `templates/index.html:12`

- jQuery
  - English: DOM helpers and integrations.
  - Hindi: DOM हैंडलिंग और प्लगइन्स के लिए।
  - Reference: `templates/index.html:16,68`

- Select2
  - English: Enhanced select boxes.
  - Hindi: बेहतर सेलेक्ट बॉक्स और सर्च।
  - Reference: `templates/index.html:21–24,70`

- SweetAlert2
  - English: Alerts, modals, toasts.
  - Hindi: अलर्ट/मोडल/टोस्ट UI को सरल बनाता है।
  - Reference: `templates/index.html:25`

- Summernote
  - English: Rich text editor for content.
  - Hindi: कंटेंट एडिटिंग के लिए रिच टेक्स्ट एडिटर।
  - Reference: `templates/index.html:36`

- Animate.css
  - English: CSS animations.
  - Hindi: CSS एनिमेशन के लिए स्टाइल्स।
  - Reference: `templates/index.html:30`

- Hyperscript
  - English: Client-side scripting via micro-syntax.
  - Hindi: हल्के क्लाइंट-साइड स्क्रिप्टिंग के लिए।
  - Reference: `templates/index.html:32`

- SortableJS
  - English: Drag-and-drop list sorting.
  - Hindi: लिस्ट/आइटम्स को ड्रैग-एंड-ड्रॉप से सॉर्ट करता है।
  - Reference: `templates/index.html:33`

- OrgChart.js
  - English: Organizational chart rendering.
  - Hindi: ऑर्गनाइजेशन चार्ट दिखाने के लिए।
  - Reference: `templates/index.html:33`

- ECharts
  - English: Interactive charts.
  - Hindi: इंटरैक्टिव चार्ट्स और ग्राफ।
  - Reference: `templates/index.html:34`

- Project Charts (`assets/js/genie_charts.js`)
  - English: Custom chart helpers and dashboard integrations.
  - Hindi: कस्टम चार्ट हेल्पर्स और डैशबोर्ड इंटीग्रेशन।
  - Reference: `templates/index.html:276`, `horilla_dashboard/templates/home/*:121,161`

## Runtime & URLs / रनटाइम और URLs

- ASGI & WSGI apps
  - English: ASGI for Channels, WSGI for Gunicorn.
  - Hindi: Channels के लिए ASGI, Gunicorn के लिए WSGI।
  - Reference: `horilla/settings/base.py:150–151`, `horilla/wsgi.py:12–16`

- URL routing
  - English: Static, summernote, API, i18n routes.
  - Hindi: स्टैटिक, समरनोट, API और i18n रूट्स।
  - Reference: `horilla/urls.py:25–35`

## Configuration / कॉन्फ़िगरेशन

- Environment variables
  - English: `.env` driven configuration (DEBUG, SECRET_KEY, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS).
  - Hindi: `.env` से कॉन्फ़िगरेशन (DEBUG, SECRET_KEY, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS)।
  - Reference: `horilla/settings/base.py:27–46`

- Static & Media
  - English: Static served via WhiteNoise; media stored under `media/`.
  - Hindi: स्टैटिक WhiteNoise से सर्व; मीडिया `media/` में स्टोर होती है।
  - Reference: `horilla/settings/base.py:357–365`