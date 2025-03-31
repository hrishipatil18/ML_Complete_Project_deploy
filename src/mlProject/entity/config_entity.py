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

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float    # define in params.yml
    l1_ratio: float # define in params.yml
    target_column: str # define in schema.yaml


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path # The directory where model evaluation results (metrics, logs) are stored.
    test_data_path: Path # The path to the test dataset used for evaluation (e.g., test.csv).
    model_path: Path # The path to the trained model file
    all_params: dict # Stores model hyperparameters 
    metric_file_name: Path # The path where evaluation metrics (accuracy, F1-score, RMSE, etc.) will be saved.
    target_column: str # Specifies the target variable (e.g., quality in wine dataset). 
    mlflow_uri: str # The MLflow tracking server URI for logging model metrics.Helps in experiment tracking and performance monitoring.