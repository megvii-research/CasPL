import os

dataset_list = [
    ['fgvc_aircraft', "data_path/fgvc-aircraft-2013b/"],
    #['food101', "data_path/food-101/"],
    #['caltech101', "data_path/caltech-101/"],
    #['oxford_pets', "data_path/oxford_pets"],
    #['stanford_cars', "data_path/stanford_cars"],
    #['oxford_flowers', "data_path/oxford_flowers"],
    # ['sun397', "data_path/sun397"],
    #['dtd', "data_path/dtd/dtd"],
    # ['eurosat', "data_path/eurosat"],
    # ['ucf101', "data_path/ucf101"],
    #['imagenet', "data_path/imagenet"],
]


GPU_NUM=0
SAVE_PATH="save_path/caspl_coop_base_to_novel"
PATH_TEACHER="save_path/caspl_teacher"

CFG_S1_DICT = [["vit_b16_c2_ep20_batch4_8+8ctx_l12"   ,8, 12]]# other datasets
#CFG_S1_DICT = [["vit_b16_c2_ep20_batch128_lr0025_8+8ctx_l12", 8, 12]] # imagenet
CFG_S2_LIST = [["vit_b16_ep50", 8, 50]]


for (DATASET, DATA) in dataset_list:
    print(DATASET, DATA)
    for (CFG_S1, KD_N_CTX_VISION_TEACHER, KD_PROMPT_DEPTH_VISION_TEACHER) in CFG_S1_DICT:
        OUT_PUT_TEACHER = ("caspl_s1_v" + str(KD_N_CTX_VISION_TEACHER) +
                           "_t" + str(KD_N_CTX_VISION_TEACHER) + "_s2_v" + str(0) + "_t" + str(0))
        DIR_NAEM = "teacher"

        for (CFG_S2, N_CTX_VISION_STUDENT, EPOCH) in CFG_S2_LIST:
            OUT_PUT = ("caspl_coop_s1_v" + str(KD_N_CTX_VISION_TEACHER) + "_t" + str(KD_N_CTX_VISION_TEACHER) +"_"
                       + CFG_S2 +"_s2_v" + str(N_CTX_VISION_STUDENT) +"_t" + str(N_CTX_VISION_STUDENT))
            RESULT_PATH = SAVE_PATH + "/output_" + OUT_PUT + "/"
            DIR_NAEM_STUDNET = "student"
            DIR_NAME_TEACHER = DIR_NAEM
            CFG_NAME = CFG_S1
            KD_N_CTX_VISION = KD_N_CTX_VISION_TEACHER
            KD_N_CTX_TEXT = KD_N_CTX_VISION_TEACHER
            NCTX = N_CTX_VISION_STUDENT
            PROMPT_DEPTH_VISION = KD_PROMPT_DEPTH_VISION_TEACHER
            PROMPT_DEPTH_TEXT = KD_PROMPT_DEPTH_VISION_TEACHER
            # traing the second step
            for COUNTER in range(1, 4):
                cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/coop/main_student.sh \
                      {DATA} {DATASET} {COUNTER} {OUT_PUT} {DIR_NAEM_STUDNET} {DIR_NAME_TEACHER} \
                      {RESULT_PATH} {CFG_S2} {CFG_NAME} \
                      {KD_N_CTX_VISION} {KD_N_CTX_TEXT} \
                      {PROMPT_DEPTH_VISION} {PROMPT_DEPTH_TEXT}\
                      {SAVE_PATH} {OUT_PUT_TEACHER} {NCTX} {PATH_TEACHER}"
                os.system(cmd)
                cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/coop/eval_student.sh \
                      {DATA} {DATASET} {COUNTER} {OUT_PUT} {DIR_NAEM_STUDNET}  \
                      {RESULT_PATH} {CFG_S2} \
                      {KD_N_CTX_VISION} {KD_N_CTX_TEXT} \
                      {PROMPT_DEPTH_VISION} {PROMPT_DEPTH_TEXT}\
                      {SAVE_PATH} {NCTX} {EPOCH}"
                os.system(cmd)















