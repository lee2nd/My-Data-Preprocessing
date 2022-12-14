# if statement with multiple string in Python
blob_name = "rmrs_AKIEXB20_PEP4_V65Q7-N2_2022-11-30single_process"
if ("PEP4" in blob_name) and ("V65Q7-N2" in blob_name): 
    print ('Present')
else:
    print ('Not Present')
