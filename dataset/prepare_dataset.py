import os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--data_root_directory", required=True, default= '/data/lungNENomics/work/nicerons/HaloAE_net/Dataset_test/test_TNE1807',   help="Root directory of the dataset.")
args = vars(ap.parse_args())
Dataset_dir = args['data_root_directory']

samples_lst = os.listdir(Dataset_dir)

output_path = '/data/lungNENomics/work/nicerons/HaloAE_net/DataSet_txt'

# for i in samples_lst: 
# 	with open(os.path.join(output_path, + i + '.txt'), 'w+') as f:
# 		inside_sample_path = os.path.join(Dataset_dir, i)
# 		acc_reject = os.listdir(inside_sample_path)
# 		new_path = os.path.join(inside_sample_path, 'accept')
# 		lst_img_accept = os.listdir(new_path)
# 		for img in 	lst_img_accept:
# 			f.write(os.path.join(new_path, img) + '\n')
# 		etape += 1
# 		print(etape)

with open(os.path.join(output_path, 'test_dataset_3.txt'), 'w+') as f:
	for folder in os.listdir(Dataset_dir):
		path = os.path.join(Dataset_dir, folder)
		lst_tiles = os.listdir(path)
		for tiles in lst_tiles:
			f.write(os.path.join(path, tiles) + '\n')
	

