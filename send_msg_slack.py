import os
import slack



def send_msg_slack():
    slack_token = os.environ['SLACK_TOKEN']
    client = slack.WebClient(token=slack_token)
    env = os.environ['ENV']

    client.chat_postMessage(
        channel="channel-name",
        text="Bom dia terráqueo, segue report do ambiente: " + env + "\n"
    )

    client.files_upload(
        channels="channel-name",
        file="report-instances-numbers-and-type",
        title="Upload report"
    )

