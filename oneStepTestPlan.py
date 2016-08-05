from testrail import *
import sys



release = 'Web UI Service - 5.5.'+sys.argv[1]
password = sys.argv[2]
#Login with username and API Key
client = APIClient('https://vic-qa-testrail.xmatters.com/testrail/')
client.user = 'ygao'
client.password = password



# Input release number from command line

print 'We will create regression test plan for milestone' + release


# Step1. Add milestone to xmatters
print 'step 1 -- Add Milestone to project Ahch-To ......'
result = client.send_post('add_milestone/16',
{
    'name' : release
})
milestoneid = result['id']

print result['name'] 
print milestoneid


print 'step 2  -- Create Basic Acceptance Test Plan based on this milestone ......'
result = client.send_post(
	'add_plan/16',
	{'name': 'Basic Acceptance Test Plan','milestone_id': milestoneid}
	)
testplanid = result['id']
print result['name'] + ' ' + str(testplanid)

print 'step 3 -- Add regression testsuites to test plan'

suites = [2808, 2809]
for suiteid in suites:
    result = client.send_post('add_plan_entry/'+str(testplanid),{'suite_id' : suiteid,'include_all' : True})
    print result['name']
