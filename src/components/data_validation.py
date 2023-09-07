
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from dataclasses import dataclass
from pathlib import Path
from loging import logger
from entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.status_file = self.config.STATUS_FILE
        self.all_required_files = self.config.ALL_REQUIRED_FILES

    def _write_validation_status(self, filename, status):
        """Helper function to write validation status."""
        with open(self.status_file, "a") as f:
            f.write(f"Validation for {filename} is {status}\n")
            
    def validate_all_files(self):
        try:
            logger.info("Start: Validate all files")
            
            # Clear the status file before writing
            open(self.status_file, 'w').close()
            
            all_files = [file for file in self.config.root_dir.parent.glob("**/*") if file.is_file()]
           
            
            for file in all_files:
                if file.name in self.all_required_files:
                    validation_status = file.stat().st_size > 0
                    self._write_validation_status(file.name, validation_status)
                    
                    if not validation_status:
                        break
            
            logger.info("End: Validate all files")
            return validation_status

        except Exception as e:
            logger.error(f"Error during validation: {e}")
            return False
