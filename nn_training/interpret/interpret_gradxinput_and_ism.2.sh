#!/bin/bash
for cluster in `seq 13 23`
do
    for fold in `seq 1 9`
    do
	CUDA_VISIBLE_DEVICES=2 python interpret_gradxinput_and_ism.py \
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
			    --model_string /srv/scratch/annashch/deeplearning/adpd/clusters_gc_classification/Cluster$cluster/DNASE.$cluster.classificationlabels.withgc.$fold \
			    --target_layer_idx -2 \
			    --outf sig.snps.Cluster$cluster.fold$fold.classification
    done
done
