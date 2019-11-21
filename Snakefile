GENES = ['SDHB', 'MEN1', 'KCNH2', 'MSH2', 'MYL2', 'BRCA2']
TISSUES = ['Brain', 'Heart', 'Blood', 'Skin']

rule all:
    input:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'


rule get_gene_counts:
    input:
        'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct.gz'
    output:
        expand('{gene}_counts.txt', gene=GENES)
    shell:
        'for gene in {GENES}; do ' \
        + 'python get_gene_counts.py --count_file {input} --gene_name $gene --out_file $gene\_counts.txt;' \
        + 'done'

rule get_tissue_samples:
    input:
        'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
    output:
        expand('{tissue}_samples.txt', tissue=TISSUES)
    shell:
        'for tissue in {TISSUES}; do ' \
        + 'python get_tissue_samples.py --attribute_file {input} --tissue_group $tissue --out_file $tissue\_samples.txt;' \
        + 'done'

rule box:
    input:
        rules.get_gene_counts.output,
        rules.get_tissue_samples.output
    output:
        'Brain-Heart-Blood-Skin_SDHB-MEN1-KCNH2-MSH2-MYL2-BRCA2.png'
    shell:
        'python box.py --tissue {TISSUES} --genes {GENES} --out_file {output} '