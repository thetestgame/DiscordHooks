from discordhooks import GenericWebhook

webhook_url = 'examplewebhook.com'

"""
Generic Webhook
"""
message = GenericWebhook(webhook_url, 'Hello World!', author='DiscordHooks')
message.send()