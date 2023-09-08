import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from components.data_ingestion import DataIngestion
from config.config import ConfigurationManager
from loging import logger
from transformers import AutoTokenizer, Pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)
        gen_kwargs = {"length_penalty": 1, "num_beams": 10, "max_length": 100}
        
        pipe = Pipeline(
            "summarization", 
            model=self.config.model_path, 
            tokenizer=tokenizer,
            device=0,
            framework="pt",
            **gen_kwargs
        )
        
        print("Summarizing text: ", text)
        output = pipe(text)[0]["summary_text"]
        print("Summary: ", output)
        
        return output
        
        
    
