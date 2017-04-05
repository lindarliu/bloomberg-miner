#This will be run on server
#scrape data from bloomberg and post it on slack
from slackclient import SlackClient
import filter_b
import sys
sys.path.append('/Users/linda/path/') 
import config_bloomberg

def scrape():
	news=filter_b.filter_bloomberg()

	SLACK_TOKEN = config_bloomberg.SLACK_TOKEN
	SLACK_CHANNEL =config_bloomberg.SLACK_CHANNEL


	sc = SlackClient(SLACK_TOKEN)

	for key in news: 

		desc = "%s \n %s"%(key,news[key])
		sc.api_call(
	    	"chat.postMessage", channel=SLACK_CHANNEL, text=desc,
	    	username='pybot', icon_emoji=':robot_face:'
		)