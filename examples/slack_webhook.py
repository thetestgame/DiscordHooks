from discordhooks import SlackWebhook, SlackAttachment

webhook_url = 'examplewebhook.com'

"""
Slack Webhook
"""
message = SlackWebhook(webhook_url, author='DiscordHooks')

attachment = SlackAttachment(
  pretext='Hello world! I am an example Slack webhook!',
  title='Example Webhook',
  title_link='https://github.com/NxtStudios/DiscordHooks',
  image_url='https://cdn.worldvectorlogo.com/logos/discord.svg')
message.addAttachment(attachment)

message.send()