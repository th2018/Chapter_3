import arcpy
arcpy.Intersect_analysis(["bas_nonref_WestMnts","mtbs_perims_DD"],"West_Mnts_mtbs")
arcpy.management.AddField("West_Mnts_mtbs","area_ratio","FLOAT")
arcpy.CalculateField_management("West_Mnts_mtbs","area_ratio",'!Shape_Area! / !AREA!',"PYTHON")

