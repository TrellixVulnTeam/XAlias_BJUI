DATA_ROOT="/data0/xyf/tunedata"
CHECKPOINT_PATH="/data0/xyf"
SAVE_PATH="/data0/xyf/blocklm_10B_chinese_202233"
DEEPSPEED_CONFIG_PATH="config_tasks/config_blocklm_10B_cnndm.json"
DATESTR=$(date +"%m-%d-%H-%M")
source $1    # Model
source $2    # Task
CUDA_VISIBLE_DEVICES=1
NUM_WORKERS=1
NUM_GPUS_PER_WORKER=1
HOST_FILE_PATH="./hostfile"
MP_SIZE=1
MASTER_PORT=$(shuf -n 1 -i 10000-65535)
OPTIONS_NCCL="NCCL_DEBUG=info NCCL_IB_DISABLE=0 NCCL_NET_GDR_LEVEL=2"
DISTRIBUTED_ARGS="${OPTIONS_NCCL} deepspeed --hostfile ${HOST_FILE_PATH} --master_port ${MASTER_PORT} --num_nodes ${NUM_WORKERS} --num_gpus ${NUM_GPUS_PER_WORKER}"
EXPERIMENT_NAME=${EXPERIMENT_NAME}_${DATESTR}
mkdir logs

run_cmd="${DISTRIBUTED_ARGS} finetune_glm.py \
       --deepspeed \
       --deepspeed_config ${DEEPSPEED_CONFIG_PATH} \
       --finetune \
       --experiment-name ${EXPERIMENT_NAME} \
       --task ${TASK_NAME} \
       --data-dir ${DATA_PATH} \
       --save ${CHECKPOINT_PATH} \
       --checkpoint-activations \
       --num-workers 1 \
       --no-load-lr-scheduler \
       $MODEL_ARGS \
       $TRAIN_ARGS \
       $COMMON_ARGS \
       $TASK_ARGS \
       --fp16 \
       --model-parallel-size ${MP_SIZE} \
       --overwrite \
       2>&1 | tee logs/log-${EXPERIMENT_NAME}.txt"
echo ${run_cmd}
eval ${run_cmd}
