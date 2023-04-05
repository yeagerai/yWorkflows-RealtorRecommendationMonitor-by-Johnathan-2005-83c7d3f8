
import typing
from typing import List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow


class RealtorRecommendationMonitorIn(BaseModel):
    facebook_api_credentials: dict
    targeted_group_ids: List[str]
    messaging_platform_credentials: dict
    melissa_api_credentials: dict


class RealtorRecommendationMonitorOut(BaseModel):
    sent_message_status: str
    extracted_user_name_and_phone: dict


class RealtorRecommendationMonitor(AbstractWorkflow):

    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: RealtorRecommendationMonitorIn, callbacks: typing.Any
    ) -> RealtorRecommendationMonitorOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)

        sent_message_status = results_dict[3].sent_message_status
        extracted_user_name_and_phone = results_dict[2].extracted_user_info

        out = RealtorRecommendationMonitorOut(
            sent_message_status=sent_message_status,
            extracted_user_name_and_phone=extracted_user_name_and_phone,
        )
        return out

load_dotenv()
realtor_recommendation_monitor_app = FastAPI()


@realtor_recommendation_monitor_app.post("/transform/")
async def transform(
    args: RealtorRecommendationMonitorIn,
) -> RealtorRecommendationMonitorOut:
    realtor_recommendation_monitor = RealtorRecommendationMonitor()
    return await realtor_recommendation_monitor.transform(args, callbacks=None)

