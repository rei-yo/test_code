
import configparser



config = configparser.ConfigParser()
config.read('./dao/config.ini', encoding='utf-8')
print("config read", config.sections())