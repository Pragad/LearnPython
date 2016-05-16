fname1 = "C:\\PRAGADHEESH\\NETAPP\\Team\\Burt_780660_Cifs_Files_Dir\\mask_test_cMode_No_fix_sh11.txt"
fname2 = "C:\\PRAGADHEESH\\NETAPP\\Team\\Burt_780660_Cifs_Files_Dir\\mask_test_mmm_cModeFix.txt"
fname3 = "C:\\PRAGADHEESH\\NETAPP\\Team\\Burt_780660_Cifs_Files_Dir\\mask_test_7mode_sh55.txt"

#fname4 = "C:\\PRAGADHEESH\\NETAPP\\Team\\Burt_780660_Cifs_Files_Dir\\mask_test_win_1.txt"
#fname5 = "C:\\PRAGADHEESH\\NETAPP\\Team\\Burt_780660_Cifs_Files_Dir\\mask_test_new_fix_1.txt"

pattern_match = True
with open(fname3) as f:
    lines = f.readlines()
    for line in lines:
        words = line.split(" ")
        if len(words) == 6:
            word_1 = words[0]
            word_2 = words[1]
            if word_1 != word_2:
                print(word_1, " NOT EQUALS ", word_2)
                pattern_match = False
if pattern_match:
    print("Successfully matched the patterns")       
else:
    print("Failed to match the patterns")       
