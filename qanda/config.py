import os
import boto3

# AWS SSM encrypted parameter store
ssm = boto3.client('ssm')


def get_ssm_param(param_name: str, required: bool = True) -> str:
    """Get an encrypted AWS Systems Manger secret."""
    response = ssm.get_parameters(
        Names=[param_name],
        WithDecryption=True,
    )
    if not response['Parameters'] or not response['Parameters'][0] or not response['Parameters'][0]['Value']:
        if not required:
            return None
        raise Exception(
            f"Configuration error: missing AWS SSM parameter: {param_name}")
    return response['Parameters'][0]['Value']


###

TWILIO_API_SID = get_ssm_param('qanda_twilio_account_sid')
TWILIO_API_SECRET = get_ssm_param('qanda_twilio_account_secret')

SLACK_OAUTH_CLIENT_ID = get_ssm_param('qa_slack_oauth_client_id')
SLACK_OAUTH_CLIENT_SECRET = get_ssm_param('qa_slack_oauth_client_secret')
SLACK_VERIFICATION_TOKEN = get_ssm_param('qanda_slack_verification_token')
SLACK_LOG_ENDPOINT = get_ssm_param('qanda_slack_log_webhook', required=False)

# maybe don't hardcode?
# SLACK_OAUTH_REDIRECT_URL = "https://qanda.llolo.lol/v1/Prod/slack/oauth"
SLACK_OAUTH_REDIRECT_URL = "https://xtx4cyxavc.execute-api.eu-central-1.amazonaws.com/Prod/slack/oauth"

SLACK_EVENT_FUNCTION = os.getenv('SLACK_EVENT_FUNCTION')
SLACK_SLASH_FUNCTION = os.getenv('SLACK_SLASH_FUNCTION')

WORKSPACE_PERMISSIONS = False  # using new developer preview workspace permissions mode?
