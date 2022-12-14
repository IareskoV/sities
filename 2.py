from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF

graph = Graph()
cade = URIRef('http://example.com/Cade')
emma = URIRef('http://example.com/Emma')

address = URIRef('http://example.com/ontology/address')
degree = URIRef('http://example.com/ontology/degree')
travel = URIRef('http://example.com/ontology/travel')

graph.add((cade, RDF.type, FOAF.Person))
graph.add((cade, FOAF.givenName, Literal('Cade')))
graph.add((cade, FOAF.gender, Literal('male')))
graph.add((cade, address, Literal(
    '1516 Henry Street, Barkley, California 94709, USA')))
graph.add((cade, degree, Literal(
    'Bachelor of Biology in Californean University, 2011')))
graph.add((cade, FOAF.interest, Literal('Birds')))
graph.add((cade, FOAF.interest, Literal('Ecology')))
graph.add((cade, FOAF.interest, Literal('Environment')))
graph.add((cade, FOAF.interest, Literal('Photography')))
graph.add((cade, FOAF.interest, Literal('Travel')))
graph.add((cade, travel, Literal('Canada')))
graph.add((cade, travel, Literal('France')))

graph.add((emma, RDF.type, FOAF.Person))
graph.add((emma, FOAF.givenName, Literal('Emma')))
graph.add((emma, FOAF.gender, Literal('female')))
graph.add((emma, address, Literal(
    'Carrer de la Guardia Civil 20, 46020 Valencia, Spain')))
graph.add((emma, degree, Literal(
    'Master of Chemics in Valencian University, 2015')))
graph.add((emma, FOAF.interest, Literal('Biking')))
graph.add((emma, FOAF.interest, Literal('Music')))
graph.add((emma, FOAF.interest, Literal('Travel')))
graph.add((emma, travel, Literal('Portugal')))
graph.add((emma, travel, Literal('Italy')))
graph.add((emma, travel, Literal('France')))
graph.add((emma, travel, Literal('Germany')))
graph.add((emma, travel, Literal('Denmark')))
graph.add((emma, travel, Literal('Sweden')))

print('------------Printing ttl serialization-----------')
ttl = graph.serialize(format='ttl')
print(ttl)

print('------------Printing xml serialization-----------')
xml = graph.serialize(format='xml')
print(xml)

graph.serialize(destination='graph.ttl', format='ttl')

graph.parse('graph.ttl')

graph.add((cade, travel, Literal('Germany')))
graph.add((emma, FOAF.age, Literal(36)))

print('------------Printing all triples-----------')
for s, p, o in graph:
    print(s, p, o)

print('------------Printing only Emma triples-----------')
for s, p, o in graph.triples((emma, None, None)):
    print(s, p, o)

print('------------Printing only names-----------')
for s, p, o in graph.triples((None, FOAF.givenName, None)):
    print(s, p, o)
