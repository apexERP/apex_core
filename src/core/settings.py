from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(v6+20k&a^k@ldn780%#c+lf4*5h%4pyo$5f)d%()i$y34atk4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    "*",
]

# Application definition

INSTALLED_APPS = [
    # jazzmin configuration
    "jazzmin",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # third party applications
    'rest_framework',
    
    # local applications
    'apps.landing',
    'apps.users',
    "apps.orders",
    'apps.tenants',
    'apps.module',
    'apps.payments',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Custom User authentication
AUTH_USER_MODEL = 'users.Users'




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static", 
]



# ========================
# Jazzmin Configuration
# ========================

JAZZMIN_SETTINGS = {
    # Title of the window
    "site_title": "apex ERP Admin",

    # Title on the login screen (19 chars max)
    "site_header": "apex ERP",

    # Title on the brand (19 chars max)
    "site_brand": "apex ERP",

    # Logo to use for your site (Points directly to your static/logo/ folder)
    "site_logo": "logo/apex_logo_64x64.png",

    # Logo to use for your site, used for login form logo
    "login_logo": True,

    # Logo to use for login form in dark themes
    "login_logo_dark": True,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site
    "site_icon": "logo/apex_logo_64x64.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to apex ERP Control Center",

    # Copyright on the footer
    "copyright": "apexERP Ltd",

    # List of model admins to search from the top search bar (Fixed string casings)
    "search_model": ["tenants.Tenants", "users.Users"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Tenants Directory", "model": "tenants.Tenants"},
        {"name": "Modules", "model": "module.Module"},
        {"name": "Users", "model": "users.Users"},
        {"name": "Payments", "model": "payments.Payments"},
        {"name": "Orders", "model": "orders.Orders"},
        {"name": "Device Logs", "model": "landing.DeviceLog"},
        {"name": "Tenant Payments", "model": "payments.TenantPayments"},
        # {"name": "Support System", "url": "https://support.apexerp.com", "new_window": True},
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to auto expand the menu
    "navigation_expanded": True,

    "hide_apps": [],

    # Hide these models when generating side menu
    "hide_models": [],

    # Order your nested apps and models logically according to your folder labels
    "order_with_respect_to": [
        "tenants",
        "tenants.Tenants",
        "tenants.TenantModules",
        "module",
        "module.Module",
        "module.ModulePrice",
        "orders",
        "payments",
        "users",
        "users.Users",
        "auth",
        "auth.Group",
        "landing",
        "landing.DeviceLog",
        "payments",
        "payments.TenantPayments",
    ],

    # Custom icons for side menu apps/models (FontAwesome 5 free icons)
    "icons": {
        # App-level icons
        "auth": "fas fa-shield-alt",
        "tenants": "fas fa-cubes",
        "module": "fas fa-puzzle-piece",
        "orders": "fas fa-shopping-cart",
        "payments": "fas fa-credit-card",
        "users": "fas fa-users-cog",

        # Model-level icons (Matching your exact lower/upper combinations)
        "auth.Group": "fas fa-users",
        "tenants.Tenants": "fas fa-building",
        "tenants.TenantModules": "fas fa-toggle-on",
        "module.Module": "fas fa-box-open",
        "module.ModulePrice": "fas fa-tags",
        "users.Users": "fas fa-user-shield",
        "orders.Orders": "fas fa-file-invoice-dollar",
        "payments.Payments": "fas fa-money-bill-wave",
        "landing": "fas fa-satellite-dish",
        "landing.DeviceLog": "fas fa-desktop",
    },
    
    # Icons used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups for a cleaner, modern SPA feel
    "related_modal_active": True,

    #############
    # UI Tweaks #
    #############
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Format overrides to fit your data layout styles
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "users.Users": "collapsible",
        "auth.group": "vertical_tabs",
        "tenants.Tenants": "horizontal_tabs",
    },
    "language_chooser": False,
}