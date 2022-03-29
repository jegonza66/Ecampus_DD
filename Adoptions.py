import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  # default='warn'
import tkinter as tk
from tkinter import filedialog
import glob
import os

import Functions


def load_files():
    # Read files
    print('Please use the dialog window to go to the location of the OLD adoptions files')
    # Open file explorer dialog
    root = tk.Tk()
    root.withdraw()
    Adoption_old_path = filedialog.askdirectory()

    print('Please use the dialog window to go to the location of the NEW adoptions files')
    root = tk.Tk()
    root.withdraw()
    Adoption_new_path = filedialog.askdirectory()

    print('Loading Old adoptions files...')
    try:
        all_old_filenames = [i.replace('\\','/') for i in glob.glob(os.path.join(Adoption_old_path, '*.csv'))]
        Old_ad_file = pd.concat([pd.read_csv(f) for f in all_old_filenames])
    except:
        all_old_filenames = [i.replace('\\', '/') for i in glob.glob(os.path.join(Adoption_old_path, '*.csv'))]
        Old_ad_file = pd.concat([pd.read_csv(f, encoding='cp1252') for f in all_old_filenames])
    print('Done')

    print('Loading New adoptions files...')
    try:
        all_new_filenames = [i.replace('\\', '/') for i in glob.glob(os.path.join(Adoption_new_path, '*.csv'))]
        New_ad_file = pd.concat([pd.read_csv(f) for f in all_new_filenames])
    except:
        all_new_filenames = [i.replace('\\', '/') for i in glob.glob(os.path.join(Adoption_new_path, '*.csv'))]
        New_ad_file = pd.concat([pd.read_csv(f, encoding='cp1252') for f in all_new_filenames])
    print('Done')

    Old_ad_file['schedule_start'] = pd.to_datetime(Old_ad_file['schedule_start']).dt.strftime("%m/%d/%Y")
    New_ad_file['schedule_start'] = pd.to_datetime(New_ad_file['schedule_start']).dt.strftime("%m/%d/%Y")

    # Rename universities with bad tenant id/name
    Functions.rename_bad_schools(Old_ad_file=Old_ad_file, New_ad_file=New_ad_file)

    # change dates format to date
    New_ad_file['schedule_start'] = pd.to_datetime(New_ad_file['schedule_start']).dt.strftime("%m/%d/%Y")

    New_ad_file = New_ad_file.reset_index(drop=True)
    Old_ad_file = Old_ad_file.reset_index(drop=True)

    # get date from file name
    date = Adoption_new_path.split('/')
    date = pd.to_datetime(''.join([date[-3], date[-2], date[-1]]), format="%Y%m%d").strftime("%d-%m-%Y")

    return Old_ad_file, New_ad_file, date


def add_new_columns(Old_ad_file, New_ad_file):
    print('Adding new concat columns.')

    Old_ad_file['catalog'] = Old_ad_file['term_name'].map(str) + '/-/' + Old_ad_file['tenant_name'].map(str)
    New_ad_file['catalog'] = New_ad_file['term_name'].map(str) + '/-/' + New_ad_file['tenant_name'].map(str)

    Old_ad_file['course_DD'] = Old_ad_file['department_name'].map(str) + '-' + Old_ad_file['course_number'].map(str) \
                               + '-' + Old_ad_file['section_code'].map(str) + '-' + Old_ad_file['term_name'].map(str)
    New_ad_file['course_DD'] = New_ad_file['department_name'].map(str) + '-' + New_ad_file['course_number'].map(str) \
                               + '-' + New_ad_file['section_code'].map(str) + '-' + New_ad_file['term_name'].map(str)

    Old_ad_file['course'] = Old_ad_file['department_name'].map(str) + '/-/' + Old_ad_file['course_number'].map(str) \
                            + '/-/' + Old_ad_file['section_code'].map(str) + '/-/' + Old_ad_file['catalog'].map(str)
    New_ad_file['course'] = New_ad_file['department_name'].map(str) + '/-/' + New_ad_file['course_number'].map(str) \
                            + '/-/' + New_ad_file['section_code'].map(str) + '/-/' + New_ad_file['catalog'].map(str)

    Old_ad_file['supercourse'] = Old_ad_file['course'].map(str) + '/-/' + Old_ad_file['sku'].map(str)
    New_ad_file['supercourse'] = New_ad_file['course'].map(str) + '/-/' + New_ad_file['sku'].map(str)

    Old_ad_file['sku concat'] = Old_ad_file['sku'].map(str) + '/-/' + Old_ad_file['tenant_name'].map(str) + '/-/' \
                                + Old_ad_file['term_name'].map(str)
    New_ad_file['sku concat'] = New_ad_file['sku'].map(str) + '/-/' + New_ad_file['tenant_name'].map(str) + '/-/' \
                                + New_ad_file['term_name'].map(str)

    Old_ad_file['schedule concat'] = Old_ad_file['schedule_start'].map(str) + '/-/' + Old_ad_file['schedule_end'].map(
        str) \
                                     + '/-/' + Old_ad_file['tenant_name'].map(str) + '/-/' + Old_ad_file[
                                         'term_name'].map(str)
    New_ad_file['schedule concat'] = New_ad_file['schedule_start'].map(str) + '/-/' + New_ad_file['schedule_end'].map(
        str) \
                                     + '/-/' + New_ad_file['tenant_name'].map(str) + '/-/' + New_ad_file[
                                         'term_name'].map(str)

    Old_ad_file['opt out concat'] = Old_ad_file['participation_model'].map(str) + '/-/' + Old_ad_file[
        'tenant_name'].map(str) \
                                    + '/-/' + Old_ad_file['term_name'].map(str)
    New_ad_file['opt out concat'] = New_ad_file['participation_model'].map(str) + '/-/' + New_ad_file[
        'tenant_name'].map(str) \
                                    + '/-/' + New_ad_file['term_name'].map(str)

    return Old_ad_file, New_ad_file


def compare_make_DD_update(Old_ad_file, New_ad_file, date):
    print('Comparing old and new files.')

    # New sections
    new_sections_index = ~New_ad_file['course'].isin(Old_ad_file['course'])
    new_sections = New_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'tenant_id', 'course', 'schedule_start',
                                'schedule_end']][new_sections_index].reset_index(drop=True). \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section_new',
                        'sku': 'Extra_SKU', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                        'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date'})
    new_sections_df = Functions.make_full_df(new_sections)
    new_sections_df['Type of Change'] = 'new section'

    # Deactivated sections
    deactivated_sections_index = ~Old_ad_file['course'].isin(New_ad_file['course'])
    deactivated_sections = Old_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'tenant_id', 'course',
                                        'schedule_start', 'schedule_end']][deactivated_sections_index]. \
        reset_index(drop=True).rename(
        columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'Extra_SKU',
                 'tenant_id': 'Extra_id', 'course': 'Extra_Section', 'schedule_start': 'Extra_Start Date',
                 'schedule_end': 'Extra_End Date'})
    deactivated_sections_df = Functions.make_full_df(deactivated_sections)
    deactivated_sections_df['Type of Change'] = 'deactivated section'

    # New Catalogs
    new_catalogs_index = ~New_ad_file['catalog'].isin(Old_ad_file['catalog'])
    new_catalogs = New_ad_file[new_catalogs_index]

    # separar por catalogo y tomar la ultima schedule end y agregar estacion y año
    new_catalogs_sorted = new_catalogs.sort_values(['catalog', 'schedule_end'], ascending=[True, False])
    new_catalogs_filtered = new_catalogs_sorted.drop_duplicates('catalog').reset_index(drop=True)
    new_catalogs_filtered['schedule_end'] = pd.to_datetime(new_catalogs_filtered['schedule_end'], format="%m/%d/%Y")
    new_catalogs_filtered['schedule_end'] = new_catalogs_filtered.schedule_end.map(Functions.seasons_of_date)
    new_catalogs_filtered = new_catalogs_filtered[['tenant_name', 'term_name', 'schedule_end', 'sku', 'tenant_id',
                                                   'course']].reset_index(drop=True). \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'schedule_end': 'Catalog Last End Date',
                        'sku': 'Extra_SKU', 'tenant_id': 'Extra_id', 'course': 'Extra_Section'})
    new_catalogs_df = Functions.make_full_df(new_catalogs_filtered)
    new_catalogs_df['Type of Change'] = 'new catalog'

    # Deactivated Catalogs
    deactivated_catalogs_index = ~Old_ad_file['catalog'].isin(New_ad_file['catalog'])
    deactivated_catalogs = Old_ad_file[deactivated_catalogs_index]
    deactivated_catalogs_sorted = deactivated_catalogs.sort_values(['catalog', 'schedule_end'], ascending=[True, False])
    deactivated_catalogs_filtered = deactivated_catalogs_sorted.drop_duplicates('catalog').reset_index(drop=True)
    deactivated_catalogs_filtered['schedule_end'] = pd.to_datetime(deactivated_catalogs_filtered['schedule_end'],
                                                                   format="%m/%d/%Y")
    deactivated_catalogs_filtered['schedule_end'] = deactivated_catalogs_filtered.schedule_end.map(
        Functions.seasons_of_date)
    deactivated_catalogs_filtered = deactivated_catalogs_filtered[['tenant_name', 'term_name', 'schedule_end', 'sku',
                                                                   'tenant_id', 'course']]. \
        reset_index(drop=True).rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'schedule_end':
        'Catalog Last End Date', 'sku': 'Extra_SKU', 'tenant_id': 'Extra_id', 'course': 'Extra_Section'})
    deactivated_catalogs_df = Functions.make_full_df(deactivated_catalogs_filtered)
    deactivated_catalogs_df['Type of Change'] = 'deactivated catalog'

    # New items
    new_items_current = New_ad_file.drop_duplicates(['sku concat', 'net_price', 'student_price'])
    new_items_index = ~new_items_current['sku concat'].isin(Old_ad_file['sku concat'])
    new_items = new_items_current[new_items_index][
        ['tenant_name', 'term_name', 'course', 'sku', 'tenant_id', 'schedule_start',
         'schedule_end', 'net_price', 'student_price']].reset_index(drop=True)
    new_items = pd.DataFrame(new_items).rename(
        columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course': 'Extra_Section',
                 'sku': 'SKU_new', 'tenant_id': 'Extra_id',
                 'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date',
                 'net_price': 'Extra_Net Price', 'student_price': 'Extra_Student Price'})
    new_items_df = Functions.make_full_df(new_items)
    new_items_df['Type of Change'] = 'new item'

    # New Schedules
    new_schedules_current = New_ad_file.drop_duplicates('schedule concat')
    new_schedules_index = ~new_schedules_current['schedule concat'].isin(Old_ad_file['schedule concat'])
    new_schedules = new_schedules_current[new_schedules_index][['schedule_start', 'schedule_end', 'tenant_name',
                                                                'term_name', 'sku', 'tenant_id', 'course']].reset_index(
        drop=True)
    new_schedules = new_schedules.rename(columns={'tenant_name': 'School', 'term_name': 'Catalog',
                                                  'schedule_start': 'Start Date', 'schedule_end': 'End Date',
                                                  'sku': 'Extra_SKU', 'tenant_id': 'Extra_id',
                                                  'course': 'Extra_Section'})
    new_schedules_df = Functions.make_full_df(new_schedules)
    new_schedules_df['Type of Change'] = 'new schedule'

    # Deactivated items
    deactivated_items_index = ~Old_ad_file['supercourse'].isin(New_ad_file['supercourse'])
    deactivated_items_all = Old_ad_file[(~deactivated_sections_index) & (deactivated_items_index)].sort_values(
        'supercourse')

    # Updated items
    updated_items_index = ~New_ad_file['supercourse'].isin(Old_ad_file['supercourse'])
    updated_items_index_old_section = (~new_sections_index) & (updated_items_index)
    updated_items_all = New_ad_file[updated_items_index_old_section].sort_values('supercourse')
    updated_items = updated_items_all.loc[updated_items_all['course'].isin(deactivated_items_all['course'])].drop_duplicates('supercourse')

    deactivated_items = deactivated_items_all.loc[~deactivated_items_all['course'].isin(updated_items_all['course'])].drop_duplicates('supercourse')
    deactivated_updated_skus = []
    for course in updated_items['course']:
        deactivated_updated_skus.append(deactivated_items_all[deactivated_items_all['course'] == course]['sku'].values)

    # repeat the updated items rows to match the amount of deactivated items for each course
    updated_items = updated_items.iloc[np.repeat(np.arange(len(updated_items)), [len(skus) for skus in deactivated_updated_skus])]

    # Additional Items
    additional_items_raw = New_ad_file.loc[New_ad_file['course'].isin(updated_items_all['course'])]
    merged = updated_items_all.merge(additional_items_raw, how='right', indicator=True)
    additional_items_index = merged['_merge'] == 'right_only'
    additional_items = merged[additional_items_index].drop('_merge', axis='columns').sort_values(
        'supercourse').drop_duplicates('supercourse').reset_index(drop=True)

    new_skus = []
    for course in additional_items['course']:
        new_skus.append(updated_items_all[updated_items_all['course'] == course]['sku'].values)

    additional_items = additional_items.iloc[np.repeat(np.arange(len(additional_items)), [len(skus) for skus in new_skus])]

    additional_items_filtered = additional_items[['tenant_name', 'term_name', 'course_DD', 'sku',
                                                  'tenant_id', 'course', 'schedule_start', 'schedule_end',
                                                  'net_price', 'student_price']].reset_index(drop=True). \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'SKU',
                        'tenant_id': 'Extra_id', 'course': 'Extra_Section', 'schedule_start': 'Extra_Start Date',
                        'schedule_end': 'Extra_End Date', 'net_price': 'Extra_Net Price',
                        'student_price': 'Extra_Student Price'}).sort_values('Section')

    updated_items_filtered = updated_items[['tenant_name', 'term_name', 'course_DD', 'sku', 'tenant_id',
                                            'course', 'schedule_start', 'schedule_end', 'net_price', 'student_price']]. \
        reset_index(drop=True).rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section',
                                               'sku': 'SKU_new', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                                               'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date',
                                               'net_price': 'Extra_Net Price',
                                               'student_price': 'Extra_Student Price'}).sort_values('Section')

    deactivated_items_filtered = deactivated_items[['tenant_name', 'term_name', 'course_DD', 'sku', 'tenant_id',
                                            'course', 'schedule_start', 'schedule_end', 'net_price', 'student_price']]. \
        reset_index(drop=True).rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section',
                                               'sku': 'SKU', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                                               'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date',
                                               'net_price': 'Extra_Net Price',
                                               'student_price': 'Extra_Student Price'}).sort_values('Section')

    if len(deactivated_updated_skus):
        deactivated_updated_skus = np.concatenate(deactivated_updated_skus).ravel()
    if len(new_skus):
        new_skus = np.concatenate(new_skus).ravel()

    updated_items_filtered['SKU'] = deactivated_updated_skus
    additional_items_filtered['SKU_new'] = new_skus

    updated_items_df = Functions.make_full_df(updated_items_filtered)
    updated_items_df['Type of Change'] = 'updated item'
    additional_items_df = Functions.make_full_df(additional_items_filtered)
    additional_items_df['Type of Change'] = 'additional item'
    deactivated_items_df = Functions.make_full_df(deactivated_items_filtered)
    deactivated_items_df['Type of Change'] = 'deactivated item'

    # Opt Out
    opt_out_index = ~Old_ad_file['opt out concat'].isin(New_ad_file['opt out concat'])
    opt_out = Old_ad_file[['tenant_name', 'term_name', 'sku', 'tenant_id', 'course']][
        ~deactivated_catalogs_index & opt_out_index]. \
        reset_index(drop=True).rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'sku': 'Extra_SKU',
                                               'tenant_id': 'Extra_id', 'course': 'Extra_Section'})
    opt_out['Previous Data'] = 'opt-in'
    opt_out['Section_new'] = 'opt-out'
    opt_out_df = Functions.make_full_df(opt_out)
    opt_out_df['Type of Change'] = 'participation model change'

    # Make matching supercourses files for net price and dates comparison
    matching_supercourse_index_old = Old_ad_file['supercourse'].isin(New_ad_file['supercourse'])
    matching_supercourse_index_new = New_ad_file['supercourse'].isin(Old_ad_file['supercourse'])
    Matching_Old_ad_file = Old_ad_file.loc[matching_supercourse_index_old].fillna('').drop_duplicates('supercourse').\
        sort_values('supercourse').reset_index(drop=True)
    Matching_New_ad_file = New_ad_file.loc[matching_supercourse_index_new].fillna('').drop_duplicates('supercourse').\
        sort_values('supercourse').reset_index(drop=True)

    # Net Price
    net_price_change_index = ~(Matching_Old_ad_file['net_price'] == Matching_New_ad_file['net_price'])
    net_price_change = Matching_Old_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'net_price', 'tenant_id',
                                             'course', 'schedule_start', 'schedule_end']][
        net_price_change_index]. \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'SKU',
                        'net_price': 'Previous Data', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                        'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date'})
    net_price_change['Net Price'] = Matching_New_ad_file['net_price'][net_price_change_index]
    net_price_df = Functions.make_full_df(net_price_change)
    net_price_df['Type of Change'] = 'net price change'

    # Student Price
    student_price_change_index = ~(Matching_Old_ad_file['student_price'] == Matching_New_ad_file['student_price'])
    student_price_change = Matching_Old_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'student_price',
                                                 'tenant_id', 'course', 'schedule_start', 'schedule_end']][
        student_price_change_index]. \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'SKU',
                        'student_price': 'Previous Data', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                        'schedule_start': 'Extra_Start Date', 'schedule_end': 'Extra_End Date'})
    student_price_change['Student Price'] = Matching_New_ad_file['student_price'][student_price_change_index]
    student_price_df = Functions.make_full_df(student_price_change)
    student_price_df['Type of Change'] = 'student price change'

    # Start date change
    schedule_start_change_index = ~(Matching_Old_ad_file['schedule_start'] == Matching_New_ad_file['schedule_start'])
    schedule_start_change = Matching_Old_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'schedule_start',
                                                  'tenant_id', 'course', 'schedule_end']][schedule_start_change_index]. \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'SKU',
                        'schedule_start': 'Previous Data', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                        'schedule_end': 'Extra_End Date'})

    schedule_start_change['Extra_Start Date'] = schedule_start_change['Previous Data'].values

    schedule_start_df = Functions.make_full_df(schedule_start_change)
    schedule_start_df['Type of Change'] = 'start date change'

    # End date change
    schedule_end_change_index = ~(Matching_Old_ad_file['schedule_end'] == Matching_New_ad_file['schedule_end'])
    schedule_end_change = Matching_Old_ad_file[['tenant_name', 'term_name', 'course_DD', 'sku', 'schedule_end',
                                                'tenant_id', 'course', 'schedule_start']][schedule_end_change_index]. \
        rename(columns={'tenant_name': 'School', 'term_name': 'Catalog', 'course_DD': 'Section', 'sku': 'SKU',
                        'schedule_end': 'Previous Data', 'tenant_id': 'Extra_id', 'course': 'Extra_Section',
                        'schedule_start': 'Extra_Start Date'})

    schedule_end_df = Functions.make_full_df(schedule_end_change)
    schedule_end_df['Type of Change'] = 'end date change'

    print('Loading adoption changes to DD_update file.')

    DD_update = pd.concat([new_sections_df, deactivated_items_df, updated_items_df, additional_items_df, new_items_df,
                           new_schedules_df, new_catalogs_df, deactivated_catalogs_df, deactivated_sections_df,
                           net_price_df, student_price_df, schedule_start_df, schedule_end_df, opt_out_df]).\
        reset_index(drop=True)
    DD_update['Date of Change (date of adoptions file of new data)'] = pd.to_datetime(date, format="%d-%m-%Y").strftime(
        "%m/%d/%Y")
    print('Done.')

    return DD_update
