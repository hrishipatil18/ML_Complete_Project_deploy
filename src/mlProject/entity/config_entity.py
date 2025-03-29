from dataclasses import dataclass # Self not needed
from pathlib import Path

## This is useful for configuration objects where you don’t want accidental modifications.

@dataclass(frozen=True)
class DataIngestionConfig:      #DataIngestionConfig class is a frozen dataclass, meaning its instances are immutable once created
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass(frozen=True) # DataValidationConfig is a dataclass that holds configuration settings for data validation.
class DataValidationConfig:
    root_dir: Path  # Specifies the root directory where validation artifacts (like logs and reports) will be stored.
    STATUS_FILE: str # A file path (as a string) where the validation status (success/failure) is logged
    unzip_data_dir: Path # The path to the dataset that needs to be validated (after extraction)
    all_schema: dict # A dictionary that holds the schema definition for validation (e.g., expected column names, data types, constraints).



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path