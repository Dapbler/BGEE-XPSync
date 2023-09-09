#!/usr/bin/bash

# Build the main XP grant script
python3 build/build_xpsmaix.py > build/template_xps_maix.baf
# Build power of ten wipe scripts up to 100M
cat build/template_xps_maix.baf | sed 's/POW//g' > xpsync/bands/xps_mai3.baf
cat build/template_xps_maix.baf | sed 's/POW/0/g' > xpsync/bands/xps_mai4.baf
cat build/template_xps_maix.baf | sed 's/POW/00/g' > xpsync/bands/xps_mai5.baf
cat build/template_xps_maix.baf | sed 's/POW/000/g' > xpsync/bands/xps_mai6.baf
cat build/template_xps_maix.baf | sed 's/POW/0000/g' > xpsync/bands/xps_mai7.baf

# Build the final grant scripts
python3 build/build_xpsgran0.py > xpsync/bands/xpsgran0.baf
python3 build/build_xpsgranx.py > build/template_xpsgranx.baf

python3 build/build_xpsgrap0.py > xpsync/bands/xpsgrap0.baf
python3 build/build_xpsgrapx.py > build/template_xpsgrapx.baf

# Now build the power 10 scripts
cat build/template_xpsgrapx.baf | sed 's/POW//g' > xpsync/bands/xpsgrap3.baf
cat build/template_xpsgrapx.baf | sed 's/POW/0/g' > xpsync/bands/xpsgrap4.baf
cat build/template_xpsgrapx.baf | sed 's/POW/00/g' > xpsync/bands/xpsgrap5.baf
cat build/template_xpsgrapx.baf | sed 's/POW/000/g' > xpsync/bands/xpsgrap6.baf
cat build/template_xpsgrapx.baf | sed 's/POW/0000/g' > xpsync/bands/xpsgrap7.baf

cat build/template_xpsgranx.baf | sed 's/POW//g' > xpsync/bands/xpsgran3.baf
cat build/template_xpsgranx.baf | sed 's/POW/0/g' > xpsync/bands/xpsgran4.baf
cat build/template_xpsgranx.baf | sed 's/POW/00/g' > xpsync/bands/xpsgran5.baf
cat build/template_xpsgranx.baf | sed 's/POW/000/g' > xpsync/bands/xpsgran6.baf
cat build/template_xpsgranx.baf | sed 's/POW/0000/g' > xpsync/bands/xpsgran7.baf


# Build the template for main PC dual class XP addition
python3 build/build_xps_pclass.py > build/template_pclass.baf
# Use the template to make the NPC dual class XP removal script
sed 's/Player1/LastSummonerOf(Myself)/' < build/template_pclass.baf \
    | sed 's/,%CLASS/,-%CLASS/' \
    | sed 's/xps_nd/xps_wipe/' > build/template_nclass.baf
# Make the class scripts for PC dual class
rm xpsync/dualxp/xps_p*.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/MAGE/' | sed 's/CLSCAT/WIZARD/' > xpsync/dualxp/xps_pmag.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/FIGHTER/' | sed 's/CLSCAT/WARRIOR/'  > xpsync/dualxp/xps_pfig.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/PALADIN/' | sed 's/CLSCAT/WARRIOR/' > xpsync/dualxp/xps_ppal.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/RANGER/' | sed 's/CLSCAT/WARRIOR/' > xpsync/dualxp/xps_pran.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/CLERIC/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_pcle.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/DRUID/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_pdru.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/THIEF/' | sed 's/CLSCAT/ROGUE/' > xpsync/dualxp/xps_pthi.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/BARD/' | sed 's/CLSCAT/ROGUE/' > xpsync/dualxp/xps_pbar.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/SORCERER/' | sed 's/CLSCAT/WIZARD/' > xpsync/dualxp/xps_psor.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/MONK/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_pmon.baf
cat build/template_pclass.baf | sed 's/CLASSNAME/SHAMAN/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_psha.baf
# Make the class scripts for NPC dual class
rm xpsync/dualxp/xps_n*.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/MAGE/' | sed 's/CLSCAT/WIZARD/' > xpsync/dualxp/xps_nmag.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/FIGHTER/' | sed 's/CLSCAT/WARRIOR/'  > xpsync/dualxp/xps_nfig.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/PALADIN/' | sed 's/CLSCAT/WARRIOR/' > xpsync/dualxp/xps_npal.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/RANGER/' | sed 's/CLSCAT/WARRIOR/' > xpsync/dualxp/xps_nran.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/CLERIC/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_ncle.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/DRUID/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_ndru.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/THIEF/' | sed 's/CLSCAT/ROGUE/' > xpsync/dualxp/xps_nthi.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/BARD/' | sed 's/CLSCAT/ROGUE/' > xpsync/dualxp/xps_nbar.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/SORCERER/' | sed 's/CLSCAT/WIZARD/' > xpsync/dualxp/xps_nsor.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/MONK/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_nmon.baf
cat build/template_nclass.baf | sed 's/CLASSNAME/SHAMAN/' | sed 's/CLSCAT/PRIEST/' > xpsync/dualxp/xps_nsha.baf

# Build the XP wipe script template
python3 build/build_xpswipe0.py > xpsync/bands/xps_wip0.baf
python3 build/build_xpswipe.py > build/xps_wipx_template.baf
# Build power of ten wipe scripts up to 100M
cat build/xps_wipx_template.baf | sed 's/POW//g' > xpsync/bands/xps_wip3.baf
cat build/xps_wipx_template.baf | sed 's/POW/0/g' > xpsync/bands/xps_wip4.baf
cat build/xps_wipx_template.baf | sed 's/POW/00/g' > xpsync/bands/xps_wip5.baf
cat build/xps_wipx_template.baf | sed 's/POW/000/g' > xpsync/bands/xps_wip6.baf
cat build/xps_wipx_template.baf | sed 's/POW/0000/g' > xpsync/bands/xps_wip7.baf

# Build INCLUDE for band baf compilation
ls xpsync/bands/ | \
    sed -E 's/(.*baf)/COPY ~xpsync\/bands\/\1~ ~override~\nCOMPILE ~override\/\1~\nDELETE + ~override\/\1~/' \
    > xpsync/include/xpsync_bands_build.tph



