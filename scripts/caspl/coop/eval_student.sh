#!/bin/bash

#cd ../..

# custom config
#DATA=/path/to/datasets
TRAINER=CasPL_CoOp


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
NCTX=${13}
EPOCH=${14}
CTP=end
SHOTS=16
CSC=False

SUB=new

COMMON_DIR=${DATASET}/shots_${SHOTS}/${TRAINER}/${CFG}/seed${SEED}
MODEL_DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/train_base/${COMMON_DIR}
DIR=${SAVE_PATH}/${OUT_PUT}/${DIR_NAME}/base2new/test_${SUB}/${COMMON_DIR}
python train.py \
--root ${DATA} \
--seed ${SEED} \
--trainer ${TRAINER} \
--dataset-config-file configs/datasets/${DATASET}.yaml \
--config-file configs/trainers/${TRAINER}/${CFG}.yaml \
--output-dir ${DIR} \
--model-dir ${MODEL_DIR} \
--load-epoch ${EPOCH} \
--eval-only \
TRAINER.COOP.N_CTX ${NCTX} \
TRAINER.COOP.CSC ${CSC} \
TRAINER.COOP.CLASS_TOKEN_POSITION ${CTP} \
DATASET.NUM_SHOTS ${SHOTS} \
DATASET.SUBSAMPLE_CLASSES ${SUB} \
KD.IS_TEST True \
KD.FIRST_TRAIN False \
KD.SECOND_TRAIN True \
KD.DIR_NAME ${DIR_NAME}"&"${SEED} \
KD.RESULT_PATH ${RESULT_PATH} \
KD.N_CTX_VISION ${KD_N_CTX_VISION} \
KD.N_CTX_TEXT ${KD_N_CTX_TEXT} \
KD.PROMPT_DEPTH_VISION ${PROMPT_DEPTH_VISION} \
KD.PROMPT_DEPTH_TEXT ${PROMPT_DEPTH_TEXT} \
KD.USE_IVLP True
