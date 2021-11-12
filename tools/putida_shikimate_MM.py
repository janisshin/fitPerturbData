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
  ext M_ccmuac_c; R_muconate_sink: $M_ccmuac_c => ;e1 * 0.1046/0.4244 * (($M_ccmuac_c))/(1 + ($M_ccmuac_c) / 0.4244);
  ext M_co2_e; R_EX_co2_e: $M_co2_e -> ; e2 * 0.6535/0.2146 * (($M_co2_e))/(1 + ($M_co2_e) / 0.2146);
  ext M_glc__D_e; R_EX_glc_e: $M_glc__D_e -> ; e3 * 0.3112/0.2597 * (($M_glc__D_e))/(1 + ($M_glc__D_e) / 0.2597);
  ext M_h2o_e; R_EX_h2o_e: $ M_h2o_e -> ;  e4* 0.2097/0.5035 * ((M_h2o_e))/(1 + (M_h2o_e) / 0.5035);
  ext M_h_e; R_EX_h_e: $M_h_e -> ; e5 * 0.9946/0.4899 * (($M_h_e))/(1 + ($M_h_e) / 0.4899);
  ext M_nh4_e; R_EX_nh4_e: $M_nh4_e -> ; e6 * 0.07/0.0938 * (($M_nh4_e))/(1 + ($M_nh4_e) / 0.0938);
  ext M_o2_e; R_EX_o2_e: $M_o2_e -> ; e7 * 0.5983/0.0218 * (($M_o2_e))/(1 + ($M_o2_e) / 0.0218);
  ext M_pi_e; R_EX_pi_e: $M_pi_e -> ; e8 * 0.1198/0.5196 * (($M_pi_e))/(1 + ($M_pi_e) / 0.5196);
  ext M_pyr_e; R_EX_pyr_e: $M_pyr_e => ; e9 * 0.5354/0.5675 * (($M_pyr_e))/(1 + ($M_pyr_e) / 0.5675);
  ext M_succ_e; R_EX_succ_e: $M_succ_e => ; e10 * 0.1492/0.9166 * (($M_succ_e))/(1 + ($M_succ_e) / 0.9166);
  R_NH4t: M_nh4_e -> M_nh4_c;e11 * 0.0413/0.7462 * ((M_nh4_e) - (M_nh4_c) / 0.7439)/(1 + (M_nh4_e) / 0.7462 + (M_nh4_c) / 0.7517);
  R_CO2t: M_co2_e -> M_co2_c;e12 * 0.6421/0.4936 * ((M_co2_e) - (M_co2_c) / 0.8807)/(1 + (M_co2_e) / 0.4936 + (M_co2_c) / 0.357);
  R_O2t: M_o2_e -> M_o2_c;  e13 * 0.0159/0.2816 * ((M_o2_e) - (M_o2_c) / 0.2778)/(1 + (M_o2_e) / 0.2816 + (M_o2_c) / 0.8453);
  R_H2Ot: M_h2o_e -> M_h2o_c;e14 * 0.575/0.3267 * ((M_h2o_e) - (M_h2o_c) / 0.7922)/(1 + (M_h2o_e) / 0.3267 + (M_h2o_c) / 0.7097);
  R_PIt2r: M_h_e + M_pi_e => M_h_c + M_pi_c; e15 * 0.0799/0.1159 * ((M_h_e)(M_pi_e) - (M_h_c)(M_pi_c) / 0.8695)/(1 + (M_h_e)(M_pi_e) / 0.1159 + (M_h_c)(M_pi_c) / 0.0466);
  R_PYRt2: M_h_e + M_pyr_e -> M_h_c + M_pyr_c;e16 * 0.1042/0.5141 * ((M_h_e)(M_pyr_e) - (M_h_c)(M_pyr_c) / 0.4186)/(1 + (M_h_e)(M_pyr_e) / 0.5141 + (M_h_c)(M_pyr_c) / 0.6135);
  R_SUCCt2_2: 2 M_h_e + M_succ_e => 2 M_h_c + M_succ_c;e17 * 0.598/0.3769 * ((pow((M_h_e),2))(M_succ_e) - (pow((M_h_c),2))(M_succ_c) / 0.2316)/(1 + (pow((M_h_e),2))(M_succ_e) / 0.3769 + (pow((M_h_c),2))(M_succ_c) / 0.0332);
  R_SUCCt3: M_h_e + M_succ_c => M_h_c + M_succ_e; e18 * 0.0974/0.3294 * ((M_h_e)(M_succ_c) - (M_h_c)(M_succ_e) / 0.9738)/(1 + (M_h_e)(M_succ_c) / 0.3294 + (M_h_c)(M_succ_e) / 0.0292);
  R_THD2: M_h_e + M_nadh_c + M_nadp_c => M_h_c + M_nad_c + M_nadph_c; e19 * 0.468/0.7787 * ((M_h_e)(M_nadh_c)(M_nadp_c) - (M_h_c)(M_nad_c)(M_nadph_c) / 0.2627)/(1 + (M_h_e)(M_nadh_c)(M_nadp_c) / 0.7787 + (M_h_c)(M_nad_c)(M_nadph_c) / 0.8063);
  R_ATPM: M_atp_c + M_h2o_c => M_adp_c + M_h_c + M_pi_c; e20 * 0.1889/0.7242 * ((M_atp_c)(M_h2o_c) - (M_adp_c)(M_h_c)(M_pi_c) / 0.9278)/(1 + (M_atp_c)(M_h2o_c) / 0.7242 + (M_adp_c)(M_h_c)(M_pi_c) / 0.3979);
  R_ATPS4r: M_atp_c + M_h2o_c + 3 M_h_c -> M_adp_c + 4 M_h_e + M_pi_c;e21 * 0.3216/0.4448 * ((M_atp_c)(M_h2o_c)(pow((M_h_c),3)) - (M_adp_c)(pow((M_h_e),4))(M_pi_c) / 0.2215)/(1 + (M_atp_c)(M_h2o_c)(pow((M_h_c),3)) / 0.4448 + (M_adp_c)(pow((M_h_e),4))(M_pi_c) / 0.0327);
  R_HCO3E: M_h_c + M_hco3_c -> M_co2_c + M_h2o_c; e22 * 0.7955/0.9095 * ((M_h_c)(M_hco3_c) - (M_co2_c)(M_h2o_c) / 0.7098)/(1 + (M_h_c)(M_hco3_c) / 0.9095 + (M_co2_c)(M_h2o_c) / 0.8338);
  R_NADTRHD: M_nad_c + M_nadph_c -> M_nadh_c + M_nadp_c; e23 * 0.7322/0.0423 * ((M_nad_c)(M_nadph_c) - (M_nadh_c)(M_nadp_c) / 0.9289)/(1 + (M_nad_c)(M_nadph_c) / 0.0423 + (M_nadh_c)(M_nadp_c) / 0.1252);

  R_ACONTa: M_cit_c -> M_acon_c + M_h2o_c;  e24 * 0.5707/0.5202 * ((M_cit_c) - (M_acon_c)(M_h2o_c) / 0.7115)/(1 + (M_cit_c) / 0.5202 + (M_acon_c)(M_h2o_c) / 0.0266);
  R_ACONTb: M_acon_c + M_h2o_c -> M_icit_c;e25 * 0.6854/0.4882 * ((M_acon_c)(M_h2o_c) - (M_icit_c) / 0.2852)/(1 + (M_acon_c)(M_h2o_c) / 0.4882 + (M_icit_c) / 0.6279);
  R_CATDOX: M_catechol_c + M_o2_c => M_ccmuac_c + 2 M_h_c; e26 * 0.1988/0.9471 * ((M_catechol_c)(M_o2_c) - (M_ccmuac_c)(pow((M_h_c),2)) / 0.7861)/(1 + (M_catechol_c)(M_o2_c) / 0.9471 + (M_ccmuac_c)(pow((M_h_c),2)) / 0.9112);
  R_CS: M_accoa_c + M_h2o_c + M_oaa_c => M_cit_c + M_coa_c + M_h_c; e27 * 0.6939/0.5502 * ((M_accoa_c)(M_h2o_c)(M_oaa_c) - (M_cit_c)(M_coa_c)(M_h_c) / 0.5013)/(1 + (M_accoa_c)(M_h2o_c)(M_oaa_c) / 0.5502 + (M_cit_c)(M_coa_c)(M_h_c) / 0.576);
  R_CYTBD: 2 M_h_c + 1.5 M_o2_c + M_q8h2_c => M_h2o_c + 2 M_h_e + M_q8_c; e28 * 0.2985/0.0248 * ((pow((M_h_c),2))(pow((M_o2_c),1.5))(M_q8h2_c) - (M_h2o_c)(pow((M_h_e),2))(M_q8_c) / 0.3563)/(1 + (pow((M_h_c),2))(pow((M_o2_c),1.5))(M_q8h2_c) / 0.0248 + (M_h2o_c)(pow((M_h_e),2))(M_q8_c) / 0.719);
  R_DHQTi: M_3dhq_c -> M_3dhsk_c + M_h2o_c; e29 * 0.3873/0.1414 * ((M_3dhq_c) - (M_3dhsk_c)(M_h2o_c) / 0.9221)/(1 + (M_3dhq_c) / 0.1414 + (M_3dhsk_c)(M_h2o_c) / 0.3543);
  R_ENO: M_3pg_c -> M_h2o_c + M_pep_c; e30 * 0.3233/0.6803 * ((M_3pg_c) - (M_h2o_c)(M_pep_c) / 0.2846)/(1 + (M_3pg_c) / 0.6803 + (M_h2o_c)(M_pep_c) / 0.8814);
  R_FBA: M_fdp_c -> M_dhap_c + M_g3p_c; e31 * 0.8589/0.5948 * ((M_fdp_c) - (M_dhap_c)(M_g3p_c) / 0.9144)/(1 + (M_fdp_c) / 0.5948 + (M_dhap_c)(M_g3p_c) / 0.348);
  R_FBP: M_fdp_c + M_h2o_c => M_f6p_c + M_pi_c; e32 * 0.6/0.0955 * ((M_fdp_c)(M_h2o_c) - (M_f6p_c)(M_pi_c) / 0.4946)/(1 + (M_fdp_c)(M_h2o_c) / 0.0955 + (M_f6p_c)(M_pi_c) / 0.0218);
  R_G6PDH2r: M_g6p_c + M_h2o_c + M_nadp_c => M_6pgc_c + 2 M_h_c + M_nadph_c; e33 * 0.8783/0.5801 * ((M_g6p_c)(M_h2o_c)(M_nadp_c) - (M_6pgc_c)(pow((M_h_c),2))(M_nadph_c) / 0.3949)/(1 + (M_g6p_c)(M_h2o_c)(M_nadp_c) / 0.5801 + (M_6pgc_c)(pow((M_h_c),2))(M_nadph_c) / 0.9372);
  R_GADktpp: M_glcn_c + M_nad_c => M_2dhglcn_c + M_h_c + M_nadh_c;e34 * 0.4762/0.531 * ((M_glcn_c)(M_nad_c) - (M_2dhglcn_c)(M_h_c)(M_nadh_c) / 0.8966)/(1 + (M_glcn_c)(M_nad_c) / 0.531 + (M_2dhglcn_c)(M_h_c)(M_nadh_c) / 0.3264);
  R_GAPD: M_adp_c + M_g3p_c + M_nad_c + M_pi_c -> M_3pg_c + M_atp_c + M_h_c + M_nadh_c; e35 * 0.5807/0.4316 * ((M_adp_c)(M_g3p_c)(M_nad_c)(M_pi_c) - (M_3pg_c)(M_atp_c)(M_h_c)(M_nadh_c) / 0.1442)/(1 + (M_adp_c)(M_g3p_c)(M_nad_c)(M_pi_c) / 0.4316 + (M_3pg_c)(M_atp_c)(M_h_c)(M_nadh_c) / 0.2833);
  R_GLCDpp: M_glc__D_c + M_h2o_e + M_q8_c => M_glcn_c + M_h_e + M_q8h2_c; e36 * 0.3932/0.7658 * ((M_glc__D_c)(M_h2o_e)(M_q8_c) - (M_glcn_c)(M_h_e)(M_q8h2_c) / 0.7813)/(1 + (M_glc__D_c)(M_h2o_e)(M_q8_c) / 0.7658 + (M_glcn_c)(M_h_e)(M_q8h2_c) / 0.3474);
  R_GLNS: M_atp_c + M_glu__L_c + M_nh4_c => M_adp_c + M_gln__L_c + M_h_c + M_pi_c; e37 * 0.5155/0.1125 * ((M_atp_c)(M_glu__L_c)(M_nh4_c) - (M_adp_c)(M_gln__L_c)(M_h_c)(M_pi_c) / 0.2065)/(1 + (M_atp_c)(M_glu__L_c)(M_nh4_c) / 0.1125 + (M_adp_c)(M_gln__L_c)(M_h_c)(M_pi_c) / 0.479);
  R_GLUDy: M_glu__L_c + M_h2o_c + M_nadp_c -> M_akg_c + M_h_c + M_nadph_c + M_nh4_c; e38 * 0.1391/0.7785 * ((M_glu__L_c)(M_h2o_c)(M_nadp_c) - (M_akg_c)(M_h_c)(M_nadph_c)(M_nh4_c) / 0.8125)/(1 + (M_glu__L_c)(M_h2o_c)(M_nadp_c) / 0.7785 + (M_akg_c)(M_h_c)(M_nadph_c)(M_nh4_c) / 0.1574);
  R_GLUN: M_gln__L_c + M_h2o_c => M_glu__L_c + M_nh4_c; e39 * 0.858/0.2646 * ((M_gln__L_c)(M_h2o_c) - (M_glu__L_c)(M_nh4_c) / 0.4683)/(1 + (M_gln__L_c)(M_h2o_c) / 0.2646 + (M_glu__L_c)(M_nh4_c) / 0.5136);
  R_GLUSy: M_akg_c + M_gln__L_c + M_h_c + M_nadph_c => 2 M_glu__L_c + M_nadp_c; e40 * 0.3441/0.7652 * ((M_akg_c)(M_gln__L_c)(M_h_c)(M_nadph_c) - (pow((M_glu__L_c),2))(M_nadp_c) / 0.9766)/(1 + (M_akg_c)(M_gln__L_c)(M_h_c)(M_nadph_c) / 0.7652 + (pow((M_glu__L_c),2))(M_nadp_c) / 0.7461);
  R_GND: M_6pgc_c + M_nadp_c => M_co2_c + M_nadph_c + M_ru5p__D_c;  e41 * 0.9045/0.2176 * ((M_6pgc_c)(M_nadp_c) - (M_co2_c)(M_nadph_c)(M_ru5p__D_c) / 0.4914)/(1 + (M_6pgc_c)(M_nadp_c) / 0.2176 + (M_co2_c)(M_nadph_c)(M_ru5p__D_c) / 0.9276);
  R_GNK: M_atp_c + M_glcn_c => M_6pgc_c + M_adp_c + M_h_c; e42 * 0.5802/0.6688 * ((M_atp_c)(M_glcn_c) - (M_6pgc_c)(M_adp_c)(M_h_c) / 0.8401)/(1 + (M_atp_c)(M_glcn_c) / 0.6688 + (M_6pgc_c)(M_adp_c)(M_h_c) / 0.6334);
  R_ICDHyr: M_icit_c + M_nadp_c -> M_akg_c + M_co2_c + M_nadph_c; e43 * 0.2936/0.6075 * ((M_icit_c)(M_nadp_c) - (M_akg_c)(M_co2_c)(M_nadph_c) / 0.1772)/(1 + (M_icit_c)(M_nadp_c) / 0.6075 + (M_akg_c)(M_co2_c)(M_nadph_c) / 0.9164);
  R_KDPGALDOL: M_2ddg6p_c => M_g3p_c + M_pyr_c; e44 * 0.7587/0.6384 * ((M_2ddg6p_c) - (M_g3p_c)(M_pyr_c) / 0.6066)/(1 + (M_2ddg6p_c) / 0.6384 + (M_g3p_c)(M_pyr_c) / 0.8887);
  R_MDH: M_mal__L_c + M_nad_c -> M_h_c + M_nadh_c + M_oaa_c; e45 * 0.9651/0.4341 * ((M_mal__L_c)(M_nad_c) - (M_h_c)(M_nadh_c)(M_oaa_c) / 0.167)/(1 + (M_mal__L_c)(M_nad_c) / 0.4341 + (M_h_c)(M_nadh_c)(M_oaa_c) / 0.4909);
  R_ME1: M_mal__L_c + M_nad_c => M_co2_c + M_nadh_c + M_pyr_c; e46 * 0.5418/0.9527 * ((M_mal__L_c)(M_nad_c) - (M_co2_c)(M_nadh_c)(M_pyr_c) / 0.9382)/(1 + (M_mal__L_c)(M_nad_c) / 0.9527 + (M_co2_c)(M_nadh_c)(M_pyr_c) / 0.1063);
  R_ME2: M_mal__L_c + M_nadp_c => M_co2_c + M_nadph_c + M_pyr_c; e47 * 0.3724/0.24 * ((M_mal__L_c)(M_nadp_c) - (M_co2_c)(M_nadph_c)(M_pyr_c) / 0.0199)/(1 + (M_mal__L_c)(M_nadp_c) / 0.24 + (M_co2_c)(M_nadph_c)(M_pyr_c) / 0.1982);
  R_NADH16: 4 M_h_c + M_nadh_c + M_q8_c => 3 M_h_e + M_nad_c + M_q8h2_c; e48 * 0.7551/0.9231 * ((pow((M_h_c),4))(M_nadh_c)(M_q8_c) - (pow((M_h_e),3))(M_nad_c)(M_q8h2_c) / 0.3393)/(1 + (pow((M_h_c),4))(M_nadh_c)(M_q8_c) / 0.9231 + (pow((M_h_e),3))(M_nad_c)(M_q8h2_c) / 0.2373);
  R_PC: M_atp_c + M_hco3_c + M_pyr_c => M_adp_c + M_h_c + M_oaa_c + M_pi_c; e49 * 0.4904/0.0857 * ((M_atp_c)(M_hco3_c)(M_pyr_c) - (M_adp_c)(M_h_c)(M_oaa_c)(M_pi_c) / 0.1133)/(1 + (M_atp_c)(M_hco3_c)(M_pyr_c) / 0.0857 + (M_adp_c)(M_h_c)(M_oaa_c)(M_pi_c) / 0.4024);
  R_PDH: M_coa_c + M_nad_c + M_pyr_c -> M_accoa_c + M_co2_c + M_nadh_c; e50 * 0.6981/0.2083 * ((M_coa_c)(M_nad_c)(M_pyr_c) - (M_accoa_c)(M_co2_c)(M_nadh_c) / 0.9391)/(1 + (M_coa_c)(M_nad_c)(M_pyr_c) / 0.2083 + (M_accoa_c)(M_co2_c)(M_nadh_c) / 0.2794);
  R_PGI: M_g6p_c -> M_f6p_c; e51 * 0.5586/0.1357 * ((M_g6p_c) - (M_f6p_c) / 0.161)/(1 + (M_g6p_c) / 0.1357 + (M_f6p_c) / 0.8625);
  R_PGLUCONDEHYDRAT: M_6pgc_c => M_2ddg6p_c + M_h2o_c; e52 * 0.3463/0.1157 * ((M_6pgc_c) - (M_2ddg6p_c)(M_h2o_c) / 0.6887)/(1 + (M_6pgc_c) / 0.1157 + (M_2ddg6p_c)(M_h2o_c) / 0.4113);
  R_PPC: M_hco3_c + M_pep_c => M_oaa_c + M_pi_c; e53 * 0.6236/0.3722 * ((M_hco3_c)(M_pep_c) - (M_oaa_c)(M_pi_c) / 0.0018)/(1 + (M_hco3_c)(M_pep_c) / 0.3722 + (M_oaa_c)(M_pi_c) / 0.9428);
  R_PPCK: M_atp_c + M_oaa_c => M_adp_c + M_co2_c + M_pep_c; e54 * 0.3044/0.6794 * ((M_atp_c)(M_oaa_c) - (M_adp_c)(M_co2_c)(M_pep_c) / 0.5157)/(1 + (M_atp_c)(M_oaa_c) / 0.6794 + (M_adp_c)(M_co2_c)(M_pep_c) / 0.296);
  R_PYK: M_adp_c + M_h_c + M_pep_c => M_atp_c + M_pyr_c; e55 * 0.8552/0.8985 * ((M_adp_c)(M_h_c)(M_pep_c) - (M_atp_c)(M_pyr_c) / 0.5167)/(1 + (M_adp_c)(M_h_c)(M_pep_c) / 0.8985 + (M_atp_c)(M_pyr_c) / 0.0737);
  R_RPE: M_ru5p__D_c -> M_xu5p__D_c; e56 * 0.6594/0.0046 * ((M_ru5p__D_c) - (M_xu5p__D_c) / 0.3433)/(1 + (M_ru5p__D_c) / 0.0046 + (M_xu5p__D_c) / 0.639);
  R_RPI: M_r5p_c -> M_ru5p__D_c; e57 * 0.3873/0.9012 * ((M_r5p_c) - (M_ru5p__D_c) / 0.548)/(1 + (M_r5p_c) / 0.9012 + (M_ru5p__D_c) / 0.3848);
  R_TALA: M_g3p_c + M_s7p_c -> M_e4p_c + M_f6p_c; e58 * 0.5929/0.7487 * ((M_g3p_c)(M_s7p_c) - (M_e4p_c)(M_f6p_c) / 0.0518)/(1 + (M_g3p_c)(M_s7p_c) / 0.7487 + (M_e4p_c)(M_f6p_c) / 0.3661);
  R_TKT1: M_g3p_c + M_s7p_c -> M_r5p_c + M_xu5p__D_c; e59 * 0.8245/0.6173 * ((M_g3p_c)(M_s7p_c) - (M_r5p_c)(M_xu5p__D_c) / 0.5559)/(1 + (M_g3p_c)(M_s7p_c) / 0.6173 + (M_r5p_c)(M_xu5p__D_c) / 0.5386);
  R_TKT2: M_e4p_c + M_xu5p__D_c -> M_f6p_c + M_g3p_c; e60 * 0.8468/0.3898 * ((M_e4p_c)(M_xu5p__D_c) - (M_f6p_c)(M_g3p_c) / 0.9774)/(1 + (M_e4p_c)(M_xu5p__D_c) / 0.3898 + (M_f6p_c)(M_g3p_c) / 0.3206);
  R_TPI: M_g3p_c -> M_dhap_c; e61 * 0.8853/0.8419 * ((M_g3p_c) - (M_dhap_c) / 0.6993)/(1 + (M_g3p_c) / 0.8419 + (M_dhap_c) / 0.5801);
  R_MALS: M_accoa_c + M_glx_c + M_h2o_c => M_coa_c + M_h_c + M_mal__L_c; e62 * 0.7669/0.7822 * ((M_accoa_c)(M_glx_c)(M_h2o_c) - (M_coa_c)(M_h_c)(M_mal__L_c) / 0.5741)/(1 + (M_accoa_c)(M_glx_c)(M_h2o_c) / 0.7822 + (M_coa_c)(M_h_c)(M_mal__L_c) / 0.2844);
  R_FUM: M_fum_c + M_h2o_c -> M_mal__L_c; e63 * 0.1596/0.5074 * ((M_fum_c)(M_h2o_c) - (M_mal__L_c) / 0.7219)/(1 + (M_fum_c)(M_h2o_c) / 0.5074 + (M_mal__L_c) / 0.9869);

  # THESE ARE THE CONSOLIDATED RXNS BELOW
  # R_GLCabcpp: M_atp_c + M_glc__D_e + M_h2o_c => M_adp_c + M_glc__D_c + M_h_c + M_pi_c;  
  # R_HEX1: M_atp_c + M_glc__D_c => M_adp_c + M_g6p_c + M_h_c;  
  R_GLCabcpp_HEX1: 2 M_atp_c + M_glc__D_e + M_h2o_c => 2 M_adp_c + M_g6p_c + 2 M_h_c + M_pi_c; e64 * 0.3212/0.0987 * ((pow((M_atp_c),2))(M_glc__D_e)(M_h2o_c) - (pow((M_adp_c),2))(M_g6p_c)(pow((M_h_c),2))(M_pi_c) / 0.7135)/(1 + (pow((M_atp_c),2))(M_glc__D_e)(M_h2o_c) / 0.0987 + (pow((M_adp_c),2))(M_g6p_c)(pow((M_h_c),2))(M_pi_c) / 0.7463);
  # R_2DHGLCK: M_2dhglcn_c + M_atp_c + 2 M_h_c => M_6p2dhglcn_c + M_adp_c;  
  # R_PGLCNDH: M_6p2dhglcn_c + M_nadph_c -> M_6pgc_c + 2 M_h_c + M_nadp_c;  
  R_2DHGLCK_PGLCNDH: M_2dhglcn_c + M_atp_c + M_nadph_c => M_6pgc_c + M_nadp_c + M_adp_c; e65 * 0.9236/0.128 * ((M_2dhglcn_c)(M_atp_c)(M_nadph_c) - (M_6pgc_c)(M_nadp_c)(M_adp_c) / 0.8659)/(1 + (M_2dhglcn_c)(M_atp_c)(M_nadph_c) / 0.128 + (M_6pgc_c)(M_nadp_c)(M_adp_c) / 0.7208);
  # R_ICL: M_icit_c -> M_glx_c + M_succ_c;  
  # R_FRD7: M_fum_c + M_q8h2_c -> M_q8_c + M_succ_c;  
  R_ICL_FRD7: M_icit_c + M_q8_c -> M_glx_c + M_fum_c + M_q8h2_c; e66 * 0.5157/0.9593 * ((M_icit_c)(M_q8_c) - (M_glx_c)(M_fum_c)(M_q8h2_c) / 0.0036)/(1 + (M_icit_c)(M_q8_c) / 0.9593 + (M_glx_c)(M_fum_c)(M_q8h2_c) / 0.4239);
  # R_AKGDH: M_adp_c + M_akg_c + M_nad_c + M_pi_c => M_atp_c + M_co2_c + M_nadh_c + M_succ_c; 
  # R_FRD7: M_fum_c + M_q8h2_c -> M_q8_c + M_succ_c;  
  R_AKGDH_FRD7: M_q8_c + M_adp_c + M_akg_c + M_nad_c + M_pi_c => M_atp_c + M_co2_c + M_nadh_c + M_fum_c + M_q8h2_c; e67 * 0.3321/0.073 * ((M_q8_c)(M_adp_c)(M_akg_c)(M_nad_c)(M_pi_c) - (M_atp_c)(M_co2_c)(M_nadh_c)(M_fum_c)(M_q8h2_c) / 0.0563)/(1 + (M_q8_c)(M_adp_c)(M_akg_c)(M_nad_c)(M_pi_c) / 0.073 + (M_atp_c)(M_co2_c)(M_nadh_c)(M_fum_c)(M_q8h2_c) / 0.942);
  # R_DDPA: M_e4p_c + M_h2o_c + M_pep_c -> M_2dda7p_c + M_pi_c; 
  # R_DHQS: M_2dda7p_c => M_3dhq_c + M_pi_c;  
  R_DDPA_DHQS: M_e4p_c + M_h2o_c + M_pep_c -> M_3dhq_c + 2 M_pi_c; e68 * 0.5412/0.1426 * ((M_e4p_c)(M_h2o_c)(M_pep_c) - (M_3dhq_c)(pow((M_pi_c),2)) / 0.3487)/(1 + (M_e4p_c)(M_h2o_c)(M_pep_c) / 0.1426 + (M_3dhq_c)(pow((M_pi_c),2)) / 0.8459);
  # R_DHSKDH: M_3dhsk_c => M_34dhbz_c + M_h2o_c;  
  # R_PCATDC: M_34dhbz_c + M_h_c -> M_catechol_c + M_co2_c; 
  R_DHSKDH_PCATDC: M_3dhsk_c + M_h_c => M_catechol_c + M_co2_c + M_h2o_c; e69 * 0.5393/0.2102 * ((M_3dhsk_c)(M_h_c) - (M_catechol_c)(M_co2_c)(M_h2o_c) / 0.7468)/(1 + (M_3dhsk_c)(M_h_c) / 0.2102 + (M_catechol_c)(M_co2_c)(M_h2o_c) / 0.7991);

  R_SHIK: M_3dhsk_c + M_nadph_c -> M_shik_c + M_nadp_c; e70 * 0.0767/0.0766 * ((M_3dhsk_c)(M_nadph_c) - (M_shik_c)(M_nadp_c) / 0.378)/(1 + (M_3dhsk_c)(M_nadph_c) / 0.0766 + (M_shik_c)(M_nadp_c) / 0.9038);
  R_SHIK3P: M_shik_c + M_atp_c -> M_adp_c + M_shik3p_c; e71 * 0.0605/0.4086 * ((M_shik_c)(M_atp_c) - (M_adp_c)(M_shik3p_c) / 0.7707)/(1 + (M_shik_c)(M_atp_c) / 0.4086 + (M_adp_c)(M_shik3p_c) / 0.4923);
  R_5EPS3P: M_shik3p_c + M_pep_c -> M_5eps3p_c + M_pi_c; e72 * 0.2928/0.4396 * ((M_shik3p_c)(M_pep_c) - (M_5eps3p_c)(M_pi_c) / 0.0224)/(1 + (M_shik3p_c)(M_pep_c) / 0.4396 + (M_5eps3p_c)(M_pi_c) / 0.1306);
  R_CHOR: M_5eps3p_c -> M_chor_c + M_pi_c; e73 * 0.8362/0.6502 * ((M_5eps3p_c) - (M_chor_c)(M_pi_c) / 0.0629)/(1 + (M_5eps3p_c) / 0.6502 + (M_chor_c)(M_pi_c) / 0.1033);
  R_PAPA: M_chor_c + M_gln__L_c-> M_4a4dch_c + M_glu__L_c; e74 * 0.6516/0.1334 * ((M_chor_c)(M_gln__L_c) - (M_4a4dch_c)(M_glu__L_c) / 0.2163)/(1 + (M_chor_c)(M_gln__L_c) / 0.1334 + (M_4a4dch_c)(M_glu__L_c) / 0.8916);
  R_PAPB: M_4a4dch_c -> M_4a4dpr_c; e75 * 0.1953/0.0657 * ((M_4a4dch_c) - (M_4a4dpr_c) / 0.6751)/(1 + (M_4a4dch_c) / 0.0657 + (M_4a4dpr_c) / 0.0304);
  R_PAPC: M_4a4dpr_c + M_nad_c -> M_4aPPA_c + M_nadh_c + M_co2_c + M_h_c; e76 * 0.9945/0.931 * ((M_4a4dpr_c)(M_nad_c) - (M_4aPPA_c)(M_nadh_c)(M_co2_c)(M_h_c) / 0.127)/(1 + (M_4a4dpr_c)(M_nad_c) / 0.931 + (M_4aPPA_c)(M_nadh_c)(M_co2_c)(M_h_c) / 0.0822);
  R_TYRB: M_4aPPA_c -> M_4aPhe_c; e77 * 0.6496/0.494 * ((M_4aPPA_c) - (M_4aPhe_c) / 0.643)/(1 + (M_4aPPA_c) / 0.494 + (M_4aPhe_c) / 0.9734);
  R_PAL: M_4aPhe_c -> $M_4acinna_c; e78 * 0.753/0.2113 * ((M_4aPhe_c) - ($M_4acinna_c) / 0.0935)/(1 + (M_4aPhe_c) / 0.2113 + ($M_4acinna_c) / 0.4657);

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