import slack 
import json
import requests

slack_token = "xoxb-3707654943089-3694992446515-cbQby5Jbak2KoQUM1dxKH85b" # 발급받은 Token 값
client = slack.WebClient(token=slack_token)

def sendToSlack(message):
    client.chat_postMessage(channel="#menu_scraping_log", text=message)