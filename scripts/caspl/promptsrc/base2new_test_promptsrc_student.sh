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
SAVE_PATH=${10}
#CFG=vit_b16_c2_ep20_batch4_4+4ctx
SHOTS=16
LOADEP=20
SUB=new


COMMON_DIR=${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}
MODEL_DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/train_base/${COMMON_DIR}
DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/test_${SUB}/${COMMON_DIR}

if [ -d "$DIR" ]; then
    echo "Evaluating model"
    echo "Results are available in ${DIR}. Resuming..."

    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR} \
    --load-epoch ${LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS ${SHOTS} \
    DATASET.SUBSAMPLE_CLASSES ${SUB} \
    KD.IS_TEST True \
    KD.FIRST_TRAIN False \
    KD.SECOND_TRAIN True \
    KD.DIR_NAME ${DIR_NAME}"&"${SEED} \
    KD.RESULT_PATH ${RESULT_PATH} \
    KD.N_CTX_VISION ${KD_N_CTX_VISION} \
    KD.N_CTX_TEXT ${KD_N_CTX_TEXT}
else
    echo "Evaluating model"
    echo "Runing the first phase job and save the output to ${DIR}"

    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    --model-dir ${MODEL_DIR} \
    --load-epoch ${LOADEP} \
    --eval-only \
    DATASET.NUM_SHOTS ${SHOTS} \
    DATASET.SUBSAMPLE_CLASSES ${SUB} \
    KD.IS_TEST True \
    KD.FIRST_TRAIN False \
    KD.SECOND_TRAIN True \
    KD.DIR_NAME ${DIR_NAME}"&"${SEED} \
    KD.RESULT_PATH ${RESULT_PATH} \
    KD.N_CTX_VISION ${KD_N_CTX_VISION} \
    KD.N_CTX_TEXT ${KD_N_CTX_TEXT}
fi