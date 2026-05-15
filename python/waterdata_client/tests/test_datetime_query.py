import pytest
from datetime import datetime, timedelta, UTC
import pandas as pd
from hydrotools.waterdata_client.request_models.continuous import ContinuousRequest

@pytest.mark.parametrize("datetime_object, datetime_field", [
    ("2026-05-13T00:00:00+00:00", "2026-05-13T00:00:00+00:00"),
    (datetime(2026, 5, 13, tzinfo=UTC), datetime(2026, 5, 13, tzinfo=UTC)),
    ("PT36H", "PT36H"),
    (timedelta(hours=36), timedelta(hours=36)),
    (pd.Timestamp("2026-05-13T00:00:00"), pd.Timestamp("2026-05-13T00:00:00"))
])
def test_datetime_validation(datetime_object, datetime_field):
    """Verifies that different types of datetime objects correctly validate."""
    model = ContinuousRequest(
        datetime=datetime_object
    )

    assert model.datetime == datetime_field
