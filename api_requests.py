import requests
import pprint
import json

kword = ["Agriculture and food", "Animals", "Armed forces and national security", 
		 "Arts, culture, religion", "Civil rights and liberties, minority issues", 
		 "Commerce", "Congress", "Crime and law enforcement", "Economics and public finance", 
		 "Education", "Emergency management", "Energy", "Environmental protection", 
		 "Families", "Finance and financial sector", "Foreign trade and international finance", 
		 "Government operations and politics", "Immigration", "International affairs", 
		 "Labor and employment", "Law", "Native Americans", "Private legislation", 
		 "Public lands and natural resources", "Science, technology, communications", 
		 "Social sciences and history", "Social security and elderly assistance","Taxation"]


def getBillData(keyw):   
	bills_params = {
					'apikey': '2282ac571e0b46b69bb7879f4de9b158',
					'keywords': keyw,
					'history.enacted': 'true',
					'per_page': 50,
					'fields': '''sponsor.party,chamber,official_title,summary_short,
								 short_title,popular_title,bill_id,history.vetoed,
								 history.enacted,last_vote_at,urls.govtrack'''
					}

	endpoint = 'https://congress.api.sunlightfoundation.com/bills'

	response = requests.get( endpoint, params=bills_params)
	data = response.json()
	data = data['results']
        
	return data

def getVoteData(qry):   
	votes_params = {
					'apikey': '2282ac571e0b46b69bb7879f4de9b158',
					'bill_id': qry,
					'fields': 'breakdown.party'
					}

	endpoint = 'https://congress.api.sunlightfoundation.com/votes'

	response = requests.get( endpoint, params=votes_params)
	data = response.json()
    
	try: 
		data = data['results'][0]['breakdown']['party']
	except Exception:
		pass
        
	return data

all_kw = {}

for kw in kword:
	bills = []
	incoming = getBillData(kw)
    
	total_r = 0
	total_d = 0
	total_i = 0
    
	sponsor_r = 0
	sponsor_d = 0
	sponsor_i = 0
    
	for bill in incoming:
		bill_id = bill['bill_id']
		year = bill['last_vote_at'][:4]
		source = bill['urls']['govtrack']
		question = bill['official_title']
		chamber = bill['chamber']
		popular_title = bill['popular_title']
		short_summary = bill['summary_short']
        
		vote_data = getVoteData(bill_id)
        
		try: 
			r_votes = vote_data['R']['Yea']
			total_r += r_votes

			d_votes = vote_data['D']['Yea']
			total_d += d_votes
            
			total_i += i_votes['I']['Yea']
			total_i += i_votes
        
		except Exception:
			pass
        
		try:
			sponsor = bill['sponsor']['party']
            
			if sponsor == 'D':
				sponsor_d += 1

			elif sponsor == 'R': 
				sponsor_r += 1

			elif sponsor == 'I':
				sponsor_i += 1

		except Exception:
			pass

		current = { 'bill_id': bill_id, 'year': year, 'source': source, 'sponsor': sponsor,'question': question, 
					'short_summary': short_summary,'chamber': chamber, 'popular_title': popular_title }   
		bills.append(current)

	all_kw[kw] = {'kw': kw, 
				  'bills': bills, 
				  'votes': {'D': total_d, 'R': total_r , 'I': total_i},
				  'sponsors': {'D': sponsor_d, 'R': sponsor_r, 'I': sponsor_i}}

with open('data2.json', 'wb') as outfile:
	json.dump(all_kw, outfile)