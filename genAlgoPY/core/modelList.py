# all of the models are in String form

# the most basic model. 
groundTruth = (""" 
  $S1 -> S2; k1*S1 - k2*S2
  S2 -> S3; k2*S2 - k3*S3
  S3 -> S4; k3*S3 - k4*S4
  S4 -> S5; k4*S4 - k5*S5
  S5 -> $S6; k5*S5 - k6*S6
  S1 = 1; 
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; k6 = 6; 
""")

# groundTruth model with enzyme terms
groundTruth_e = (""" 
  R1: $S1 -> S2; (e1) * (k1*S1 - k2*S2)
  R2: S2 -> S3; (e2) * (k2*S2 - k3*S3)
  R3: S3 -> S4; (e3) * (k3*S3 - k4*S4)
  R4: S4 -> S5; (e4) * (k4*S4 - k5*S5)
  R5: S5 -> $S6; (e5) * (k5*S5 - k6*S6)
  S1 = 1; 
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; k6 = 6; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
""") 

# groundTruth model with reverse reaction constants replaced with Keq terms
groundTruth_mod = (""" 
  v1: $S1 -> S2; k1*S1 * (1-(S2/S1)/Keq1)
  v2: S2 -> S3; k2*S2 * (1-(S3/S2)/Keq2)
  v3: S3 -> S4; k3*S3 * (1-(S4/S3)/Keq3)
  v4: S4 -> S5; k4*S4 * (1-(S5/S4)/Keq4)
  v5: S5 -> $S6; k5*S5 * (1-(S6/S5)/Keq5)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; 
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
""")

# groundTruth model with reverse reaction constants replaced with Keq terms and enzyme terms
groundTruth_mod_e = (""" 
  v1: $S1 -> S2; (e1) * k1*S1 * (1-(S2/S1)/Keq1)
  v2: S2 -> S3; (e2) * k2*S2 * (1-(S3/S2)/Keq2)
  v3: S3 -> S4; (e3) * k3*S3 * (1-(S4/S3)/Keq3)
  v4: S4 -> S5; (e4) * k4*S4 * (1-(S5/S4)/Keq4)
  v5: S5 -> $S6; (e5) * k5*S5 * (1-(S6/S5)/Keq5)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; 
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
""")

# v = Vm1/Km1*(S1 - S2/Keq)/(1 + S1/Km1 + S2/Km2)
# Michaelis-Menten model
groundTruth_MM = (""" 
  v1: $S1 -> S2; Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> $S6; Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")

# Michaelis-Menten model with e 
groundTruth_MM_e = (""" 
  v1: $S1 -> S2; e1 * Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; e2 * Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; e3 * Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; e4 * Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> $S6; e5 * Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1; S6 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")



