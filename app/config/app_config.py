class AppConfigConstants:
    DEFAULT_PAGE_SIZE = 10
    MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB
    ALLOWED_EXTENSIONS = [".txt", ".pdf", ".docx", ".csv", ".json"]
    TOKEN_EXPIRY_DAYS = 7
    PUBLIC_URL_PREFIXES = [
        "/api/auth/register",
        "/api/auth/login",
        "/api/schema",
        "/api/docs",
        "/api/redoc",
        "/admin",
    ]
