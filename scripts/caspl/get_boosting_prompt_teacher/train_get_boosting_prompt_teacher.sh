#!/bin/bash

#cd ../..

# custom config
#DATA="/path/to/dataset/folder"
TRAINER=CasPL

DATA=$1
DATASET=$2
SEED=$3
OUT_PUT=$4
DIR_NAME=$5
CFG=$6
SAVE_PATH=$7
#CFG=vit_b16_c2_ep20_batch4_4+4ctx
#SHOTS=16


DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/first_stage/boosting_prompt/${DATASET}/shots_all/${TRAINER}/${CFG}/seed${SEED}
if [ -d "$DIR" ]; then
    echo "Results are available in ${DIR}. Resuming..."
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    KD.FIRST_TRAIN True \
    KD.SECOND_TRAIN False
else
    echo "Run this job and save the output to ${DIR}"
    python train.py \
    --root ${DATA} \
    --seed ${SEED} \
    --trainer ${TRAINER} \
    --dataset-config-file configs/datasets/${DATASET}.yaml \
    --config-file configs/trainers/${TRAINER}/${CFG}.yaml \
    --output-dir ${DIR} \
    KD.FIRST_TRAIN True \
    KD.SECOND_TRAIN False
fi