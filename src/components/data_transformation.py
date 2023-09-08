import sys
import os
import json
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from dataclasses import dataclass
from pathlib import Path
from loging import logger
from entity import DataTransformationConfig
from datasets import Dataset, DatasetDict, load_from_disk
from transformers import AutoTokenizer

class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        target_encodings = self.tokenizer(text_target=example_batch['summary'], max_length = 128, truncation = True )

        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"]

        }
        
    def transform_data_to_transformers_format(self):
        # Load each of your datasets
        with open(os.path.join(self.config.data_path, "train.json"), 'r',encoding='utf-8') as file:
            train_data = json.load(file)

        with open(os.path.join(self.config.data_path, "test.json"), 'r',encoding='utf-8') as file:
            test_data = json.load(file)
        
        with open(os.path.join(self.config.data_path, "val.json"), 'r',encoding='utf-8') as file:
            val_data = json.load(file)

        # Convert each list of dictionaries to a HuggingFace Dataset
        train_dataset = Dataset.from_dict({k: [dic[k] for dic in train_data] for k in train_data[0]})
        test_dataset = Dataset.from_dict({k: [dic[k] for dic in test_data] for k in test_data[0]})
        val_dataset = Dataset.from_dict({k: [dic[k] for dic in val_data] for k in val_data[0]})
        
        
        
        dataset_dict = DatasetDict({
            'train': train_dataset,
            'test': test_dataset,  
            'validation': val_dataset
        })
        
        save_path = os.path.join(self.config.data_path, "transformers_format_data")
        dataset_dict.save_to_disk(save_path)
        
    def convert_to_features(self):
        load_path = os.path.join(self.config.data_path, "transformers_format_data")
        loaded_dataset_dict = load_from_disk(load_path)

        # Assuming self.convert_examples_to_features is defined elsewhere in your class
        loaded_train_dataset = loaded_dataset_dict['train'].map(self.convert_examples_to_features, batched=True)
        loaded_test_dataset = loaded_dataset_dict['test'].map(self.convert_examples_to_features, batched=True)
        loaded_val_dataset = loaded_dataset_dict['validation'].map(self.convert_examples_to_features, batched=True)

        # Combine the processed datasets
        processed_dataset_dict = DatasetDict({
            'train': loaded_train_dataset,
            'test': loaded_test_dataset,
            'validation': loaded_val_dataset
        })

        save_path = os.path.join(self.config.root_dir, "transformed_data")
        processed_dataset_dict.save_to_disk(save_path)