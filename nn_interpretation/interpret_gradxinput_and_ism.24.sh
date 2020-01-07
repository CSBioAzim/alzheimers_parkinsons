#!/bin/bash
for cluster in 24
do
    for fold in `seq 0 9`
    do
	CUDA_VISIBLE_DEVICES=3 python interpret_gradxinput_and_ism.py \
		    --bed_path=/srv/scratch/annashch/deeplearning/adpd/interpret/SigSNPs_AllClusters_MergedUnique.csv \
		    --ref_allele_col noneffect \
		    --alt_allele_col effect \
		    --compute_gc \
		    --flank_size 500 \
		    --chrom_col chr \
		    --pos_col start \
		    --rsid_col rsid \
		    --ref_fasta /mnt/data/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
		    --batch_size 123 \
		    --model_string /srv/scratch/annashch/deeplearning/adpd/microglia_gc/classification/ADPD.Cluster24.pseudobulk.classificationlabels.withgc.$fold \
		    --target_layer_idx -2 \
		    --outf sig.snps.Cluster$cluster.fold$fold.classification
	CUDA_VISIBLE_DEVICES=3 python interpret_gradxinput_and_ism.py \
		    --bed_path=/srv/scratch/annashch/deeplearning/adpd/interpret/SigSNPs_AllClusters_MergedUnique.csv \
		    --ref_allele_col noneffect \
		    --alt_allele_col effect \
		    --compute_gc \
		    --flank_size 500 \
		    --chrom_col chr \
		    --pos_col start \
		    --rsid_col rsid \
		    --ref_fasta /mnt/data/GRCh38_no_alt_analysis_set_GCA_000001405.15.fasta \
		    --batch_size 123 \
		    --model_string /srv/scratch/annashch/deeplearning/adpd/microglia_gc/regression/ADPD.Cluster24.pseudobulk.regressionlabels.withgc.$fold \
		    --target_layer_idx -2 \
		    --outf sig.snps.Cluster$cluster.fold$fold.regression
	
    done
done
