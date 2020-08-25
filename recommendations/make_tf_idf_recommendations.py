import json
import networkx as nx
from collections import Counter
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
def print_graph_progress(done, total = 3023145):
	print('\033c')
	print("making graph: " + str(100 * done / total) + "% done")
G = nx.DiGraph()


clickstream_data_file = open("../../overlapping-internal-clickstream-enwiki-2020-04.txt")
test = open("../../test_data_set.txt")
result = open("Result.txt", "w+")
summary_file = open("preprocessed_content.txt")
summary = {}
for line in summary_file:
	summary = json.loads(line)
	break
summary_file.close()

all_nodes = set()

hindi_to_english = {}

done = 0
for line in clickstream_data_file:
	edge = json.loads(line)
	en_title_1 = edge["node1"]["en_title"].strip().lower().replace("_", " ")
	hi_title_1 = edge["node1"]["hi_title"].strip().lower().replace("_", " ")

	en_title_2 = edge["node2"]["en_title"].strip().lower().replace("_", " ")
	hi_title_2 = edge["node2"]["hi_title"].strip().lower().replace("_", " ")

	weight = edge["weight"]
	
	hindi_to_english[hi_title_1] = en_title_1

	G.add_edge(en_title_1, en_title_2)
	G[en_title_1][en_title_2]["weight"] = weight
	G.nodes[en_title_1]["hi_title"] = hi_title_1
	G.nodes[en_title_2]["hi_title"] = hi_title_2
	done += 1
	print_graph_progress(done)

clickstream_data_file.close()
for line in test:
	source_hi_title = line.strip().lower().replace("_", " ")
	result.write(source_hi_title)				# remove
	result.write(":\n")						# remove
	if source_hi_title not in hindi_to_english.keys():
		result.write("No information about the current page in clickstream data")
	else:
		source_en_title = hindi_to_english[source_hi_title]
		all_article = []
		all_article.append(source_en_title)
		for article in G[source_en_title]:
			if G.nodes[article]["hi_title"] == "":
				all_article.append(str(article).strip().lower().replace("_", " "))
		content = []
		for article in all_article:
			content.append(summary[article])
		DF = {}
		for token in content:
			for w in token:
				if w not in DF.keys():
					DF[w] = 0
				DF[w] += 1
		total_vocab_size = len(DF)
		total_vocab = [x for x in DF]

		def cosine_sim(a, b):
			num = np.linalg.norm(a)*np.linalg.norm(b)
			cos_sim = 0
			if num != 0:
				cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
			return cos_sim

		def doc_freq(word):
			c = 0
			try:
				c = DF[word]
			except:
				pass
			return c
		N = len(all_article)
		tf_idf = {}
		for i in range(N):
			tokens = content[i]
			counter = Counter(tokens)
			word_vount = len(tokens)
			for token in np.unique(tokens):
				tf = counter[token]/word_vount
				df = doc_freq(token)
				idf = np.log((N + 1) / (df + 1))
				tf_idf[i, token] = tf*idf
		D = np.zeros((N, total_vocab_size))
		for i in tf_idf:
			try:
				ind = total_vocab.index(i[1])
				D[i[0]][ind] = tf_idf[i]
			except:
				pass
		recommendations = []
		for i in range(1, N):
			recommendations.append((cosine_sim(D[0], D[i]), i))
		recommendations.sort(reverse=True)
		for i in range(len(recommendations)):
			number = recommendations[i][1]
			sim = recommendations[i][0]
			result.write(all_article[number])
			result.write(" (")
			result.write(str(sim))
			result.write(")")
			result.write("\n")
			if i == 4:
				break
	result.write("\n\n--------------------------------------------\n\n")

