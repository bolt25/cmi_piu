"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from kedro_cmi_piu.pipelines import create_pipeline

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    # pipelines["__default__"] = sum(pipelines.values())

    data_processing_pipeline = create_pipeline()

    return {
        "__default__": data_processing_pipeline,
        "data_processing": data_processing_pipeline,
    }



# import spaceflights.pipelines.data_processing as dp
# import spaceflights.pipelines.data_science as ds


# def register_pipelines() -> Dict[str, Pipeline]:
#     """Register the project's pipelines.
#
#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     data_processing_pipeline = dp.create_pipeline()
#     data_science_pipeline = ds.create_pipeline()
#
#     return {
#         "__default__": data_processing_pipeline + data_science_pipeline,
#         "data_processing": data_processing_pipeline,
#         "data_science": data_science_pipeline,
#     }

