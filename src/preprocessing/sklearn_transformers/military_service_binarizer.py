from pathlib import Path
from typing import TYPE_CHECKING, Union, Optional

if TYPE_CHECKING:
    from pandas import DataFrame
    from sklearn.preprocessing import LabelBinarizer

from joblib import load
from sklearn.base import BaseEstimator, TransformerMixin


class MilitaryServiceBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self,  path: Union[Path, str]) -> None:
        self.path = path
        self._binarizer: "LabelBinarizer" = load(self.path)

    def fit(
            self,
            dataframe: "DataFrame",
            y: Optional["DataFrame"] = None
    ) -> "MilitaryServiceBinarizer":
        self._binarizer.fit(dataframe)
        return self

    def transform(
            self,
            dataframe: "DataFrame",
            column: str = "military_service"
    ) -> "DataFrame":
        dataframe[column] = self._binarizer.transform(dataframe[column])
        return dataframe
