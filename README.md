# RSS To Discord

A simple script that transmits RSS feeds to your Discord channel.

## how to deploy
___
###**get your bot token**

go to discord, and create a new channel.
edit the channel setting.
in ``Integrations``, create a new ``Webhook``, and copy the link.

###**set up the script**

+ install the [requirements](/requirements.txt) file:
  
```pip3 install -r requirements.txt```

+ create a new file, `config.ini` and enter the following params:

```
[discord]
id = <YOUR ID>
token = <YOUR TOKEN>
```
+ to get your id & token, go to the link you're copied, and copy them.

for example:
```json
{
    "type": 1, 
    "id": "<YOUR ID>", 
    "name": "RSS feed", 
    "avatar": null, 
    "channel_id": "1234567890", 
    "guild_id": "1234567890", 
    "application_id": null, 
    "token": "<YOUR TOKEN>"
}
```
+ change (or not...) the [url-feed](/main.py#L16).

And... you are ready to start!

> you can set to print every update, by remove the `h` [here](/main.py#L32).
___
## Run the script
+ give permissions to the script:
```
chmod +x main.py
```
and run it:
```
./main.py
```
you will get feed updates to your discord channel. yeah!
___
___

*NOTE:*

*If you want to change the frequency of checking updates, you can edit the number listed [here](/main.py#L43), in seconds.*

*By default, updates will check every 60 seconds.*




