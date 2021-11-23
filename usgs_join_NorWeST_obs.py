import arcpy
arcpy.SpatialJoin_analysis("usgs_wt_ID_10m_NorWeST_obs","S_USA","usgs_join_NorWeST_obs","JOIN_ONE_TO_ONE","KEEP_ALL","#","CLOSEST")

