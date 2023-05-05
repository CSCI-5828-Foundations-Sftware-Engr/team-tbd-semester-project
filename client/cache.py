from flask_caching import Cache

# TODO: Updated 'SimpleCache' to 'simple' to match convention
cache = Cache(config={'CACHE_TYPE': 'simple'})
