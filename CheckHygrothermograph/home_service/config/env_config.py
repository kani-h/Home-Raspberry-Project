class Config:
    PROTOCOL = 'http'
    HOST = 'localhost'
    PORT = '8080'
    BASE_PATH = '/'


class LocalConfig(Config):
    PROTOCOL = 'http'
    HOST = 'localhost'
    PORT = '8080'
    BASE_PATH = '/'


class DevelopmentConfig(Config):
    PROTOCOL = 'http'
    HOST = '192.168.1.46'
    PORT = '8080'
    BASE_PATH = '/'


class ProductionConfig(Config):
    PROTOCOL = 'http'
    HOST = 'localhost'
    PORT = '8080'
    BASE_PATH = '/'
