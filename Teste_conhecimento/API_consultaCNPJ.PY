import requests

cnpj = input('Digite o CNPJ que deseja pesquisar: ')

def getCNPJ(cnpj):
    url = 'https://api-publica.speedio.com.br/buscarcnpj?cnpj={}'.format(cnpj)

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json ()
        if 'erro' not in data:
            print('Nome Fantasia: {}'.format(data['NOME FANTASIA']))
            print('Razão Social: {}'.format(data['RAZAO SOCIAL']))
            print('CNPJ: {}'.format(data['CNPJ']))
            print('Status: {}'.format(data['STATUS']))
            print('Cnae Principal Descrição: {}'.format(data['CNAE PRINCIPAL DESCRICAO']))
            print('Cnae Principal Código: {}'.format(data['CNAE PRINCIPAL CODIGO']))
            print('Data de Abertura da empresa: {}'.format(data['DATA ABERTURA']))
            print('DDD: {}'.format(data['DDD']))
            print('Telefone: {}'.format(data['TELEFONE']))
            print('Email: {}'.format(data['EMAIL']))
            print('Tipo de Logradouro: {}'.format(data['TIPO LOGRADOURO']))
            print('Logradouro: {}'.format(data['LOGRADOURO']))
            print('Número: {}'.format(data['NUMERO']))
            print('Complemento: {}'.format(data['COMPLEMENTO']))
            print('Bairro: {}'.format(data['BAIRRO']))
            print('Município: {}'.format(data['MUNICIPIO']))
            print('UF: {}'.format(data['UF']))

        else:
            print('CNPJ inválido!')
    else:
        print('Erro ao consultar o CNPJ!')



if __name__ == '__main__':
    getCNPJ(cnpj)


48294522000170