import requests

def queryGrapAL(stmt):
    data = "{\"statements\": [{\"statement\": \"" + stmt + "\"}]}"
    r = requests.post("https://grapal.allenai.org:7473/db/data/transaction/commit", data=data)
    return r.json()

def getCoauthors(last,first):
    stmt = "MATCH (a:Author {last: '" + last + "',first: '" + first + "'})-[:AUTHORS]->(p:Paper),(b:Author)-[:AUTHORS]->(p) RETURN distinct(b)"
    loaded_r = queryGrapAL(stmt)
    l = []
    if 'results' in loaded_r:
        for o in loaded_r['results'][0]['data']:
            l.append(o['row'][0])
    return l

def getCoauthors2(last,first):
    stmt = "MATCH (a:Author {last: '" + last + "',first: '" + first + "'})-[:AUTHORS]->(p:Paper),(b:Author)-[:AUTHORS]->(p),(b)-[:AUTHORS]->(p2:Paper),(c:Author)-[:AUTHORS]->(p2) RETURN distinct(c)"
    loaded_r = queryGrapAL(stmt)
    l = []
    if hasattr(loaded_r, 'results'):
        for o in loaded_r['results'][0]['data']:
            l.append(o['row'][0])
    return l

if __name__ == '__main__':
	print(getCoauthors('Velardi', 'Paola'))