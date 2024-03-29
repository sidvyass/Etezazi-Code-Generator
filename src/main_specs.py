"""Contains on the data strucs that we need to make use of the GUI"""
certs_dict = {
    "oem" : [
        "N/A",
        "Boeing  (BAC)",
        "Northrop Grumman (NGC)",
        "Sikorsky",
        "Lockheed Martin (LMCO)",
        "General Dynamics",
        "Spirit Aerosystem (SPS)",
        "Bombardier (BABS)",
        "HARWARE/STANDARD COMPONENTS",
        "GULFSTREAM",
    ]
,
    "material" : [
        "N/A",
        "Aluminium",
        "Steel/CRES",
        "Titanium",
        "Copper",
        "Nickel"
    ]
,
    "ndt" : [
        "N/A",
        "PENETRANT INSPECT PER BAC5423",
        "MAG PARTICLE INSPECT PER BAPS 176-004 CLASS A",
        "INSPECTION PENETRANT,ETCH PRIOR ASTM E1417, GT23A, GP17G.",
        "PENETRANT INSPECT PER ACS-PRS-7005, CLASS AA IN INDICATED AREAS AND CLASS A IN REMAINDER",
        "INSPECTION, PENETRANT PER MIL-I-6866",
        "MAGNETIC PARTICLE INSPECT PER BAC5424, REV U, CLASS B ",
        "INSPECTION BY PENETRANT GR A TYPE 1 PER ASTM E 1417",
        "PENETRANT INSPECT PER CSTI002 AFTER MACHINING AND BEFORE SURFACE FINISH IS APPLIED",
        "USI",
        "PENETRANT INSPECTION PER PS21202, CLASS A",
        "INSPECTION, FLUORESCENT PENETRANT  PER MIL-I-6866",
        "MAGNETIC INSPECTION PER BAC5424, CLASS B",
        "INSPECTION, MAGNETIC PARTICLE PER NGT23K",
        "ULTRASONIC INSPECT PER BAC5439, CLASS B.",
        "MAGNETIC PARTICLE INSPECT PER BAC 5424, CLASS A",
        "PENETRANT INSPECT PER MIL-STD-1907, GRADE A"
        ]
,
    "anodize" : [
        "N/A",
        "F-17.31 BORIC ACID-SULFURIC ACID ANODIZE IN ACCORDANCE WITH BAC 5632, CLASS 1 OR CLASS 5 OR CHROMIC ACID ANODIZE AT 22 VOLTS IN ACCORDANCE WITH BAC 5019, CLASS 3 OR CLASS 5.",
        "SULFURIC ACID ANODIZE IN ACCORDANCE WITH MIL-A-8625, TYPE II, CLASS 1",
        "CHROMIC ACID ANODIZE PER BAC5019, OR MIL–A–8625, TYPE I",
        "PHOSPHORIC ACID ANODIZE IN ACCORDANCE WITH BAC5555",
        "COATING ANODIZE, SULFURIC ACID, NON DYED,SEALED IN 5% AQUEOUS SOLUTION OF  SODIUM DICHROMATE PER  MIL-A-8625TY2CL1",
        "PASSIVATE  PER BAPS 180-015",
        "ANODIZE IN ACCORDANCE WITH BAC5019, CLASS 3",
        "F-14.251 - APPLY DIRECTIONAL COARSE GRAIN BUFF SATIN FINISH TO THE SPECIFIED DECORATIVESURFACE USING 120 GRIT ALUMINUM OXIDE OR EQUIVALENT & SULFURIC ACID ANODIZE",
        "3220 - COATING, INTEGRAL FUEL TANK, APPLICATION OF TRANSLUCENT CHROME YELLOW, PER GC130AS2B, GSS4306,  MIL-C-27725TY2CL, COATING,ANODIZE,SULFURIC ACID,  NON DYED,SEALED IN 5% AQUEOUS, SOLUTION OF SODIUM DICHROMATE  OR POTASSIUM DICHROMATE, PER MIL-A-8625TY2CL1. ",
        "PASSIVATE PER AMS2700",
        "ANODIZE PER SS8483 MIL-A-8625 TY II B, OPTIONAL TY I C",
        "PASSIVATE IN ACCORDANCE WITH BAC5625 REV E, METHOD II",
        "ANODIC COATING, CHROMIC ACID, OF ALUMINIUM & ITS ALLOYS PER MIL-A-8625, TY 1 OR IB, CL 1.",
        "PHOSPHATE-FLUORIDE COATING IN ACCORDANCE WITH BAC5861",
        "F-14.801 - 1) CLEAN IN ACCORDANCE WITH BAC5753 2) APPLY A UNIFORM DIRECTIONAL COARSE GRAIN SATIN FINISH TO THE SPECIFIED DECORATIVE SURFACE USING 120 GRIT ABRASIVE ",
        "PASSIVATION OF CORROSION, RESISTANT STEEL (TYPE 300 AND 400 SERIES) AND PRECIPITATION HARDENABLE STAINLESS STEEL , EXCEPT A-286  PER MIL-S-5002, GSS7021",
        "ANODIZE, HARDCOAT, UNSEALED PER MIL-A-8625 TYPE 3, GSS9031",
        " 1. [F-17.35] Boric acid-sulfuric acid anodize in accordance with BAC5632, Class 1 or Class 5 or chromic acid anodize at 22 volts in accordance with BAC5019, Class 3 or Class 5.",
        "[F-17.01]: Treat in accordance with MIL-C-5541 (colored film) or MIL-A-8625 Type I, Class 1 (chromic acid anodize), except seal in dilute chromate solution in accordance with BAC5019.",
        "[F-2.20] ANODIZE IN ACCORDANCE WITH MIL-PRF-8625, TYPE I OR TYPE IC (PREFERRED), CLASS 1. (F- 2.20 PER D2-5000 MANDATORY FOR BOEING AND THEIR SUBCONTRACTORS)",
        "[F-18.13]: Chromic acid anodize in accordance with MIL-A-8625, Type I, Class 1, except seal in dilute chromate solution in accordance with BAC5019.",
        "Chromic acid anodize at 22 volts and seal in dilute chromate solution in accordance with BAC5019, Class 3.",
        "[F-17.50]: BORIC ACID-SULFURIC ACID ANODIZE IN ACCORDANCE WITH BAC 5632, CLASS 5 OR APPLY CHEMICAL CONVERSION COATING TO ALL SURFACES IN ACCORDANCE WITH MIL-C-5541, CLASS 1A OR BAC5719, CLASS A OR CLASS C.",
        "CONVERSION COAT PER PS 13209 OR 13204",
        "MIL–C–5541, Class 3"
    ]
,
    "chemfilm" : [
        "N/A",
        "ALODINE 60 IN ACCORDANCE WITH BAC5719, TYPE I, CLASS D",
        "CADMIUM PLATE IN ACCORDANCE WITH QQ-P-416, TYPE II, CLASS 2 OR BAC5701,TYPE II, CLASS 2",
        "[F-17.07] APPLY CHEMICAL CONVERSION COATING TO ALL SURFACES IN ACCORDANCE WITH MIL-C-5541, CLASS 1A OR BAC 5719, CLASS A OR CLASS C.",
        "APPLY CHEMICAL CONVERSION COATING PER MIL-DTL-5541, CL3",
        "APPLY CHEMICAL CONVERSION COATING TO EXTERIOR SURFACES PER MIL-C-5541CL3.",
        "APPLY MIL-PRF-46010 SOLID FILM LUBRICANT TO INDICATED SURFACE",
        "TREAT SURFACE IN ACCORDANCE WITH MIL-C-5541, COLORED COATING.",
        "COATING,CHEMICAL FILM,ALODINE 600/OR EQUIVALENT PER MIL-C-5541CL3.",
        "APPLY DRY FILM LUBE TO COMPLETE BOLT PER PS18021",
        "APPLY MIL-PRF-46010 SOLID FILM LUBRICANT TO INDICATED SURFACE",
        "CHEMICAL FILM (COLORED) PER CSFS027",
        "CHEMICAL TREAT TO MEET THE REQUIREMENTS OF MIL–C–5541, CLASS 1A.",
        "COATING, CHEMICAL FILM, ALODINE 600/1200 PER MIL-C-5541, CL 1A",
        "PLATING, CADMIUM, UP TO 220KSI PER QQ-P-416C62TY2",
        "CHEMICAL FILM (ALODINE 1200) PER MIL-C-5541 CL2, GSS9010",
        "TREAT SURFACE TO MEET REQUIREMENTS OF MIL-C-5541, COLORED COATING, OR MIL-A-8625, TYPE I, CLASS 1 (CHROMIC ACID ANODIZE), EXCEPT SEAL IN DILUTE CHROMATE SOLUTION IN ACCORDANCE WITH BAC5019.",
        "PLATING, CADMIUM, VACUUM DEPOSITED, TYPE 2, CLASS 2 PER GSS8056",
        "APPLY CHEMICAL TREAT ENTIRE PART TO MEET THE REQUIREMENTS OF MIL–C–5541, CLASS 3.",
        "F-19.83 APPLY HIGH TEMPERATURE SOLID FILM LUBRICANT IN ACCORDANCE WITH BAC 5814",
        "[F-15.06] Cadmium plate in accordance with QQ-P-416, Type II, Class 2 or BAC5701, Type II, Class 2.",
        "[F-17.26]: Apply chemical conversion coating to all surfaces in accordance with BAC5719, Type I, Class A.",
        "[F-17.33]: Apply chemical conversion coating in accordance with BAC5719, Type I, Class D.",
        "F-15.43 THIN DENSE CHROMIUM PLATE IN ACCORDANCE WITH BAC 5709, CLASS 4. APPLY TO ENTIRE PART.",
        "COATING,ANODIZE,SULFURIC ACID, NON DYED,SEALED PER MIL-A-8625TY2CL1 MASK SURFACE MARKED WITH 'ROUND' SYMBOL. OMIT HARDCOAT AT THESE SURFACES.COATING, ANODIZE, HARDCOAT, UNSEALED, PER MIL-A-8625TY3CL1 ",
    ]
,
    "Masking (Omit Primer)" : [
        "N/A",
        "Applicable",
    ]

,    # NO. 14 excel sheet missing
    "prime" : [
        "N/A",
        "ONE COAT OF BMS10-11, TYPE I PRIMER PER BAC5736",
        "[F-20.03]TWO COATS OF BMS10-11, TYPE I PRIMER IN ACCORDANCE WITH BAC5736",
        "BMS 5-70 TYPE I PRIMER PER BAC 5514-570",
        "PRIMER,EPOXY POLYAMIDE, TYPE I, CLASS C, PER  MIL-PRF-23377, GSS4310",
        "F-19.47 APPLY ONE COAT OF BMS 10-79, TYPE III PRIMER IN ACCORDANCE WITH BAC 5882.",
        "F-18.06 TREAT SURFACE IN ACCORDANCE WITH MIL-DTL-5541, COLORED COATING APPLY ONE COAT OF BMS10-11, TYPE I PRIMER IN ACCORDANCE WITH BAC5736 REV",
        "APPLY ALUMINIZED EPOXY PRIMER IN ACCORDANCE WITH BAC5755, TYPE 10.",
        "EPOXY PRIMER PER MIL-PRF-85582, TYPE II, CLASS C1 OR C2",
        "PRIMER, EPOXY, SKYDROL RESISTANT, WATER REDUCTIBLE, LOW VOC PER GAMPS 3116, GMS 5005.",
        "PRIMER, EPOXY POLYAMIDE PER GP111V1, GSS4310",
        "CMFS029 PRIMER BY SPAY APPLICATION PER CSFS007 OR CSFS084",
        "ONE COAT OF BMS 10-11, TYPE I PRIMER IN ACCORDANCE WITH BAC5739",
        "APPLY TWO COATS OF PRIMER PER PS13646",
        "APPLY MIL–PRF–23377, TYPE I, CLASS C OR MIL–PRF–85582, TYPE I, CLASS C1 OR C2 PRIMER TO A DRY FILM THICKNESS OF 0.0006 TO 0.001 INCH IN ACCORDANCE WITH MIL–F–18264 TO AREAS NOT REQUIRING ELECTRIC BONDING",
        "APPLY ONE COAT OF BMS 10-11, TYPE I PRIMER IN ACCORDANCE WITH BAC5736.",
        "[F-2.68]: Apply AMS–C–27725 to a minimum dry film thickness of 0.0008 inch in accordance with MIL–F–18264. (Boeing application use: BAC5793.)",
        "F-19.47 APPLY ONE COAT OF BMS 10-79, TYPE III PRIMER IN ACCORDANCE WITH BAC 5882. +   [F-20.03] TWO COATS OF BMS10-11, TYPE I PRIMER IN ACCORDANCE WITH BAC5736",
        "[F-19.22]: APPLY ONE COAT OF BMS 10-20, TYPE II COATING IN ACCORDANCE WITH BAC 5793.",
        "[F-19.46]: Apply one coat of BMS10-79, Type II primer in accordance with BAC5882.",
        "EPOXY PRIMER PER PS 13646 PRIMER THICKNESS: 0.8 to 1.4 MIL",
    ]
,
    "Masking (Omit Top Coat)" : [
        "N/A",
        "Applicable",
    ]
,
    "Top Coat" : [
        "N/A",
        "ONE COAT OF BMS10-60, TYPE I GLOSS ENAMEL,  COLOR 17886, PER FED-STD-595, IN ACCORDANCE WITH BAC5845",
        "ONE COAT OF BMS10-11, TYPE II ENAMEL, COLOR BAC 702 WHITE GLOSS IN ACCORDANCE WITH BAC 5736 REV W",
        "TOP COAT GLOSS WHITE #672 PER 123AB50008, MIL-PRF-85285",
        "Apply BMS10-83, Type II enamel in accordance with BAC5755, Type 4.",
        "COATING, POLYURETHANE, HIGH-SOLIDS, GRAY PER FED-STD-595 COLOR NO. 16440 PER GSS4510, MIL-PRF-85285.",
        "COATING, POLYURETHANE, HIGH-SOLIDS, GRAY PER FED-STD-595 COLOR NO. 36231 PER GSS4510, MIL-PRF-85285.",
        "APPLY BMS 10-60, TYPE II, GLOSS ENAMEL IN ACCORDANCE WITH BAC 5845.",
        "COATING,POLYURETHANE,HIGH-SOLIDS,WHITE PER FED-STD-595, COLOR NO. 17925 PER GSS4510, MIL-PRF-85285.",
        "ACRYLIC LACQUER, CAMOUFLAGE, DARK GULL GRAY 36231 PER GP110H3J1, GSS4407",
        "APPLY LIGHT GRAY #668 PER 123AB50008 DWG SHT 1 ZN E2 (INT. FINISH TABLE). CAMOF POLYURETHANE LT GULL GRAY, MIL-PRF-85285",
        "TOPCOAT WITH MIL–PRF–85285, TYPE 1 OR TYPE II FOR GROUND EQUIPMENT TO A MINIMUM DRY FILM THICKNESS OF 0.0015 INCH IN ACCORDANCE WITH MIL–F–18264 (BOEING APPLICATION USE: BAC5896.)",
        "APPLY TOPCOAT WITH MIL–PRF–85285, TYPE I OR TYPE II FOR GROUND EQUIPMENT TO A MINIMUM DRY FILM THICKNESS OF 0.0015 INCH IN ACCORDANCE WITH MIL–F–18264",
        "F-14.9625 (APPLY TO INDICATED SURFACE IN 3D MODEL) APPLY BMS 10-86, TYPE I OR TYPE II, ABRASION RESISTANT TEFLON COATING, COLOR BAC 707 GRAY IN ACCORDANCE WITH BAC 5710, TYPE 27. APPLY TO INDICATED SURFACE IN 3D MODEL.",
        "[F-14.9814]: APPLY BMS10-60, TYPE I, GLOSS ENAMEL, COLOR BAC 7025 GRAY IN ACCORDANCE WITH, BAC5845.",
        "PAINT, ACRYLIC LACQUER, GLOSS, INSIGNIA WHITE PER FED-STD-595 COLOR NO. 17875 PER MIL-L-81352COMPG, GP110HW1, GSS4407",
        "[F-2.68]: Apply AMS–C–27725 to a minimum dry film thickness of 0.0008 inch in accordance with MIL–F–18264. (Boeing application use: BAC5793.)",
        "[SRF-14.9625]: Apply BMS10-86, Type I or Type II, abrasion resistant Teflon coating, color BAC 707 gray in accordance with BAC5710, Type 27.",
        "F-12.6589-17925: Topcoat with MIL–PRF–85285 (, Type I or Type II for ground equipment to a minimum dry film thickness of 0.0015 inch in accordance with MIL–F–18264. (Boeing application use: BAC5896.) COLOR: FED–STD–595 #17925",
    ]
,
    "MISC1" : [
        "N/A",
        "PAINT LACQUER STICK CRAYON FILLER ENGRAVING STAMPED MARKING WHITE PER FED-STD-595 COLOR NO. 37778 PER TT-F-325TY1 GP110BA03",
    ]
}

ht_certs_dict = {}
