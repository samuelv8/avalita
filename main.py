import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = []
materias = {
    '1° FUND': {
        'HUM-01': [],
        'CES-10': [],
        'CES-11': ['CES-10'],
        'HUM-70': [],
        'MAT-12': [],
        'MAT-22': ['MAT-12'],
        'MAT-17': [],
        'MAT-27': ['MAT-17'],
        'QUI-18': [],
        'QUI-28': ['QUI-18'],
        'MPG-03': [],
        'MPG-04': ['MPG-03'],
        'FIS-15': [],
        'FIS-16': [],
    },
    '2° FUND': {
        'CCI-22': ['CES-10'],
        'EST-10': [],
        'MOQ-13': ['MAT-12', 'MAT-22'],
        'MAT-36': ['MAT-22'],
        'MAT-46': ['MAT-36'],
        'MAT-32': ['MAT-27'],
        'MAT-42': ['MAT-36'],
        'MTP-02': ['MPG-04'],
        'MEB-01': ['MAT-36', 'MAT-32', 'QUI-28'],
        'FIS-26': ['FIS-16', 'FIS-15'],
        'FIS-32': ['FIS-15', 'FIS-16'],
        'FIS-46': ['FIS-26', 'FIS-32'],
    },
    '1° COMP': {
        'CES-11': ['CES-10'],
        'CES-12': ['CES-11'],
        'CES-22': ['CES-11'],
        'CES-28': ['CES-22'],
        'CES-29': ['CES-28'],
        'EES-10': ['MAT-46', 'MAT-32', 'FIS-46']
    }
}
for ano, dependencias in materias.items():
    nodes += list(dependencias.keys())

edges = []
for ano, dependencias in materias.items():
    for m in dependencias:
        edges.extend([(n, m) for n in dependencias[m]])

G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.draw(G, with_labels=True, font_size=8, node_size=1000)
plt.show()
