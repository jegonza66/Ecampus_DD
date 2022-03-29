import Paths_Credentials
import Adoptions
import Functions

# Define DD_update file save path
Credentials = Paths_Credentials.Path()

# Get Verba Connect username and password
Credentials = Paths_Credentials.Verba_Credentials(Credentials)

# Load adoptions files
Old_ad_file, New_ad_file, date = Adoptions.load_files()

# add new concantenated columns
Old_ad_file, New_ad_file = Adoptions.add_new_columns(Old_ad_file=Old_ad_file, New_ad_file=New_ad_file)

# Compare ald and new files
DD_update = Adoptions.compare_make_DD_update(Old_ad_file=Old_ad_file, New_ad_file=New_ad_file, date=date)

# Complete no expected change on deactivated catalogs and sections
DD_update = Functions.complete_deactivated_catalog_section(DD_update=DD_update)

# Save DD1_update file before Check in Connect
Functions.save_DD1(DD_update=DD_update, Credentials=Credentials, date=date)

# Sort rows by school and catalog to check them in order
DD_update = DD_update.sort_values(['School', 'Catalog', 'Type of Change']).reset_index(drop=True)