import pandas as pd
import numpy as np
from dagster import asset, MetadataValue

@asset
def raw_data():
    """Пример ассета с pandas и numpy"""
    df = pd.DataFrame({
        'id': range(1, 101),
        'value': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })

    # Добавляем метаданные для отображения в UI
    return df, {
        "row_count": len(df),
        "columns": MetadataValue.md(str(list(df.columns))),
        "preview": MetadataValue.md(df.head().to_markdown())
    }

@asset
def processed_data(raw_data):
    result = raw_data.assign(
        value_squared=raw_data['value'] ** 2,
        is_high=raw_data['value'] > 0
    )
    return result

all_assets = [raw_data, processed_data]