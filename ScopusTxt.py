from pybliometrics.scopus import ScopusSearch
query = 'TITLE-ABS-KEY(segregation) AND PUBYEAR BEF 1921'
s = ScopusSearch(query)
output_file = '1800-1921.txt'
with open(output_file, 'w') as f:
    print(s, file=f)

print(f'A saida foi salva no arquivo {output_file}')
