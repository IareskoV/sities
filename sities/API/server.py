import json
from flask import Flask
from flask import request
from rdflib import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib.namespace import RDFS, OWL
from flask_cors import CORS


graph = Graph()
app = Flask(__name__)
CORS(app)

q = 'SELECT ?country ?population FROM <http://dbpedia.org/> WHERE { ?country rdf:type dbo:Country . ?country dbo:populationTotal ?population . ?country dbo:wikiPageWikiLink dbc:Eastern_European_countries}ORDER BY DESC (?population)'


@app.route("/all")
def hello_world():
    arayOfSities = []
    graph.parse('https://dbpedia.org/resource/Ukraine')
    for s, p, o in graph:
        if p == (URIRef('http://dbpedia.org/property/city')):
            print(s, p, o)
            arayOfSities.append(o)

    return arayOfSities


@app.route("/city")
def city():
    usr = request.args.get('name')
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    query ="""
    SELECT ?item ?name ?image ?text WHERE {
  ?item rdf:type dbo:HistoricBuilding.
  ?item dbo:location dbr:%s.
  ?item dbp:name ?name.
  ?item dbo:thumbnail ?image.
  ?item dbo:abstract ?text.
  FILTER langMatches(lang(?text),'en')
 }"""%(usr)

    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

@app.route("/cite")
def cite():
    SitesInfo = []
    usr = request.args.get('name')
    usr = usr.replace(' ','_')
    graph.parse('http://dbpedia.org/resource/%s'%(usr))
    name = ''
    desc = ''
    for o in graph.objects(None, RDFS.label):
        if (o.language == 'en'):
            name = o
    for s, p, o in graph:
        if p == (URIRef('http://dbpedia.org/ontology/abstract')):
            if o.language == 'en':
                print(s,p,o)
                desc = o



    return [name,desc]
