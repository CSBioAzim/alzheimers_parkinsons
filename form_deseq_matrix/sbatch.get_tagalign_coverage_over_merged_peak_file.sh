#get the counts for each sample within each peak                                                                                                                                                                  export numfiles=$(cat tagAlign.files.txt | wc -l)
echo $numfiles
for i in $(seq 1 $numfiles)
do
    cur_sample_name=$(head -n $i tagAlign.files.txt | tail -n1 | cut -f1)
    echo $cur_sample_name > counts.$cur_sample_name.txt
    cur_tagalign=$(head -n $i tagAlign.files.txt | tail -n1 | cut -f2)
    echo "$cur_sample_name $cur_tagalign"
    sbatch -p akundaje,euan,normal,owners -o $cur_sample_name.o -e $cur_sample_name.e -J $cur_sample_name get_tagalign_coverage_over_merged_peak_file.sh $cur_tagalign $cur_sample_name 
done
