name_map={}
name_map[13]="astrocytes"
name_map[14]="astrocytes"
name_map[15]="astrocytes"
name_map[16]="astrocytes"
name_map[17]="astrocytes"
name_map[1]="excitatory_neurons"
name_map[3]="excitatory_neurons"
name_map[4]="excitatory_neurons"
name_map[11]="inhibitory_neurons"
name_map[12]="inhibitory_neurons"
name_map[2]="inhibitory_neurons"
name_map[24]="microglia"
name_map[19]="oligodendrocytes"
name_map[20]="oligodendrocytes"
name_map[21]="oligodendrocytes"
name_map[22]="oligodendrocytes"
name_map[23]="oligodendrocytes"
name_map[10]="opcs"
name_map[8]="opcs"
name_map[9]="opcs"
name_map[5]="nigral_neurons"
name_map[6]="nigral_neurons"
name_map[18]="doublets"
name_map[7]="unknown"

import sys
import os 
cur_name=sys.argv[1]
cur_cluster_number=cur_name.split('/')[-1].split('.')[1]
cur_cluster_name=name_map[int(cur_cluster_number)]
folder='/'.join(cur_name.split('/')[0:-1])
snp=cur_name.split('/')[-1].split('.')[0]
fold=cur_name.split('/')[-1].split('.')[2]
new_name=folder+'/'+snp+'.'+cur_cluster_number+"_"+cur_cluster_name+"."+fold+".svg"
print(new_name)
os.rename(cur_name,new_name)



