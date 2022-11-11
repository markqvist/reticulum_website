# Rede de Teste Pública
Se você quiser experimentar sem criar nenhuma rede física, você é bem-vindo para entrar na Rede de Teste Pública Reticulum. A rede de teste é apenas isso, uma rede informal para teste e experimentação. Estará online na maior parte do tempo e qualquer um pode entrar, mas isso também significa que não há garantia da disponibilidade do serviço.

A rede de teste executa a última versão do Reticulum (muitas vezes antes da versão ser publicamente lançacada).
Algumas vezes versões experimentais do Reticulum podem ser utilizada em nós da rede de teste, que pode causar instabilidade. Se nada disso importa para você, você pode entrar na rede de teste via TCP ou I2P.

Adicione uma das seguintes interfaces no arquivo de configuração do seu Reticulum:

```
# Interface TCP/IP para o Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# Interface TCP/IP para o Frankfurt Hub
  [[RNS Testnet Frankfurt]]
    type = TCPClientInterface
    enabled = yes
    target_host = frankfurt.connect.reticulum.network
    target_port = 5377

# Interface para o I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = mrwqlsioq4hoo2lmeeud7dkfscnm7yxak7dmiyvsrnpfag3z5tsq.b32.i2p

# Interface para o I2P Hub B
  [[RNS Testnet I2P Hub B]]
    type = I2PInterface
    enabled = yes
    peers = iwoqtz22dsr73aemwpw7guocplsjjoamyl7sogj33qtcd6ds4mza.b32.i2p
```

A rede de teste também contém o número de nós da [Nomad Network](https://github.com/markqvist/nomadnet) e nós de propagação [LXMF](https://github.com/markqvist/lxmf).

<p align="right"><a href="docs_pt-br.html">Próxima Página: Leia o Manual</a></p>
