<img src="https://maxcdn.icons8.com/Share/icon/Logos//discord_logo1600.png" align="right" height=300>

DiscordHooks
============
DiscordHooks is an open source library for sending messages to Discord from Python 2.7 using Discords built in channel webhooks

## Supports
DiscordHooks currently supports the following Discord webhooks
* Generic
* Slack

## Example

*Generic Webhook*
```python
from discordhooks import GenericWebhook

"""
Generic Webhook
"""
message = GenericWebhook('examplewebhook.com', 'Hello World!', author='DiscordHooks')
message.send()
```

*Slack Webhook*
```python
from discordhooks import SlackWebhook, SlackAttachment

"""
Slack Webhook
"""
message = SlackWebhook('examplewebhook.com', author='DiscordHooks')

attachment = SlackAttachment(
  pretext='Hello world! I am an example Slack webhook!',
  title='Example Webhook',
  title_link='https://github.com/NxtStudios/DiscordHooks',
  image_url='https://cdn.worldvectorlogo.com/logos/discord.svg')
message.addAttachment(attachment)

message.send()
```

## License
Licensed under the BSD 3-clause "New" or "Revised" license. See the provided LICENSE file for details