model *putida_core()

  // Compartments and Species:
  compartment c, e;
  species M_2ddg6p_c in c, M_2dhglcn_c in c; # M_2dda7p_c in c, M_34dhbz_c in c
  species M_3dhq_c in c, M_3dhsk_c in c, M_3pg_c in c; # M_6p2dhglcn_c in c
  species M_6pgc_c in c, M_accoa_c in c, M_acon_c in c, M_adp_c in c, M_akg_c in c;
  species M_atp_c in c, M_catechol_c in c, M_ccmuac_c in c, M_cit_c in c;
  species M_co2_c in c, M_co2_e in e, M_coa_c in c, M_dhap_c in c, M_e4p_c in c;
  species M_f6p_c in c, M_fdp_c in c, M_fum_c in c, M_g3p_c in c, M_g6p_c in c;
  species M_glc__D_c in c, M_glc__D_e in e, M_glcn_c in c, M_gln__L_c in c;
  species M_glu__L_c in c, M_glx_c in c, M_h2o_c in c, M_h2o_e in e, M_h_c in c;
  species M_h_e in e, M_hco3_c in c, M_icit_c in c, M_mal__L_c in c, M_nad_c in c;
  species M_nadh_c in c, M_nadp_c in c, M_nadph_c in c, M_nh4_c in c, M_nh4_e in e;
  species M_o2_c in c, M_o2_e in e, M_oaa_c in c, M_pep_c in c, M_pi_c in c;
  species M_pi_e in e, M_pyr_c in c, M_pyr_e in e, M_q8_c in c, M_q8h2_c in c;
  species M_r5p_c in c, M_ru5p__D_c in c, M_s7p_c in c, M_succ_c in c, M_succ_e in e;
  species M_xu5p__D_c in c;

  // Reactions:  
  ext M_ccmuac_c; R_muconate_sink: $M_ccmuac_c => ; e * 1.759/0.4301*(M_ccmuac_c/0.7936)/(1 + M_ccmuac_c/0.9366);
  ext M_co2_e; R_EX_co2_e: $M_co2_e -> ; e * 1.759/0.4301*(M_co2_e/0.7936)/(1 + M_co2_e/0.9366);
  ext M_glc__D_e; R_EX_glc_e: $M_glc__D_e -> ; 0.466*(M_glc__D_e);
  ext M_h2o_e; R_EX_h2o_e: $ M_h2o_e -> ;  0.673*(M_h2o_e);
  ext M_h_e; R_EX_h_e: $M_h_e -> ;  0.371*(M_h_e);
  ext M_nh4_e; R_EX_nh4_e: $M_nh4_e -> ;  0.063*(M_nh4_e);
  ext M_o2_e; R_EX_o2_e: $M_o2_e -> ;  0.3901*(M_o2_e);
  ext M_pi_e; R_EX_pi_e: $M_pi_e -> ;  0.6361*(M_pi_e);
  ext M_pyr_e; R_EX_pyr_e: $M_pyr_e => ;  0.219*(M_pyr_e);
  ext M_succ_e; R_EX_succ_e: $M_succ_e => ;  0.613*(M_succ_e);
  R_NH4t: M_nh4_e -> M_nh4_c; 1.988*(M_nh4_e)-1.242*(M_nh4_c);
  R_CO2t: M_co2_e -> M_co2_c; 1.113*(M_co2_e)-1.835*(M_co2_c);
  R_O2t: M_o2_e -> M_o2_c;  1.671*(M_o2_e)-1.04*(M_o2_c);
  R_H2Ot: M_h2o_e -> M_h2o_c; 1.826*(M_h2o_e)-1.2691*(M_h2o_c);
  R_PIt2r: M_h_e + M_pi_e => M_h_c + M_pi_c;  1.001*(M_h_e)*(M_pi_e)-1.458*(M_h_c)*(M_pi_c);
  R_PYRt2: M_h_e + M_pyr_e -> M_h_c + M_pyr_c;  1.271*(M_h_e)*(M_pyr_e)-1.303*(M_h_c)*(M_pyr_c);
  R_SUCCt2_2: 2 M_h_e + M_succ_e => 2 M_h_c + M_succ_c; 1.943*(pow((M_h_e),2))*(M_succ_e)-1.134*(pow((M_h_c),2))*(M_succ_c);
  R_SUCCt3: M_h_e + M_succ_c => M_h_c + M_succ_e; 1.214*(M_h_e)*(M_succ_c)-1.01*(M_h_c)*(M_succ_e);
  R_THD2: M_h_e + M_nadh_c + M_nadp_c => M_h_c + M_nad_c + M_nadph_c; 1.468*(M_h_e)*(M_nadh_c)*(M_nadp_c)-1.522*(M_h_c)*(M_nad_c)*(M_nadph_c);
  R_ATPM: M_atp_c + M_h2o_c => M_adp_c + M_h_c + M_pi_c;  1.471*(M_atp_c)*(M_h2o_c)-1.06*(M_adp_c)*(M_h_c)*(M_pi_c);
  R_ATPS4r: M_atp_c + M_h2o_c + 3 M_h_c -> M_adp_c + 4 M_h_e + M_pi_c;  1.467*(M_atp_c)*(M_h2o_c)*(pow((M_h_c),3))-1.9529999999999998*(M_adp_c)*(pow((M_h_e),4))*(M_pi_c);
  R_HCO3E: M_h_c + M_hco3_c -> M_co2_c + M_h2o_c; 1.217*(M_h_c)*(M_hco3_c)-1.88*(M_co2_c)*(M_h2o_c);
  R_NADTRHD: M_nad_c + M_nadph_c -> M_nadh_c + M_nadp_c;  1.533*(M_nad_c)*(M_nadph_c)-1.026*(M_nadh_c)*(M_nadp_c);

  R_ACONTa: M_cit_c -> M_acon_c + M_h2o_c;  1.365*(M_cit_c)-1.071*(M_acon_c)*(M_h2o_c);
  R_ACONTb: M_acon_c + M_h2o_c -> M_icit_c; 1.338*(M_acon_c)*(M_h2o_c)-1.035*(M_icit_c);
  R_CATDOX: M_catechol_c + M_o2_c => M_ccmuac_c + 2 M_h_c;  1.509*(M_catechol_c)*(M_o2_c)-1.876*(M_ccmuac_c)*(pow((M_h_c),2));
  R_CS: M_accoa_c + M_h2o_c + M_oaa_c => M_cit_c + M_coa_c + M_h_c; 1.671*(M_accoa_c)*(M_h2o_c)*(M_oaa_c)-1.202*(M_cit_c)*(M_coa_c)*(M_h_c);
  R_CYTBD: 2 M_h_c + 1.5 M_o2_c + M_q8h2_c => M_h2o_c + 2 M_h_e + M_q8_c; 1.767*(pow((M_h_c),2))*(pow((M_o2_c),1.5))*(M_q8h2_c)-1.874*(M_h2o_c)*(pow((M_h_e),2))*(M_q8_c);
  R_DHQTi: M_3dhq_c -> M_3dhsk_c + M_h2o_c; 1.494*(M_3dhq_c)-1.472*(M_3dhsk_c)*(M_h2o_c);
  R_ENO: M_3pg_c -> M_h2o_c + M_pep_c;  1.556*(M_3pg_c)-1.534*(M_h2o_c)*(M_pep_c);
  R_FBA: M_fdp_c -> M_dhap_c + M_g3p_c; 1.191*(M_fdp_c)-1.886*(M_dhap_c)*(M_g3p_c);
  R_FBP: M_fdp_c + M_h2o_c => M_f6p_c + M_pi_c; 1.354*(M_fdp_c)*(M_h2o_c)-1.112*(M_f6p_c)*(M_pi_c);
  R_G6PDH2r: M_g6p_c + M_h2o_c + M_nadp_c => M_6pgc_c + 2 M_h_c + M_nadph_c;  1.504*(M_g6p_c)*(M_h2o_c)*(M_nadp_c)-1.480*(M_6pgc_c)*(pow((M_h_c),2))*(M_nadph_c);
  R_GADktpp: M_glcn_c + M_nad_c => M_2dhglcn_c + M_h_c + M_nadh_c;  1.282*(M_glcn_c)*(M_nad_c)-1.177*(M_2dhglcn_c)*(M_h_c)*(M_nadh_c);
  R_GAPD: M_adp_c + M_g3p_c + M_nad_c + M_pi_c -> M_3pg_c + M_atp_c + M_h_c + M_nadh_c; 1.449*(M_adp_c)*(M_g3p_c)*(M_nad_c)*(M_pi_c)-1.95*(M_3pg_c)*(M_atp_c)*(M_h_c)*(M_nadh_c);
  R_GLCDpp: M_glc__D_c + M_h2o_e + M_q8_c => M_glcn_c + M_h_e + M_q8h2_c; 1.119*(M_glc__D_c)*(M_h2o_e)*(M_q8_c)-1.086*(M_glcn_c)*(M_h_e)*(M_q8h2_c);
  R_GLNS: M_atp_c + M_glu__L_c + M_nh4_c => M_adp_c + M_gln__L_c + M_h_c + M_pi_c;  1.013*(M_atp_c)*(M_glu__L_c)*(M_nh4_c)-1.714*(M_adp_c)*(M_gln__L_c)*(M_h_c)*(M_pi_c);
  R_GLUDy: M_glu__L_c + M_h2o_c + M_nadp_c -> M_akg_c + M_h_c + M_nadph_c + M_nh4_c;  1.9061*(M_glu__L_c)*(M_h2o_c)*(M_nadp_c)-1.581*(M_akg_c)*(M_h_c)*(M_nadph_c)*(M_nh4_c);
  R_GLUN: M_gln__L_c + M_h2o_c => M_glu__L_c + M_nh4_c; 1.708*(M_gln__L_c)*(M_h2o_c)-1.728*(M_glu__L_c)*(M_nh4_c);
  R_GLUSy: M_akg_c + M_gln__L_c + M_h_c + M_nadph_c => 2 M_glu__L_c + M_nadp_c; 1.521*(M_akg_c)*(M_gln__L_c)*(M_h_c)*(M_nadph_c)-1.246*(pow((M_glu__L_c),2))*(M_nadp_c);
  R_GND: M_6pgc_c + M_nadp_c => M_co2_c + M_nadph_c + M_ru5p__D_c;  1.557*(M_6pgc_c)*(M_nadp_c)-1.732*(M_co2_c)*(M_nadph_c)*(M_ru5p__D_c);
  R_GNK: M_atp_c + M_glcn_c => M_6pgc_c + M_adp_c + M_h_c;  1.65*(M_atp_c)*(M_glcn_c)-1.379*(M_6pgc_c)*(M_adp_c)*(M_h_c);
  R_ICDHyr: M_icit_c + M_nadp_c -> M_akg_c + M_co2_c + M_nadph_c; 1.903*(M_icit_c)*(M_nadp_c)-1.422*(M_akg_c)*(M_co2_c)*(M_nadph_c);
  R_KDPGALDOL: M_2ddg6p_c => M_g3p_c + M_pyr_c; 1.837*(M_2ddg6p_c)-1.738*(M_g3p_c)*(M_pyr_c);
  R_MDH: M_mal__L_c + M_nad_c -> M_h_c + M_nadh_c + M_oaa_c;  1.438*(M_mal__L_c)*(M_nad_c)-1.588*(M_h_c)*(M_nadh_c)*(M_oaa_c);
  R_ME1: M_mal__L_c + M_nad_c => M_co2_c + M_nadh_c + M_pyr_c;  1.242*(M_mal__L_c)*(M_nad_c)-1.818*(M_co2_c)*(M_nadh_c)*(M_pyr_c);
  R_ME2: M_mal__L_c + M_nadp_c => M_co2_c + M_nadph_c + M_pyr_c;  1.242*(M_mal__L_c)*(M_nadp_c)-1.818*(M_co2_c)*(M_nadph_c)*(M_pyr_c);
  R_NADH16: 4 M_h_c + M_nadh_c + M_q8_c => 3 M_h_e + M_nad_c + M_q8h2_c;  1.42*(pow((M_h_c),4))*(M_nadh_c)*(M_q8_c)-1.476*(pow((M_h_e),3))*(M_nad_c)*(M_q8h2_c);
  R_PC: M_atp_c + M_hco3_c + M_pyr_c => M_adp_c + M_h_c + M_oaa_c + M_pi_c; 1.779*(M_atp_c)*(M_hco3_c)*(M_pyr_c)-1.564*(M_adp_c)*(M_h_c)*(M_oaa_c)*(M_pi_c);
  R_PDH: M_coa_c + M_nad_c + M_pyr_c -> M_accoa_c + M_co2_c + M_nadh_c; 1.6*(M_coa_c)*(M_nad_c)*(M_pyr_c)-1.984*(M_accoa_c)*(M_co2_c)*(M_nadh_c);
  R_PGI: M_g6p_c -> M_f6p_c;  1.729*(M_g6p_c)-1.915*(M_f6p_c);
  R_PGLUCONDEHYDRAT: M_6pgc_c => M_2ddg6p_c + M_h2o_c;  1.713*(M_6pgc_c)-1.161*(M_2ddg6p_c)*(M_h2o_c);
  R_PPC: M_hco3_c + M_pep_c => M_oaa_c + M_pi_c;  1.08*(M_hco3_c)*(M_pep_c)-1.6802*(M_oaa_c)*(M_pi_c);
  R_PPCK: M_atp_c + M_oaa_c => M_adp_c + M_co2_c + M_pep_c; 1.327*(M_atp_c)*(M_oaa_c)-1.749*(M_adp_c)*(M_co2_c)*(M_pep_c);
  R_PYK: M_adp_c + M_h_c + M_pep_c => M_atp_c + M_pyr_c;  1.1*(M_adp_c)*(M_h_c)*(M_pep_c)-1.908*(M_atp_c)*(M_pyr_c);
  R_RPE: M_ru5p__D_c -> M_xu5p__D_c;  1.776*(M_ru5p__D_c)-1.514*(M_xu5p__D_c);
  R_RPI: M_r5p_c -> M_ru5p__D_c;  1.297*(M_r5p_c)-1.361*(M_ru5p__D_c);
  R_TALA: M_g3p_c + M_s7p_c -> M_e4p_c + M_f6p_c; 1.413*(M_g3p_c)*(M_s7p_c)-1.205*(M_e4p_c)*(M_f6p_c);
  R_TKT1: M_g3p_c + M_s7p_c -> M_r5p_c + M_xu5p__D_c; 1.647*(M_g3p_c)*(M_s7p_c)-1.8052*(M_r5p_c)*(M_xu5p__D_c);
  R_TKT2: M_e4p_c + M_xu5p__D_c -> M_f6p_c + M_g3p_c; 1.517*(M_e4p_c)*(M_xu5p__D_c)-1.7571*(M_f6p_c)*(M_g3p_c);
  R_TPI: M_g3p_c -> M_dhap_c; 1.491*(M_g3p_c)-1.165*(M_dhap_c);
  R_MALS: M_accoa_c + M_glx_c + M_h2o_c => M_coa_c + M_h_c + M_mal__L_c; 1.558*(M_accoa_c)*(M_glx_c)*(M_h2o_c)-1.733*(M_coa_c)*(M_h_c)*(M_mal__L_c)
  R_FUM: M_fum_c + M_h2o_c -> M_mal__L_c; 1.961*(M_fum_c)*(M_h2o_c)-1.078*(M_mal__L_c)

  # THESE ARE THE CONSOLIDATED RXNS BELOW
  # R_GLCabcpp: M_atp_c + M_glc__D_e + M_h2o_c => M_adp_c + M_glc__D_c + M_h_c + M_pi_c;  
  # R_HEX1: M_atp_c + M_glc__D_c => M_adp_c + M_g6p_c + M_h_c;  
  R_GLCabcpp_HEX1: 2 M_atp_c + M_glc__D_e + M_h2o_c => 2 M_adp_c + M_g6p_c + 2 M_h_c + M_pi_c;  1.078*(pow((M_atp_c),2))*(M_glc__D_e)*(M_h2o_c)-1.413*(pow((M_adp_c),2))*(M_g6p_c)*(pow((M_h_c),2))*(M_pi_c);
  # R_2DHGLCK: M_2dhglcn_c + M_atp_c + 2 M_h_c => M_6p2dhglcn_c + M_adp_c;  
  # R_PGLCNDH: M_6p2dhglcn_c + M_nadph_c -> M_6pgc_c + 2 M_h_c + M_nadp_c;  
  R_2DHGLCK_PGLCNDH: M_2dhglcn_c + M_atp_c + M_nadph_c => M_6pgc_c + M_nadp_c + M_adp_c;  1.385*(M_2dhglcn_c)*(M_atp_c)*(M_nadph_c)-1.677*(M_6pgc_c)*(M_nadp_c)*(M_adp_c);
  # R_ICL: M_icit_c -> M_glx_c + M_succ_c;  
  # R_FRD7: M_fum_c + M_q8h2_c -> M_q8_c + M_succ_c;  
  R_ICL_FRD7: M_icit_c + M_q8_c -> M_glx_c + M_fum_c + M_q8h2_c;  1.396*(M_icit_c)*(M_q8_c)-1.173*(M_glx_c)*(M_fum_c)*(M_q8h2_c);
  # R_AKGDH: M_adp_c + M_akg_c + M_nad_c + M_pi_c => M_atp_c + M_co2_c + M_nadh_c + M_succ_c; 
  # R_FRD7: M_fum_c + M_q8h2_c -> M_q8_c + M_succ_c;  
  R_AKGDH_FRD7: M_q8_c + M_adp_c + M_akg_c + M_nad_c + M_pi_c => M_atp_c + M_co2_c + M_nadh_c + M_fum_c + M_q8h2_c; 1.9302*(M_q8_c)*(M_adp_c)*(M_akg_c)*(M_nad_c)*(M_pi_c)-1.396*(M_atp_c)*(M_co2_c)*(M_nadh_c)*(M_fum_c)*(M_q8h2_c);
  # R_DDPA: M_e4p_c + M_h2o_c + M_pep_c -> M_2dda7p_c + M_pi_c; 
  # R_DHQS: M_2dda7p_c => M_3dhq_c + M_pi_c;  
  R_DDPA_DHQS: M_e4p_c + M_h2o_c + M_pep_c -> M_3dhq_c + 2 M_pi_c;  1.548*(M_e4p_c)*(M_h2o_c)*(M_pep_c)-1.710*(M_3dhq_c)*(pow((M_pi_c),2));
  # R_DHSKDH: M_3dhsk_c => M_34dhbz_c + M_h2o_c;  
  # R_PCATDC: M_34dhbz_c + M_h_c -> M_catechol_c + M_co2_c; 
  R_DHSKDH_PCATDC: M_3dhsk_c + M_h_c => M_catechol_c + M_co2_c + M_h2o_c; 1.54*(M_3dhsk_c)*(M_h_c)-1.9181*(M_catechol_c)*(M_co2_c)*(M_h2o_c);

  R_SHIK: M_3dhsk_c + M_nadph_c -> M_shik_c + M_nadp_c; 1.93*(M_3dhsk_c)*(M_nadph_c)-1.76*(M_shik_c)*(M_nadp_c);
  R_SHIK3P: M_shik_c + M_atp_c -> M_adp_c + M_shik3p_c; 1.32*(M_shik_c)*(M_atp_c)-1.47*(M_adp_c)*(M_shik3p_c);
  R_5EPS3P: M_shik3p_c + M_pep_c -> M_5eps3p_c + M_pi_c; 1.12*(M_shik3p_c)*(M_pep_c)-1.05*(M_5eps3p_c)*(M_pi_c);
  R_CHOR: M_5eps3p_c -> M_chor_c + M_pi_c; 1.74*(M_5eps3p_c)-1.60*(M_chor_c)*(M_pi_c);
  R_PAPA: M_chor_c + M_gln__L_c-> M_4a4dch_c + M_glu__L_c; 1.53*(M_chor_c)*(M_gln__L_c)-1.13*(M_4a4dch_c)*(M_glu__L_c);
  R_PAPB: M_4a4dch_c -> M_4a4dpr_c; 1.08*(M_4a4dch_c)-1.44*(M_4a4dpr_c);
  R_PAPC: M_4a4dpr_c + M_nad_c -> M_4aPPA_c + M_nadh_c + M_co2_c + M_h_c; 1.23*(M_4a4dpr_c)*(M_nad_c)-1.75*(M_4aPPA_c)*(M_nadh_c)*(M_co2_c)*(M_h_c);
  R_TYRB: M_4aPPA_c -> M_4aPhe_c; 1.46*(M_4aPPA_c)-1.94*(M_4aPhe_c);
  R_PAL: M_4aPhe_c -> $M_4acinna_c; 1.04*(M_4aPhe_c)-1.05*(M_4acinna_c);

  // Species initializations:
  # M_2dda7p_c  =	0.3839399985	;
  M_2ddg6p_c  =	0.7057897284	;
  M_2dhglcn_c =	0.7367059204	;
  # M_34dhbz_c  =	0.8391326117	;
  M_3dhq_c  =	0.6690307574	;
  M_3dhsk_c =	0.4483794762	;
  M_3pg_c =	0.1791109565	;
  # M_6p2dhglcn_c =	0.4117012427	;
  M_6pgc_c  =	0.5213138195	;
  M_accoa_c =	0.01906305228	;
  M_acon_c  =	0.01868593144	;
  M_adp_c =	0.421901755	;
  M_akg_c =	0.5531344988	;
  M_atp_c =	0.4257262025	;
  M_catechol_c  =	0.0383608419	;
  M_ccmuac_c  =	0.1604952063	;
  M_cit_c =	0.7644601687	;
  M_co2_c =	0.08550737284	;
  M_co2_e =	0.3101432197	;
  M_coa_c =	0.550249993	;
  M_dhap_c  =	0.6794459914	;
  M_e4p_c =	0.9599282675	;
  M_f6p_c =	0.005863482857	;
  M_fdp_c =	0.969583869	;
  M_fum_c =	0.03998545533	;
  M_g3p_c =	0.05478684328	;
  M_g6p_c =	0.2994662107	;
  M_glc__D_c  =	0.04645243764	;
  M_glc__D_e  =	0.9056905778	;
  M_glcn_c  =	0.5546185522	;
  M_gln__L_c  =	0.393592952	;
  M_glu__L_c  =	0.6888715784	;
  M_glx_c =	0.1841600945	;
  M_h2o_c =	0.6750081211	;
  M_h2o_e =	0.6182407343	;
  M_h_c =	0.1975639456	;
  M_h_e =	0.5210584359	;
  M_hco3_c  =	0.9107613345	;
  M_icit_c  =	0.4955700663	;
  M_mal__L_c  =	0.1665700939	;
  M_nad_c =	0.1164424662	;
  M_nadh_c  =	0.7339217238	;
  M_nadp_c  =	0.6424746919	;
  M_nadph_c =	0.01926718312	;
  M_nh4_c =	0.4019365581	;
  M_nh4_e =	0.9528450855	;
  M_o2_c  =	0.3913148877	;
  M_o2_e  =	0.4500891887	;
  M_oaa_c =	0.2127708972	;
  M_pep_c =	0.8820200696	;
  M_pi_c  =	0.0492549438	;
  M_pi_e  =	0.7463446625	;
  M_pyr_c =	0.1193622661	;
  M_pyr_e =	0.1920500933	;
  M_q8_c  =	0.7879344641	;
  M_q8h2_c  =	0.9498789496	;
  M_r5p_c =	0.9450299058	;
  M_ru5p__D_c =	0.810188931	;
  M_s7p_c =	0.2577424753	;
  M_succ_c  =	0.08493027499	;
  M_succ_e  =	0.6896038985	;
  M_xu5p__D_c =	0.5240476197	;
  M_shik_c = 0.21497;
  M_shik3p_c = 0.149122;
  M_5eps3p_c = 0.4912;
  M_chor_c = 0.912280;
  M_4a4dch_c = 0.1228;
  M_4a4dpr_c = 0.22807;
  M_4aPPA_c = 0.28070;
  M_4aPhe_c = 0.80701;
  M_4acinna_c = 0.001000;

  // Compartment initializations:
  c = 1; 
  e = 1;

  // Variable initializations:
  cobra_default_lb = -1000;
  cobra_default_ub = 999999;
  cobra_0_bound = 0;
  minus_inf = -inf;
  plus_inf = inf;
  R_ATPM_lower_bound = 8.39;
  R_ATPM_lower_bound has mmol_per_gDW_per_hr;
  R_EX_glc_e_lower_bound = -7.03;
  R_EX_glc_e_lower_bound has mmol_per_gDW_per_hr;
  R_GLCabcpp_upper_bound = 999999;
  R_GLCabcpp_upper_bound has mmol_per_gDW_per_hr;
  R_GNK_upper_bound = 999999;
  R_GNK_upper_bound has mmol_per_gDW_per_hr;
  R_HEX1_upper_bound = 999999;
  R_HEX1_upper_bound has mmol_per_gDW_per_hr;

  // Other declarations:
  const c, e, cobra_default_lb, cobra_default_ub, cobra_0_bound, minus_inf;
  const plus_inf, R_ATPM_lower_bound, R_EX_glc_e_lower_bound, R_GLCabcpp_upper_bound;
  const R_GNK_upper_bound, R_HEX1_upper_bound;

  // Unit definitions:
  unit mmol_per_gDW_per_hr = 1e-3 mole / (gram * 3600 second);

  // Display Names:
  M_shik_c is "shikimate";
  M_shik3p_c is "shikimate 3-phosphate";
  M_5eps3p_c is "5-enolpyruvylshikimate 3-phosphate";
  M_chor_c is "chorismate";
  M_4a4dch_c is "4-amino-4-deoxychorismate";
  M_4a4dpr_c is "4-amino-4-deoxyprephenate";
  M_4aPPA_c is "4-amino-PPA";
  M_4aPhe_c is "4-aminophenylalanine";
  M_4acinna_c is "4-aminocinnamic acid";
  
  # M_2dda7p_c is "3-deoxy-D-arabino-heptulosonate-7-phosphate";
  M_2ddg6p_c is "2-dehydro-3-deoxy-D-gluconate 6-phosphate";
  M_2dhglcn_c is "2-Dehydro-D-gluconate";
  # M_34dhbz_c is "protocatechuate";
  M_3dhq_c is "3-dehydroquinate";
  M_3dhsk_c is "3-dehydroshikimate";
  M_3pg_c is "3-Phospho-D-glycerate";
  # M_6p2dhglcn_c is "6-Phospho-2-dehydro-D-gluconate";
  M_6pgc_c is "6-Phospho-D-gluconate";
  M_accoa_c is "Acetyl-CoA";
  M_acon_c is "cis-Aconitate";
  M_adp_c is "ADP";
  M_akg_c is "2-Oxoglutarate";
  M_atp_c is "ATP";
  M_catechol_c is "catechol";
  M_ccmuac_c is "cis,cis-muconate";
  M_cit_c is "Citrate";
  M_co2_c is "CO2";
  M_co2_e is "CO2";
  M_coa_c is "Coenzyme A";
  M_dhap_c is "Dihydroxyacetone phosphate";
  M_e4p_c is "D-Erythrose 4-phosphate";
  M_f6p_c is "D-Fructose 6-phosphate";
  M_fdp_c is "D-Fructose 1,6-bisphosphate";
  M_fum_c is "Fumarate";
  M_g3p_c is "Glyceraldehyde 3-phosphate";
  M_g6p_c is "D-Glucose 6-phosphate";
  M_glc__D_c is "D-Glucose";
  M_glc__D_e is "D-Glucose (p)";
  M_glcn_c is "D-Gluconate";
  M_gln__L_c is "L-Glutamine";
  M_glu__L_c is "L-Glutamate";
  M_glx_c is "Glyoxylate";
  M_h2o_c is "H2O";
  M_h2o_e is "H2O";
  M_h_c is "H+";
  M_h_e is "H+";
  M_hco3_c is "hydrogen carbonate";
  M_icit_c is "Isocitrate";
  M_mal__L_c is "L-Malate";
  M_nad_c is "Nicotinamide adenine dinucleotide";
  M_nadh_c is "Nicotinamide adenine dinucleotide - reduced";
  M_nadp_c is "Nicotinamide adenine dinucleotide phosphate";
  M_nadph_c is "Nicotinamide adenine dinucleotide phosphate - reduced";
  M_nh4_c is "Ammonium";
  M_nh4_e is "Ammonium";
  M_o2_c is "O2";
  M_o2_e is "O2";
  M_oaa_c is "Oxaloacetate";
  M_pep_c is "Phosphoenolpyruvate";
  M_pi_c is "Phosphate";
  M_pi_e is "Phosphate";
  M_pyr_c is "Pyruvate";
  M_pyr_e is "Pyruvate";
  M_q8_c is "Ubiquinone-8";
  M_q8h2_c is "Ubiquinol-8";
  M_r5p_c is "alpha-D-Ribose 5-phosphate";
  M_ru5p__D_c is "D-Ribulose 5-phosphate";
  M_s7p_c is "Sedoheptulose 7-phosphate";
  M_succ_c is "Succinate";
  M_succ_e is "Succinate";
  M_xu5p__D_c is "D-Xylulose 5-phosphate";

  # # R_2DHGLCK is "DEHYDOGLUCONOKINASE-RXN"
  # R_DHQTi is "3-DEHYDROQUINATE-DEHYDRATASE-RXN";
  # # R_DHQS is "3-DEHYDROQUINATE-SYNTHASE-RXN";
  # R_ACONTa is "ACONITATEDEHYDR-RXN[CCO-CYTOSOL]-CIT//CIS-ACONITATE/WATER.38.";
  # R_ACONTb is "ACONITATEHYDR-RXN[CCO-CYTOSOL]-CIS-ACONITATE/WATER//THREO-DS-ISO-CITRATE.55.";
  # # R_AKGDH is "2OXOGLUTARATEDEH-RXN";
  # R_ATPM is "ATPASE-RXN";
  # R_ATPS4r is "ATPSYN-RXN[CCO-PM-BAC-NEG]-ATP/PROTON/WATER//ADP/Pi/PROTON.48.";
  # # R_Biomass_Ecoli_core_w_GAM is "Biomass Objective Function with GAM";
  # R_CATDOX is "CATECHOL-12-DIOXYGENASE-RXN";
  # R_CO2t is "TRANS-RXN0-545";
  # R_CS is "RXN-14905";
  # R_CYTBD is "cytochrome oxidase bd (ubiquinol-8: 2 protons)";
  # # R_DDPA is "DAHPSYN-RXN";
  # # R_DHSKDH is "DHSHIKIMATE-DEHYDRO-RXN";
  # R_ENO is "2PGADEHYDRAT-RXN";
  # R_EX_co2_e is "CO2 exchange";
  # R_EX_glc_e is "D-Glucose exchange";
  # R_EX_h2o_e is "H2O exchange";
  # R_EX_h_e is "H+ exchange";
  # R_EX_nh4_e is "Ammonia exchange";
  # R_EX_o2_e is "O2 exchange";
  # R_EX_pi_e is "Phosphate exchange";
  # R_EX_pyr_e is "Pyruvate exchange";
  # R_EX_succ_e is "Succinate exchange";
  # R_FBA is "F16ALDOLASE-RXN";
  # R_FBP is "F16BDEPHOS-RXN[CCO-CYTOSOL]-FRUCTOSE-16-DIPHOSPHATE/WATER//FRUCTOSE-6P/Pi.59.";
  # # R_FRD7 is "R601-RXN[CCO-PM-BAC-NEG]-FUM/REDUCED-MENAQUINONE//SUC/CPD-9728.54.";
  # # R_FUM is "FUMHYDR-RXN[CCO-CYTOSOL]-MAL//FUM/WATER.28.";
  # R_G6PDH2r is "GLU6PDEHYDROG-RXN";
  # R_GADktpp is "1.1.1.215-RXN"
  # R_GAPD is "GAPOXNPHOSPHN-RXN";
  # R_GLCDpp is "Glucose dehydrogenase (ubiquinone-8 as acceptor) (periplasm)";
  # # R_GLCabcpp is "D-glucose transport via ABC system (periplasm)";
  # R_GLNS is "GLUTAMINESYN-RXN";
  # R_GLUDy is "GLUTDEHYD-RXN";
  # R_GLUN is "GLUTAMIN-RXN";
  # R_GLUSy is "GLUTAMATESYN-RXN";
  # R_GND is "RXN-9952";
  # R_GNK is "gluconokinase";
  # R_H2Ot is "TRANS-RXN-145";
  # R_HCO3E is "RXN0-5224";
  # # R_HEX1 is "hexokinase (D-glucose:ATP)";
  # R_ICDHyr is "ISOCITDEH-RXN";
  # # R_ICL is "ISOCIT-CLEAV-RXN";
  # R_KDPGALDOL is "KDPGALDOL-RXN";
  # # R_MALS is "MALSYN-RXN";
  # R_MDH is "MALATE-DEH-RXN[CCO-CYTOSOL]-MAL/NAD//OXALACETIC_ACID/NADH/PROTON.50.";
  # # R_ME1 is "1.1.1.39-RXN";
  # R_ME2 is "MALIC-NADP-RXN";
  # R_NADH16 is "NADH dehydrogenase (ubiquinone-8 & 3 protons)";
  # R_NADTRHD is "PYRNUTRANSHYDROGEN-RXN";
  # R_NH4t is "TRANS-RXN0-206";
  # R_O2t is "TRANS-RXN0-474";
  # R_PC is "PYRUVATE-CARBOXYLASE-RXN";
  # R_PDH is "PYRUVDEH-RXN";
  # R_PGI is "PGLUCISOM-RXN";
  # # R_PGLCNDH is "1.1.1.43-RXN"
  # R_PGLUCONDEHYDRAT is "PGLUCONDEHYDRAT-RXN";
  # R_PIt2r is "TRANS-RXN-114";
  # R_PPC is "PEPCARBOX-RXN";
  # R_PPCK is "PEPCARBOXYKIN-RXN";
  # # R_PCATDC is "PROTOCATECHUATE-DECARBOXYLASE-RXN";
  # R_PYK is "PEPDEPHOS-RXN";
  # R_PYRt2 is "R_eyruvate_transport_in_via_eroton_symport";
  # R_RPE is "RIBULP3EPIM-RXN";
  # R_RPI is "RIB5PISOM-RXN";
  # R_SUCCt2_2 is "TRANS-RXN-121";
  # R_SUCCt3 is "succinate transport out via proton antiport";
  # R_TALA is "TRANSALDOL-RXN";
  # R_THD2 is "TRANS-RXN0-277";
  # R_TKT1 is "1TRANSKETO-RXN";
  # R_TKT2 is "2TRANSKETO-RXN";
  # R_TPI is "TRIOSEPISOMERIZATION-RXN";
  # R_muconate_sink is "muconate_sink";

  # R_GLCabcpp_HEX1 is "GLCabcpp_HEX1";
  # R_2DHGLCK_PGLCNDH is "2DHGLCK_PGLCNDH"; 
  # R_ICL_FRD7 is "ICL_FRD7"; 
  # R_AKGDH_FRD7 is "AKGDH_FRD7"; 
  # R_MALS_ME1 is "MALS_ME1"; 
  # R_FUM_ME1 is "FUM_ME1";
  # R_DDPA_DHQS is "DDPA_DHQS";
  # R_DHSKDH_PCATDC is "DHSKDH_PCATDC";



  // SBO terms:
  cobra_default_lb.sboTerm = 626
  cobra_default_ub.sboTerm = 626
  cobra_0_bound.sboTerm = 626
  minus_inf.sboTerm = 625
  plus_inf.sboTerm = 625
  R_ATPM_lower_bound.sboTerm = 625
  R_EX_glc_e_lower_bound.sboTerm = 625
  R_GLCabcpp_upper_bound.sboTerm = 625
  R_GNK_upper_bound.sboTerm = 625
  R_HEX1_upper_bound.sboTerm = 625

end