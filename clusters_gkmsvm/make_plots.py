#generate plots for snps
import argparse
import pickle
from dragonn.vis import *
import os.path


def parse_args():
    parser=argparse.ArgumentParser(description="generate plots for ADPD SNPs")
    parser.add_argument("--input_pickle_classification")
    parser.add_argument("--input_pickle_regression")
    parser.add_argument("--cluster")
    parser.add_argument("--fold")
    parser.add_argument("--outpng_prefix",default="")
    return parser.parse_args()

def plot_seq_importance(tracks,labels, ylim,xlim=None, figsize=(25, 6),snp_pos=0, cluster=0, fold=0, rsid='rs1234567'):
    num_plots=len(tracks)
    f,axes=plt.subplots(num_plots,dpi=80,figsize=figsize)
    show=False
    tracks=[i.squeeze() for i in tracks]
    seq_len = tracks[0].shape[0]
    if xlim is None:
        xlim = (0, seq_len)
    for plot_index in range(num_plots):
        cur_track=tracks[plot_index]
        axes[plot_index]=plot_bases_on_ax(cur_track,axes[plot_index],show_ticks=True)
        axes[plot_index].set_xlim(xlim)
        axes[plot_index].set_ylim(ylim)
        cur_label=labels[plot_index]
        axes[plot_index].set_title(':'.join([rsid,cluster,fold,'gkmSVM','gkmExplain',cur_label]))
        axes[plot_index].axvline(x=snp_pos,color='k',linestyle='--')
        axes[plot_index].tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off
    plt.subplots_adjust(hspace=0.8)
    plt.savefig('/oak/stanford/groups/akundaje/projects/alzheimers_parkinsons/svm_snp_tracks/png/cluster'+str(cluster)+'/'+rsid+'_fold'+str(fold)+'.png',dpi=120)
    plt.savefig('/oak/stanford/groups/akundaje/projects/alzheimers_parkinsons/svm_snp_tracks/svg/cluster'+str(cluster)+'/'+rsid+'_fold'+str(fold)+'.svg',dpi=120,format='svg')
    plt.close()
    return

def main():
    args=parse_args()
    #load the input pickle
    classification=pickle.load(open(args.input_pickle_classification,'rb'))
    print("loaded classification pickle")
    regression=pickle.load(open(args.input_pickle_regression,'rb'))
    print("loaded regression pickle")
    snps=classification['rsid']
    class_gradxinput_ref=classification['gradxinput_ref']
    class_gradxinput_alt=classification['gradxinput_alt']
    class_gradxinput_delta=classification['gradxinput_delta']
    class_ism=classification['ism']
    class_ismxinput=classification['ismxinput']
    reg_gradxinput_ref=regression['gradxinput_ref']
    reg_gradxinput_alt=regression['gradxinput_alt']
    reg_gradxinput_delta=regression['gradxinput_delta']
    reg_ism=regression['ism']
    reg_ismxinput=regression['ismxinput']
    print("plotting...")
    for index in range(len(snps)):
        cur_snp=snps[index]
        print(cur_snp)
        cur_title='.'.join([cur_snp,args.cluster,args.fold,'png'])
        if os.path.isfile(cur_title):
            continue

        #make the plot for the current snp
        cur_tracks=[class_gradxinput_ref[index],
                    class_gradxinput_alt[index],
                    class_gradxinput_delta[index],
                    reg_gradxinput_ref[index],
                    reg_gradxinput_alt[index],
                    reg_gradxinput_delta[index],
                    class_ismxinput[index],
                    reg_ismxinput[index]]
        minvals=[]
        maxvals=[]
        #classification y bounds
        class_min=min([np.amin(i) for i in [class_gradxinput_ref[index],class_gradxinput_alt[index],class_gradxinput_delta[index]]])
        minvals.append(class_min)
        minvals.append(class_min)
        minvals.append(class_min)
        class_max=max([np.amax(i) for i in [class_gradxinput_ref[index],class_gradxinput_alt[index],class_gradxinput_delta[index]]])
        maxvals.append(class_max)
        maxvals.append(class_max)
        maxvals.append(class_max)


        #regression y bounds
        reg_min=min([np.amin(i) for i in [reg_gradxinput_ref[index],reg_gradxinput_alt[index],reg_gradxinput_delta[index]]])
        minvals.append(reg_min)
        minvals.append(reg_min)
        minvals.append(reg_min)
        reg_max=max([np.amax(i) for i in [reg_gradxinput_ref[index],reg_gradxinput_alt[index],reg_gradxinput_delta[index]]])
        maxvals.append(reg_max)
        maxvals.append(reg_max)
        maxvals.append(reg_max)

        #ism classification y bounds
        minvals.append(np.amin(class_ismxinput[index]))
        maxvals.append(np.amax(class_ismxinput[index]))

        #ism regression y bounds
        minvals.append(np.amin(reg_ismxinput[index]))
        maxvals.append(np.amax(reg_ismxinput[index]))

        ylim=[(minvals[i],maxvals[i]) for i in range(len(cur_tracks))]
        cur_labels=[]
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'classification','gradxinput','noneffect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'classification','gradxinput','effect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'classification','gradxinput','effect - noneffect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'regression','gradxinput','noneffect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'regression','gradxinput','effect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'regression','gradxinput','effect - noneffect']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'classification','ismxinput']))
        cur_labels.append(':'.join([cur_snp,args.cluster,args.fold,'regression','ismxinput']))
        plot_seq_importance(cur_tracks,
                            cur_labels,
                            xlim=(400,600),
                            ylim=ylim,
                            figsize=(18, 16),title=cur_title,
                            snp_pos=501)
if __name__=="__main__":
    main()

