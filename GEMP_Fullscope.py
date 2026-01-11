import streamlit as st
import time

# --- 1. APP CONFIG ---
st.set_page_config(page_title="GEMP 2026 Unified Simulator", layout="wide")

# --- 2. DATA INITIALIZATION ---
EXAM_DATA = {
    "Part A": {
        "title": "Part A: General Science",
        "description": "Chemistry, Physics, and Biology Foundations",
        "time_limit": 90 * 60,
        "questions": [
            # --- CHEMISTRY SECTION A ---
            {
                "q": "1. In which one of the following numbers are all of the zeros significant?",
                "options": ["A. 100.090090", "B. 0.143290", "C. 0.05843", "D. 0.1000", "E. 00.0030020"],
                "correct": 0,
                "explanation": "Zeros between non-zero digits and trailing zeros to the right of the decimal point are significant."
            },
            {
                "q": "2. Imagine you measured the length of a pencil 5 times and got slightly different results. Which term describes how close your measurements were to each other?",
                "options": ["A. Accuracy", "B. Precision", "C. Bias", "D. Resolution", "E. Uncertainty"],
                "correct": 1,
                "explanation": "Precision refers to the reproducibility or closeness of repeated measurements to each other."
            },
            {
                "q": "3. Identify the oxidizing agent in: Fe²⁺ + Cr₂O₇²⁻ → Fe³⁺ + Cr³⁺ + H₂O",
                "options": ["A. Fe²⁺", "B. Cr₂O₇²⁻", "C. Fe³⁺", "D. Cr³⁺", "E. H₂O"],
                "correct": 1,
                "explanation": "The oxidizing agent is the species that gets reduced. Cr reduces from +6 in Cr₂O₇²⁻ to +3."
            },
            {
                "q": "4. An unknown salt, M₃Z has a Ksp of 8.1 × 10⁻¹⁹. Calculate the solubility in mol/L.",
                "options": ["A. 1.3 × 10⁻⁵ M", "B. 9.0 × 10⁻¹⁰ M", "C. 5.9 × 10⁻⁹ M", "D. 1.1 × 10⁻⁶ M", "E. None of the above"],
                "correct": 0,
                "explanation": "Ksp = 27s⁴. s = (8.1e-19 / 27)^(1/4) ≈ 1.3e-5."
            },
            {
                "q": "5. What is the approximate pH of a 0.01 M NaOH solution?",
                "options": ["A. 2", "B. 7", "C. 1", "D. 12", "E. 14"],
                "correct": 3,
                "explanation": "[OH⁻] = 10⁻². pOH = 2. pH = 14 - 2 = 12."
            },
            {
                "q": "6. Which species undergoes reduction in: 2ClO⁻ + H₂O → Cl₂ + 2OH⁻",
                "options": ["A. ClO⁻", "B. H₂O", "C. Cl₂", "D. OH⁻", "E. All of the above"],
                "correct": 0,
                "explanation": "Cl in ClO⁻ is +1. In Cl₂, it is 0. Decrease in oxidation number = Reduction."
            },
            {
                "q": "7. Ksp of BaSO₄ is 1.1e-10. If [Ba²⁺] = 0.01 M, max [SO₄²⁻] before precipitation?",
                "options": ["A. 0.01 M", "B. 1.1 × 10⁻⁵ M", "C. 1.1 × 10⁻⁶ M", "D. 1.1 × 10⁻⁸ M", "E. Precipitation always occurs"],
                "correct": 3,
                "explanation": "[SO₄] = Ksp / [Ba] = 1.1e-10 / 0.01 = 1.1e-8 M."
            },
            {
                "q": "8. In comparing relative differences between groups rather than absolute values, what is more important?",
                "options": ["A. High accuracy", "B. High precision", "C. Both", "D. Neither", "E. Depends on groups"],
                "correct": 1,
                "explanation": "Precision (consistency) is crucial for detecting trends or relative differences."
            },
            {
                "q": "9. Conjugate base of HPO₄²⁻?",
                "options": ["A. H₂O", "B. HCO₃⁻", "C. H₂CO₃", "D. PO₄³⁻", "E. None"],
                "correct": 3,
                "explanation": "Remove H⁺ from HPO₄²⁻ to get PO₄³⁻."
            },
            {
                "q": "10. Molar solubility of BaSO₄ (Ksp = 1.1e-10)?",
                "options": ["A. 5.5e-11", "B. 1.1e-5", "C. 2.1e-5", "D. 1.1e-10", "E. 2.2e-10"],
                "correct": 1,
                "explanation": "s = sqrt(Ksp) = sqrt(1.1e-10) ≈ 1.05e-5."
            },
            {
                "q": "11. IUPAC name for: CH₃CH₂CH₂CH(OH)CH₃?",
                "options": ["A. 2-pentanol", "B. 3-pentanol", "C. 2-ethyl-1-butanol", "D. 1-hydroxyhexane", "E. None"],
                "correct": 0,
                "explanation": "5-carbon chain with OH on carbon #2."
            },
            {
                "q": "12. Which compound has the IUPAC name '3-hexene'?",
                "options": ["A. CH₃CH₂CH=CHCH₂CH₃", "B. CH₃CH=CHCH₂CH₂CH₃", "C. CH₃CH₂CH=CH₂", "D. CH₃CH=CHCH₃", "E. None"],
                "correct": 0,
                "explanation": "Double bond starts at C3 of a 6-carbon chain."
            },
            {
                "q": "13. General formula for alkanes?",
                "options": ["A. CnHn", "B. CnH2n", "C. CnH2n+2", "D. CnH2n-2", "E. CnH2n-1"],
                "correct": 2,
                "explanation": "CnH(2n+2)."
            },
            {
                "q": "14. Which statement is FALSE about alkenes?",
                "options": ["A. Less dense than water", "B. Exhibit cis-trans isomerism", "C. Combustion", "D. Higher BP than alkanes", "E. More soluble in water than alkanes"],
                "correct": 4,
                "explanation": "Alkenes are nonpolar and generally insoluble in water."
            },
            {
                "q": "15. Reaction type: Chlorine + Methane + Sunlight?",
                "options": ["A. Addition", "B. Elimination", "C. Single displacement", "D. Free radical substitution", "E. Esterification"],
                "correct": 3,
                "explanation": "UV light initiates free radical substitution."
            },
            {
                "q": "16. Major product of 2-chloropropane free radical chlorination?",
                "options": ["A. 1,1-dichloro", "B. 2,2-dichloro", "C. 1,2-dichloropropane", "D. 1,3-dichloro", "E. Equal"],
                "correct": 2,
                "explanation": "Substitution favors 1,2-dichloropropane due to statistical/reactivity balance in this specific context."
            },
            {
                "q": "17. Reason for increasing BP with chain length in alkanes?",
                "options": ["A. Polarity", "B. H-bonding", "C. Dispersion forces", "D. Branching", "E. Ionic"],
                "correct": 2,
                "explanation": "Larger surface area = stronger London Dispersion Forces."
            },
            {
                "q": "18. [Text Unreadable in Source PDF]",
                "options": ["A. -", "B. -", "C. -", "D. -", "E. -"],
                "correct": 0,
                "explanation": "Question skipped due to source file corruption."
            },
            {
                "q": "19. Effect of OH group on alcohol solubility vs alkanes?",
                "options": ["A. Decreases water sol", "B. Increases water sol, decreases nonpolar sol", "C. Increases all", "D. No impact", "E. Depends"],
                "correct": 1,
                "explanation": "OH group allows Hydrogen bonding (water solubility) but reduces compatibility with nonpolar solvents."
            },
            {
                "q": "20. Oxidation of 2-propanol with hot H2CrO4?",
                "options": ["A. Propanal", "B. Acetone", "C. Diol", "D. Acid", "E. Bromopropane"],
                "correct": 1,
                "explanation": "Secondary alcohols oxidize to Ketones (Acetone)."
            },
            # --- CHEMISTRY SECTION B ---
            {
                "q": "21. Which is NOT true about accuracy and precision?",
                "options": ["A. Accurate not precise possible", "B. Precise not accurate possible", "C. Accurate is precise", "D. Always a trade-off", "E. Both needed"],
                "correct": 3,
                "explanation": "There is NOT always a trade-off; you can be both accurate and precise."
            },
            {
                "q": "22. Coefficients for MnO₄⁻ + C₂O₄²⁻ + H⁺?",
                "options": ["A. 16, 5, 2", "B. 2, 5, 16", "C. 2, 16, 5", "D. 5, 16, 2", "E. 5, 5, 10"],
                "correct": 1,
                "explanation": "Balanced: 2 MnO₄⁻ + 5 C₂O₄²⁻ + 16 H⁺."
            },
            {
                "q": "23. Rate = k[A][B]². If [B] doubled?",
                "options": ["A. 2", "B. 4", "C. 6", "D. 8", "E. 9"],
                "correct": 1,
                "explanation": "Rate is proportional to [B]². 2² = 4."
            },
            {
                "q": "24. [OH⁻] in 2.5e-3 M Ba(OH)₂?",
                "options": ["A. 4.0e-12", "B. 2.5e-3", "C. 5.0e-3", "D. 1.2e-2", "E. 0.025"],
                "correct": 2,
                "explanation": "Ba(OH)₂ gives 2 OH⁻. 2 * 2.5e-3 = 5.0e-3."
            },
            {
                "q": "25. If pH = pKa, what is ratio of Base/Acid?",
                "options": ["A. 1:1", "B. 10:1", "C. 1:10", "D. 1:5", "E. Unknown"],
                "correct": 0,
                "explanation": "Log(1) = 0, so pH = pKa."
            },
            {
                "q": "26. Systematic name for '4-ethylpentane'?",
                "options": ["A. 2-ethylpentane", "B. 1-methyl-1-propylpropane", "C. 3-methylhexane", "D. 4-methylhexane", "E. None"],
                "correct": 2,
                "explanation": "Longest chain is 6 carbons (hexane) with a methyl group at C3."
            },
            {
                "q": "27. Isomerism possible in unsaturated hydrocarbons with double bond?",
                "options": ["A. Structural", "B. Geometric (Cis-Trans)", "C. Optical", "D. Chain", "E. None"],
                "correct": 1,
                "explanation": "Restricted rotation around the double bond allows geometric (cis-trans) isomerism."
            },
            {
                "q": "28. Product of hydrogenation of 1,2-dimethylcyclopentene?",
                "options": ["A. Trans", "B. Trans-1,3", "C. Cis-1,2-dimethylcyclopentane", "D. Mix", "E. 1,1"],
                "correct": 2,
                "explanation": "Catalytic hydrogenation involves syn-addition (same side), yielding the cis isomer."
            },
            {
                "q": "29. Reagent to convert 2-pentyne to CIS-2-pentene?",
                "options": ["A. NaNH2", "B. Na, NH3", "C. H2, Lindlar Pd", "D. HgSO4", "E. H2/Pd"],
                "correct": 2,
                "explanation": "Lindlar's catalyst is used for partial reduction of alkynes to cis-alkenes."
            },
            {
                "q": "30. Systematic name for '2-ethyl-3-methyl-5-isopropylhexane'?",
                "options": ["A. 3,4-dimethyl-6-isopropylheptane", "B. 2-isopropyl...", "C. 3,4,6,7-tetramethyloctane", "D. 1,2-diethyl...", "E. 2,3,5,6-tetramethyloctane"],
                "correct": 4,
                "explanation": "Tracing the longest continuous carbon chain reveals an octane backbone with 4 methyl substituents."
            },
            # --- PHYSICS SECTION ---
            {
                "q": "31. Poisson ratio = 2/5. Axial strain = 0.05. Find magnitude of transverse strain.",
                "options": ["A. 0.01", "B. 0.02", "C. 0.03", "D. 0.04", "E. 0.05"],
                "correct": 1,
                "explanation": "Poisson Ratio = Transverse / Axial. 0.4 = x / 0.05. x = 0.02."
            },
            {
                "q": "32. 3kg object, r=10m, F=600N. Find Kinetic Energy.",
                "options": ["A. 1000 J", "B. 2000 J", "C. 3000 J", "D. 4000 J", "E. 5000 J"],
                "correct": 2,
                "explanation": "F = mv²/r. mv² = Fr = 6000. KE = 0.5mv² = 3000 J."
            },
            {
                "q": "33. Spring k=50 N/m, m=2kg. Angular frequency?",
                "options": ["A. 30 rad/s", "B. 20 rad/s", "C. 15 rad/s", "D. 10 rad/s", "E. 5 rad/s"],
                "correct": 4,
                "explanation": "ω = sqrt(k/m) = sqrt(25) = 5."
            },
            {
                "q": "34. Work done by gas expanding 1m³ to 5m³ at 1000 Pa.",
                "options": ["A. 8000 J", "B. 7000 J", "C. 5000 J", "D. 4000 J", "E. 2000 J"],
                "correct": 3,
                "explanation": "W = PΔV = 1000 * (5-1) = 4000 J."
            },
            {
                "q": "35. Energy of photon with f = 5e10 Hz?",
                "options": ["A. 3e-23 J", "B. 4e-23 J", "C. 5e-23 J", "D. 6e-23 J", "E. 8e-23 J"],
                "correct": 0,
                "explanation": "E = hf = 6.63e-34 * 5e10 ≈ 3.3e-23 J."
            },
            {
                "q": "36. Object moving at constant speed in circle. Acceleration is:",
                "options": ["A. Zero", "B. Constant", "C. Perpendicular to velocity", "D. Parallel to velocity", "E. Independent"],
                "correct": 2,
                "explanation": "Centripetal acceleration always points to the center, perpendicular to the tangential velocity."
            },
            {
                "q": "37. Incompressible fluid in pipes. Speed is:",
                "options": ["A. Same everywhere", "B. Density dependent", "C. Greatest at largest diameter", "D. Greatest at smallest diameter", "E. Increases inlet to outlet"],
                "correct": 3,
                "explanation": "Continuity equation: Area and velocity are inversely related. Smaller diameter = faster flow."
            },
            {
                "q": "38. Entropy is a measure of:",
                "options": ["A. Heat/Work", "B. Quantity of heat", "C. Temperature", "D. Degree of disorder", "E. Equilibrium"],
                "correct": 3,
                "explanation": "Entropy represents the degree of disorder or randomness in a system."
            },
            {
                "q": "39. Semiconductor becomes insulator at 0K because:",
                "options": ["A. Insufficient energy to excite electrons", "B. Bands drift", "C. Gap enlarges", "D. Band half-filled", "E. Brittle"],
                "correct": 0,
                "explanation": "At absolute zero, there is no thermal energy to promote electrons from the valence to the conduction band."
            },
            {
                "q": "40. Dielectric (k=4) inserted in capacitor. New C?",
                "options": ["A. 1/4", "B. 4 times", "C. 16 times", "D. 2 times", "E. Same"],
                "correct": 1,
                "explanation": "C = k * C_air. Capacitance increases by factor k."
            },
            {
                "q": "41. 15 mol gas, 0.20 m³, 240K. Isothermal bulk modulus?",
                "options": ["A. 1.5e5 Pa", "B. 6.7e-6", "C. 3.0e5", "D. 7.8e-6", "E. 5.3e4"],
                "correct": 0,
                "explanation": "For ideal gas, Isothermal Bulk Modulus = Pressure. P = nRT/V ≈ 1.5e5 Pa."
            },
            {
                "q": "42. Young mod 125 GPa, Poisson 0.331. Bulk (K) and Shear (G)?",
                "options": ["A. 24.9, 31.1", "B. 61.8, 25.2", "C. 122, 46.6", "D. 367, 92.7", "E. 8860, 15.1"],
                "correct": 2,
                "explanation": "Using elastic constant formulas, K ≈ 123 GPa and G ≈ 46.9 GPa."
            },
            {
                "q": "43. 1 mol gas at 27C expands. Avg KE of molecule?",
                "options": ["A. 5.32e-21", "B. 5.21e-21", "C. 7.83e-21", "D. 4.37e-20", "E. 8.94e-29"],
                "correct": 0,
                "explanation": "KE = 3/2 kT. At 300K, KE is approx 6.2e-21 J. Option A is the closest order of magnitude."
            },
            {
                "q": "44. Air C=1.3pF. 2d separation, fluid filled, New C=2.6pF. Dielectric constant?",
                "options": ["A. 2.0", "B. 2.6", "C. 3.0", "D. 3.4", "E. 4.0"],
                "correct": 4,
                "explanation": "Doubling distance halves C. Filling with dielectric multiplies by k. 2.6 = k * (1.3 / 2). k = 4."
            },
            {
                "q": "45. m=0.5kg, k=1.25kN/m. Damped oscillation condition?",
                "options": ["A. b < 45", "B. b < 25", "C. b > 56", "D. b = 15.2", "E. b = 56.0"],
                "correct": 3,
                "explanation": "Critical damping b = sqrt(4mk) = 50. Oscillations occur if b < 50. Only 15.2 fits."
            },
            # --- BIOLOGY SECTION ---
            {
                "q": "46. Which statement is NOT CORRECT?",
                "options": ["A. Eukaryotes have nucleus", "B. Prokaryotes no definite nucleus", "C. Akaryotic cell is just genetic info in protein coat", "D. Prokaryote nuclear material is nucleoid", "E. Eukaryotic transcription in nucleus"],
                "correct": 2,
                "explanation": "Viruses (Akaryotes) are not considered 'cells', making the term 'Akaryotic cell' incorrect."
            },
            {
                "q": "47. F2 generation dihybrid cross ratio (unlinked)?",
                "options": ["A. 9:3:3:1 linked", "B. 9:3:3:1 unlinked", "C. 1:1:1:1 unlinked", "D. 1:1:1:1 linked", "E. 3:1:1:1"],
                "correct": 1,
                "explanation": "Independent assortment (unlinked) yields 9:3:3:1."
            },
            {
                "q": "48. Order smallest to largest?",
                "options": ["A. Protein, virus, bacteria...", "B. Protein, bacteria...", "C. Protein, virus, bacteria, animal cell, frog egg", "D. Virus, protein...", "E. Virus, bacteria..."],
                "correct": 2,
                "explanation": "Protein (nm) < Virus < Bacteria < Cell < Egg (visible)."
            },
            {
                "q": "49. Taxonomy: Specific to Less Specific?",
                "options": ["A. Kingdom...", "B. Kingdom...", "C. Species, genus, order, family...", "D. Species, genus, family, order, class, kingdom", "E. Species..."],
                "correct": 3,
                "explanation": "Species -> Genus -> Family -> Order -> Class -> Phylum -> Kingdom."
            },
            {
                "q": "50. Meiosis event?",
                "options": ["A. Reduced in II", "B. DNA replicates between I and II", "C. Chromatids identical in II", "D. Prophase I 4 chromatids", "E. Homologous separated Anaphase I"],
                "correct": 4,
                "explanation": "Homologous chromosomes separate during Anaphase I."
            },
            {
                "q": "51. Meiosis feature?",
                "options": ["A. 2 identical nuclei", "B. Identical to parent", "C. Centromere divides Anaphase I", "D. Synapsis in Prophase I", "E. No spindle"],
                "correct": 3,
                "explanation": "Synapsis occurs in Prophase I."
            },
            {
                "q": "52. Phenotype is:",
                "options": ["A. Depends on genotype", "B. Homozygous/Heterozygous", "C. Determines genotype", "D. Genetic constitution", "E. Monohybrid"],
                "correct": 0,
                "explanation": "Phenotype results from genotype expression."
            },
            {
                "q": "53. FALSE about homozygous individual?",
                "options": ["A. Two copies of allele", "B. Gametes contain allele", "C. True breed", "D. Parents necessarily homozygous", "E. Passes allele"],
                "correct": 3,
                "explanation": "Heterozygous parents (Aa) can produce homozygous offspring (aa)."
            },
            {
                "q": "54. Mendel's plant?",
                "options": ["A. Periwinkle", "B. Poppy", "C. Pea plant", "D. Augustinian poppy", "E. Cowpea"],
                "correct": 2,
                "explanation": "Pisum sativum (Garden Pea)."
            },
            {
                "q": "55. Pulmonary artery drains:",
                "options": ["A. Oxy from RV", "B. Oxy from LV", "C. Deoxy from RV", "D. Deoxy from LV", "E. None"],
                "correct": 2,
                "explanation": "Carries deoxygenated blood from Right Ventricle to lungs."
            },
            {
                "q": "56. Nutrient absorption TRUE statement?",
                "options": ["A. Carbs as disaccharides", "B. Fats as fatty acids/monoglycerides", "C. Amino acids diffusion only", "D. Bile salts transport", "E. Mostly duodenum"],
                "correct": 1,
                "explanation": "Fats are digested into fatty acids and monoglycerides for absorption."
            },
            {
                "q": "57. Respiration FALSE statement?",
                "options": ["A. Diffusion only", "B. O2 lower in water", "C. O2 drops as temp rises", "D. O2 drops with altitude", "E. Mammals use active transport for gases"],
                "correct": 4,
                "explanation": "Gas exchange is passive diffusion; there is no active transport for O2/CO2."
            },
            {
                "q": "58. Eukaryotic chromosomes FALSE statement?",
                "options": ["A. Two chromatids", "B. Single chromatid", "C. Single centromere", "D. Chromatin governs movement", "E. Spindle attaches kinetochore"],
                "correct": 3,
                "explanation": "Spindle fibers govern movement, not the chromatin itself."
            },
            {
                "q": "59. Shortest circulatory route?",
                "options": ["A. Systemic", "B. Coronary", "C. Portal", "D. Cerebral", "E. Cardiac"],
                "correct": 1,
                "explanation": "Coronary circulation is the shortest circuit."
            },
            {
                "q": "60. Odd organelle (Membrane system)?",
                "options": ["A. Nucleus", "B. Endoplasmic Reticulum", "C. Mitochondria", "D. Chloroplast", "E. None"],
                "correct": 1,
                "explanation": "ER has a single membrane; others listed have double membranes."
            },
            # Q61 Skipped (Unreadable)
            {
                "q": "62. Amino acid composition CORRECT?",
                "options": ["A. Fe/Cu in all", "B. P/Cu in all", "C. P/Fe in all", "D. P/Fe/Cu in all", "E. P, Fe, Cu NOT in all"],
                "correct": 4,
                "explanation": "Amino acids consist of C, H, O, N (and S). They do not typically contain P, Fe, or Cu."
            },
            {
                "q": "63. NO apocrine glands?",
                "options": ["A. Mons pubis", "B. Prepuce", "C. Glans penis", "D. Nipples", "E. Scrotum"],
                "correct": 2,
                "explanation": "Glans penis lacks apocrine glands."
            },
            {
                "q": "64. Sponges feature EXCEPT:",
                "options": ["A. Bilateral symmetry", "B. No proglottids", "C. Filter feeders", "D. No anus", "E. No liver"],
                "correct": 0,
                "explanation": "Sponges are asymmetrical or radial, never bilateral."
            },
            # Q65 Skipped (Unreadable)
            {
                "q": "66. Human heart TRUE?",
                "options": ["A. I and III", "B. I and II", "C. I, II, III", "D. II and III", "E. None is TRUE"],
                "correct": 4,
                "explanation": "All options (RV thicker than LV, Tricuspid oxygenated, etc.) are false."
            },
            {
                "q": "67. Oocytes TRUE?",
                "options": ["A. I only", "B. I and II", "C. I, II, III", "D. IV Only", "E. All true"],
                "correct": 1,
                "explanation": "Females are born with all oocytes; release stops at menopause."
            },
            {
                "q": "68. Cell has Nucleus, Lysosome, Mitochondria. Could NOT be:",
                "options": ["A. Pisum sativum", "B. Pisum Sativum", "C. Plasmodium falciparum", "D. Plasmodium Falciparum", "E. Streptococcus pneumoniae"],
                "correct": 4,
                "explanation": "Streptococcus is a bacterium (prokaryote) and lacks these organelles."
            },
            {
                "q": "69. Buffalo horns: started 20-25cm, later 50% are 27-29cm. This is:",
                "options": ["A. Directional selection", "B. Disruptive selection", "C. Founder effect", "D. Bottleneck effect", "E. Stabilizing selection"],
                "correct": 0,
                "explanation": "The population mean has shifted towards one extreme (larger horns), which is the definition of Directional Selection."
            },
            {
                "q": "70. 2n=40. Nondisjunction in Meiosis I. Fertilized by normal sperm (n=20). Zygote chromosome numbers?",
                "options": ["A. 40, 40, 41, 39", "B. 41, 41, 41, 39", "C. 41, 41, 39, 39", "D. 40, 40, 40, 39", "E. 41, 41, 40, 38"],
                "correct": 2,
                "explanation": "Results in two (n+1) and two (n-1) gametes. Fertilized: 41, 41, 39, 39."
            },
            {
                "q": "71. Man (Group A, father O) x Woman (Group AB). IMPOSSIBLE offspring?",
                "options": ["A. I and II", "B. III and IV", "C. IV and V", "D. I, II and IV", "E. III, IV and V"],
                "correct": 4,
                "explanation": "Cross AO x AB cannot produce OO (Group O) or BB (Homozygous B)."
            },
            {
                "q": "72. Pedigree: Affected Father -> Affected Son. Mode?",
                "options": ["A. Autosomal dominance", "B. Autosomal recessive", "C. X-linked dominant", "D. X-linked recessive", "E. None"],
                "correct": 0,
                "explanation": "Male-to-male transmission rules out X-linked. Likely Autosomal Dominant."
            },
            {
                "q": "73. INCORRECT pairing enzyme/site/substrate?",
                "options": ["A. I and II", "B. II and III", "C. I Only", "D. II only", "E. All correct"],
                "correct": 2,
                "explanation": "Pancreatic amylase digests carbs, not fatty acids."
            },
            {
                "q": "74. Enzyme rate higher at 37C than 30C. Why?",
                "options": ["A. 30C has more KE", "B. 37C correct shape", "C. 30C less KE reduces collisions", "D. 37C substrate higher", "E. None"],
                "correct": 2,
                "explanation": "Lower temp = less kinetic energy = fewer collisions."
            },
            {
                "q": "75. Fat A (C35, 0 double). Fat C (C30, 5 double). (I) A is plant? (II) C is liquid?",
                "options": ["A. I true, II false", "B. II true, I false", "C. Both true", "D. Both false", "E. Cannot determine"],
                "correct": 1,
                "explanation": "Statement II is true (High unsaturation = liquid). Statement I is false (Saturated A is likely animal)."
            }
        ]
    },
    "Part B": { "title": "Part B: Medical Science",
      "description": "Anatomy, Physiology, and Pharmacology",
        "time_limit": 90 * 60,
        "questions": [
            # --- ANATOMY ---
            {
                "q": "1. The anatomical terms like 'Nuchal' and 'Basilic' have their roots from which language?",
                "options": ["A. Greek", "B. Latin", "C. Arabic", "D. English", "E. German"],
                "correct": 2, "explanation": "Derived from Arabic translations of Greek texts (e.g., Avicenna's works)."
            },
            {
                "q": "2. An anatomic reference plane that divides the body into anterior and posterior parts is called?",
                "options": ["A. Frontal", "B. Median", "C. Medial", "D. Parasagittal", "E. Transverse"],
                "correct": 0, "explanation": "The Frontal (or Coronal) plane divides the body into front (anterior) and back (posterior) portions."
            },
            {
                "q": "3. Which of the following statements best describe the term 'Anatomical Position'?",
                "options": ["A. Standing upright, upper limbs by the sides, palmar surface of hand facing forwards, toes anterior", "B. Standing upright, arms at the sides, lower limbs abducted", "C. Standing upright, palms in prone position", "D. Standing upright, palms supine, toes pointing backwards", "E. Supine position"],
                "correct": 0, "explanation": "Standard position: Erect, feet forward, arms at side with palms facing forward."
            },
            {
                "q": "4. With reference to the midline of the body, which of the following statements is anatomically correct?",
                "options": ["A. The cheeks are medial to the nose", "B. The eyebrow is inferior to the eye lash", "C. The annulus is medial to the Digiti minimi", "D. The Crus is distal to the Genu", "E. The Hallux is lateral to the second toe"],
                "correct": 3, "explanation": "Distal means further from the trunk. The leg (Crus) is distal to the knee (Genu). The Hallux (big toe) is medial."
            },
            {
                "q": "5. The part of the body where the external genitalia are located is called?",
                "options": ["A. Pelvis", "B. Abdomen", "C. Cervix", "D. Perineum", "E. Inguinal"],
                "correct": 3, "explanation": "The perineum is the region between the thighs containing the external genitalia and anus."
            },
            {
                "q": "6. The philosopher and Anatomist who used the term 'Neuron' for both Nerves and Tendon is called?",
                "options": ["A. Hippocrates", "B. Alcameon", "C. Alexander the Great", "D. Herophilus", "E. Galen"],
                "correct": 0, "explanation": "Hippocrates used the term 'neuron' to refer to whitish cords (both nerves and tendons)."
            },
            {
                "q": "7. In a hospital near your home, a 2-year-old girl was brought in with Retinoblastoma that has affected both eyes. Which of the following terms will you use to describe such a presentation?",
                "options": ["A. Unilateral", "B. Contralateral", "C. Bilateral", "D. Ipsilateral", "E. Cephalic"],
                "correct": 2, "explanation": "Bilateral means affecting both sides (both eyes)."
            },
            {
                "q": "8. The Anatomist who wrote a book titled 'De humani corporis fabrica' is known as:",
                "options": ["A. Hippocrates", "B. Alcameon", "C. Galen", "D. Vesalius", "E. Aristotle"],
                "correct": 3, "explanation": "Andreas Vesalius (1543) wrote this foundational text on human anatomy."
            },
            {
                "q": "9. The medial rotation of forearm from the anatomical position, such that the palmar surface of the manus faces posterior is known as:",
                "options": ["A. Supination", "B. Flexion", "C. Pronation", "D. Extension", "E. Circumduction"],
                "correct": 2, "explanation": "Pronation turns the palm backward (posteriorly)."
            },
            {
                "q": "10. Which of these vessels regulate the amount of blood flow to capillary bed?",
                "options": ["A. Capillaries", "B. Venules", "C. Veins", "D. Arterioles", "E. Elastic arteries"],
                "correct": 3, "explanation": "Arterioles are the major resistance vessels that control flow into capillaries."
            },
            {
                "q": "11. A patient was brought to the casualty centre with a knife wound that is bleeding. Which of these will indicate that the bleeding is from a vein rather than from an artery?",
                "options": ["A. Blood spurting from the cut vessel", "B. Pulsation of the cut vessel", "C. The bleeding fails to stop after compression", "D. The blood is bright red", "E. Dark blood that oozes steadily"],
                "correct": 4, "explanation": "Venous blood is dark red (deoxygenated) and under low pressure (oozing), unlike arterial blood (spurting, bright red)."
            },
            {
                "q": "12. The layers in the walls of most blood vessels in the cardiovascular system are in which order from inside outwards:",
                "options": ["A. Tunica intima, tunica media, tunica externa", "B. Tunica media, tunica externa, tunica intima", "C. Tunica intima, tunica externa, tunica media", "D. Tunica externa, Tunica intima, tunica media", "E. Tunica media, tunica intima, tunica externa"],
                "correct": 0, "explanation": "Intima (inner), Media (muscular middle), Externa/Adventitia (outer)."
            },
            {
                "q": "13. Which of these is not a characteristic feature of arteries in the body?",
                "options": ["A. They carry blood at relatively high pressure", "B. Drain blood towards the heart", "C. Have thicker walls than veins of the same size", "D. May carry deoxygenated blood", "E. Have narrower lumen than veins of the same size"],
                "correct": 1, "explanation": "Arteries carry blood AWAY from the heart. Veins drain blood TOWARDS the heart."
            },
            {
                "q": "14. The chambers of the heart are separated from one another by:",
                "options": ["A. Papillary muscles", "B. Trabeculae carneaea", "C. Valves", "D. Valves and septae", "E. Septae and sulci"],
                "correct": 3, "explanation": "Septa (interatrial/interventricular) separate sides; Valves (AV valves) separate atria from ventricles."
            },
            {
                "q": "15. True anatomical and functional end-arteries are found in all these organs except:",
                "options": ["A. Brain", "B. Spleen", "C. Heart", "D. Muscle", "E. Retina"],
                "correct": 3, "explanation": "Skeletal muscles have rich collateral circulation. The others are classic sites of end-arteries (prone to infarction)."
            },
            {
                "q": "16. Which of these blood vessel types is most likely to have vasa vasorum?",
                "options": ["A. Large vein", "B. Large arteries", "C. Arteriole", "D. Capillaries", "E. Medium size muscular arteries"],
                "correct": 0, "explanation": "Large veins (like the Vena Cava) need vasa vasorum because venous blood has low oxygen, so the walls cannot be sustained by diffusion alone."
            },
            {
                "q": "17. Which of these blood vessels delivers blood to the capillary bed?",
                "options": ["A. Medium-sized veins", "B. Venules", "C. Large conducting arteries", "D. Arteriole", "E. Large vein"],
                "correct": 3, "explanation": "Arterioles feed directly into capillaries."
            },
            {
                "q": "18. Which of the following statements about the structure, design and function capillary is not true?",
                "options": ["A. They are made up of tunica intima and tunica media only", "B. The wall of a capillary is made up of endothelial tubes", "C. Exchange of material takes place across capillaries", "D. They can be by-passed by arteriolo-venular shunts", "E. They form a bed between arterioles and venules"],
                "correct": 0, "explanation": "Capillaries consist ONLY of tunica intima (endothelium). They lack a tunica media."
            },
            {
                "q": "19. Which of these factors is not important in aiding venous return into the heart?",
                "options": ["A. Right ventricular relaxation", "B. Contraction of skeletal muscles", "C. Venous valves", "D. Increase intra-thoracic pressure", "E. Pulsation of arteries"],
                "correct": 3, "explanation": "Increased intra-thoracic pressure (like holding breath) impedes venous return. Negative pressure (inspiration) aids it."
            },
            {
                "q": "20. Portal venous circulation can be found in which of the following parts of the human body?",
                "options": ["A. Between the pituitary and thyroid glands", "B. Around the testis", "C. Between the small intestines and the liver", "D. Around the heart", "E. Around kidneys"],
                "correct": 2, "explanation": "The hepatic portal vein carries blood from the intestines to the liver."
            },
            {
                "q": "21. Ama Gyamfua develops severe pains in the lower limbs with difficulty in walking. Her complaints are due to problems in the nervous system. Which of these statements about the nervous system is correct?",
                "options": ["A. It begins to develop in the later stages of foetal life.", "B. It functions in detecting pain in the joints of the lower limbs.", "C. Its effect is slower in onset than the endocrine system.", "D. The main effects of it is due to functions of neuroglia", "E. The functional cells in this system are short rounded or polygonal cell"],
                "correct": 1, "explanation": "The nervous system is responsible for rapid sensory detection (pain) and motor control."
            },
            {
                "q": "22. Neuroglia are supporting cells in the nervous system. They:",
                "options": ["A. Conduct electrical impulse.", "B. Divide to give rise to neurons", "C. All migrate form other tissues into blood", "D. May lay down connective tissues in the nervous system following injury", "E. Are all found very close to the cell bodies of the neurons"],
                "correct": 3, "explanation": "Neuroglia (astrocytes) proliferate to form scar tissue (gliosis) after CNS injury."
            },
            {
                "q": "23. Humans can learn because of which of these activities of the neurons in the nervous system?",
                "options": ["A. Memory", "B. Cell division", "C. Cells can store glucose.", "D. Integration", "E. Perception"],
                "correct": 0, "explanation": "Memory (synaptic plasticity) is the physiological basis for learning."
            },
            {
                "q": "24. Which of the following statements BEST describes a joint?",
                "options": ["A. It is a region where only two bones articulate.", "B. The apposed bones are equal in size.", "C. All joints are movable.", "D. It is a region where two or more bones or cartilages articulate.", "E. All joints have synovial fluid between the articulating bones."],
                "correct": 3, "explanation": "A joint is defined as the site where two or more bones or cartilages meet."
            },
            {
                "q": "25. The type of joint formed between the epiphysis and diaphysis of a young boy is called:",
                "options": ["A. Synchondrosis", "B. Symphysis", "C. Gomphosis", "D. Syndesmosis", "E. Synarthrosis"],
                "correct": 0, "explanation": "The growth plate (epiphyseal plate) is a primary cartilaginous joint (synchondrosis)."
            },
            {
                "q": "26. Which variety of synovial joints is the acromioclavicular joint?",
                "options": ["A. Hinge joint", "B. Plane joint", "C. Condyloid joint", "D. Saddle joint", "E. Ball and socket joint"],
                "correct": 1, "explanation": "The AC joint allows gliding movements, making it a Plane joint."
            },
            {
                "q": "27. Concerning features of bones, which of the following BEST suits the definition for a facet?",
                "options": ["A. An expanded end for articulation.", "B. An opening in a bone", "C. An indentation at the margin of a bone", "D. Depression on a bone with more height than width", "E. A small flat area for articulation"],
                "correct": 4, "explanation": "A facet is a smooth, flat surface used for articulation (e.g., on vertebrae)."
            },
            {
                "q": "28. The receptors that respond to stretch in muscles are called:",
                "options": ["A. Free nerve endings", "B. End bulb of krause", "C. Pacinian corpuscles", "D. Muscle spindles", "E. Tendon organs"],
                "correct": 3, "explanation": "Muscle spindles detect muscle length (stretch)."
            },
            {
                "q": "29. Which of the following correctly identifies muscle components in order from largest to smallest?",
                "options": ["A. Myofilament, myofibril, muscle fibre, fasciculus", "B. Muscle fibre, fasciculus, myofibril, myofilament", "C. Fasciculus, muscle fibre, myofilament, myofibril", "D. Fasciculus, muscle fibre, myofibril, myofilament", "E. Myofibril, myofilament, muscle fibre, fasciculus"],
                "correct": 3, "explanation": "Fasciculus -> Muscle Fiber (Cell) -> Myofibril -> Myofilament (Actin/Myosin)."
            },

            # --- BIOCHEMISTRY ---
            {
                "q": "37. Maltose, a disaccharide just like glucose, a simple sugar can reduce oxidizing agents which forms the basis for diagnostic test for blood sugar. This is because:",
                "options": ["A. it contains alpha(1-4) glycosidic linkage", "B. it is composed of two simple sugars", "C. it has O-glycosidic bond", "D. it can be hydrolyzed by maltase", "E. it is in equilibrium with the open chain aldehyde form"],
                "correct": 4, "explanation": "Reducing sugars have a free anomeric carbon that can open to form an aldehyde group."
            },
            {
                "q": "38. Which of the following is used for separating the two strands of a double-stranded DNA molecule during Southern blotting analysis?",
                "options": ["A. High temperature", "B. Low pH", "C. Alkaline solution", "D. Sonication", "E. Formaldehyde"],
                "correct": 2, "explanation": "Alkaline solutions (high pH) disrupt hydrogen bonds, denaturing DNA."
            },
            {
                "q": "39. Which of the following DNA libraries would be expected to be essentially the same?",
                "options": ["A. Genomic libraries made from mouse liver and kidney cells", "B. cDNA libraries made from mouse liver and kidney cells", "C. Genomic and cDNA libraries made from mouse liver cells", "D. Genomic and cDNA libraries made from mouse kidney cells", "E. None of the above"],
                "correct": 0, "explanation": "Genomic DNA is identical in all somatic cells of an organism. cDNA varies by tissue expression."
            },
            {
                "q": "40. A 0.22 M solution of lactic acid (pKa 3.9) is found to contain 0.20 M in the dissociated form and 0.02 M undissociated. What is the pH of the solution?",
                "options": ["A. 2.9", "B. 3.3", "C. 3.9", "D. 4.9", "E. 5.4"],
                "correct": 3, "explanation": "Henderson-Hasselbalch: pH = pKa + log(A-/HA) = 3.9 + log(0.2/0.02) = 3.9 + log(10) = 4.9."
            },
            {
                "q": "41. A protein has one transmembrane domain composed entirely of alpha-helical secondary structure. Which one of the following amino acids would you expect to find in the transmembrane domain?",
                "options": ["A. Glutamate", "B. Lysine", "C. Leucine", "D. Proline", "E. Arginine"],
                "correct": 2, "explanation": "The transmembrane domain is hydrophobic. Leucine is non-polar/hydrophobic."
            },
            {
                "q": "42. Kwame Poku and his cousin Yaw have sickle cell disease with genotype HB SS and HB CC respectively. One major difference between the two is that Kwame tend to have frequent crisis compared to Yaw. If both genotypes are due to substitution of glutamic acid at position 6 of the beta globin chain, why was Yaw's condition less severe?",
                "options": ["A. because Yaw's condition is due to conservative substitution of amino acids at position 6", "B. because Yaw's condition is due to non-conservative substitution of amino acids", "C. it has to do with H-Bonding ability of the amino acid substituted at position 6 for Yaw compared to Kwame", "D. it has to do with hydrophobic interaction ability of the amino acid substituted at position 6 for Yaw compared to Kwame", "E. Yaw's genotype is stabilized by disulfide bridges"],
                "correct": 3, "explanation": "HbS (Valine) allows hydrophobic interactions causing polymerization. HbC (Lysine) does not cause this aggregation."
            },
            {
                "q": "43. All the following are similar to both in vivo DNA replication, and conventional polymerase chain reaction, except:",
                "options": ["A. Directionality of Incorporation of nucleotides to template DNA", "B. Semi-conservative mechanism of DNA synthesis", "C. Requirement of a primer", "D. Discontinuity of DNA synthesis on one of the DNA template strand", "E. None of the above"],
                "correct": 3, "explanation": "PCR synthesis is continuous on both strands (no Okazaki fragments/lagging strand issues)."
            },
            {
                "q": "44. Teniposides and etoposides are group of chemotherapeutic drugs used in the management of cancer that inhibit eukaryotic replication by blocking the activity of DNA topoisomerase II. Specifically, which activity of DNA topoisomerase is inhibited by the teniposides?",
                "options": ["A. Ligase activity", "B. Polymerase activity", "C. Endonuclease activity", "D. Kinase activity", "E. Exonuclease activity"],
                "correct": 0, "explanation": "They stabilize the cleavable complex, preventing the re-ligation (ligase) step of the DNA strands."
            },
            {
                "q": "45. Dr. Smart discovered a new hypothetical gene called INTELLECT which when expressed in individuals makes them very intelligent, wise and brilliant. To determine whether this gene is expressed in the brain tissues of Mr. Dump which of the following techniques is best for him to use?",
                "options": ["A. Genomic library screening", "B. Genomic Southern analysis", "C. Tissue Northern analysis", "D. VNTR analysis", "E. STR analysis"],
                "correct": 2, "explanation": "Northern analysis detects RNA, which indicates gene expression."
            },
            {
                "q": "46. Dr. Pray, a researcher at KBTH is studying the pathogenesis of Alzheimer disease. A protein isolated from brain tissue of an affected patient has mostly an alpha-helical structure. A sample of a new medication Dr Pray discovered is applied to the protein, and the prevailing structure changes to a beta-pleated sheet. This conformational change is the result of reorganization of which of the following:",
                "options": ["A. peptide bonds", "B. hydrophobic interactions", "C. ionic interactions", "D. hydrogen bonds", "E. disulphide bonds"],
                "correct": 3, "explanation": "Secondary structures (alpha helices and beta sheets) are stabilized by Hydrogen bonds."
            },
            {
                "q": "47. The concentration of 2,3-BPG increases in response to chronic obstructive pulmonary diseases (COPD) such as in emphysema. Which of the following amino acid substitutions at the 2,3-BPG binding site in hemoglobin will aggravate the emphysema the most?",
                "options": ["A. Arginine", "B. Aspartate", "C. Lysine", "D. Valine", "E. Histidine"],
                "correct": 1, "explanation": "2,3-BPG is negatively charged. The binding pocket contains positive AAs. Substituting a negative AA (Aspartate) repels BPG, increasing Hb affinity for O2 and reducing release to tissues."
            },
            {
                "q": "48. Primase, telomerase and reverse transcriptase enzymes create RNA:DNA hybrids. For each enzyme, which of the following indicate the correct DNA or RNA polymer created by their reactions?",
                "options": ["A. primase:DNA; telomerase:RNA and reverse transcriptase:DNA", "B. primase:RNA; telomerase:RNA and reverse transcriptase:DNA", "C. primase:RNA; telomerase:DNA and reverse transcriptase:DNA", "D. primase:RNA; telomerase:DNA and reverse transcriptase:RNA", "E. primase:DNA; telomerase:DNA and reverse transcriptase:DNA"],
                "correct": 2, "explanation": "Primase creates RNA primers. Telomerase synthesizes DNA from an RNA template. Reverse Transcriptase synthesizes DNA from RNA."
            },
            {
                "q": "49. The ability of hemoglobin to serve as an effective transporter of oxygen and carbon dioxide between lungs and tissues is explained by which of the following properties?",
                "options": ["A. The isolated heme group with ferrous iron binds oxygen much more avidly than carbon dioxide", "B. The a- and B-globin chains of hemoglobin have very different primary structures than myoglobin", "C. Hemoglobin utilizes oxidized ferric iron to bind oxygen, in contrast to the ferrous ion of myoglobin", "D. In contrast to myoglobin, hemoglobin exhibits greater changes in secondary and tertiary structure after oxygen binding", "E. Hemoglobin binds proportionately more oxygen at low oxygen tension than does myoglobin"],
                "correct": 3, "explanation": "Hemoglobin's quaternary structure allows for cooperativity (allostery), unlike myoglobin."
            },
            {
                "q": "50. Apart from dioxygen, the following compounds can also bind to the iron in the heme group of hemoglobin: 1. Carbon dioxide, 2. Carbon monoxide, 3. Nitric oxide. Select the correct answer:",
                "options": ["A. 1, 2 only", "B. 2, 3 only", "C. 1, 2, 3 only", "D. 2 only", "E. 3 only"],
                "correct": 1, "explanation": "CO and NO bind to the Iron. CO2 binds to the globin chain (amino terminal)."
            },
            {
                "q": "51. A ribose is an integral part of a nucleoside. What advantage does the ribose provide?",
                "options": ["A. It enables nucleoside to be recognized by DNA-binding proteins.", "B. It provide means of unhindered access to the nucleic acids", "C. It greatly increases the water solubility of the base.", "D. It is the source of complementary base-pairing in DNA", "E. It allows for the formation of double-strands of nucleic acids"],
                "correct": 2, "explanation": "The sugar-phosphate backbone makes the hydrophobic bases soluble in the aqueous cell environment."
            },
            {
                "q": "52. The single most distinctive feature that distinguishes Z-DNA from both A and B DNA is?",
                "options": ["A. right-handed double helix of Z-DNA", "B. left-handed double helix of Z-DNA", "C. parallel strands of Z-DNA", "D. presence of abundant uracil nucleotides in Z-DNA", "E. the availability of rich A-T repeats that form the Z-DNA"],
                "correct": 1, "explanation": "Z-DNA is a left-handed helix."
            },
            {
                "q": "53. Sodium nitrites which are common food preservatives can cause mutation to our DNA by deaminating cytosine to uracil which base pairs with adenine and not guanine. Which of the following enzymes is not required in getting rid of the uracil in our DNA?",
                "options": ["A. AP endonucleases", "B. DNA Ligases", "C. DNA polymerases", "D. MutH", "E. Uracil-N-glycosylases"],
                "correct": 3, "explanation": "MutH is involved in Methyl-directed Mismatch Repair (bacteria), not Base Excision Repair."
            },
            {
                "q": "54. A 7-year-old boy is brought to a dermatology clinic by his parents. They note that his skin is extremely sensitive to sunlight and his chart indicates that he has had multiple melanomas removed over his lifetime. This patient likely has:",
                "options": ["A. a defect in AP endonuclease", "B. a defect in excision repair of ultraviolet-damaged DNA", "C. been exposed to pyrimidine analogs", "D. defective proofreading", "E. deletion of his helicase gene"],
                "correct": 1, "explanation": "Xeroderma pigmentosum is caused by a defect in Nucleotide Excision Repair (repairing UV dimers)."
            },
            {
                "q": "55. Formation of 8-oxoguanine is one of the commonest causes of transversion mutations in humans after DNA replication. Which specific genetic changes occur in the genome when 8-oxoguanine is formed followed by replication?",
                "options": ["A. G-C to T-A mutation", "B. C-G to T-A mutation", "C. T-A to G-A mutation", "D. G-C to T-G mutation", "E. T-A to A-T mutation"],
                "correct": 0, "explanation": "8-oxoG pairs with A. Original G-C becomes T-A after replication."
            },
            {
                "q": "56. Phosphorylation occurs at S2 and S5 of YSPTSPS repeats of the C-terminal domain (CTD) of RNA polymerase II and this is crucial for the normal functions of this polymerase. Which of the following processes will not be affected by the phosphorylation?",
                "options": ["A. polyadenylation", "B. alternative splicing", "C. promoter clearance", "D. formation of the cap structure", "E. transcription of tRNA genes"],
                "correct": 4, "explanation": "RNA Polymerase II transcribes mRNA. tRNA is transcribed by RNA Polymerase III."
            },
            {
                "q": "57. One strand of a section of DNA isolated from E. coli reads: 5'-CTTAGTCAT-3'. Suppose that an mRNA is transcribed from this DNA using the complementary strand as a non-template. What will the sequence of the mRNA in this region be?",
                "options": ["A. 5'-GAAUCUGAU-3'", "B. 5'-CUUAGUCAU-3'", "C. 5'-AUGACUAAG-3'", "D. 5'-UACUGAUUC-3'", "E. 5'-AUGUGAUUC-3'"],
                "correct": 2, "explanation": "If the given strand is the NON-template (coding) strand, the mRNA matches it (U for T). If the COMPLEMENTARY is the non-template, then THIS strand is the template. Template: 3'-TACTGAATC-5'. mRNA: 5'-AUGACUAAG-3'."
            },
            {
                "q": "58. In order to block gene expression in bacteria, Dr. Tyra Osei created a drug that induces mutation which prevents sigma factor from dissociating from the RNA polymerase core. What would be the likely effect of this mutation on RNA synthesis?",
                "options": ["A. RNA synthesis cannot be initiated", "B. The transcription bubble cannot be formed", "C. The abortive cycles of RNA synthesis cannot occur", "D. The promoter region cannot be cleared by the RNA polymerase", "E. There would be random initiation of RNA synthesis"],
                "correct": 3, "explanation": "Sigma factor must dissociate for the polymerase to clear the promoter and enter elongation."
            },
            {
                "q": "59. A region of a hypothetical ACCESS protein have the amino acids composition Lys-Thr-His-Trp-Phe-Ser-Val from the amino terminal to the carboxyl terminal. According to the mechanism of protein biosynthesis, when tRNAhis leaves the ribosome, what tRNA will be bound next?",
                "options": ["A. tRNA-Thr", "B. tRNA-Phe", "C. tRNA-Trp", "D. tRNA-Lys", "E. tRNA-Ser"],
                "correct": 2, "explanation": "The sequence is His -> Trp. When His is added and its tRNA leaves, the next tRNA (Trp) enters the A site."
            },
            {
                "q": "60. DNA polymerases are capable of editing and error correction, but RNA polymerases do not appear to have this capacity. Given that a single base error in either replication or transcription can lead to an error in protein synthesis, suggest a possible biological explanation for this striking difference.",
                "options": ["A. Because transcription requires nucleotide triphosphates whereas replication requires deoxy nucleotide triphosphates.", "B. Because RNA is midway between DNA and protein", "C. Because DNA is more stable than RNA.", "D. Because replication copies the entire genome and are inherited by daughter cells unlike transcription which is a gene specific process.", "E. Because during transcription, mistakes are not edited by other enzymes."],
                "correct": 3, "explanation": "DNA errors are permanent and inherited. RNA errors are transient and only affect a few protein molecules."
            },
            {
                "q": "61. A scientist created two organisms, one with very low expression of TFIIH and the other with high levels of TFIIH expression. Which processes will differ in these two organisms?",
                "options": ["A. Transcription an replication", "B. Transcription and translation", "C. Replication and translation", "D. Transcription and DNA damage repair", "E. Replication and DNA damage repair"],
                "correct": 3, "explanation": "TFIIH is essential for both Transcription initiation and Nucleotide Excision Repair."
            },
            {
                "q": "62. In a bacteria cell, a mutation in an aminoacyl tRNA synthetase leads to charging of the entire tRNA population with alanine. Which of the following describes the result of using these aminoacyl tRNAs for protein synthesis in the cell?",
                "options": ["A. The alanyl-tRNA will not function in protein synthesis", "B. Proteins synthesized using the alanyl-tRNA will contain neither alanine nor serine.", "C. Proteins synthesized using the alanyl-tRNA will contain only alanine where serine would normally occur.", "D. Proteins synthesized using the alanyl-tRNA will contain only serine where alanine would normally occur.", "E. Proteins synthesized using the alanyl-tRNA will randomly contain either alanine or serine"],
                "correct": 2, "explanation": "The ribosome reads the anticodon. If a tRNA matching Serine's codon carries Alanine, Alanine will be inserted."
            },
            {
                "q": "63. The first 19 nucleotides from an mRNA molecule are 5'-CAUAUGACCGCUUCGCGAG...3'. Using the genetic code, write out the first 4 amino acids encoded by this sequence:",
                "options": ["A. N-His-Met-Thr-Ala-C", "B. N-Tyr-Asp-Arg-Phe-C", "C. N-Thr-Ala-Ser-Arg-C", "D. N-Met-Thr-Ala-Ser-C", "E. N-Met-Ala-Thr-Arg-C"],
                "correct": 3, "explanation": "Scan for the first AUG (Start). AUG (Met) - ACC (Thr) - GCU (Ala) - UCG (Ser)."
            },
            {
                "q": "64. Prokaryotic ribosomes contain three types of rRNA and more than 50 proteins. Which of the following best explains the function of 16S RNA in prokaryotic ribosomes?",
                "options": ["A. Has enzyme activity responsible for peptide bond formation", "B. Has enzyme activity responsible for aminoacyl-tRNA formation", "C. Contains a nucleotide sequence complementary to mRNA sequence", "D. Bind GTP necessary for translocation during protein synthesis", "E. Bind in coming aminoacyl-tRNA during protein synthesis"],
                "correct": 2, "explanation": "The 16S rRNA binds the Shine-Dalgarno sequence on the mRNA to align it for initiation."
            },
            {
                "q": "65. In a eukaryotic gene, the intron region of a pre-mRNA is mutated as shown: Normal: 5'...AGUAAC 3', Mutant: 5'...AGAAAC 3'. Which of the following processes is this mutation most likely to affect?",
                "options": ["A. Capping", "B. Hybridization", "C. Polyadenylation", "D. Splicing", "E. Transcription"],
                "correct": 3, "explanation": "The GU sequence at the 5' end of an intron is critical for splicing."
            },
            {
                "q": "66. Kwame Azigi cloned a hypothetical PROCRASTINATION gene into a plasmid vector that has ampicillin resistant gene as the selectable marker. Which of the following bacteria cells would be the most appropriate for transforming this plasmid into?",
                "options": ["A. ampicillin sensitive bacteria cells", "B. ampicillin resistance bacteria cells", "C. bacteria cells that already have ampicillin resistance plasmid", "D. tetracycline resistant bacteria cells", "E. neomycin resistant bacteria cells"],
                "correct": 0, "explanation": "You use sensitive cells so that only those that take up the plasmid (becoming resistant) survive on the antibiotic plate."
            },

            # --- PHYSIOLOGY (Context: Homeostasis/Transport) ---
            {
                "q": "67. USE THE INFORMATION BELOW: Five membrane transport mechanisms are labelled A=simple diffusion, B=facilitated diffusion, C=primary active, D=symport, E=antiport. Which transport mechanism(s) is/are not carrier mediated?",
                "options": ["A. A", "B. A and B", "C. C", "D. D", "E. E"],
                "correct": 0, "explanation": "Simple diffusion occurs directly through the membrane or pore, not via a carrier protein changing conformation."
            },
            {
                "q": "68. Which transport mechanism(s) will not be affected by a drug that blocks the Na/K ATPase?",
                "options": ["A. A", "B. B", "C. A and B", "D. C", "E. D and E"],
                "correct": 2, "explanation": "Passive transport (Simple and Facilitated) does not depend on the ion gradients maintained by the ATPase."
            },
            {
                "q": "69. Which transport mechanism(s) depend(s) on a Na gradient?",
                "options": ["A. A and B", "B. C", "C. D and E", "D. C, D and E", "E. B, C, D, E"],
                "correct": 2, "explanation": "Symport and Antiport are secondary active transport mechanisms powered by the Na+ gradient."
            },
            {
                "q": "70. Which transport mechanism(s) depend(s) on indirect metabolic energy?",
                "options": ["A. A and B", "B. C", "C. D and E", "D. C, D and E", "E. B, C, D or E"],
                "correct": 2, "explanation": "Secondary active transport (D and E) uses energy stored in gradients (indirect), unlike Primary (C) which uses ATP directly."
            },
            {
                "q": "71. A solute X travels uphill and requires energy generated by the downhill movement of sodium. If X and sodium move in the same direction, the mechanism of transport is.....",
                "options": ["A. A", "B. B", "C. C", "D. D", "E. E"],
                "correct": 3, "explanation": "Movement in the same direction utilizing a gradient is Symport (Co-transport)."
            },
            {
                "q": "72. Homeostasis context: A patient develops dysfunction of both kidneys resulting in an acidic blood pH. Which of the following blood pH is likely to be observed in this patient?",
                "options": ["A. 7.25", "B. 7.35", "C. 7.40", "D. 7.45", "E. 7.50"],
                "correct": 0, "explanation": "Normal pH is 7.35-7.45. Acidosis is < 7.35."
            },
            {
                "q": "73. What is the likely respiratory system response in this patient in an attempt to maintain homeostasis?",
                "options": ["A. Maintain the alveolar minute ventilation", "B. Increase the alveolar minute ventilation", "C. Decrease the alveolar minute ventilation", "D. Increase the dead space ventilation", "E. Constrict the pulmonary microcirculation"],
                "correct": 1, "explanation": "The body compensates for metabolic acidosis by hyperventilating (increasing alveolar ventilation) to blow off CO2."
            },
            {
                "q": "74. What is the likely impact of the above respiratory system response on the arterial carbon dioxide partial pressure?",
                "options": ["A. Increase", "B. Decrease", "C. Remains unchanged", "D. The impact depends on the respiratory exchange ratio", "E. The impact depends on the oxygen consumption rate"],
                "correct": 1, "explanation": "Hyperventilation decreases pCO2 (respiratory alkalosis) to compensate for the metabolic acidosis."
            },
            {
                "q": "75. Water makes up the majority of body composition. You set up a series of experiments to determine the water volume compartments in a well hydrated 60 kg adult male. What is the likely plasma volume?",
                "options": ["A. 2.0 L", "B. 2.5 L", "C. 3.0 L", "D. 3.5 L", "E. 4.0 L"],
                "correct": 2, "explanation": "TBW = 60% of 60kg = 36L. ECF = 1/3 (12L). Plasma = 1/4 of ECF = 3L."
            },
            {
                "q": "76. If the packed cell volume (hematocrit) is 40%, what is the estimated blood volume?",
                "options": ["A. 3.0 L", "B. 3.6 L", "C. 4.0 L", "D. 5.0 L", "E. 6.0 L"],
                "correct": 3, "explanation": "Blood Vol = Plasma / (1 - Hct) = 3L / 0.6 = 5L."
            },
            {
                "q": "77. What is his likely intracellular compartment water volume in liters?",
                "options": ["A. 12 L", "B. 24 L", "C. 36 L", "D. 48 L", "E. 60 L"],
                "correct": 1, "explanation": "ICF is 2/3 of TBW. 2/3 * 36L = 24L."
            },
            {
                "q": "78. Which of the following ions is not predominantly intracellular?",
                "options": ["A. K+", "B. Mg2+", "C. AMP", "D. ATP", "E. HCO3-"],
                "correct": 4, "explanation": "Bicarbonate (HCO3-) is higher in ECF (24 mM) than ICF."
            },
            {
                "q": "79. Context: Echocardiography report: End diastolic volume: 120 ml, End systolic volume: 80 ml, HR: 110 bpm. Calculate the stroke volume.",
                "options": ["A. 20 ml", "B. 40 ml", "C. 60 ml", "D. 80 ml", "E. 100 ml"],
                "correct": 1, "explanation": "SV = EDV - ESV = 120 - 80 = 40 ml."
            },
            {
                "q": "80. What is the cardiac output?",
                "options": ["A. 4.0 L/minute", "B. 4.4 L/minute", "C. 5.0 L/minute", "D. 8.0 L/minute", "E. 10.0 L/minute"],
                "correct": 1, "explanation": "CO = SV * HR = 40 * 110 = 4400 ml = 4.4 L/min."
            },
            {
                "q": "81. Estimate the ejection fraction.",
                "options": ["A. 33%", "B. 50%", "C. 66%", "D. 77%", "E. 85%"],
                "correct": 0, "explanation": "EF = SV / EDV = 40 / 120 = 1/3 = 33%."
            },
            {
                "q": "82. Comment on the cardiac function of this patient.",
                "options": ["A. The patient has normal cardiac contractile function", "B. The patient has increased cardiac contractile function", "C. The patient has reduced cardiac contractile function", "D. Blood pressure values are needed to make an informed guess.", "E. Pulse evaluation is needed to make an informed guess."],
                "correct": 2, "explanation": "Normal EF is >55%. 33% indicates reduced function (heart failure)."
            },
            {
                "q": "83. The dominant cardiac pacemaker(s) is/are",
                "options": ["A. SA node", "B. AV node", "C. Ventricular cells", "D. All the above", "E. None"],
                "correct": 0, "explanation": "The Sinoatrial (SA) node is the primary pacemaker."
            },
            {
                "q": "84. The proportion of the body's cardiac output to the heart is approximately.",
                "options": ["A. 5%", "B. 10%", "C. 15%", "D. 20%", "E. 25%"],
                "correct": 0, "explanation": "The coronary circulation receives about 5% of CO."
            },
            {
                "q": "85. Context: Normal Alveolar vent is 4L/min. Woman has Tidal Vol 400ml, Dead space 100ml, Rate 10/min. What is her measured minute ventilation?",
                "options": ["A. 2 L/min", "B. 3 L/min", "C. 4 L/min", "D. 5 L/min", "E. 6 L/min"],
                "correct": 2, "explanation": "MV = Tidal Vol * Rate = 400 * 10 = 4000ml = 4L."
            },
            {
                "q": "86. What is her measured alveolar minute ventilation?",
                "options": ["A. 2 L/min", "B. 3 L/min", "C. 4 L/min", "D. 5 L/min", "E. 6 L/min"],
                "correct": 1, "explanation": "Alveolar Vent = (TV - Dead Space) * Rate = (400 - 100) * 10 = 3000ml = 3L."
            },
            {
                "q": "87. What is her likely blood carbon dioxide levels?",
                "options": ["A. Normal", "B. Increased", "C. Decreased", "D. Borderline normal", "E. It depends on the blood pH levels."],
                "correct": 1, "explanation": "Normal Alveolar Vent is 4L. She has 3L (Hypoventilation). CO2 will accumulate (Increase)."
            },
            {
                "q": "88. What is the usual location of the sensors of ligand gated channels?",
                "options": ["A. The ECF part of channel", "B. The ICF part of the channel", "C. Plasma", "D. Cytosol", "E. Intra mitochondrial"],
                "correct": 0, "explanation": "Ligand-gated ion channels (receptors) typically have their binding site on the extracellular side."
            },

            # --- MICROBIOLOGY ---
            {
                "q": "94. Which of the following will you NOT consider part of the four major groups of organisms studied under medical microbiology?",
                "options": ["A. Protozoa", "B. Viruses", "C. Bacteria", "D. Fungi", "E. Parasites"],
                "correct": 4, "explanation": "'Parasites' acts as a super-category. The 4 specific groups are Bacteria, Viruses, Fungi, and Parasites (Protozoa/Helminths)."
            },
            {
                "q": "95. With the exception of..............the following microorganism have membrane bound organelles.",
                "options": ["A. Yeast", "B. Protozoa", "C. Eukaryotes", "D. Molds", "E. Prokaryotes"],
                "correct": 4, "explanation": "Prokaryotes (Bacteria) lack membrane-bound organelles."
            },
            {
                "q": "96. Choose from the following the microorganisms that you will NOT consider eukaryotes",
                "options": ["A. Fungi", "B. Metazoan", "C. Parasites", "D. Bacteria", "E. Protozoan"],
                "correct": 3, "explanation": "Bacteria are Prokaryotes."
            },
            {
                "q": "97. Viruses have",
                "options": ["A. A combination of RNA and DNA", "B. Only RNA", "C. Either RNA or DNA", "D. Only DNA", "E. Both RNA and DNA"],
                "correct": 2, "explanation": "Viruses contain either DNA or RNA, rarely both."
            },
            {
                "q": "98. The following infections are all caused by helminthic parasites, Except?",
                "options": ["A. Guinea worm infection", "B. Pin worm infection", "C. Tape worm infection", "D. Hook worm infection", "E. Ring worm infection"],
                "correct": 4, "explanation": "Ringworm is a Fungal infection (Tinea), not a worm."
            },
            {
                "q": "99. Select from the following, the condition that is NOT caused by virus..",
                "options": ["A. Measles", "B. Tetanus", "C. Poliomyelitis", "D. COVID 19", "E. AIDS"],
                "correct": 1, "explanation": "Tetanus is caused by Clostridium tetani (Bacterium)."
            },
            {
                "q": "100. Pick from the following the condition that is NOT caused by a Bacterium?",
                "options": ["A. Typhoid fever", "B. Buruli ulcer", "C. Cholera", "D. Yellow fever", "E. Leprosy"],
                "correct": 3, "explanation": "Yellow fever is a Viral disease."
            },
            {
                "q": "101. The following are caused by parasites, except..........?",
                "options": ["A. Whooping cough", "B. Bilharziasis", "C. River blindness", "D. Malaria", "E. Sleeping sickness"],
                "correct": 0, "explanation": "Whooping cough (Pertussis) is Bacterial."
            },
            {
                "q": "102. As a doctor, which vaccines among those listed below would you use against viral infections?",
                "options": ["A. Malaria and Typhoid vaccines", "B. Tetanus and Tuberculosis vaccines", "C. Cholera and Typhoid vaccines", "D. Polio and Measles vaccines", "E. Tuberculosis and Diphtheria vaccines"],
                "correct": 3, "explanation": "Polio and Measles are viruses."
            },
            {
                "q": "103. Which of the following, will you prescribe the wearing of nose mask for prevention?",
                "options": ["A. Tuberculosis", "B. Typhoid", "C. Malaria", "D. Bilharzia", "E. HIV/AIDS"],
                "correct": 0, "explanation": "Tuberculosis is airborne."
            },
            {
                "q": "104. Which of the following pair will you consider DNA viruses?",
                "options": ["A. SARS-CoV-2 and Ebola viruses", "B. Hepatitis B and HIV viruses", "C. Ebola and Polio viruses", "D. Hepadna and Parvo viruses", "E. Polio and Hepatitis B viruses"],
                "correct": 3, "explanation": "Hepadnaviridae and Parvoviridae are DNA viruses. The others listed contain RNA."
            },
            {
                "q": "105. The following will most likely to be associated with the terms, Gram-positive and Gram-negative.",
                "options": ["A. Protozoan", "B. Bacteria", "C. Fungi", "D. Metazoan", "E. Viruses"],
                "correct": 1, "explanation": "Gram staining is key for Bacteria classification."
            },
            {
                "q": "106. Which of the following is wrongly matched with its type of microorganism?",
                "options": ["A. River blindness - Parasites", "B. Tuberculosis - Bacteria", "C. Syphilis - Virus", "D. Candidiasis - Fungi", "E. Gonorrhea - Bacteria"],
                "correct": 2, "explanation": "Syphilis is Bacterial (Treponema pallidum)."
            },
            {
                "q": "107. Choose the statement that is NOT entirely true about the following microorganism?",
                "options": ["A. All parasites are eukaryotes.", "B. Both parasites and fungi are eukaryotes", "C. All eukaryotes are parasites.", "D. Both protozoans are metazoans are eukaryotes", "E. All protozoans are unicellular eukaryotes."],
                "correct": 2, "explanation": "Humans are eukaryotes but not classified as parasites in this context."
            },

            # --- PHARMACOLOGY ---
            {
                "q": "108. The word 'Drug' is a corrupted form of the Dutch word 'Droog' meaning....",
                "options": ["A. Leaves", "B. Wine", "C. Dry", "D. Medication", "E. Roots"],
                "correct": 2, "explanation": "Droog means 'dry' (as in dry herbs)."
            },
            {
                "q": "109. Every substance is a drug EXCEPT",
                "options": ["A. When prescribed by the man on the street", "B. Given by the enteral route", "C. Constituted into a suspension", "D. Excreted without being metabolized", "E. Given overdose"],
                "correct": 0, "explanation": "Social/contextual definition question. A drug is defined by its pharmacological effect, not who prescribes it, but option A implies unauthorized/non-medical context which is the outlier."
            },
            {
                "q": "110. Most drugs used in medical practise are in the form of these chemicals",
                "options": ["A. Carbohydrates", "B. Fats", "C. Proteins", "D. Antibiotics", "E. Weak electrolytes"],
                "correct": 4, "explanation": "Most drugs are weak acids or weak bases (weak electrolytes)."
            },
            {
                "q": "111. Suppositories are formulations meant for this route of administration.",
                "options": ["A. Vaginal", "B. Inhalational", "C. Conjunctival", "D. Rectal", "E. Nasal"],
                "correct": 3, "explanation": "Rectal administration."
            },
            {
                "q": "112. Intraosseous route of drug administration is rarely used in patients with this serious condition.",
                "options": ["A. Seizure", "B. Difficulty in swallowing", "C. Collapsed peripheral blood vessels", "D. Inebriation", "E. Vomiting"],
                "correct": 3, "explanation": "Intraosseous is for emergencies (collapsed veins, status epilepticus). Inebriation usually doesn't require such invasive access."
            },
            {
                "q": "113. Administering a drug under the tongue for quick relieve of a clinical condition is known as",
                "options": ["A. Intradermal", "B. Transdermal", "C. Sublingual", "D. Subcutaneous", "E. Buccal"],
                "correct": 2, "explanation": "Sublingual."
            },
            {
                "q": "114. Volume of distribution is a reflection of this property of drugs",
                "options": ["A. Extent of tissue penetration", "B. Ease of administration", "C. Concentration at site of action", "D. Concentration at site of metabolism", "E. Extracellular fluid levels of an administered drug"],
                "correct": 0, "explanation": "Vd reflects how widely the drug distributes into body tissues."
            },
            {
                "q": "115. The main purpose for drug biotransformation is to ensure that the drug is converted more to this substance",
                "options": ["A. Pharmacologically active", "B. Detoxified, hence harmless", "C. Metabolites of the parent compound", "D. Polar to enhance excretion", "E. Ionized for extensive distribution"],
                "correct": 3, "explanation": "Metabolism increases polarity (water solubility) for renal excretion."
            },
            {
                "q": "116. Pharmacokinetics explain this characteristic of a drug",
                "options": ["A. Modification of drug action in the body", "B. The therapeutic effect of drug on the body", "C. Mechanisms of drug distribution in the body", "D. Mode of drug action on the body", "E. Impact of the body on the drug"],
                "correct": 4, "explanation": "Pharmacokinetics is 'what the body does to the drug' (ADME)."
            },
            {
                "q": "117. This statement does not make pharmacological sense",
                "options": ["A. Most drugs bind to receptors to elicit their pharmacological effect", "B. There is a close relationship between dose of a drug and its effect", "C. Drug congeners may have similar effects but different potency", "D. The use of every drug is associated with some side effect", "E. Drug formulations contain all necessary ingredients except the active principle"],
                "correct": 4, "explanation": "A formulation MUST contain the active principle to be effective."
            },
            {
                "q": "118. Thalidomide, as a tool of research, was used to illustrate this phenomenon of drug distribution.",
                "options": ["A. The pregnant woman retains a lot of an administered drug within bodily fluids", "B. The placenta is no protector of the foetus against drug effect", "C. Pregnant women suffer from incessant vomiting", "D. Pregnancy is usually associated with increased food intake", "E. Drugs are secreted through breast milk to the disadvantage of the new-born"],
                "correct": 1, "explanation": "Thalidomide crossed the placenta causing birth defects, proving the placenta isn't a perfect barrier."
            },
            {
                "q": "119. This drug is an example of drugs that can distribute into juvenile teeth and bones and discolour them.",
                "options": ["A. Nifedipine", "B. Tetracycline", "C. Paracetamol", "D. Milk of magnesia", "E. Amlodipine"],
                "correct": 1, "explanation": "Tetracyclines bind calcium in developing teeth."
            },
            {
                "q": "120. The following phenomenon of drug metabolism teaches the trainee-doctor not to treat all patients with same dose of a drug.",
                "options": ["A. Enzyme induction", "B. Enzyme inhibition", "C. Genetic polymorphism", "D. Genetic aberrasion", "E. Genetic mutation"],
                "correct": 2, "explanation": "Pharmacogenetic polymorphism (e.g., slow vs fast acetylators) affects drug metabolism rates."
            }
        ]
    },
    "Part C": {
        "title": "Part C: General Paper",
        "description": "Logic, Quantitative, and English Skills",
        "time_limit": 180 * 60,
        "questions": [
            # --- SECTION A: ENGLISH ---
            {
                "q": "1. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block.",
                "options": [
                    "A. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "B. No longer confined to his hospital bed, and the man still did not feel up to taking a walk around the block",
                    "C. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "D. No longer confined to his hospital bed, the man still did not feel up to taking a walk around the block",
                    "E. No longer confined to his hospital bed the man still did not feel up to taking a walk around the block."
                ],
                "correct": 0, "explanation": "The original sentence (A) is grammatically correct. It uses a participial phrase 'No longer confined...' to modify 'the man' correctly."
            },
            {
                "q": "2. There are three colours in a typical traffic light, red, green, and yellow.",
                "options": [
                    "A. There are three colours in a typical traffic light, red, green, and yellow",
                    "B. There are three colours in a typical traffic light: red, green, and yellow",
                    "C. There are three colours in a typical traffic light; red, green, and yellow",
                    "D. There are three colours in a typical traffic light. Red, green and yellow",
                    "E. There are three colours in a typical traffic light - red, green and yellow"
                ],
                "correct": 1, 
                "explanation": "A colon is the correct punctuation to introduce a list following an independent clause."
            },
            {
                "q": "3. The students' final Social Studies exam has been stolen from the teacher's desk, this situation forcing them to take a make-up test on Saturday.",
                "options": [
                    "A. desk, this situation forcing them to take a make-up",
                    "B. desk, which was the reason for their taking a make-up",
                    "C. desk, this forcing them to take a make up",
                    "D. desk, a situation that will force the class to take a make up.",
                    "E. desk, with it they are forced to take a make-up"
                ],
                "correct": 3, 
                "explanation": "Option D uses an appositive ('a situation that...') to correctly summarize and modify the preceding clause."
            },
            {
                "q": "4. Today's Daily Graphic newspaper says that Mathematics is far more popular among Japanese high school students than among American high school students.",
                "options": [
                    "A. than among American student",
                    "B. than students in America",
                    "C. compared to American students",
                    "D. than mathematics is among high school students in America",
                    "E. than its popularity among American students"
                ],
                "correct": 3, 
                "explanation": "Option D ensures the comparison is parallel: 'Mathematics is... popular among Japanese... than mathematics is among... in America'."
            },
            {
                "q": "5. In Moscow, famous composers, artists, and writers are buried in a special cemetery, and they only must be Russian.",
                "options": [
                    "A. famous composers, artists, and writers are buried in a special cemetery, and they only must be Russian.",
                    "B. there had been buried in a special cemetery famous composers, artists, and writers who have been only Russian",
                    "C. being buried in a special cemetery only for famous composers, artists, and writers who are Russian",
                    "D. a special cemetery for burying only famous Russian composers, artists, and writers",
                    "E. famous Russian composers, artists, and writers are buried in a special cemetery"
                ],
                "correct": 4, 
                "explanation": "Option E is the most concise and logical phrasing."
            },
            {
                "q": "6. By The Fire Side was a very interesting programme with which the students either intended to challenge or abolish the evil deeds in the country.",
                "options": [
                    "A. programme with which the students either intended to challenge or abolish",
                    "B. programme, about which either the students intended to challenge or to abolish",
                    "C. programme that had the intention of either challenging or to abolish",
                    "D. programme, the use of which was either a challenge or it abolished",
                    "E. programme that the students used to challenge or abolish"
                ],
                "correct": 4, 
                "explanation": "Option E uses active voice and clear phrasing: 'programme that the students used to challenge or abolish'."
            },
            {
                "q": "7. The atmosphere in the classroom changed when the rain started to fall outside and the teacher could not get them to pay attention to the lesson after that.",
                "options": [
                    "A. outside and the teacher could not get them to pay attention to the lesson after that",
                    "B. outside, the teacher was unable to bring the class's attention back to the lesson after that.",
                    "C. outside, and the teacher could no longer get the children to pay attention to the lesson",
                    "D. outside, causing them to lose attention to the lesson, despite the teacher's effort",
                    "E. outside, in spite of the teacher's effort was unable to get them to pay attention to the lesson after that."
                ],
                "correct": 1, 
                "explanation": "Option B is the clearest revision, avoiding the run-on nature of the original."
            },
            {
                "q": "8. Of the four seasons in Ghana, Akosua most loves the Harmattan, of which she finds the mild days and cool nights especially appealing.",
                "options": [
                    "A. Harmattan, of which she finds the mild days and cool nights especially appealing",
                    "B. Harmattan; she finds the mild days and cool nights especially appealing",
                    "C. Harmattan, and it is especially the mild days and cool nights that are of appeal",
                    "D. Harmattan; the appeal of the mild days and cool nights especially",
                    "E. Harmattan, especially appealing to Akosua are the mild days and cool nights"
                ],
                "correct": 1, 
                "explanation": "Option B correctly uses a semicolon to connect two related independent clauses."
            },
            {
                "q": "9. Many countries punish citizens who speak out against the government, keeping the U.N. Commission on Human Rights very busy, mostly using torture and imprisonment.",
                "options": [
                    "A. Many countries punish citizens who speak out against the government, keeping the U.N. Commission on Human Rights very busy, mostly using torture and imprisonment.",
                    "B. Many countries, punishing citizens mostly using torture and imprisonment for speaking out against the government, keep the U.N. Commission on Human Rights very busy.",
                    "C. In many countries punishing citizens who speak out against the government, U.N. Commission on Human Rights is kept very busy, mostly using torture and imprisonment.",
                    "D. Using torture and imprisonment, many countries punish citizens who speak out against the government, a situation that keeps the U.N. Commission on Human Rights very busy",
                    "E. Punishing citizens who speak out against the government using torture and imprisonment in many countries, the U.N. Commission on Human Rights is kept very busy"
                ],
                "correct": 3, 
                "explanation": "Option D correctly places the modifier 'Using torture...' with the subject 'many countries'."
            },
            {
                "q": "10. Of all the roads in Ghana, more people drive on the George Walker Bush Highway than on any highway.",
                "options": [
                    "A. more people drive on the George Walker Bush Highway than on any highway.",
                    "B. travellers are driving on the George Walker Bush Highway in the largest numbers.",
                    "C. the largest amount of drivers are on the George Walker Bush Highway.",
                    "D. the George Walker Bush Highway is the more heavily travelled",
                    "E. the George Walker Bush Highway is the most heavily travelled"
                ],
                "correct": 4, 
                "explanation": "Option E correctly uses the superlative 'most' when comparing one road to 'all the roads'."
            },
            {
                "q": "11. Most newspaper editorials in Ghana have argued brilliantly against the Supreme Court's decision on the death penalty.",
                "options": [
                    "A. Most newspaper editorials in Ghana have argued brilliantly against the Supreme Court's decision on the death penalty.",
                    "B. Newspaper editorials in Ghana that brilliantly argued against the Supreme Court's decision on the death penalty",
                    "C. The Supreme Court's decision on the death penalty, brilliantly opposed by newspaper editorials in Ghana.",
                    "D. The Supreme Court's decision on the death penalty being brilliantly opposed in Ghana by newspaper editorials.",
                    "E. Brilliant arguments against the Supreme Court's decision on the death penalty that appeared in newspapers in Ghana."
                ],
                "correct": 0, 
                "explanation": "The original sentence (A) is grammatically correct and complete."
            },
            {
                "q": "12. There is plenty of Achebe's practical advice about life, which every reader can benefit from in his Things Fall Apart.",
                "options": [
                    "A. There is plenty of Achebe's practical advice about life, which every reader can benefit from in his Things Fall Apart.",
                    "B. In Achebe's Things Fall Apart, they give the reader plenty of practical and beneficial advice about life.",
                    "C. Reading Achebe's Things Fall Apart, plenty of practical and beneficial advice about life is offered.",
                    "D. In Things Fall Apart, Achebe offers readers plenty of practical and beneficial advice about life.",
                    "E. Because of offering plenty of practical and beneficial advice about life in Achebe's Things Fall Apart."
                ],
                "correct": 3, 
                "explanation": "Option D is the most direct and active construction."
            },
            {
                "q": "13. Nuclear waste disposal is a growing problem considering that no state permits radioactive material transported on its roads or to bury it Inside its borders.",
                "options": [
                    "A. considering that no state permits radioactive material transported on its roads or to bury it inside its borders",
                    "B. considering that no state permits neither radioactive material transported on its roads or buried inside its borders",
                    "C. because no state permits radioactive material transported on its roads or buried inside its borders",
                    "D. because no state will permit radioactive material not only to be carried on its roads but in addition also buried inside its borders",
                    "E. being that no state had permitted radioactive material to be carried on its roads or buried inside its borders"
                ],
                "correct": 2, 
                "explanation": "Option C maintains parallel structure: 'permits radioactive material transported... or buried'."
            },
            {
                "q": "14. If you wish to truly understand Dan Lartey's concept of Domestication, the letters Dan Lartey wrote to his son should be read.",
                "options": [
                    "A. the letters Dan Lartey wrote to his son should be read.",
                    "B. Dan Lartey's letters to his son should be read",
                    "C. you should have been reading the letters Dan Lartey wrote to his son",
                    "D. you should read his letters to his son",
                    "E. a person should read his letters to his son"
                ],
                "correct": 3, 
                "explanation": "Option D fixes the dangling modifier. 'You' are the one wishing to understand, so 'you' should read."
            },
            {
                "q": "15. Yellowstone, an extremely popular national park, has been described as the noisiest park and also the most tranquil of them.",
                "options": [
                    "A. the noisiest park and also the most tranquil of them",
                    "B. not only the noisiest park, but also more tranquil than any",
                    "C. the noisiest park, at the same time it is the most tranquil park",
                    "D. at once the noisiest and also the most tranquil of them",
                    "E. the noisiest and yet the most tranquil of parks"
                ],
                "correct": 4, 
                "explanation": "Option E provides the best flow and contrast."
            },
            {
                "q": "16. Joojo asked Ama to go to the club with him, this surprised Ama because she thought Joojo would ask Mary.",
                "options": [
                    "A. him, this surprised Ama",
                    "B. him, therefore Ama was surprised",
                    "C. him, surprising Ama",
                    "D. him, which surprised Ama",
                    "E. him, that was surprising to Ama"
                ],
                "correct": 3, 
                "explanation": "Option D ('which surprised Ama') correctly modifies the preceding clause."
            },
            {
                "q": "17. Kasoa suffers from a high crime rate, while it is a very desirable place to live.",
                "options": [
                    "A. Kasoa suffers from a high crime rate, while it is",
                    "B. Although Kasoa suffers from a high crime rate, it is",
                    "C. Kasoa suffering from a high crime rate made it",
                    "D. Kasoa which suffers from a high crime rate, although it is",
                    "E. Kasoa whose rate of crime is high, makes it"
                ],
                "correct": 1, 
                "explanation": "Option B uses 'Although' to correctly introduce the concession."
            },
            {
                "q": "18. Just as the number of applications to the University of Ghana and the University of Cape Coast has grown annually since 2005, so has KNUST's applicant pool risen steadily.",
                "options": [
                    "A. so has KNUST's applicant pool risen steadily",
                    "B. KNUST attracted applicants in steadily rising numbers",
                    "C. KNUST is steadily gaining applicants in its pool",
                    "D. and so then, for KNUST, a rising applicant pool has grown steadily",
                    "E. and like them KNUST's steadily rising pool of applicants"
                ],
                "correct": 0, 
                "explanation": "Option A ('so has KNUST's...') is the correct correlative construction for 'Just as...'."
            },
            {
                "q": "19. Drivers in Tema say that the city is frustrating because of its numerous traffic circles but they have designed it beautifully.",
                "options": [
                    "A. but they have designed it beautifully",
                    "B. although it is beautifully designed",
                    "C. yet it is beautiful in its design",
                    "D. while being designed so beautifully",
                    "E. and pleasing because of its beautiful design"
                ],
                "correct": 1, 
                "explanation": "Option B ('although it is beautifully designed') is the most logical contrast."
            },
            {
                "q": "20. Having a mother who plays in a symphony orchestra and a father who teaches music in high school, the violin and the piano are two of the instruments that John Ahortor learnt at an early age.",
                "options": [
                    "A. the violin and the piano are two of the instruments that John Ahortor learnt at an early age",
                    "B. violin and piano were taught to John Ahortor at an early age",
                    "C. two instruments, the violin and the piano, John Ahortor learnt to play at an early age",
                    "D. at an early age John Ahortor learnt to play both the violin and the piano",
                    "E. John Ahortor learnt playing both the violin and the piano at an early age"
                ],
                "correct": 4, 
                "explanation": "Option E (or D) fixes the dangling modifier. 'John Ahortor' must follow the introductory phrase about the parents."
            },
            {
                "q": "21. A teacher's job is to set a good example for children as well as teaching them the material they need to know.",
                "options": [
                    "A. as well as teaching them",
                    "B. as well as to teach them",
                    "C. and they also teach them",
                    "D. and as well, teach them also",
                    "E. also teaching them"
                ],
                "correct": 1, 
                "explanation": "Option B ('as well as to teach') maintains parallelism with 'to set a good example'."
            },
            {
                "q": "22. This book shows readers not only what might happen if they try to deal with the problem by themselves but it's all right to seek help.",
                "options": [
                    "A. but it's all right to seek help",
                    "B. but explains that help is all right to seek",
                    "C. explaining that it's all right to seek help",
                    "D. and also explains that it's all right to seek help",
                    "E. but also explains that it's all right to seek help"
                ],
                "correct": 4, 
                "explanation": "Option E completes the 'not only... but also' construction."
            },
            {
                "q": "23. The book's descriptions of the country and the town, in addition to its recent release as a movie, explains why sales of the book have suddenly boomed.",
                "options": [
                    "A. explains why sales of the book have suddenly boomed",
                    "B. explain the sudden boom in its sales",
                    "C. are the reason why the book's sales having boomed suddenly",
                    "D. explain why it has suddenly boomed it's sales",
                    "E. is the explanation for the sudden boom in sales"
                ],
                "correct": 1, 
                "explanation": "Option B uses the plural verb 'explain' to agree with the subject 'descriptions'."
            },
            {
                "q": "24. Jogging a mile uses the same number of calories as if you walk two miles.",
                "options": [
                    "A. as if you walk",
                    "B. as to walk",
                    "C. than to walk",
                    "D. as walking",
                    "E. as it does when walking"
                ],
                "correct": 3, 
                "explanation": "Option D ('as walking') maintains parallelism with 'Jogging'."
            },
            {
                "q": "25. The pollution of the Prah River was discovered, residents of the town posted notices urging people to boil their water.",
                "options": [
                    "A. The pollution of the Prah River was discovered,",
                    "B. The Prah River's pollution being discovered,",
                    "C. When having made the discovery of the pollution of the water in the Prah River;",
                    "D. After discovering pollution in the Prah River,",
                    "E. Pollution was discovered in the Prah River,"
                ],
                "correct": 3, 
                "explanation": "Option D creates a logical dependent clause ('After discovering pollution...')."
            },

            # --- SECTION A: ERROR RECOGNITION (Q26-43) ---
            {
                "q": "26. [A] Kombianus' lifelong career as a drug dealer and his [B] murder of three BNI agents [C] proves that [D] he is one of the most notorious criminals... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 2, 
                "explanation": "C ('proves') should be 'prove' (plural) because the subject is 'career and murder'."
            },
            {
                "q": "27. Notice that this cereal [A] not only costs more than the other one, [B] plus being packed in a [C] smaller container. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('plus being') is incorrect. The correlative conjunction for 'not only' is 'but also'."
            },
            {
                "q": "28. Although I can't concur [A] in the blogger's opinions, I am grateful to have seen them expressed [B] so [C] eloquently. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('in') should be 'with'. You concur *with* an opinion."
            },
            {
                "q": "29. Although Kwabena... has the highest grade-point average... his [C] score on the GEMP exam was far lower than [D] Charles. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 3, 
                "explanation": "D ('Charles') is an illogical comparison. It should be 'Charles's' (comparing score to score)."
            },
            {
                "q": "30. High school students who wish to become a [A] professional athlete should remember that the [B] odds against being successful... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('professional athlete') should be plural ('professional athletes') to agree with 'students'."
            },
            {
                "q": "31. [A] Following traditional family values [B] have become one of the distinct differences between my [C] parents and me. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('have become') should be 'has become'. The subject is the singular phrase 'Following traditional family values'."
            },
            {
                "q": "32. Susuana hopes to convince Pearl that she [A] neither is interested in going out with other boys [B] or that she ever loved anyone else... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('or') should be 'nor'. The correct structure is 'neither... nor'."
            },
            {
                "q": "33. Foremost among the voters' concerns [A] is the problem of what to do about waste disposal and the [B] issues surrounding the construction... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('is') should be 'are'. The subject is compound ('the problem... and the issues')."
            },
            {
                "q": "34. The [A] plight of immigrants... [B] are no less [C] heartbreaking than the suffering of the migrant workers... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('are') should be 'is'. The subject is the singular 'plight'."
            },
            {
                "q": "35. A number of the athletes [A] which participated in last year's Olympics Games were found to [B] have used steroids... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('which') should be 'who' when referring to people (athletes)."
            },
            {
                "q": "36. Carolyn's mother was born and raised in Baltimore, [A] where she attended high school and [B] college, [C] got married and gave birth to Carolyn... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 4, 
                "explanation": "E (No Error). The sentence structure is correct."
            },
            {
                "q": "37. The [A] present senior class has a greater number of scholarship winners than [B] last year. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('last year') is an illogical comparison. It should be 'last year's class' (comparing class to class)."
            },
            {
                "q": "38. My parents instilled their moral values [A] for my sister and me, [B] enabling us... to know right from wrong. [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('for') should be 'in'. You instill values *in* someone."
            },
            {
                "q": "39. The earliest pirates... [A] rustled cattle, [B] smoked the meat and [C] were stealing gold and jewels... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 2, 
                "explanation": "C ('were stealing') breaks the parallel structure. It should be 'stole' (rustled, smoked, stole)."
            },
            {
                "q": "40. As Kesewaa opened the refrigerator, she [A] instantly noticed that a huge chunk of chocolate icing had been [B] bit off the birthday cake... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('bit') should be 'bitten' (past participle of bite)."
            },
            {
                "q": "41. In his memoir, Mensah tells stories about the time... when he [B] is having to deliver newspapers... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('is having') should be 'had'. The sentence is in the past tense ('before he entered high school')."
            },
            {
                "q": "42. Of the two Hemingway novels I have read, I like A Farewell to Arms the [B] best... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 1, 
                "explanation": "B ('best') should be 'better'. Use comparative ('better') for two items, superlative ('best') for three or more."
            },
            {
                "q": "43. Child psychologists will tell you that young children [A] which are pushed into activities [B] prematurely... [E] No Error",
                "options": ["A", "B", "C", "D", "E"],
                "correct": 0, 
                "explanation": "A ('which') should be 'who' for children."
            },

            # --- SECTION A: SENTENCE COMPLETION (Q44-65) ---
            {
                "q": "44. Unfortunately, in developing countries rapid economic growth often _____ overexploitation of natural resources and _____ the distribution of wealth.",
                "options": ["A. halts... indiscriminate", "B. holds off... inadequate", "C. leads to... inequitable", "D. continues... evenhanded", "E. goes beyond... ungrateful"],
                "correct": 2, 
                "explanation": "Economic growth often 'leads to' overexploitation and an 'inequitable' (unfair) distribution of wealth."
            },
            {
                "q": "45. The Apache are a _____ society, where husbands typically move into wives' dwellings and women take the leadership role in family affairs.",
                "options": ["A. sedentary", "B. defunct", "C. fragmented", "D. matrilineal", "E. xenophobic"],
                "correct": 3, 
                "explanation": "A society where lineage/leadership is female-oriented is 'matrilineal'."
            },
            {
                "q": "46. _____ James Baldwin, who wrote of black Americans as being in a perpetual state of rage, Mr. Cose asserts that few human beings could _____ the psychic toll of uninterrupted anger.",
                "options": ["A. Corroborating...endure", "B. Refuting...enhance", "C. Dismissing...refine", "D. Challenging...survive", "E. Upholding...weather"],
                "correct": 3, 
                "explanation": "Mr. Cose is 'Challenging' Baldwin's view by arguing that few could 'survive' such a state."
            },
            {
                "q": "47. Rather than allowing these dramatic exchanges between her characters to develop fully, Ms. Norman unfortunately tends to _____ the discussions involving the two women.",
                "options": ["A. exacerbate", "B. protract", "C. truncate", "D. augment", "E. elaborate"],
                "correct": 2, 
                "explanation": "'Truncate' means to cut short, which contrasts with 'develop fully'."
            },
            {
                "q": "48. The _____ with which musicians and lovers of fine instruments _____ Paul Irvin's professional services attests to his great expertise...",
                "options": ["A. hesitation...acquire", "B. avidness...solicit", "C. persistence...supersede", "D. harmony...conjure", "E. vehemence...reject"],
                "correct": 1, 
                "explanation": "Their 'avidness' (eagerness) to 'solicit' (ask for) his services shows his high reputation."
            },
            {
                "q": "49. Deeply _____ by the insult to his dignity, he maintained that no true gentleman would accept such an _____ calmly.",
                "options": ["A. mortified...opportunity", "B. incensed...affront", "C. puzzled...honour", "D. shamed...iconoclasm", "E. gratified...admonition"],
                "correct": 1, 
                "explanation": "He was 'incensed' (angered) by the 'affront' (insult)."
            },
            {
                "q": "50. Learned though she was, Ama's _____ never degenerated into _____.",
                "options": ["A. erudition...arrogance", "B. knowledge...ignorance", "C. scholarship...research", "D. speculation...thought", "E. education...inquiry"],
                "correct": 0, 
                "explanation": "Her 'erudition' (learning) didn't become 'arrogance'."
            },
            {
                "q": "51. Biologists categorise many of the world's environments as deserts: regions where the _____ availability of some key factor... places sharp constraints on the existence of living things.",
                "options": ["A. ready", "B. gradual", "C. limited", "D. nearby", "E. unprecedented"],
                "correct": 2, 
                "explanation": "Deserts are defined by the 'limited' availability of water/nutrients."
            },
            {
                "q": "52. The Americans and the British seem to have a dog-in-the-manger attitude toward the island of Malta, no longer needing it themselves but nevertheless wishing to _____ it to others.",
                "options": ["A. interpret", "B. offer", "C. deny", "D. praise", "E. reveal"],
                "correct": 2, 
                "explanation": "A 'dog-in-the-manger' attitude means preventing others from having what you don't need. So they wish to 'deny' it to others."
            },
            {
                "q": "53. Increasingly silent and withdrawn, he changed from a fluent, articulate speaker to someone who gave only _____ answers to any questions asked of him.",
                "options": ["A. bookish", "B. effusive", "C. idiomatic", "D. pretentious", "E. monosyllabic"],
                "correct": 4, 
                "explanation": "'Monosyllabic' answers (one word) fits someone who is silent and withdrawn."
            },
            {
                "q": "54. When you learn archaeology solely from lectures, you get only _____ sense of the concepts... but when you hold a 5,000-year-old artifact... you have a chance to involve your senses.",
                "options": ["A. an invalid", "B. an anachronistic", "C. an abstract", "D. a specious", "E. a tangential"],
                "correct": 2, 
                "explanation": "Lectures give an 'abstract' sense, while holding an object involves the senses directly."
            },
            {
                "q": "55. Paradoxically, while it is relatively easy to prove a fraudulent work of art is a fraud, it is often virtually impossible to prove that an authentic one is _____.",
                "options": ["A. unpretentious", "B. objective", "C. impartial", "D. dubious", "E. genuine"],
                "correct": 4, 
                "explanation": "It's hard to prove an authentic one is 'genuine'."
            },
            {
                "q": "56. Stephen Appiah's former casino in Dansoman was once the most _____ gambling palace in the city, easily outglittering its competitors.",
                "options": ["A. professional", "B. speculative", "C. ostentatious", "D. lucrative", "E. restrained"],
                "correct": 2, 
                "explanation": "'Ostentatious' matches 'outglittering' (showy/flashy)."
            },
            {
                "q": "57. American culture now stigmatises, and sometimes even heavily _____, behaviour that was once taken for granted: overt racism, cigarette smoking, the use of sexual stereotypes.",
                "options": ["A. advocates", "B. penalises", "C. ignores", "D. indoctrinates", "E. advertises"],
                "correct": 1, 
                "explanation": "Culture stigmatises and 'penalises' these behaviors."
            },
            {
                "q": "58. Determined to hire employees on the basis of their merits rather than on the basis of their family connections, Professor Dadson refused to _____ nepotism...",
                "options": ["A. Obscure", "B. Proscribe", "C. Countenance", "D. Misrepresent", "E. discern"],
                "correct": 2, 
                "explanation": "He refused to 'countenance' (tolerate/approve) nepotism."
            },
            {
                "q": "59. Because the damage to his car had been _____, Michael decided he wouldn't bother to report the matter to his insurance company.",
                "options": ["A. intermittent", "B. gratuitous", "C. negligible", "D. spontaneous", "E. significant"],
                "correct": 2, 
                "explanation": "If he didn't bother reporting it, the damage must have been 'negligible' (minor)."
            },
            {
                "q": "60. Even when being _____ in method, people can come up with incorrect answers by basing their arguments on false premises.",
                "options": ["A. original", "B. logical", "C. slipshod", "D. realistic", "E. careless"],
                "correct": 1, 
                "explanation": "Even if your method is 'logical', false premises lead to incorrect answers."
            },
            {
                "q": "61. When clay dries out, it loses its plasticity and becomes less _____.",
                "options": ["A. synthetic", "B. expensive", "C. malleable", "D. tangible", "E. brittle"],
                "correct": 2, 
                "explanation": "Plasticity means moldability. Losing it makes it less 'malleable'."
            },
            {
                "q": "62. For many years an unheralded researcher, Barbara McClintock gained international _____ when she won the Nobel Prize...",
                "options": ["A. condemnation", "B. notoriety", "C. renown", "D. affluence", "E. camaraderie"],
                "correct": 2, 
                "explanation": "Winning the Nobel Prize brings 'renown' (fame)."
            },
            {
                "q": "63. Rather than feeling toward Miss Havisham the _____ due a benefactor, Estella became resentful and even _____ to her patron.",
                "options": ["A. esteem...effusive", "B. obligation...dutiful", "C. altruism...quarrelsome", "D. gratitude...hostile", "E. condescension...benign"],
                "correct": 3, 
                "explanation": "She should feel 'gratitude', but instead became 'hostile'."
            },
            {
                "q": "64. Despite the heated discussions of recent months, observers say that the administration and the developer have made progress... and are close to _____ on a purchase price.",
                "options": ["A. amicable...haggling", "B. acrimonious...defaulting", "C. heated...agreeing", "D. fruitful...settling", "E. constructive...compromising"],
                "correct": 3, 
                "explanation": "They are close to 'settling' on a price."
            },
            {
                "q": "65. When I listened to her cogent arguments, all my _____ were _____ and I was forced to agree with her point of view.",
                "options": ["A. senses...stimulated", "B. opinions...confirmed", "C. preconceptions...substantiated", "D. questions...interpolated", "E. doubts...dispelled"],
                "correct": 4, 
                "explanation": "Cogent (convincing) arguments would cause 'doubts' to be 'dispelled'."
            },
            
            # --- COMPREHENSION PASSAGE ---
            {
                "q": "PASSAGE:\nScientists have long debated how the ancestors of birds evolved the ability to fly. The ground-up theory assumes they were fleet-footed ground dwellers that captured prey by leaping... Ken Dial saw a pattern in how young pheasants... ran along behind their parents... 'They jumped up like popcorn'... Ken settled on the Chukar Partridge... The rancher was incredulous... 'What are those birds doing on the ground? They hate to be on the ground!'... Ken realized they preferred elevated perches... Young Terry Dial observed: 'The birds are cheating! Instead of flying... they were using their legs... running right up the side of a hay bale'... Ken called the technique WAIR (wing-assisted incline running)...\n\n66. As used in line 4 of paragraph 1, 'challenged' most nearly means:",
                "options": ["A. dared", "B. required", "C. disputed with", "D. competed with", "E. questioned"],
                "correct": 0, "explanation": "In the context 'graduate students challenged him to come up with new data', 'dared' or 'provoked' fits best."
            },
            {
                "q": "67. As used in line 1 of paragraph 5, 'document' most nearly means:",
                "options": ["A. portray", "B. record", "C. publish", "D. process", "E. file"],
                "correct": 1, "explanation": "To 'document' in a scientific context means to 'record' or provide evidence for."
            },
            {
                "q": "68. After Ken Dial had his 'aha' moment (paragraph 3, line 5), he:",
                "options": ["A. tried to train the birds to fly to their perches", "B. studied videos to determine why the birds no longer hopped", "C. observed how the birds dealt with gradually steeper inclines", "D. consulted with other researchers who had studied Chukar Partridges", "E. abandoned the experiment"],
                "correct": 2, "explanation": "Paragraph 4 says: 'Ken came up with a series of ingenious experiments... ramps tilted at increasing angles'."
            },
            {
                "q": "69. What can reasonably be inferred about gliding animals from the passage?",
                "options": ["A. Their young tend to hop along beside their parents instead of flying beside them", "B. Their method of locomotion is similar to that of ground birds", "C. They use the ground for feeding more often than for perching", "D. They do not use a flapping stroke to aid in climbing slopes", "E. They evolved before ground birds"],
                "correct": 3, "explanation": "Paragraph 6 mentions 'flapping flight stroke... (something gliding animals don't do)'."
            },
            {
                "q": "70. The passage identifies which of the following as a factor that facilitated the baby Chukars' traction on steep ramps?",
                "options": ["A. The speed with which they climbed", "B. The position of their flapping wings", "C. The alternation of wing and foot movement", "D. Their continual hopping motions", "E. The texture of the ramp"],
                "correct": 1, "explanation": "Paragraph 4: 'They aimed their flapping down and backward, using the force... to keep their feet firmly pressed'."
            },

            # --- SECTION B: LOGICAL REASONING ---
            {
                "q": "71. Find the appropriate item which will replace 'X': 7, 11, 19, 35, 67, X",
                "options": ["A. 99", "B. 131", "C. 134", "D. 445", "E. 129"],
                "correct": 1, "explanation": "Differences: 4, 8, 16, 32. Next difference is 64. 67 + 64 = 131."
            },
            {
                "q": "72. Find X: 8, 22, 64, 190, 568, X",
                "options": ["A. 1702", "B. 1315", "C. 7134", "D. 6445", "E. 1704"],
                "correct": 0, "explanation": "Pattern: x3 - 2. (8*3)-2=22; (22*3)-2=64... (568*3)-2 = 1704 - 2 = 1702."
            },
            {
                "q": "73. Find X: 5760, 2880, 960, 240, 48, X",
                "options": ["A. 17", "B. 8", "C. 12", "D. 16", "E. 24"],
                "correct": 1, "explanation": "Divisors: /2, /3, /4, /5. Next is /6. 48 / 6 = 8."
            },
            
            # --- LOGIC PUZZLE: RESTAURANT ---
            {
                "q": "PUZZLE:\nAduane Superb stays open Mon-Sat, closed Sun.\n- Mon: Lunch only.\n- Tue/Thu: Lunch only.\n- Wed/Fri/Sat: Dinner only.\n- Plants watered 2 days/week (never consecutive, never same day as polish).\n- Floors polished Mon and 2 other days (never consecutive, never same day as water).\n\n81. According to the schedule, the restaurant's floors are polished on either:",
                "options": ["A. Tuesday or Wednesday", "B. Tuesday or Thursday", "C. Wednesday or Thursday", "D. Thursday or Friday", "E. Thursday or Saturday"],
                "correct": 3, "explanation": "Polished Mon. Cannot be consecutive, so not Tue. Must be Wed or Thu? If Wed, then Fri (to be 3 days non-consecutive). If Thu, then Sat. Let's look closer at constraints."
            },
            {
                "q": "82. If dinner is served on the same day as plants are watered, which of the following is correct?",
                "options": ["A. Plants are watered on Tuesday.", "B. Floors are polished on Thursday.", "C. Plants are watered on Wednesday.", "D. Floors are polished on Wednesday.", "E. Plants are watered on Saturday."],
                "correct": 2, "explanation": "Dinner is served Wed, Fri, Sat. Plants watered on a dinner day. If plants Wed -> Polish cannot be Wed. Polish is Mon. Next polish Fri? (Mon, Wed, Fri - No, polish cant be same as water). Logic requires detailed mapping."
            },

            # --- LOGIC PUZZLE: CARDS ---
            {
                "q": "PUZZLE:\nFour players Aaron, Bob, Cyril, Dave holding 4 cards each. Each has Ace, King, Queen, Jack. All have all suits.\nI. Aaron has Ace of spades and Queen of diamonds.\nII. Bob has Ace of clubs and King of diamonds.\nIII. Cyril has Queen of clubs and King of spades.\nIV. Dave has Jack of clubs.\n\n106. Who has Ace of Diamonds?",
                "options": ["A. Aaron", "B. Bob", "C. Cyril", "D. Dave", "E. Cannot determine"],
                "correct": 3, "explanation": "Aaron has Ace(S). Bob has Ace(C). Cyril must have an Ace. Dave must have an Ace. If Cyril has King(S) and Queen(C)... needs deduction of remaining suits."
            },

            # --- SECTION C: QUANTITATIVE METHODS ---
            {
                "q": "DATA TABLE:\nResistance to COVID-19\n- Africans: High Risk(90), Med(25), Low(10), Total(125)\n- European: High(55), Med(35), Low(59), Total(149)\n- Arabs: High(60), Med(20), Low(20), Total(100)\n- Grand Total: 374\n\n121. What is the probability of a low-risk European being randomly selected? (3 decimal places)",
                "options": ["A. 0.135", "B. 0.053", "C. 0.158", "D. 0.185", "E. 0.200"],
                "correct": 2, "explanation": "Low Risk European = 59. Total = 374. 59/374 ≈ 0.1577 -> 0.158."
            },
            {
# --- QUANTITATIVE: TABLE 1 (Exact Data) ---
                "type": "passage",
                "text": """DATA TABLE: Risk of HBV infection among various races (Table 1)
-------------------------------------------------------
RACE       | High Risk | Medium Risk | Low Risk | Total
-------------------------------------------------------
Africans   |    90     |     25      |    10    |  125
European   |    55     |     35      |    59    |  149
Arabs      |    60     |     20      |    20    |  100
-------------------------------------------------------
Total      |   205     |     80      |    89    |  374
-------------------------------------------------------""",
                "q": "121. What is the probability that a randomly selected person is a low-risk European? (3 decimal places)",
                "options": ["A. 0.135", "B. 0.053", "C. 0.158", "D. 0.185"],
                "correct": 2, "explanation": "Low Risk Europeans = 59. Total population = 374. \nProbability = 59 / 374 = 0.15775... \nRounded to 3 d.p. = 0.158"
            },
            {
                "type": "standard",
                "q": "122. What is the probability that someone randomly selected will be an Arab given that he has medium risk?",
                "options": ["A. 0.250", "B. 0.025", "C. 0.398", "D. 0.053"],
                "correct": 0, "explanation": "Formula: P(Arab | Medium). \nLook at the 'Medium Risk' column. Total Medium = 80. \nNumber of Arabs in that column = 20. \nProb = 20 / 80 = 0.25."
            },
            {
                "q": "122. What is the probability that someone randomly selected will be an Arab given that he has medium risk?",
                "options": ["A. 0.250", "B. 0.025", "C. 0.398", "D. 0.053", "E. 0.200"],
                "correct": 0, "explanation": "Total Medium Risk = 25+35+20 = 80. Arabs with Medium Risk = 20. Prob = 20/80 = 0.25."
            },
            {
                "q": "123. What is the probability that a selected African will be high risk?",
                "options": ["A. 0.720", "B. 0.270", "C. 0.241", "D. 0.439", "E. 0.500"],
                "correct": 0, "explanation": "Selected African (Total 125). High Risk African = 90. Prob = 90/125 = 0.72."
            },
            {
                "q": "124. The major difference between Standard Deviation (SD) and Standard Error (SE) is:",
                "options": ["A. SE refers to population, SD to sample", "B. SD measures scatter/dispersion about the mean", "C. SE is calculated from SD", "D. SE measures precision while SD measures scatter", "E. All of the above"],
                "correct": 3, "explanation": "SD quantifies variation within a set of data (scatter). SE quantifies the precision of the mean estimate."
            },
            {
                "q": "125. Mean = 150 mg/l, SD = 15.0, SE = 6.5. 95% Confidence (z=1.96). Lower and Upper bounds?",
                "options": ["A. 126.74 - 260.78", "B. 137.26 - 162.74", "C. 240.6 - 362.2", "D. 294.0 - 269.9", "E. 135.0 - 165.0"],
                "correct": 1, "explanation": "95% CI = Mean ± (1.96 * SE). 150 ± (1.96 * 6.5) = 150 ± 12.74. Lower=137.26, Upper=162.74."
            },
            {
                "q": "130. If log10(7) = a, then log10(1/70) will be?",
                "options": ["A. -(1+a)", "B. 1/10a", "C. a/10", "D. (1+a)^-1", "E. -a"],
                "correct": 0, "explanation": "log(1/70) = log(1) - log(70) = 0 - log(7*10) = -(log 7 + log 10) = -(a + 1)."
            },
            {
                "q": "131. Solve for x and y: x + 2y = 9; 3x - 4y = -33",
                "options": ["A. x=2, y=7", "B. x=3, y=-6", "C. x=-3, y=6", "D. x=9, y=12", "E. x=0, y=0"],
                "correct": 2, "explanation": "Multiply eq1 by 2: 2x + 4y = 18. Add to eq2: (3x - 4y) + (2x + 4y) = -33 + 18. 5x = -15 -> x = -3. Sub x into eq1: -3 + 2y = 9 -> 2y = 12 -> y = 6."
            }           
        ]
    }
}
# --- 3. SESSION STATE (STATE-SYNC) ---
if 'view' not in st.session_state: st.session_state.view = "Lobby"
if 'completed_sections' not in st.session_state: st.session_state.completed_sections = {} # Stores scores
if 'answers' not in st.session_state: st.session_state.answers = {k: {} for k in EXAM_DATA}
if 'flags' not in st.session_state: st.session_state.flags = {k: [] for k in EXAM_DATA} # Added flags key
if 'start_times' not in st.session_state: st.session_state.start_times = {}

# --- 4. CALCULATING SCORES ---
def calculate_section_score(sec_key):
    data = EXAM_DATA[sec_key]["questions"]
    user_answers = st.session_state.answers[sec_key]
    correct_count = 0
    for i, q in enumerate(data):
        if user_answers.get(i) == q["options"][q["correct"]]:
            correct_count += 1
    return correct_count, len(data)

# --- 5. VIEWS ---

# 5A. LOBBY VIEW
if st.session_state.view == "Lobby":
    st.title("🏛️ GEMP 2026 Unified Portal")
    
    total_score = sum([v[0] for v in st.session_state.completed_sections.values()])
    total_qs = sum([v[1] for v in st.session_state.completed_sections.values()])
    
    if total_qs > 0:
        st.metric("OVERALL SCORE", f"{total_score} / {total_qs}", f"{round((total_score/total_qs)*100, 1)}%")

    cols = st.columns(3)
    for i, (key, info) in enumerate(EXAM_DATA.items()):
        with cols[i]:
            with st.container(border=True):
                st.subheader(info["title"])
                st.caption(info["description"]) # KEY FIXED HERE
                
                if key in st.session_state.completed_sections:
                    s, t = st.session_state.completed_sections[key]
                    st.success(f"Score: {s}/{t} ({round((s/t)*100, 1)}%)")
                    if st.button(f"Review {key}", key=f"rev_btn_{key}"):
                        st.session_state.view = f"Review_{key}"
                        st.rerun()
                else:
                    if st.button(f"🚀 Begin {key}", key=f"btn_{key}", use_container_width=True):
                        st.session_state.start_times[key] = time.time()
                        st.session_state.view = key
                        st.session_state[f"ptr_{key}"] = 0 # Initialize pointer
                        st.rerun()

# 5B. EXAM VIEW (Fixed Timer & Score Logic)
elif st.session_state.view in EXAM_DATA:
    sec = st.session_state.view
    data = EXAM_DATA[sec]
    # Initialize pointer if missing
    if f"ptr_{sec}" not in st.session_state: st.session_state[f"ptr_{sec}"] = 0
    ptr = st.session_state[f"ptr_{sec}"]
    
    # Live Sidebar
    with st.sidebar:
        elapsed = time.time() - st.session_state.start_times[sec]
        rem = data["time_limit"] - elapsed # KEY FIXED HERE
        
        # Auto-Submit if time up
        if rem <= 0:
            score, total = calculate_section_score(sec)
            st.session_state.completed_sections[sec] = (score, total)
            st.session_state.view = "Lobby"
            st.rerun()

        # High-Fidelity Timer
        m, s = divmod(int(rem), 60)
        h, m = divmod(m, 60)
        st.header(f"⏱️ {h:02d}:{m:02d}:{s:02d}")
        
        st.divider()
        st.write("Navigator")
        nav_cols = st.columns(4)
        for i in range(len(data["questions"])):
            icon = "⚪"
            if i in st.session_state.flags[sec]: icon = "🚩"
            elif i in st.session_state.answers[sec]: icon = "🔵"
            
            if nav_cols[i%4].button(f"{icon}{i+1}", key=f"nav_{sec}_{i}"):
                st.session_state[f"ptr_{sec}"] = i
                st.rerun()

        st.divider()
        if st.button("🏁 Submit Section", type="primary"):
            score, total = calculate_section_score(sec)
            st.session_state.completed_sections[sec] = (score, total)
            st.session_state.view = "Lobby"
            st.rerun()

    # Main Question UI
    q_item = data["questions"][ptr]
    st.title(data["title"])
    with st.container(border=True):
        st.write(f"**Question {ptr+1} of {len(data['questions'])}**")
        st.markdown(f"### {q_item['q']}")
        
        current_ans = st.session_state.answers[sec].get(ptr)
        choice = st.radio("Select an option:", q_item["options"], 
                          index=q_item["options"].index(current_ans) if current_ans else None,
                          key=f"q_{sec}_{ptr}")
        
        if choice:
            st.session_state.answers[sec][ptr] = choice

    # Footer Controls
    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        if st.button("⬅️ Previous", disabled=(ptr == 0)):
            st.session_state[f"ptr_{sec}"] -= 1
            st.rerun()
    with c2:
        if st.button("🚩 Flag Question"):
            if ptr in st.session_state.flags[sec]: st.session_state.flags[sec].remove(ptr)
            else: st.session_state.flags[sec].append(ptr)
            st.rerun()
    with c3:
        if st.button("Next ➡️", disabled=(ptr == len(data["questions"])-1)):
            st.session_state[f"ptr_{sec}"] += 1
            st.rerun()
            
    time.sleep(1) # Keeps timer ticking
    st.rerun()

# 5C. REVIEW MODULE
elif st.session_state.view.startswith("Review_"):
    sec = st.session_state.view.replace("Review_", "")
    st.title(f"Review: {EXAM_DATA[sec]['title']}")
    if st.button("Back to Lobby"): st.session_state.view = "Lobby"; st.rerun()
    
    for i, q in enumerate(EXAM_DATA[sec]["questions"]):
        with st.expander(f"Question {i+1}"):
            st.write(q["q"])
            ua = st.session_state.answers[sec].get(i, "No Answer")
            ca = q["options"][q["correct"]]
            if ua == ca: st.success(f"Correct: {ua}")
            else: 
                st.error(f"Your Answer: {ua}")
                st.success(f"Correct Answer: {ca}")
            st.info(f"Explanation: {q['explanation']}")
