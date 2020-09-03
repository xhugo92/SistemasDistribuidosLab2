1: 
Será usado um dicionario para guardar as ocorrencias das palavras e uma string para a mensagem de erro

2:
O cliente manda como uma mensagem os N nomes dos arquivos a serem lidos e espera como respostas as N mensagens

O servidor recebe uma mensagem com o nome de N arquivos separados por espaço e envia como resposta N mensagens do resultado daquele processamento

3:
Foi nescessario o uso da biblioteca Json pra transformar o dicionario em byte para ser enviado como mensagem.

Preferi enviar N mensagens ao invés de um para minimizar o processamento do lado do Cliente, ficando responsavel somente pelo envio e recebimento de mensagens
	
