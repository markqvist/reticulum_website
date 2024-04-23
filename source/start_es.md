# Empezar
La mejor manera de empezar a usar el protocolo Reticulum depende de que
quieras hacer. Para más detalles y ejemplos, consulte la sección [Empezar rapidito](manual/gettingstartedfast.html) del [Manual de Reticulum](manual/index.html).

## Software experimental
**¡A saber!** Reticulum todavía está en fase beta. Esto significa que, aunque ya funciona muy bien y es muy estable, es muy
posible que todavía haya errores o fallos críticos en el comportamiento, la privacidad o la seguridad del sistema en su conjunto.
Utilice Reticulum si se siente cómodo con esto y comprende las implicaciones.

## Comunidad y Soporte

Si estas teniendo algún problema o algo no esta funcionando, estos son algunos excelentes lugares para pedir ayuda:

- El [foro de discusión](https://github.com/markqvist/Reticulum/discussions) en Github
- El [Canal de Reticulum en Matrix](https://matrix.to/#/#reticulum:matrix.org) en `#reticulum:matrix.org`
- El [Subreddit de Reticulum](https://reddit.com/r/reticulum)

## Instalación
Para instalar reticulum y utilidades relacionadas, la forma más fácil es usando pip:

```bash
pip install rns
```

Podes ejecutar entonces cualquier programa que use Reticulum, o iniciar Reticulum como un servicio del sistema con [la utilidad rnsd](manual/using.html#the-rnsd-utility).

Si `pip` no es disponible en tu sistema, instala primero `python3` y `python3-pip` para tu sistema operativo.

La primera vez que inicia, Reticulum crea un archivo de configuración por defecto, proporcionando conectividad básica con pares
de Reticulum que puedan ser localmente localizables. Si cualquiera de esos pares locales son instancias de transporte, puede que
te conecten con redes más grandes. El archivo de configuración contiene algunos ejemplos y referencias para crear configuraciones
más complejas.

Para ejemplos más detallados sobre como expandir la comunicación a más medios, como paquetes de radio o Lora, puertos seriales,
o a través de enlaces rápidos de IP e Internet utilizando las interfaces UDP y TCP, peguele una mirada a la sección
[Interfaces soportadas](manual/interfaces.html) del [Manual de Reticulum](manual/index.html).

## Utilidades Incluidas

Reticulum incluye una serie de utilidades para gestionar sus redes, ver el estado y la información, y otras tareas. Puede leer
más sobre estos programas en la sección [Utilidades Incluidas](manual/using.html#utilidades-incluidas) del [Manual de Reticulum](manual/index.html).

- El servicio/daemon `rnsd` para correr Reticulum como un servicio siempre disponible
- Una utilidad de estado de la interfaz llamada `rnstatus`, para mostrar info sobre interfaces
- La herramienta de búsqueda y gestión de rutas `rnpath` le permite ver y modificar tablas de rutas
- Una herramienta de diagnóstico llamada `rnprobe` para comprobar la conectividad con los destinos, similar a `ping`
- Un sencillo programa de transferencia de archivos llamado `rncp` que facilita la copia de archivos a sistemas remotos.
- El programa de ejecución remota de comandos `rnx` que le permite ejecutar comandos, programas y recuperar output de sistemas remotos.

Todas las herramientas, incluidas `rnx` y `rncp`, funcionan bien y con fiabilidad incluso en enlaces de muy bajo ancho de banda como LoRa o radio por paquetes.

## Programas que usan Reticulum
Si quiere rápidamente hacerse una idea de lo que puede hacer Reticulum, peguele una mirada a los siguientes recursos:

- Para una plataforma de comunicaciones *mesh* sin conexión a la red, encriptada y resiliente, consulte [Nomad Network](https://github.com/markqvist/NomadNet).
- La aplicación para Android, Linux y macOS [Sideband](https://github.com/markqvist/sideband) tiene una interfaz gráfica y se centra en facilidad de uso.
- [LXMF](https://github.com/markqvist/lxmf) es un protocolo de transferencia de mensajes distribuido, tolerante a retrasos e interrupciones y basado en Reticulum.

## Dependencias

La instalación del paquete `rns` requiere las dependencias que se enumeran a continuación. Casi todos los sistemas y distribuciones tienen paquetes disponibles para estas dependencias, y cuando se instala el paquete `rns` con `pip`, también se descargan e instalan.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

En sistemas más inusuales, y en algunos casos raros, puede que no sea posible instalar o incluso compilar uno o más de los módulos anteriores. En tales situaciones, puede utilizar en su lugar el paquete `rnspure`, que no requiere dependencias externas para su instalación. Tenga en cuenta que el contenido de los paquetes `rns` y `rnspure` es *idéntico*. La única diferencia es que el paquete `rnspure` no necesita dependencias externas para su instalación.

Independientemente de cómo se instale e inicie Reticulum, este cargará las dependencias externas sólo si son *necesarias* y están *disponibles*. Si, por ejemplo, desea utilizar Reticulum en un sistema que no admite [pyserial](https://github.com/pyserial/pyserial), es perfectamente posible hacerlo utilizando el paquete `rnspure`, pero Reticulum no podrá utilizar interfaces basadas en serial. Todos los demás módulos disponibles seguirán cargándose cuando sea necesario.

**Atenti!** Si utiliza el paquete `rnspure` para ejecutar Reticulum en sistemas que no soportan [PyCA/cryptography](https://github.com/pyca/cryptography), es importante que lea y comprenda la sección [Primitivas Criptográficas](crypto_es.html) de este sitio.

## Desempeño

Reticulum busca cubrir un amplio rango de desempeño utilizable, pero prioriza la funcionalidad y el desempeño sobre medios de baja capacidad de ancho de banda. El objetivo es ofrecer un entorno de desempeño dinámico que va desde 250 bit por segundo hasta 1 giga bit por segundo en hardware normal.

Actualmente, el rango de desempeño utilizable está aproximadamente en 150 bit por segundo a 40 mega bits por segundo, mientras que los medios físicos más rápidos no están saturados. El desempeño superior a este nivel se reserva para actualizaciones futuras, pero no es prioritario hasta que la formatos de cable y API hayan sido establecidos.

<p align="right"><a href="hardware_es.html">Próximo Tema: Hardware soportado</a></p>
