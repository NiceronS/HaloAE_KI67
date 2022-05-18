#!/bin/bash
conda deactivate
conda activate MIL_RNN_efficient
python ~/HaloAE/train.py --epochs 251  \ # Number of training epochs Warning by default the model is saved each 10 epochs 
			 --model_name_checkpoint HaloAE_adapt_fixed_hazelnut.pt \ # Name of the models
             --run_directory runs_HaloAE_adapt_fixed_hazelnut \ # Name of tensorboard log directory 
			--learning_rate 1e-4 \ # Default learning rate
			--MVTEC_object hazelnut \ # Object 
			--data_root_directory /home/XXXX/LNENWork/MvTech \ # Path to MVTec dataset
			--summury_path /home/XXXX/LNENWork/MvTech/TensorboardLog \ # Path to the folder containing the log folder
			--weight_initialisation None \ # Path to the model to initialize the weights if any None
			--checkpoint_path /home/XXXX/LNENWork/MvTech/ModelsFeaturesMaps # Path to the folder containing the checkpoints
