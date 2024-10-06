from os import getenv

SECRET_KEY = getenv("SECRET_KEY", "071319")


DB_NAME = getenv("DB_NAME", "ssisweb")          
DB_USER = getenv("DB_USER", "root")
DB_PASSWORD = getenv("DB_PASSWORD", "")         
DB_HOST = getenv("DB_HOST", "127.0.0.1")        

# Cloudinary configuration
CLOUDINARY_CLOUD_NAME = getenv("CLOUDINARY_CLOUD_NAME", "dgdcd3h6a")
CLOUDINARY_API_KEY = getenv("CLOUDINARY_API_KEY", "235993918262734")
CLOUDINARY_API_SECRET = getenv("CLOUDINARY_API_SECRET", "SGjalrWwA8ywhxySnxfD3-0pn3U")
