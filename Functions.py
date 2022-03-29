import pandas as pd
import os

def rename_bad_schools(Old_ad_file, New_ad_file):

    # Alexandria
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('alex', na=False)] = 'ecampus-alextechcc'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('alex', na=False)] = 'Alex Tech'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('alex', na=False)] = 'ecampus-alextechcc'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('alex', na=False)] = 'Alex Tech'

    # Bluefield
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('bluefielduniversity', na=False)] = 'ecampus-bluefielduniversity'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('bluefielduniversity', na=False)] = 'Bluefield'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('bluefielduniversity', na=False)] = 'ecampus-bluefielduniversity'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('bluefielduniversity', na=False)] = 'Bluefield'

    # Beckfield
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('beckfield', na=False)] = 'ecampus-beckfieldcollege'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('beckfield', na=False)] = 'Beckfield'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('beckfield', na=False)] = 'ecampus-beckfieldcollege'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('beckfield', na=False)] = 'Beckfield'

    # CCSJ
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.lower().str.contains('ccsj', na=False)] = 'ecampus-ccsj'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('ccsj', na=False)] = 'CCSJ'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.lower().str.contains('ccsj', na=False)] = 'ecampus-ccsj'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('ccsj', na=False)] = 'CCSJ'

    # CMC
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.lower().str.contains('cmc', na=False)] = 'ecampus-cmc'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('cmc', na=False)] = 'CMC'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.lower().str.contains('cmc', na=False)] = 'ecampus-cmc'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('cmc', na=False)] = 'CMC'

    # Elmhurst
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.contains('elmhurst', na=False)] = 'ecampus-elmhurstcollege'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('elmhurst', na=False)] = 'Elmhurst'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.contains('elmhurst', na=False)] = 'ecampus-elmhurstcollege'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('elmhurst', na=False)] = 'Elmhurst'

    # Fox Valley
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('fox valley', na=False)] = 'ecampus-foxvalleytech'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('fox valley', na=False)] = 'Fox Valley'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('fox valley', na=False)] = 'ecampus-foxvalleytech'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('fox valley', na=False)] = 'Fox Valley'

    # Hodges
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('hodgesuniversity', na=False)] = 'ecampus-hodgesuniversity'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('hodgesuniversity', na=False)] = 'Hodges'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('hodgesuniversity', na=False)] = 'ecampus-hodgesuniversity'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('hodgesuniversity', na=False)] = 'Hodges'

    # Iowa
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.contains('iwu', na=False)] = 'ecampus-iowawesleyanuniversity'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('iwu', na=False)] = 'IWU'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.contains('iwu', na=False)] = 'ecampus-iowawesleyanuniversity'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('iwu', na=False)] = 'IWU'

    # Johnson
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('johnson', na=False)] = 'ecampus-johnsoncollege'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('johnson', na=False)] = 'Johnson'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('johnson', na=False)] = 'ecampus-johnsoncollege'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('johnson', na=False)] = 'Johnson'

    # Limestone
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('limestone', na=False)] = 'ecampus-limestonecollege'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('limestone', na=False)] = 'Limestone'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('limestone', na=False)] = 'ecampus-limestonecollege'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('limestone', na=False)] = 'Limestone'

    # New Engalnd
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.contains('new england', na=False)] = 'ecampus-newenglandcollege'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.contains('new england', na=False)] = 'New England College'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.contains('new england', na=False)] = 'ecampus-newenglandcollege'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.contains('new england', na=False)] = 'New England College'

    # Owens
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.lower().str.contains('owens', na=False)] = 'ecampus-owenscc'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('owens', na=False)] = 'Owens'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.lower().str.contains('owens', na=False)] = 'ecampus-owenscc'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('owens', na=False)] = 'Owens'

    # Ozarks
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.lower().str.contains('ozarks', na=False)] = 'ecampus-universityofozarks'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('ozarks', na=False)] = 'Ozarks'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.lower().str.contains('ozarks', na=False)] = 'ecampus-universityofozarks'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('ozarks', na=False)] = 'Ozarks'

    # Reinhardt
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('reinhardt', na=False)] = 'ecampus-reinhardtuniversity'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('reinhardt', na=False)] = 'Reinhardt'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('reinhardt', na=False)] = 'ecampus-reinhardtuniversity'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('reinhardt', na=False)] = 'Reinhardt'

    # Schreiner
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('schreiner', na=False)] = 'ecampus-schreineruniversity'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('schreiner', na=False)] = 'Schreiner'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('schreiner', na=False)] = 'ecampus-schreineruniversity'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('schreiner', na=False)] = 'Schreiner'

    # Sussex
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('sussex', na=False)] = 'ecampus-sussexcountycc'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('sussex', na=False)] = 'Sussex'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('sussex', na=False)] = 'ecampus-sussexcountycc'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('sussex', na=False)] = 'Sussex'

    # Syracuse
    Old_ad_file['tenant_id'][Old_ad_file['tenant_name'].str.lower().str.contains('syracuse', na=False)] = 'ecampus-syracuseuniv'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('syracuse', na=False)] = 'Syracuse'
    New_ad_file['tenant_id'][New_ad_file['tenant_name'].str.lower().str.contains('syracuse', na=False)] = 'ecampus-syracuseuniv'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('syracuse', na=False)] = 'Syracuse'

    # Wisconsin Miwaukee
    Old_ad_file['tenant_id'][Old_ad_file['tenant_id'].str.contains('eCampus_UofWisconsinMilwaukee', na=False)] = 'ecampus-uwm'
    Old_ad_file['tenant_id'][Old_ad_file['tenant_id'].str.lower().str.contains('uwm', na=False)] = 'ecampus-uwm'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('uwm', na=False)] = 'UWM'
    Old_ad_file['tenant_name'][Old_ad_file['tenant_name'].str.lower().str.contains('wisconsin milwaukee', na=False)] = 'UWM'

    New_ad_file['tenant_id'][New_ad_file['tenant_id'].str.contains('eCampus_UofWisconsinMilwaukee', na=False)] = 'ecampus-uwm'
    New_ad_file['tenant_id'][New_ad_file['tenant_id'].str.lower().str.contains('uwm', na=False)] = 'ecampus-uwm'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('uwm', na=False)] = 'UWM'
    New_ad_file['tenant_name'][New_ad_file['tenant_name'].str.lower().str.contains('wisconsin milwaukee', na=False)] = 'UWM'

    # Villa Maria
    Old_ad_file['tenant_id'][
        Old_ad_file['tenant_name'].str.lower().str.contains('villa maria', na=False)] = 'ecampus-villamariacollege'
    Old_ad_file['tenant_name'][
        Old_ad_file['tenant_name'].str.lower().str.contains('villa maria', na=False)] = 'Villa Maria'
    New_ad_file['tenant_id'][
        New_ad_file['tenant_name'].str.lower().str.contains('villa maria', na=False)] = 'ecampus-villamariacollege'
    New_ad_file['tenant_name'][
        New_ad_file['tenant_name'].str.lower().str.contains('villa maria', na=False)] = 'Villa Maria'


def make_full_df(df):

    column_names = ['Date of Change (date of adoptions file of new data)', 'Type of Change', 'School', 'Catalog',
                    'Catalog Last End Date', 'Section', 'SKU', 'Previous Data', 'Section_new',
                    'Total Estimated Enrollments', 'SKU_new', 'Net Price', 'Student Price', 'Start Date', 'End Date',
                    'Change made in Connect?', 'Reason change not made', 'Issue',
                    'If New Schedule, are the key dates available?', 'New Item Work complete', 'Notes', 'Publisher',
                    'Issue with Tracker']

    full_df = pd.DataFrame(columns=column_names)

    for key in df.keys():
        full_df[key] = df[key]

    return full_df


def seasons_of_date(date):
    year = str(date.year)
    seasons = {'Spring': pd.date_range(start='21/03/' + year, end='20/06/' + year),
               'Summer': pd.date_range(start='21/06/' + year, end='22/09/' + year),
               'Fall': pd.date_range(start='23/09/' + year, end='20/12/' + year)}

    if date in seasons['Spring']:
        return 'Spring {}. Last end date {}'.format(year, date.strftime("%m/%d/%Y"))
    if date in seasons['Summer']:
        return 'Summer {}. Last end date {}'.format(year, date.strftime("%m/%d/%Y"))
    if date in seasons['Fall']:
        return 'Fall {}. Last end date {}'.format(year, date.strftime("%m/%d/%Y"))
    else:
        return 'Winter {}. Last end date {}'.format(year, date.strftime("%m/%d/%Y"))



def complete_deactivated_catalog_section(DD_update):

    deactivated_catalogs = DD_update[DD_update['Type of Change'] == 'deactivated catalog'][
        ['School', 'Catalog']].reset_index(drop=True)
    for index, row in deactivated_catalogs.iterrows():
        School = deactivated_catalogs.iloc[index]['School']
        Catalog = deactivated_catalogs.iloc[index]['Catalog']

        DD_update.loc[(DD_update['Type of Change'] == 'deactivated catalog') & (DD_update['School'] == School) & (
                DD_update['Catalog'] == Catalog), 'Change made in Connect?'] = 'No Expected Change'

        DD_update.loc[(DD_update['Type of Change'] == 'deactivated section') & (DD_update['School'] == School) & (
                DD_update['Catalog'] == Catalog), 'Change made in Connect?'] = 'No Expected Change'

    return DD_update


def save_DD1(DD_update, Credentials, date):
    # DD1_Save = DD_update.loc[:, ~DD_update.columns.str.startswith('Extra')]
    DD1_Save = DD_update.sort_values(['Type of Change', 'School', 'Catalog']).reset_index(drop=True)

    path_1 = Credentials['csv_save_path'] + 'DD1/'
    os.makedirs(path_1, exist_ok=True)
    file_name = path_1 + 'DD1 Update {}.xlsx'.format(date)
    DD1_Save.to_excel(file_name, index=False)
    print('\nDD1_update {} file saved to {}'.format(date, path_1))

def save_DD2(DD_update, Credentials, date):
    # DD2_Save = DD_update.loc[:, ~DD_update.columns.str.startswith('Extra')]
    DD2_Save = DD_update.sort_values(['Type of Change', 'School', 'Catalog']).reset_index(drop=True)
    path_2 = Credentials['csv_save_path'] + 'DD2/'
    os.makedirs(path_2, exist_ok=True)
    file_name = path_2 + 'DD2 Update {}.xlsx'.format(date)
    DD2_Save.to_excel(file_name, index=False)
    print('\nDD2_update {} file saved to {}'.format(date, path_2))