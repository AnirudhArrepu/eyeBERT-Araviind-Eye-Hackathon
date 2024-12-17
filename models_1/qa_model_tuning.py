# -*- coding: utf-8 -*-
"""qA-model-tuning

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zC5YRHg6tl9XuryfZQcSCBzFkJvfnCuz
"""

!pip install simpletransformers

import logging
import json

from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs

model_type = "bert"
model_name = "bert-base-cased"

if model_type == "bert":
  model_name = "bert-base-cased"
elif model_type == "roberta":
  model_name = "robert-base"
elif model_type == "distilbert":
  model_type = "roberta"
  model_name = "distilroberta-base"
elif model_type == "electra-base":
  model_type = "electra"
  model_name = "google/electra-base-discriminator"
elif model_type == "electra-small":
  model_type = "electra"
  model_name = "google/electra-small-discriminator"
elif model_type == "xlnet":
  model_name = "xlnet-base-cased"

model_args = QuestionAnsweringArgs()
model_args.train_batch_size = 16
model_args.evaluate_during_training = True
model_args.n_best_size=3
model_args.num_train_epochs = 10

train_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "use_cached_eval_features": True,
    "output_dir": f"outputs/{model_type}",
    "best_model_dir": f"outputs/{model_type}/best_model",
    "evaluate_during_training": True,
    "max_seq_length": 128,
    "num_train_epochs": 5,
    "evaluate_during_training_steps": 1000,
    # "wandb_project": "Question Answer Application",
    # "wandb_kwargs": {"name": model_name},
    "save_model_every_epoch": False,
    "save_eval_checkpoints": False,
    "n_best_size":3,
    # "use_early_stopping": True,
    # "early_stopping_metric": "mcc",
    # "n_gpu": 2,
    # "manual_seed": 4,
    # "use_multiprocessing": False,
    "train_batch_size": 128,
    "eval_batch_size": 64,
    # "config": {
    #     "output_hidden_states": True
    # }
}

model = QuestionAnsweringModel(model_type,model_name,args = train_args)

with open("train.json","r") as train_file:
  train = json.load(train_file)

with open("test.json","r") as test_file:
  test = json.load(test_file)

!rm -rf outputs

model.train_model(train,eval_data=test)
