"""Listas
Em uma turma de alunos do ensino médio, o professor deseja bonificar alunos mais participativos em aula. Para isso, ele faz perguntas em diferentes momentos da aula e, o aluno que responder primeiro, ele anota o nome. Ao final da disciplina, o professor confere suas anotações e, para cada aluno que respondeu, ele conta a quantidade de vezes que respondeu uma questão e bonifica com 0.1 pontos na média para cada resposta.

Visando maior praticidade, o professor deseja criar um programa em python que recebe uma lista com o nome dos alunos que fizeram as questões. Por exemplo:

A = ['junior', 'junior', alice', 'cecilia', 'junior', 'carlos', 'carlos', 'alice']

Dada a lista, crie um programa que retorne o aluno que tiver maior ocorrêcia na lista. Por exemplo, na lista A acima, deverá retornar 'junior', já que esse aluno é o que mais participou das aulas, possuindo maior ocorrência na lista.

Dica: utilize a função count.

Observação: em caso de empate, ordene os nomes e retorne o primeiro após a ordenação. Por exemplo, supondo a lista A = ['junior', alice', 'cecilia', 'junior', 'carlos', 'carlos', 'alice'], temos junior, alice e carlos com a mesma ocorrência na lista (2). Para decidir entre os três, ordene e retorne Alice."""






def aluno_mais_participativo(lista_alunos):
  """
  Função que recebe uma lista de nomes de alunos e retorna o aluno com maior ocorrência na lista.

  Parâmetros:
    lista_alunos (list): Lista de nomes de alunos.

  Retorno:
    str: Nome do aluno com maior ocorrência na lista.
  """
  # Dicionário para armazenar a contagem de participações de cada aluno
  contagem_alunos = {}

  # Conta as participações de cada aluno
  for aluno in lista_alunos:
    if aluno in contagem_alunos:
      contagem_alunos[aluno] += 1
    else:
      contagem_alunos[aluno] = 1

  # Encontra o aluno com maior ocorrência
  maior_participacao = max(contagem_alunos.values())
  alunos_mais_participativos = [aluno for aluno, participacao in contagem_alunos.items() if participacao == maior_participacao]

  # Ordena a lista de alunos mais participativos em ordem alfabética
  alunos_mais_participativos.sort()

  # Retorna o primeiro aluno da lista ordenada
  return alunos_mais_participativos[0]

# Exemplo de uso
lista_alunos = ['junior', 'junior', 'alice', 'cecilia', 'junior', 'carlos', 'carlos', 'alice']

aluno_mais_participante = aluno_mais_participativo(lista_alunos)
print(f"O aluno com maior ocorrência na lista é: {aluno_mais_participante}")










glglglglglglglglglgl