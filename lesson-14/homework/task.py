## Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import pandas as pd
import numpy as np

data = {
    "Name": [""],     
    "Species": [""],  
    "Age": [np.nan]   
}
Rooster = pd.DataFrame(data)
print(Rooster)

#Populate your new table with the following values:

#Name	          Species	  Age
#Benjamin Sisko	Human	    40
#Jadzia Dax	    Trill	   300
#Kira Nerys	    Bajoran	  29

import pandas as pd
import numpy as np

data = {
    "Name": ["Benjamin Sisko", "Jadzia Dax", "Kira Nerys"],
    "Species": ["Human", "Trill", "Bajoran"],
    "Age": [40, 300, 29]
}

Rooster = pd.DataFrame(data)
print(Rooster)

# Update the Name of Jadzia Dax to be Ezri Dax
Rooster.loc[Rooster["Name"] == "Jadzia Dax", "Name"] = "Ezri Dax"
# Display the Name and Age of everyone in the table classified as Bajoran.
bajoran_ = Rooster[Rooster["Species"] == "Bajoran"][["Name", "Age"]]
