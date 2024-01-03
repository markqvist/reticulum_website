# Começar

A melhor forma de começar com o framework Reticulum depende do que você quer fazer. para detalhes completos e exemplos, olhe na seção [Começo Rápido](manual/gettingstartedfast.html) do [Manual Reticulum](manual/index.html).

## Software Experimental

*Atenção!* Reticulum ainda está em beta, Isso significa que ele atualmente executa bem, muito estável, mesmo assim ainda pode ter bugs críticos e falhas no funcionamento, privacidade ou a segurança do sistema como um todo.
Utilize o Reticulum se estiver confortável em relação a isso e entenda suas implicações.

## Comunidade e Ajuda

Se você estiver com problemas ou se algo não estiver funcionando, aqui estão alguns ótimos lugares para pedir ajuda:

- O [fórum de discussão](https://github.com/markqvist/Reticulum/discussions) no GitHub
- O canal da [Matrix do Retículum](https://matrix.to/#/#reticulum:matrix.org) em `#reticulum:matrix.org`
- O [subreddit Reticulum](https://reddit.com/r/reticulum)

## Instalação

Para instalar o Reticulum e utilitários relacionados no seu sistema, a forma mais fácil é via pip:

```bash
pip install rns
```

Feito isto, é possível utilizar qualquer programa que utilize o Reticulum ou inicie o Reticulum como um serviço do sistema com a [ferramenta rnsd](https://reticulum.network/manual/using.html#the-rnsd-utility).

Se o `pip` não estiver disponível no seu sistema, instale o `python3` ou `python3-pip` no seu sistema antes.

Durante a primeira execução, Reticulum irá criar um arquivo de configuração padrão, provendo conexão básica para outros pares Reticulum que podem ser alcançados. Se algum desses pares locais são Instâncias de Transporte, isso poderá te conectar a redes maiores. O arquivo de configuração padrão tem alguns exemplos e referências para criar uma configuração mais complexa.

Para exemplos mais detalhados de como expandir a comunicação por muitos dispositivos, tais como rádio amador, LoRa, portas seriais, links rápidos de IP ou pela Internet utilizando UDP ou TCP, leia mais na seção de [Interfaces Suportadas](manual/interfaces.html) do [Manual Reticulum](manual/index.html).

## Ferramentas Incluídas

Reticulum incluí uma variedade de ferramentas úteis para gerenciar suas redes, como ver estado, informações e outras tarefas. Você pode ler mais sobre essas ferramentas na seção de [Utilitários Incluídos](manual/using.html#included-utility-programs) do [Manual Reticulum](manual/index.html).

- O serviço de sistema `rnsd` (daemon) para executar o Reticulum é um serviço sempre disponível.
- Uma ferramenta para interface de estado chamada `rnstatus`, que mostra informações sobre as interfaces.
- A ferramenta para bloqueio de caminho e gerenciamento `rnpath` permitindo que você observe e modifique tabelas de caminho.
- Uma ferramenta de diagnóstico chamada `rnprobe` para checar a conectividade nos destinos.
- Um programa simples de transferência de arquivos chamado `rncp` tornando fácil de copiar arquivos para sistemas remotos.
- Um programa de comandos remotos `rnx` que permite você executar comandos e programas para obter dados de sistemas remotos.

Todas as ferramentas, incluindo `rnx` e `rncp`, funcionam de forma confiável e bem mesmo sob links de baixa largura de banda como LoRa e rádio amador.

## Programas utilizando Reticulum

Se você quiser ter uma noção do que o Reticulum é capaz de fazer, veja os seguintes projetos.

- Para uma plataforma de comunicação mesh resiliente, isolada da Internet e criptografada, veja a [Nomad Network](https://github.com/markqvist/NomadNet).
- O app [Sideband](https://github.com/markqvist/Sideband) para Android, Linux e MacOSX possuí interface gráfica e foca em facilidade.
- [LXMF](https://github.com/markqvist/LXMF) é um protocolo de transferência de mensagens distribuído, resistente a delays e interrupções, criado no Reticulum.

## Dependências

A instalação do pacote padrão `rns` requer as dependências listadas abaixo. Quase todos os sistemas e distribuições tem pacotes disponíveis para estas dependências, quando o pacote `rns` é instalado via `pip`, eles serão baixados e instalados em conjunto.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

Em alguns sistemas ou em raros casos, pode não ser possível instalar ou até compilar um ou mais dos módulos acima. Em tais situações, você pode utilizar o pacote `rnspure` no lugar, que não irá pedir dependências externas para instalação. Note que o conteúdo dos pacotes `rns` e `rnspure` é idêntico. A única diferença são as listas do pacote `rnspure` que não requerem dependências para instalação.

Não importa como o Reticulum é instalado ou iniciado, ele vai carregar as dependências externas apenas caso forem necessárias ou disponíveis. Se por exemplo você quer utilizar o Reticulum em um sistema que não suporta o [pyserial](https://github.com/pyserial/pyserial), é perfeitamente possível utilizar o pacote rnspure, mas o Reticulum em sistemas que não suportam a [PyCA/cryptography](https://github.com/pyca/cryptography), é importante que você leia e entenda a seção de [Criptografia](crypto.html) neste site.

## Desempenho

Reticulum possuí um grande potencial de desempenho, mas prioriza  a funcionalidade e desempenho em dispositivos de baixa largura de rede. O objetivo é fornecer desempenho dinâmico de 250 bits por segundo para 1 gigabit por segundo em hardware normal.

Atualmente o desempenho usual é aproximadamente 500 bits por segundo até 20 megabits por segundo, com dispositivos físicos mais rápidos que isso não sendo saturados. O desempenho além do nível atual é esperado para as próximas atualizações, mas não com prioridade alta até que o formato de cabo e API estejam maduros.

<p align="right"><a href="hardware_pt-br.html">Próxima Página: Hardware Compátivel</a></p>
