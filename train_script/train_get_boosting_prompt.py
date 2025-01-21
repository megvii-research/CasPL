import os

dataset_list = [
    ['fgvc_aircraft', "data_path/fgvc-aircraft-2013b/"],
    ['food101', "data_path/food-101/"],
    ['caltech101', "data_path/caltech-101/"],
    ['oxford_pets', "data_path/oxford_pets"],
    ['stanford_cars', "data_path/stanford_cars"],
    ['oxford_flowers', "data_path/oxford_flowers"],
    ['sun397', "data_path/sun397"],
    ['dtd', "data_path/dtd/dtd"],
    ['eurosat', "data_path/eurosat"],
    ['ucf101', "data_path/ucf101"],
    ['imagenet', "data_path/imagenet"],
]


GPU_NUM=0
SAVE_PATH="save_path/caspl_teacher"
CFG_S1_DICT = [["vit_b16_c2_ep20_batch4_8+8ctx_l12"   ,8]]# other datasets
#CFG_S1_DICT = [["vit_b16_c2_ep20_batch128_lr0025_8+8ctx_l12", 8]] #imagenet

for (DATASET, DATA) in dataset_list:
    print(DATASET, DATA)
    for (CFG_S1, KD_N_CTX_TEACHER) in CFG_S1_DICT:
        # traing the first step
        OUT_PUT_TEACHER = "caspl_promptsrc_s1_v" + str(KD_N_CTX_TEACHER) + "_t" + str(KD_N_CTX_TEACHER) + "_s2_v" + str(0) + "_t" + str(0)
        DIR_NAEM = "teacher"
        for COUNTER in range(1, 2):
            cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/get_boosting_prompt_teacher/train_get_boosting_prompt_teacher.sh \
                  {DATA} {DATASET} {COUNTER} {OUT_PUT_TEACHER} {DIR_NAEM} {CFG_S1} {SAVE_PATH}"
            os.system(cmd)

















