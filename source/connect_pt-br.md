# Rede de Teste Pública
Se você quiser experimentar sem criar nenhuma rede física, você é bem-vindo para entrar na Rede de Teste Pública Reticulum. A rede de teste é apenas isso, uma rede informal para teste e experimentação. Estará online na maior parte do tempo e qualquer um pode entrar, mas isso também significa que não há garantia da disponibilidade do serviço.

A rede de teste executa a última versão do Reticulum (muitas vezes antes da versão ser publicamente lançada).
Algumas vezes versões experimentais do Reticulum podem ser utilizada em nós da rede de teste, que pode causar instabilidade. Se nada disso importa para você, você pode entrar na rede de teste via TCP ou I2P.

Adicione uma das seguintes interfaces no arquivo de configuração do seu Reticulum:

```
# Interface TCP/IP para o Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# Interface TCP/IP para o BetweenTheBorders Hub
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = reticulum.betweentheborders.com
    target_port = 4242

# Interface para o I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

A rede de teste também contém o número de nós da [Nomad Network](https://github.com/markqvist/nomadnet) e nós de propagação [LXMF](https://github.com/markqvist/lxmf).

# Pontos de entrada da comunidade
Vários pontos de entrada disponíveis publicamente para redes Reticulum foram fornecidos pela comunidade. Para uso diário, é recomendado usar estes em vez da testnet.

Você pode conectar seus dispositivos ou instâncias a um ou mais destes para obter acesso a quaisquer redes Reticulum às quais eles estejam fisicamente conectados.

O ideal é configurar um nó de transporte Reticulum que seus próprios dispositivos possam alcançar localmente e, em seguida, conectar esse nó de transporte a alguns pontos de entrada públicos. Isso fornecerá conexões eficientes e redundância caso algum deles fique inativo.

{PUBLIC_ENTRYPOINTS}

<p align="right"><a href="docs_pt-br.html">Próxima Página: Leia o Manual</a></p>
