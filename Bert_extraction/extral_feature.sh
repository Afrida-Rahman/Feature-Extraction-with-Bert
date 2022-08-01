# /mnt/raid5/data3/xlzhu/learn_DL/BERT_pretrain/model_pt/multi_cased_L-12_H-768_A-12
# /mnt/raid5/data3/xlzhu/learn_DL/BERT_pretrain/model_pt/probert
#export BERT_BASE_DIR=/mnt/raid5/data3/xlzhu/learn_DL/BERT_pretrain/model_pt/probert
export BERT_BASE_DIR=/bert_base/bert_pretrained_models/multi_cased_L-12_H-768_A-12

#python /bert_base/bert_base_utils/bert/extract_features.py \
#    --input_file=/bert_base/data/fold10/valid.txt \
#    --output_file=/bert_base/bert_base_features/fold10/valid.json \
#    --layers=-1 \
#    --vocab_file=$BERT_BASE_DIR/vocab.txt \
#    --bert_config_file=$BERT_BASE_DIR/bert_config.json \
#    --init_checkpoint=$BERT_BASE_DIR/model.ckpt \
#    --max_seq_length=64 \
#    --batch_size=32


python G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\bert_base_utils\bert/extract_features.py --input_file=G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\data\fold10/valid.txt --output_file=G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\bert_base_features\fold10/valid.json --layers=-1 --vocab_file=G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\bert_pretrained_models\multi_cased_L-12_H-768_A-12/vocab.txt --bert_config_file=G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\bert_pretrained_models\multi_cased_L-12_H-768_A-12/bert_config.json --init_checkpoint=G:\pycharmProjects\Gly-ML-BERT-DL\Bert_extraction\bert_base\bert_pretrained_models\multi_cased_L-12_H-768_A-12/bert_model.ckpt --max_seq_length=64 --batch_size=32