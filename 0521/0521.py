ubike=iface.addVectorLayer(r"D:\QGIS3.12\QGIS 3.4\黃饕上課\B190010171V013.shp",'ubike','ogr')
#iface.showAttributeTable(ubike)

# field = shp的columns name
for field in ubike.fields():
    print(field.name())
    print(field.precision())
    print(field.name(),"is",field.typeName())
    
ubike.featureCount() # 有幾個點
ubike.selectedFeatureCount () # 選了幾個點
ubike.selectByExpression('"Lat" >23.5') # 注意冒號
