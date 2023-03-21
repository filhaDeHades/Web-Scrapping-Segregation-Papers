import csv
from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch

#ab = AbstractRetrieval("10.1016/j.softx.2019.100263")
#print(ab.title)

'''
ab.idxterms --> termos utilizados para indexar o artigo
ab.authors --> Autores
ab.affiliation --> Instituição a que é afiliada
ab.title --> Titulo
ab.abstract / ab.description --> resumo
'''

def CodesFromScopus(query, outputName):
    s = ScopusSearch(query)
    with open(outputName, 'w') as f:
        print(s, file=f)

    print(f'A saida foi salva no arquivo {outputName}')

def RetrieveCodes(fileName):
    """from txt to list

    Args:
        fileName (string): Name of the file contain the
        codes to the abstracts (.txt file).

    Returns:
        List: List of all the codes in the .txt file.
    """
    
    file = open(fileName, "r")
    codes = []
    for line in file.readlines():
        codes.append(line.strip().split())
    file.close()
    return codes


def RetrieveInformation(codesList):
    """from List of codes to List of Dict information

    Args:
        codesList (_type_): _description_
    """
    lista = []
    for code in codesList:
        ab = AbstractRetrieval(code)
        if ab.abstract == None:
            dic1 = {'title': ab.title, 'idxterms': ab.idxterms, 'abstract': ab.description, 'authors': ab.authors, 'affiliation': ab.affiliation}
        else:
            dic1 = {'title': ab.title, 'idxterms': ab.idxterms, 'abstract': ab.abstract, 'authors': ab.authors, 'affiliation': ab.affiliation}
        lista.append(dic1)
        return lista


def SaveAbstractInformation(absInfo, fileName):
    """from list item to csv

    Args:
        absInfo (List): List of Dict contain the
        abstracts information.
        fileName (string): Name of the .csv file
        were the information will be saved.
    """

    file = open(fileName, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)
    header = ['Title', 'Idx Terms', 'Abstract', 'Authors', 'Affiliation']
    writer.writerow(header)
    for dic in absInfo:
        writer.writerow([dic['title'], dic['idxterms'], dic['abstract'], dic['authors'], dic['affiliation']])
    file.close()


if __name__ == "__main__":
    pass
    try:
        CodesFromScopus('TITLE-ABS-KEY(segregation) AND PUBYEAR BEF 1921', '1800-1921.txt')
        codesList = RetrieveCodes('1800-1921.txt')
        informationList = RetrieveInformation(codesList)
        SaveAbstractInformation(informationList, '1800-1921.csv')
    except:
        print('\033[91m Nao foi possivel rodar o codigo. \033[00m')

    ''' TESTES
    print(RetrieveCodes("testCodes.txt"))
    dic1 = {'title': 'Test', 'idxterms': 'gato, sapo, lago', 'abstract': 'descrição aqui', 'authors': 'jorge, julia', 'affiliation': 'instituto'}
    dic2 = {'title': 'Test 2', 'idxterms': 'cachorro, sabonete, rã', 'abstract': 'descrição aqui 2', 'authors': 'jose, narciso', 'affiliation': 'instituto 2'}
    lista = [dic1, dic2]
    print(lista)
    SaveAbstractInformation(lista, 'testCsv.csv')'''