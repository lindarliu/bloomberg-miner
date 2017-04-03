from slackclient import SlackClient
import filter_b

news=filter_b.filter_bloomberg()

SLACK_TOKEN = "xoxp-117346601648-117985581315-117985971603-6b66d34991f68a95d6f05d0be8bd12ab"
SLACK_CHANNEL = "#bloomberg"


sc = SlackClient(SLACK_TOKEN)

for key in news: 

	desc = "%s \n %s"%(key,news[key])
	sc.api_call(
    	"chat.postMessage", channel=SLACK_CHANNEL, text=desc,
    	username='pybot', icon_emoji=':robot_face:'
	)