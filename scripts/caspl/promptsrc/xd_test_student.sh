#!/bin/bash


# custom config
#DATA="/path/to/dataset/folder"
TRAINER=CasPL_PromptSRC

DATA=$1
DATASET=$2
SEED=$3
OUT_PUT=$4
DIR_NAME=$5
RESULT_PATH=$6
CFG=$7
KD_N_CTX_VISION=$8
KD_N_CTX_TEXT=$9
PROMPT_DEPTH_VISION=${10}
PROMPT_DEPTH_TEXT=${11}
SAVE_PATH=${12}

#CFG=vit_b16_c2_ep5_batch4_4+4ctx_cross_datasets
SHOTS=16

COMMON_DIR=${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}
COMMON_DIR_SAVE=${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}
MODEL_DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/train_base/${COMMON_DIR}
DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/test_${SUB}/${COMMON_DIR_SAVE}

if [ -d "$DIR" ]; then
    echo "Results are available in ${DIR}. Resuming..."
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR} \
    --load-epoch 20 \
    --eval-only \
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
    --model-dir ${MODEL_DIR} \
    --load-epoch 20 \
    --eval-only \
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