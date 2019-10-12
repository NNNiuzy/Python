import pygal.maps.world

# pygal.i18n已不被遗弃
# pygal两位国别码列表表示法：pygal.maps.world.COUNTRIES.items()


for code, name in pygal.maps.world.COUNTRIES.items():
    print(code, name)
