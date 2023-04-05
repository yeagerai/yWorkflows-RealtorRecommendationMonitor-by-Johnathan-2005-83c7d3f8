
# RealtorRecommendationMonitor

The RealtorRecommendationMonitor is a Yeager Workflow that continuously monitors targeted Facebook groups for posts related to real estate recommendations using the provided Facebook API credentials. Upon detecting a relevant post, the workflow extracts the user's name and phone number using the Melissa API, and sends a message to the user using the specified messaging platform credentials. The workflow returns the sent message status, as well as the extracted user name and phone number.

## Initial generation prompt
description: "IOs - 'Input: Facebook API credentials, targeted group IDs, messaging\
  \ platform credentials,\n  Melissa API credentials. Output: Sent message status,\
  \ extracted user name and phone\n  number.'\n"
name: RealtorRecommendationMonitor


## Transformer breakdown
- Monitor specific Facebook groups using targeted_group_ids and facebook_api_credentials
- Detect posts related to real estate recommendations
- Extract user's name and phone number using melissa_api_credentials
- Send a message to the user using messaging_platform_credentials
- Return sent_message_status and extracted_user_name_and_phone

## Parameters
[]

        