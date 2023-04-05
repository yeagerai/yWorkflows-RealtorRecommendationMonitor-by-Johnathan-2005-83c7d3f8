
import pytest
from pydantic import ValidationError
from mock import AsyncMock
from fastapi.testclient import TestClient
from app import RealtorRecommendationMonitor, RealtorRecommendationMonitorIn, RealtorRecommendationMonitorOut, realtor_recommendation_monitor_app

client = TestClient(realtor_recommendation_monitor_app)

# Test cases with mocked input and expected output data
test_cases = [
    (
        RealtorRecommendationMonitorIn(
            facebook_api_credentials={"api_key": "key123"},
            targeted_group_ids=["group1", "group2"],
            messaging_platform_credentials={"token": "token123"},
            melissa_api_credentials={"key": "melissa_key123"},
        ),
        {"sent_message_status": "success", "extracted_user_name_and_phone": {"name": "John Doe", "phone": "+123456789"}},
        RealtorRecommendationMonitorOut(sent_message_status="success", extracted_user_name_and_phone={"name": "John Doe", "phone": "+123456789"}),
    ),
    (
        RealtorRecommendationMonitorIn(
            facebook_api_credentials={"api_key": "key456"},
            targeted_group_ids=["group1", "group3"],
            messaging_platform_credentials={"token": "token456"},
            melissa_api_credentials={"key": "melissa_key456"},
        ),
        {"sent_message_status": "failed", "extracted_user_name_and_phone": None},
        # For this test case, an error will be raised because sent_message_status is 'failed'
    ),
]


@pytest.mark.parametrize("input_data, mock_results_dict, expected_output", test_cases)
async def test_realtor_recommendation_monitor(input_data, mock_results_dict, expected_output):
    # Create an instance of RealtorRecommendationMonitor and mock the superclass's transform method
    realtor_recommendation_monitor = RealtorRecommendationMonitor()
    realtor_recommendation_monitor.transform = AsyncMock(return_value=mock_results_dict)

    # Call the component's transform() method with the mocked input
    if expected_output is None:
        with pytest.raises(ValidationError):
            output = await realtor_recommendation_monitor.transform(input_data, callbacks=None)
    else:
        output = await realtor_recommendation_monitor.transform(input_data, callbacks=None)
        # Assert the output matches the expected output
        assert output == expected_output


# Test with TestClient (FastAPI) for realtor_recommendation_monitor_app POST /transform/ endpoint
@pytest.mark.parametrize("input_data, mock_results_dict, expected_output", test_cases)
async def test_realtor_recommendation_monitor_endpoint(input_data, mock_results_dict, expected_output):
    with realtor_recommendation_monitor_app.container.transform.override(AsyncMock(return_value=mock_results_dict)):
        response = client.post("/transform/", json=input_data.dict())
        if expected_output is None:
            assert response.status_code == 422  # Validation Error
        else:
            assert response.status_code == 200
            assert response.json() == expected_output.dict()
