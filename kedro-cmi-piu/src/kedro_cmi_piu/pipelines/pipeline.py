from kedro.pipeline import Pipeline, node

from ..nodes.data_preprocess import setIndex


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=setIndex,
                inputs=["train"],
                outputs="train_set_index",
                name="set_train_index"
            ),
            node(
                func=setIndex,
                inputs=["scoring"],
                outputs="scoring_set_index",
                name="set_scoring_index"
            ),
        ]
    )