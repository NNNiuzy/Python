from pygal.maps.world import World

wm = World()
wm.title = 'North, Central, and South America'

# add()接受一个标签和一个列表，其后者包含我们要突出的国家的国别码
# 每次调用add()都将为指定的国家选择一种新颜色，并在图标左边显示该颜色和指定的标签
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('america.svg')
