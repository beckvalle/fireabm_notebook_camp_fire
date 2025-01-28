import os
import argparse
import glob
import csv

def main():
    parser = argparse.ArgumentParser(description='Collect results from FireABM simulation.')
    parser.add_argument('-ifd',    '--in_folder',          required=True, type=str, dest='in_folder', 
                        help='a directory containing simulation results')
    parser.add_argument('-ofd',    '--output_file',          required=True, type=str, dest='out_file', 
                        help='a file used to store combined simulation results')
    
    args = parser.parse_args()
    print('current_directory: ', os.getcwd()) 
    print('in_folder: ', args.in_folder)
    full_in_folder = os.path.join(os.getcwd(), args.in_folder) 
    print('full in_folder: ', full_in_folder)
    print()
    print('out_file: ', args.out_file)
    full_out_file = os.path.join(os.getcwd(), args.out_file) 
    print('full out_file: ', full_out_file)
    print()
    assert os.path.isdir(full_in_folder), "path to input folder not found"
    
    all_files = glob.glob(full_in_folder+"/*.txt")
    print('total number files:', len(all_files))
    fieldnames = ['Exp_no', 'NB_no',
                  'Treat_no', 'Rep_no', 'Seed',
                  'Elpsd_time_TS',
                  'Total_cars', 'Stuck_cars',
                  'Num_rds_in_bbox',
                  'veh_by_strat',
                  'Finish_time',
                  'Treat_desc', 'Exp_desc', 'RG_file',
                  'Veh_stat_by_time',
                  'Cong_by_time',
                  'Veh_by_edge',
                  'Init_Veh_coords']
    
    with open(full_out_file, 'w') as out_csvfile:
        writer = csv.DictWriter(out_csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
    
        for data_file in all_files:
            with open(data_file, 'r') as in_csvfile:
                reader = csv.DictReader(in_csvfile, delimiter='\t')
                for row in reader:
                    writer.writerow(row)
    print('collection complete')
    
    
if __name__ == '__main__':
    main()
