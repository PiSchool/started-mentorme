from flask_injector import inject
from .goog_ext import GoogleExtractor
from .citations import getCoauthors, getCoauthors2

LIMIT_LIST = 5

@inject
def search_person(text):

	tot_name = text.split()
	f_name = tot_name[0]
	l_name = tot_name[1]
	r = getCoauthors(l_name, f_name)
	#r2 = getCoauthors2(l_name, f_name)
	res = filter_mentor(r[:LIMIT_LIST])
	#res2 = filter_mentor(r2[:LIMIT_LIST])
	#res = res + res2
	if len(res) > 0:
		return res, 200
	else:
		return res, 404


def filter_mentor(candidate_list: list):
	return_list = []
	ge = GoogleExtractor(5)
	for elem in candidate_list:
		try:
			full_name = elem['first'] + ' ' + elem['last']
			start, link = ge.is_startupper(full_name)
			if start:
				elem['link'] = link
				return_list.append(elem)
		except Exception as e:
			print(e)
			pass
	return return_list