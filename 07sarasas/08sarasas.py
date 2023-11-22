cmUgis = [186, 205, 193, 201, 178, 205, 211, 217, 168, 158, 205, 165]
coliUgis =[round(cm / 2.54, 2) for cm in cmUgis]
print(coliUgis)

txtUgis = ['Aukstas' if i >= 180 else 'Vidutinis' if i >= 160 else 'Zemas' for i in cmUgis]
print(txtUgis)