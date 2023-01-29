import in_data as InD
import keeper as DB
import out_data as OD

def Click_Button():
    string_input = InD.indata()
    result = DB.save_data(string_input) 
    OD.outdata(result)
    
