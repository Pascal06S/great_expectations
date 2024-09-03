from logging import Logger
from typing import Any, ClassVar, Literal, Optional, Type

from great_expectations_v1.compatibility import azure
from great_expectations_v1.datasource.fluent import _SparkFilePathDatasource
from great_expectations_v1.datasource.fluent.config_str import (
    ConfigStr,
)
from great_expectations_v1.datasource.fluent.data_asset.path.spark.csv_asset import CSVAsset
from great_expectations_v1.datasource.fluent.data_connector import (
    S3DataConnector,
)
from great_expectations_v1.datasource.fluent.interfaces import (
    BatchMetadata,
    SortersDefinition,
)
from great_expectations_v1.datasource.fluent.spark_datasource import (
    SparkDatasourceError,
)

logger: Logger

class SparkAzureBlobStorageDatasourceError(SparkDatasourceError): ...

class SparkAzureBlobStorageDatasource(_SparkFilePathDatasource):
    # class attributes
    data_connector_type: ClassVar[Type[S3DataConnector]] = ...

    # instance attributes
    type: Literal["spark_abs"] = "spark_abs"

    # Azure Blob Storage specific attributes
    azure_options: dict[str, ConfigStr | Any] = {}
    # private
    _azure_client: azure.BlobServiceClient | None
    def add_csv_asset(  # noqa: PLR0913
        self,
        name: str,
        *,
        batch_metadata: Optional[BatchMetadata] = ...,
        abs_container: str = ...,
        abs_name_starts_with: str = "",
        abs_delimiter: str = "/",
        abs_recursive_file_discovery: bool = False,
        header: bool = ...,
        infer_schema: bool = ...,
        order_by: Optional[SortersDefinition] = ...,
    ) -> CSVAsset: ...