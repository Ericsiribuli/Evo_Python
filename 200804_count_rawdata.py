#原始二代reads数






#质控后reads数量
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s1-163_d1_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s2-164_d1_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s3-165_d1_only_umi.txt

wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s1-166_d3_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s2-167_d3_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s3-168_d3_only_umi.txt

wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s1-169_d5_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s2-170_d5_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s3-171_d5_only_umi.txt

wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s1-172_d7_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s2-173_d7_only_umi.txt
wc -l /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/AUU/s3-174_d7_only_umi.txt

#TGY
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/TG_27-28-29_total_result.txt" s1-52_d1_num_umi.txt s2-53_d1_num_umi.txt s3-54_d1_num_umi.txt s1-55_d3_num_umi.txt s2-56_d3_num_umi.txt s3-57_d3_num_umi.txt s1-58_d5_num_umi.txt s2-59_d5_num_umi.txt s3-60_d5_num_umi.txt s1-61_d7_num_umi.txt s2-62_d7_num_umi.txt s3-63_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TG_filter_geno_umi_final_8-2.txt" s1-52_d1_num_umi.txt s2-53_d1_num_umi.txt s3-54_d1_num_umi.txt s1-55_d3_num_umi.txt s2-56_d3_num_umi.txt s3-57_d3_num_umi.txt s1-58_d5_num_umi.txt s2-59_d5_num_umi.txt s3-60_d5_num_umi.txt s1-61_d7_num_umi.txt s2-62_d7_num_umi.txt s3-63_d7_num_umi.txt

#TGS
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/TG_27-28-29_total_result.txt" s1-64_d1_num_umi.txt s2-65_d1_num_umi.txt s3-66_d1_num_umi.txt s1-67_d3_num_umi.txt s2-68_d3_num_umi.txt s3-69_d3_num_umi.txt s1-70_d5_num_umi.txt s2-71_d5_num_umi.txt s3-72_d5_num_umi.txt s1-73_d7_num_umi.txt s2-74_d7_num_umi.txt s3-75_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TG_filter_geno_umi_final_8-2.txt" s1-64_d1_num_umi.txt s2-65_d1_num_umi.txt s3-66_d1_num_umi.txt s1-67_d3_num_umi.txt s2-68_d3_num_umi.txt s3-69_d3_num_umi.txt s1-70_d5_num_umi.txt s2-71_d5_num_umi.txt s3-72_d5_num_umi.txt s1-73_d7_num_umi.txt s2-74_d7_num_umi.txt s3-75_d7_num_umi.txt

#AGY
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/AG_200623_101855_subreads_blasr.result" s1-76_d1_num_umi.txt s2-77_d1_num_umi.txt s3-78_d1_num_umi.txt s1-79_d3_num_umi.txt s2-80_d3_num_umi.txt s3-81_d3_num_umi.txt s1-82_d5_num_umi.txt s2-83_d5_num_umi.txt s3-84_d5_num_umi.txt s1-85_d7_num_umi.txt s2-86_d7_num_umi.txt s3-87_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AG_filter_geno_umi_final_8-2.txt" s1-76_d1_num_umi.txt s2-77_d1_num_umi.txt s3-78_d1_num_umi.txt s1-79_d3_num_umi.txt s2-80_d3_num_umi.txt s3-81_d3_num_umi.txt s1-82_d5_num_umi.txt s2-83_d5_num_umi.txt s3-84_d5_num_umi.txt s1-85_d7_num_umi.txt s2-86_d7_num_umi.txt s3-87_d7_num_umi.txt

#AGS
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/AG_200623_101855_subreads_blasr.result" s1-88_d1_num_umi.txt s2-89_d1_num_umi.txt s3-90_d1_num_umi.txt s1-91_d3_num_umi.txt s2-92_d3_num_umi.txt s3-93_d3_num_umi.txt s1-94_d5_num_umi.txt s2-95_d5_num_umi.txt s3-96_d5_num_umi.txt s1-97_d7_num_umi.txt s2-98_d7_num_umi.txt s3-99_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AG_filter_geno_umi_final_8-2.txt" s1-88_d1_num_umi.txt s2-89_d1_num_umi.txt s3-90_d1_num_umi.txt s1-91_d3_num_umi.txt s2-92_d3_num_umi.txt s3-93_d3_num_umi.txt s1-94_d5_num_umi.txt s2-95_d5_num_umi.txt s3-96_d5_num_umi.txt s1-97_d7_num_umi.txt s2-98_d7_num_umi.txt s3-99_d7_num_umi.txt

#TUY
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/TU_16-17-18_total_result.txt"  s1-103_d1_num_umi.txt s2-104_d1_num_umi.txt s3-105_d1_num_umi.txt s1-106_d3_num_umi.txt s2-107_d3_num_umi.txt s3-108_d3_num_umi.txt s1-109_d5_num_umi.txt s2-110_d5_num_umi.txt s3-111_d5_num_umi.txt s1-112_d7_num_umi.txt s2-113_d7_num_umi.txt s3-114_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TU_filter_geno_umi_final_8-2.txt" s1-103_d1_num_umi.txt s2-104_d1_num_umi.txt s3-105_d1_num_umi.txt s1-106_d3_num_umi.txt s2-107_d3_num_umi.txt s3-108_d3_num_umi.txt s1-109_d5_num_umi.txt s2-110_d5_num_umi.txt s3-111_d5_num_umi.txt s1-112_d7_num_umi.txt s2-113_d7_num_umi.txt s3-114_d7_num_umi.txt

#TUS
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/TU_16-17-18_total_result.txt"  s1-115_d1_num_umi.txt s2-116_d1_num_umi.txt s3-117_d1_num_umi.txt s1-118_d3_num_umi.txt s2-119_d3_num_umi.txt s3-120_d3_num_umi.txt s1-121_d5_num_umi.txt s2-122_d5_num_umi.txt s3-123_d5_num_umi.txt s1-124_d7_num_umi.txt s2-125_d7_num_umi.txt s3-126_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TU_filter_geno_umi_final_8-2.txt" s1-115_d1_num_umi.txt s2-116_d1_num_umi.txt s3-117_d1_num_umi.txt s1-118_d3_num_umi.txt s2-119_d3_num_umi.txt s3-120_d3_num_umi.txt s1-121_d5_num_umi.txt s2-122_d5_num_umi.txt s3-123_d5_num_umi.txt s1-124_d7_num_umi.txt s2-125_d7_num_umi.txt s3-126_d7_num_umi.txt

#TUU
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/TU_16-17-18_total_result.txt" s1-127_d1_num_umi.txt s2-128_d1_num_umi.txt s3-129_d1_num_umi.txt s1-130_d3_num_umi.txt s2-131_d3_num_umi.txt s3-132_d3_num_umi.txt s1-133_d5_num_umi.txt s2-134_d5_num_umi.txt s3-135_d5_num_umi.txt s1-136_d7_num_umi.txt s2-137_d7_num_umi.txt s3-138_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TU_filter_geno_umi_final_8-2.txt" s1-127_d1_num_umi.txt s2-128_d1_num_umi.txt s3-129_d1_num_umi.txt s1-130_d3_num_umi.txt s2-131_d3_num_umi.txt s3-132_d3_num_umi.txt s1-133_d5_num_umi.txt s2-134_d5_num_umi.txt s3-135_d5_num_umi.txt s1-136_d7_num_umi.txt s2-137_d7_num_umi.txt s3-138_d7_num_umi.txt

#AUY
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/AU_200623_101855_subreads_blasr.result" s1-139_d1_num_umi.txt s2-140_d1_num_umi.txt s3-141_d1_num_umi.txt s1-142_d3_num_umi.txt s2-143_d3_num_umi.txt s3-144_d3_num_umi.txt s1-145_d5_num_umi.txt s2-146_d5_num_umi.txt s3-147_d5_num_umi.txt s1-148_d7_num_umi.txt s2-149_d7_num_umi.txt s3-150_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AU_filter_geno_umi_final_8-2.txt" s1-139_d1_num_umi.txt s2-140_d1_num_umi.txt s3-141_d1_num_umi.txt s1-142_d3_num_umi.txt s2-143_d3_num_umi.txt s3-144_d3_num_umi.txt s1-145_d5_num_umi.txt s2-146_d5_num_umi.txt s3-147_d5_num_umi.txt s1-148_d7_num_umi.txt s2-149_d7_num_umi.txt s3-150_d7_num_umi.txt

#AUS
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/AU_200623_101855_subreads_blasr.result"  s1-151_d1_num_umi.txt s2-152_d1_num_umi.txt s3-153_d1_num_umi.txt s1-154_d3_num_umi.txt s2-155_d3_num_umi.txt s3-156_d3_num_umi.txt s1-157_d5_num_umi.txt s2-158_d5_num_umi.txt s3-159_d5_num_umi.txt s1-160_d7_num_umi.txt s2-161_d7_num_umi.txt s3-162_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AU_filter_geno_umi_final_8-2.txt" s1-151_d1_num_umi.txt s2-152_d1_num_umi.txt s3-153_d1_num_umi.txt s1-154_d3_num_umi.txt s2-155_d3_num_umi.txt s3-156_d3_num_umi.txt s1-157_d5_num_umi.txt s2-158_d5_num_umi.txt s3-159_d5_num_umi.txt s1-160_d7_num_umi.txt s2-161_d7_num_umi.txt s3-162_d7_num_umi.txt

#AUU
python 200805_count_barcode_beforefilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/AU_200623_101855_subreads_blasr.result"  s1-163_d1_num_umi.txt s2-164_d1_num_umi.txt s3-165_d1_num_umi.txt s1-166_d3_num_umi.txt s2-167_d3_num_umi.txt s3-168_d3_num_umi.txt s1-169_d5_num_umi.txt s2-170_d5_num_umi.txt s3-171_d5_num_umi.txt s1-172_d7_num_umi.txt s2-173_d7_num_umi.txt s3-174_d7_num_umi.txt
python 200805_count_barcode_afterfilter.py "/mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AU_filter_geno_umi_final_8-2.txt" s1-163_d1_num_umi.txt s2-164_d1_num_umi.txt s3-165_d1_num_umi.txt s1-166_d3_num_umi.txt s2-167_d3_num_umi.txt s3-168_d3_num_umi.txt s1-169_d5_num_umi.txt s2-170_d5_num_umi.txt s3-171_d5_num_umi.txt s1-172_d7_num_umi.txt s2-173_d7_num_umi.txt s3-174_d7_num_umi.txt

#相关性图pearson的code
python 200807_all_pearson_geno_nowt.py AGY_sample.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/AG_filter_geno_umi_final_8-2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/AGY/ >AGY_pearson_nowt.txt
python 200807_all_pearson_geno_nowt.py TUY_sample.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/TU_filter_geno_umi_final_8-2.txt /mnt/data2/disk/smrtanalysis/pacbio_data_new/new_illumina_data_2-14/20202015_sample_data/ura3_new_6-16/TUY/ >TUY_pearson_nowt.txt