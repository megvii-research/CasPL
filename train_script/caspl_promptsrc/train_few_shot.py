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
SAVE_PATH="save_path/caspl_promptsrc_few_shot"
PATH_TEACHER = "save_path/caspl_teacher"
#PATH_TEACHER = "kd_num_depth_12_imagenet_only"

#CFG_S1_DICT = [["vit_b16_c2_ep20_batch128_lr08_8+8ctx_l12"   ,8, 12]]
CFG_S1_DICT = [["vit_b16_c2_ep20_batch4_8+8ctx_l12"   ,8, 12]]
CFG_S2_LIST = [["vit_b16_c2_ep50_batch4_8+8ctx_few_shot_l12"   ,8]]
SHOTS_LIST = [1, 2, 4, 8, 16]

for (DATASET, DATA) in dataset_list:
    print(DATASET, DATA)
    for (CFG_S1, KD_N_CTX_VISION_TEACHER, PROMPT_DEPTH_VISION_TEACHER) in CFG_S1_DICT:
        # traing the first step
        OUT_PUT_TEACHER = "caspl_s1_v" + str(KD_N_CTX_VISION_TEACHER) + "_t" + str(KD_N_CTX_VISION_TEACHER) + "_s2_v" + str(0) + "_t" + str(0)
        DIR_NAEM = "teacher"

        for SHOTS_LIST_STUDENT in SHOTS_LIST:
            for (CFG_S2, N_CTX_VISION_STUDENT) in CFG_S2_LIST:
                OUT_PUT = "caspl_promptsrc_s1_int_v" + str(KD_N_CTX_VISION_TEACHER) + "_t" + str(KD_N_CTX_VISION_TEACHER) + "_s2_int_v" + str(N_CTX_VISION_STUDENT) \
                          +"_t" + str(N_CTX_VISION_STUDENT) +"_student_shots" + str(SHOTS_LIST_STUDENT) + "_" +str(CFG_S1)
                RESULT_PATH = SAVE_PATH + "/output_" + OUT_PUT + "/"
                DIR_NAEM_STUDNET = "student"
                DIR_NAME_TEACHER = DIR_NAEM
                CFG_NAME = CFG_S1
                KD_N_CTX_VISION = KD_N_CTX_VISION_TEACHER
                KD_N_CTX_TEXT = KD_N_CTX_VISION_TEACHER
                PROMPT_DEPTH_VISION = PROMPT_DEPTH_VISION_TEACHER
                PROMPT_DEPTH_TEXT = PROMPT_DEPTH_VISION_TEACHER
                if DATASET in ['imagenet', 'caltech101', 'oxford_pets', 'food101', 'ucf101', 'sun397']:
                    GPA_MEAN = 30
                    GPA_STD = 30
                else:
                    GPA_MEAN = 45
                    GPA_STD = 5
                # traing the second step
                for COUNTER in range(1, 4):
                    cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/promptsrc/few_shot_promptsrc_student.sh \
                          {DATA} {DATASET} {COUNTER} {OUT_PUT} {DIR_NAEM_STUDNET} {DIR_NAME_TEACHER} \
                          {RESULT_PATH} {CFG_S2} {CFG_NAME} \
                          {KD_N_CTX_VISION} {KD_N_CTX_TEXT} \
                          {PROMPT_DEPTH_VISION} {PROMPT_DEPTH_TEXT}\
                          {SAVE_PATH} {OUT_PUT_TEACHER} \
                          {SHOTS_LIST_STUDENT} {GPA_MEAN} {GPA_STD} {PATH_TEACHER}"
                    os.system(cmd)





