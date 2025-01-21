import os

dataset_list = [
    ['imagenet', "data_path/imagenet"],
]

dataset_list_test = [
    ['imagenet', "data_path/imagenet"],
    ['imagenetv2', "data_path/imagenetv2"],
    ['imagenet_sketch', "data_path/imagenet_sketch"],
    ['imagenet_r', "data_path/imagenet_r"],
]

GPU_NUM=0
SAVE_PATH="save_path/caspl_maple_cross_dataset"
PATH_TEACHER="save_path/caspl_teacher"
#PATH_TEACHER = "kd_num_depth_12_imagenet_only"
#CFG_S1_DICT = [["vit_b16_c2_ep20_batch128_lr0025_8+8ctx_l12", 8, 12]]

CFG_S1_DICT = [["vit_b16_c2_ep20_batch128_lr0025_4+4ctx_l1", 4, 1]]
CFG_S2_LIST = [["vit_b16_c8_ep5_batch4_8ctx_cross_datasets_l12"   ,8, 12]]


for (DATASET, DATA) in dataset_list:
    print(DATASET, DATA)
    for (CFG_S1, KD_N_CTX_VISION_TEACHER, PROMPT_DEPTH_VISION_TEACHER) in CFG_S1_DICT:
        OUT_PUT_TEACHER = ("caspl_s1_v" + str(KD_N_CTX_VISION_TEACHER) +
                           "_t" + str(KD_N_CTX_VISION_TEACHER) + "_s2_v" + str(0) + "_t" + str(0))
        DIR_NAEM = "teacher"

        for (CFG_S2, N_CTX_VISION_STUDENT, LAYER_STUDENT) in CFG_S2_LIST:
            OUT_PUT = ("caspl_maple_s1_v" + str(KD_N_CTX_VISION_TEACHER) +
                       "_t" + str(KD_N_CTX_VISION_TEACHER) + "_s2_v" + str(N_CTX_VISION_STUDENT) \
                      +"_t" + str(N_CTX_VISION_STUDENT) + "_l" + str(LAYER_STUDENT) + "_" + str(CFG_S2))
            RESULT_PATH = SAVE_PATH + "/output_" + OUT_PUT + "/"
            DIR_NAEM_STUDNET = "student"
            DIR_NAME_TEACHER = DIR_NAEM
            CFG_NAME = CFG_S1
            KD_N_CTX_VISION = KD_N_CTX_VISION_TEACHER
            KD_N_CTX_TEXT = KD_N_CTX_VISION_TEACHER
            PROMPT_DEPTH_VISION = PROMPT_DEPTH_VISION_TEACHER
            PROMPT_DEPTH_TEXT = PROMPT_DEPTH_VISION_TEACHER
            # traing the second step
            for COUNTER in range(1, 4):
                cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/maple/xd_train_student.sh \
                      {DATA} {DATASET} {COUNTER} {OUT_PUT} {DIR_NAEM_STUDNET} {DIR_NAME_TEACHER} \
                      {RESULT_PATH} {CFG_S2} {CFG_NAME} \
                      {KD_N_CTX_VISION} {KD_N_CTX_TEXT} \
                      {PROMPT_DEPTH_VISION} {PROMPT_DEPTH_TEXT}\
                      {SAVE_PATH} {OUT_PUT_TEACHER} {PATH_TEACHER}"
                os.system(cmd)

                for (DATASET_TEST, DATA_TEST) in dataset_list_test:
                    cmd = f"CUDA_VISIBLE_DEVICES={GPU_NUM} bash scripts/caspl/maple/xd_test_student.sh \
                          {DATA_TEST} {DATASET_TEST} {COUNTER} {OUT_PUT} {DIR_NAEM_STUDNET}  \
                          {RESULT_PATH} {CFG_S2} \
                          {KD_N_CTX_VISION} {KD_N_CTX_TEXT} \
                          {PROMPT_DEPTH_VISION} {PROMPT_DEPTH_TEXT}\
                          {SAVE_PATH}"
                    os.system(cmd)















