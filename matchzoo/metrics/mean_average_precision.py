"""Mean average precision metric for ranking."""
import numpy as np

from matchzoo.engine.base_metric import (
    BaseMetric, sort_and_couple, RankingMetric
)


class MeanAveragePrecision(RankingMetric):
    """Mean average precision metric."""

    ALIAS = ['mean_average_precision', 'map']

    def __init__(self, threshold: float = 0.):
        """
        :class:`MeanAveragePrecision` constructor.

        :param threshold: The threshold of relevance degree.
        """
        self._threshold = threshold

    def __repr__(self):
        """:return: Formated string representation of the metric."""
        return f"{self.ALIAS[0]}({self._threshold})"

    def __call__(self, y_true: np.array, y_pred: np.array, threshold=10) -> float:
        """
        Calculate mean average precision.

        Example:
            >>> y_true = [0, 1, 0, 0]
            >>> y_pred = [0.1, 0.6, 0.2, 0.3]
            >>> MeanAveragePrecision()(y_true, y_pred)
            1.0

        :param y_true: The ground true label of each document.
        :param y_pred: The predicted scores of each document.
        :return: Mean average precision.
        """
        result = 0.
        pos = 0
        coupled_pair = sort_and_couple(y_true, y_pred)

        # num_not_larger_than_threshold = 0
        # for idx, (label, score) in enumerate(coupled_pair):
        #     if label > self._threshold:
        #         pos += 1.
        #         result += pos / (idx + 1.)
        #     else: num_not_larger_than_threshold += 1
        #     if num_not_larger_than_threshold == threshold: break

        for idx, (label, score) in enumerate(coupled_pair):
            if label > self._threshold:
                pos += 1.
                result += pos / (idx + 1.)
        if pos == 0:
            return 0.
        else:
            return result / pos