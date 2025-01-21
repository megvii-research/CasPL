#!/bin/bash

# custom config
#DATA="/path/to/dataset/folder"
TRAINER=CasPL_PromptSRC
TRAINER2=CasPL

DATA=$1
DATASET=$2
SEED=$3
OUT_PUT=$4
DIR_NAME=$5
DIR_NAME_TEACHER=$6
RESULT_PATH=$7
CFG=$8
CFG_NAME=$9
KD_N_CTX_VISION=${10}
KD_N_CTX_TEXT=${11}
PROMPT_DEPTH_VISION=${12}
PROMPT_DEPTH_TEXT=${13}
SAVE_PATH=${14}
OUT_PUT_TEACHER=${15}
PATH_TEACHER=${16}
#CFG=vit_b16_c2_ep5_batch4_4+4ctx_cross_datasets
SHOTS=16

COMMON_DIR=${DATASET}/shots_all/${TRAINER2}/${CFG_NAME}/seed1
MODEL_DIR=${PATH_TEACHER}/${OUT_PUT_TEACHER}/${DIR_NAME_TEACHER}/first_stage/boosting_prompt/${COMMON_DIR}
DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/train_base/${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}

if [ -d "$DIR" ]; then
    echo "Results are available in ${DIR}. Resuming..."
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR}\
    --load-epoch 20 \
    DATASET.NUM_SHOTS ${SHOTS} \
    KD.IS_TEST True \
    KD.FIRST_TRAIN False \
    KD.SECOND_TRAIN True \
    KD.DIR_NAME ${DIR_NAME}"&"${SEED} \
    KD.RESULT_PATH ${RESULT_PATH} \
    KD.PROMPT_DEPTH_VISION ${PROMPT_DEPTH_VISION} \
    KD.PROMPT_DEPTH_TEXT ${PROMPT_DEPTH_TEXT} \
    KD.N_CTX_VISION ${KD_N_CTX_VISION} \
    KD.N_CTX_TEXT ${KD_N_CTX_TEXT}
else
    echo "Run this job and save the output to ${DIR}"
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR}\
    --load-epoch 20 \
    DATASET.NUM_SHOTS ${SHOTS} \
    KD.IS_TEST True \
    KD.FIRST_TRAIN False \
    KD.SECOND_TRAIN True \
    KD.DIR_NAME ${DIR_NAME}"&"${SEED} \
    KD.RESULT_PATH ${RESULT_PATH} \
    KD.PROMPT_DEPTH_VISION ${PROMPT_DEPTH_VISION} \
    KD.PROMPT_DEPTH_TEXT ${PROMPT_DEPTH_TEXT} \
    KD.N_CTX_VISION ${KD_N_CTX_VISION} \
    KD.N_CTX_TEXT ${KD_N_CTX_TEXT}
fi