# Testnet publica


Si sólo quiere empezar a experimentar sin construir ninguna red física, le invitamos a unirse a la red pública de pruebas de Reticulum.
La red de pruebas es precisamente eso, una red informal para probar y experimentar. Estará activa la mayor parte del tiempo y cualquiera puede unirse a ella, pero esto también significa que no hay garantías de disponibilidad del servicio.

La red de pruebas ejecuta la últimisima versión de Reticulum (a menudo incluso un poco antes de su lanzamiento público). A veces pueden desplegarse versiones experimentales de Reticulum en nodos de la red de pruebas, lo que significa que pueden producirse comportamientos extraños. Si nada de esto le asusta, puede unirse a la red de prueba a través de TCP o I2P.

Sólo tiene que añadir una de las siguientes interfaces a su archivo de configuración de Reticulum:

```
# TCP/IP interfaz al Dublin Hub
  [[RNS Testnet Dublin]]
    type = TCPClientInterface
    enabled = yes
    target_host = dublin.connect.reticulum.network
    target_port = 4965

# TCP/IP interfaz al BetweenTheBorders Hub (proporcionado por la comunidad)
  [[RNS Testnet BetweenTheBorders]]
    type = TCPClientInterface
    enabled = yes
    target_host = betweentheborders.com
    target_port = 4242

# Interfaz a I2P Hub A
  [[RNS Testnet I2P Hub A]]
    type = I2PInterface
    enabled = yes
    peers = g3br23bvx3lq5uddcsjii74xgmn6y5q325ovrkq2zw2wbzbqgbuq.b32.i2p
```

La red de pruebas también contiene varios nodos de [Nomad Network](https://github.com/markqvist/nomadnet), y nodos de propagación [LXMF](https://github.com/markqvist/lxmf).

<p align="right"><a href="docs_es.html">Siguiente tema: Leer el manual</a></p>
