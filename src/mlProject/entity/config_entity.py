from dataclasses import dataclass # Self not needed
from pathlib import Path

## This is useful for configuration objects where you don’t want accidental modifications.

@dataclass(frozen=True)
class DataIngestionConfig:      #DataIngestionConfig class is a frozen dataclass, meaning its instances are immutable once created
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path