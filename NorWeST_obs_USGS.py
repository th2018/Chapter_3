import arcpy
arcpy.SelectLayerByAttribute_management("S_USA.NorWeST_TemperaturePoints","NEW_SELECTION","SOURCE LIKE 'USGS%'")
arcpy.FeatureClassToFeatureClass_conversion("S_USA.NorWeST_TemperaturePoints",r"C:\Users\taohuang\Documents\Tao\Data\norwest","S_USA.NorWeST_TemperaturePoints_USGS")

