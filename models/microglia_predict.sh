CUDA_VISIBLE_DEVICES=$2 kerasAC_predict \
    --model_hdf5 /mnt/lab_data3/soumyak/adpd/deeplearning/models/regression/single_cell/$1.model.1 \
    --data_path /mnt/lab_data3/soumyak/adpd/deeplearning/inputs/sc.input.hdf5 \
    --predictions_pickle /mnt/lab_data3/soumyak/adpd/deeplearning/predictions/regression/single_cell/pickles/$1.preds.1 \
    --batch_size 1000 \
    --threads 40 \
    --tasks $1 \
    --max_queue_size 1000 \
    --predict_chroms $3 \
    --ref_fasta /mnt/data/annotations/by_release/hg38/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
    --performance_metrics_regression_file /mnt/lab_data3/soumyak/adpd/deeplearning/predictions/regression/single_cell/performance/$1.perfs.1 \
