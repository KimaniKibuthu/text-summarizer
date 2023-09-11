import sys
import torch
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from config.config import ConfigurationManager
from loging import logger
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 1, "num_beams": 10, "max_length": 100}
        
        pipe = pipeline(
            "summarization", 
            model=self.config.model_path, 
            tokenizer=tokenizer,
            device=0 if torch.cuda.is_available() else -1,
            framework="pt",
            **gen_kwargs
        )
        
        print("Summarizing text: ", text)
        output = pipe(text)[0]["summary_text"]
        print("Summary: ", output)
        
        return output
        
        
if __name__ == "__main__":
    prediction_pipeline = PredictionPipeline()
    prediction_pipeline.predict("The US has over 70000 cases of coronavirus and over 1000 deaths ")   
