ATLAS='DK'

INPUT_FILE='/data/vision/polina/users/razvan/research/brain-coloring-website/static/generated/385B81CB7778C9BF/385B81CB7778C9BF_DK_template.csv'

OUTPUT_FOLDER = '../generated/385B81CB7778C9BF'

BRAIN_TYPE = 'pial'

IMG_TYPE = 'cortical-inner'

COLORS_RGB = [(1.0, 1.0, 1.0), (1.0, 1.0, 0.0), (1.0, 0.5, 0.0), (1.0, 0.0, 0.0)]

RESOLUTION = (1200, 900)

BACKGROUND_COLOR = (1.0, 1.0, 1.0)

cortAreasIndexMapDK = {'bankssts': 'bankssts', 'caudalanteriorcingulate': 'caudalanteriorcingulate', 'caudalmiddlefrontal': 'caudalmiddlefrontal', 'cuneus': 'cuneus', 'entorhinal': 'entorhinal', 'frontalpole': 'frontalpole', 'fusiform': 'fusiform', 'inferiorparietal': 'inferiorparietal', 'inferiortemporal': 'inferiortemporal', 'insula': 'insula', 'isthmuscingulate': 'isthmuscingulate', 'lateraloccipital': 'lateraloccipital', 'lateralorbitofrontal': 'lateralorbitofrontal', 'lingual': 'lingual', 'medialorbitofrontal': 'medialorbitofrontal', 'middletemporal': 'middletemporal', 'paracentral': 'paracentral', 'parahippocampal': 'parahippocampal', 'parsopercularis': 'parsopercularis', 'parsorbitalis': 'parsorbitalis', 'parstriangularis': 'parstriangularis', 'pericalcarine': 'pericalcarine', 'postcentral': 'postcentral', 'posteriorcingulate': 'posteriorcingulate', 'precentral': 'precentral', 'precuneus': 'precuneus', 'rostralanteriorcingulate': 'rostralanteriorcingulate', 'rostralmiddlefrontal': 'rostralmiddlefrontal', 'superiorfrontal': 'superiorfrontal', 'superiorparietal': 'superiorparietal', 'superiortemporal': 'superiortemporal', 'supramarginal': 'supramarginal', 'temporalpole': 'temporalpole', 'transversetemporal': 'transversetemporal', 'unknown': -1}

cortAreasIndexMapDestrieux = {'G_Ins_lg_and_S_cent_ins': 'G_Ins_lg_and_S_cent_ins', 'G_and_S_cingul-Ant': 'G_and_S_cingul-Ant', 'G_and_S_cingul-Mid-Ant': 'G_and_S_cingul-Mid-Ant', 'G_and_S_cingul-Mid-Post': 'G_and_S_cingul-Mid-Post', 'G_and_S_frontomargin': 'G_and_S_frontomargin', 'G_and_S_occipital_inf': 'G_and_S_occipital_inf', 'G_and_S_paracentral': 'G_and_S_paracentral', 'G_and_S_subcentral': 'G_and_S_subcentral', 'G_and_S_transv_frontopol': 'G_and_S_transv_frontopol', 'G_cingul-Post-dorsal': 'G_cingul-Post-dorsal', 'G_cingul-Post-ventral': 'G_cingul-Post-ventral', 'G_cuneus': 'G_cuneus', 'G_front_inf-Opercular': 'G_front_inf-Opercular', 'G_front_inf-Orbital': 'G_front_inf-Orbital', 'G_front_inf-Triangul': 'G_front_inf-Triangul', 'G_front_middle': 'G_front_middle', 'G_front_sup': 'G_front_sup', 'G_insular_short': 'G_insular_short', 'G_oc-temp_lat-fusifor': 'G_oc-temp_lat-fusifor', 'G_oc-temp_med-Lingual': 'G_oc-temp_med-Lingual', 'G_oc-temp_med-Parahip': 'G_oc-temp_med-Parahip', 'G_occipital_middle': 'G_occipital_middle', 'G_occipital_sup': 'G_occipital_sup', 'G_orbital': 'G_orbital', 'G_pariet_inf-Angular': 'G_pariet_inf-Angular', 'G_pariet_inf-Supramar': 'G_pariet_inf-Supramar', 'G_parietal_sup': 'G_parietal_sup', 'G_postcentral': 'G_postcentral', 'G_precentral': 'G_precentral', 'G_precuneus': 'G_precuneus', 'G_rectus': 'G_rectus', 'G_subcallosal': 'G_subcallosal', 'G_temp_sup-G_T_transv': 'G_temp_sup-G_T_transv', 'G_temp_sup-Lateral': 'G_temp_sup-Lateral', 'G_temp_sup-Plan_polar': 'G_temp_sup-Plan_polar', 'G_temp_sup-Plan_tempo': 'G_temp_sup-Plan_tempo', 'G_temporal_inf': 'G_temporal_inf', 'G_temporal_middle': 'G_temporal_middle', 'Lat_Fis-ant-Horizont': 'Lat_Fis-ant-Horizont', 'Lat_Fis-ant-Vertical': 'Lat_Fis-ant-Vertical', 'Lat_Fis-post': 'Lat_Fis-post', 'Pole_occipital': 'Pole_occipital', 'Pole_temporal': 'Pole_temporal', 'S_calcarine': 'S_calcarine', 'S_central': 'S_central', 'S_cingul-Marginalis': 'S_cingul-Marginalis', 'S_circular_insula_ant': 'S_circular_insula_ant', 'S_circular_insula_inf': 'S_circular_insula_inf', 'S_circular_insula_sup': 'S_circular_insula_sup', 'S_collat_transv_ant': 'S_collat_transv_ant', 'S_collat_transv_post': 'S_collat_transv_post', 'S_front_inf': 'S_front_inf', 'S_front_middle': 'S_front_middle', 'S_front_sup': 'S_front_sup', 'S_interm_prim-Jensen': 'S_interm_prim-Jensen', 'S_intrapariet_and_P_trans': 'S_intrapariet_and_P_trans', 'S_oc-temp_lat': 'S_oc-temp_lat', 'S_oc-temp_med_and_Lingual': 'S_oc-temp_med_and_Lingual', 'S_oc_middle_and_Lunatus': 'S_oc_middle_and_Lunatus', 'S_oc_sup_and_transversal': 'S_oc_sup_and_transversal', 'S_occipital_ant': 'S_occipital_ant', 'S_orbital-H_Shaped': 'S_orbital-H_Shaped', 'S_orbital_lateral': 'S_orbital_lateral', 'S_orbital_med-olfact': 'S_orbital_med-olfact', 'S_parieto_occipital': 'S_parieto_occipital', 'S_pericallosal': 'S_pericallosal', 'S_postcentral': 'S_postcentral', 'S_precentral-inf-part': 'S_precentral-inf-part', 'S_precentral-sup-part': 'S_precentral-sup-part', 'S_suborbital': 'S_suborbital', 'S_subparietal': 'S_subparietal', 'S_temporal_inf': 'S_temporal_inf', 'S_temporal_sup': 'S_temporal_sup', 'S_temporal_transverse': 'S_temporal_transverse', 'Unknown': 'Unknown'}

cortAreasIndexMapTourville = {'caudalanteriorcingulate': 'caudalanteriorcingulate', 'caudalmiddlefrontal': 'caudalmiddlefrontal', 'cuneus': 'cuneus', 'entorhinal': 'entorhinal', 'fusiform': 'fusiform', 'inferiorparietal': 'inferiorparietal', 'inferiortemporal': 'inferiortemporal', 'insula': 'insula', 'isthmuscingulate': 'isthmuscingulate', 'lateraloccipital': 'lateraloccipital', 'lateralorbitofrontal': 'lateralorbitofrontal', 'lingual': 'lingual', 'medialorbitofrontal': 'medialorbitofrontal', 'middletemporal': 'middletemporal', 'paracentral': 'paracentral', 'parahippocampal': 'parahippocampal', 'parsopercularis': 'parsopercularis', 'parsorbitalis': 'parsorbitalis', 'parstriangularis': 'parstriangularis', 'pericalcarine': 'pericalcarine', 'postcentral': 'postcentral', 'posteriorcingulate': 'posteriorcingulate', 'precentral': 'precentral', 'precuneus': 'precuneus', 'rostralanteriorcingulate': 'rostralanteriorcingulate', 'rostralmiddlefrontal': 'rostralmiddlefrontal', 'superiorfrontal': 'superiorfrontal', 'superiorparietal': 'superiorparietal', 'superiortemporal': 'superiortemporal', 'supramarginal': 'supramarginal', 'transversetemporal': 'transversetemporal', 'unknown': 'unknown'}

subcortAreasIndexMap = {'Left-Accumbens-area': 'Accumbens-area', 'Left-Caudate': 'Caudate', 'Left-Cerebellum-White-Matter': 'Cerebellum-White-Matter', 'Left-Inf-Lat-Vent': 'Inf-Lat-Vent', 'Left-Pallidum': 'Pallidum', 'Left-Thalamus-Proper': 'Thalamus-Proper', 'Left-Amygdala': 'Amygdala', 'Left-Cerebellum-Cortex': 'Cerebellum-Cortex', 'Left-Hippocampus': 'Hippocampus', 'Left-Lateral-Ventricle': 'Lateral-Ventricle', 'Left-Putamen': 'Putamen', 'Left-VentralDC': 'VentralDC'}

