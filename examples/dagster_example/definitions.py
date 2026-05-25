from dagster import Definitions
from .assets import all_assets
from .jobs import main_job

defs = Definitions(
    assets=all_assets,
    jobs=[main_job],
)