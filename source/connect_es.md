# Inicialización de la Conectividad  
  
Reticulum no es un servicio al que te suscribes, ni es una única red global a la que te "unes". Es una *pila de red*; un conjunto de herramientas para construir sistemas de comunicación que se alineen con tus valores específicos, requisitos y entorno operativo. La forma en que eliges conectarte con otros pares de Reticulum es enteramente tu elección.  
  
Cuando comienzas a usar Reticulum por primera vez, necesitas una forma de obtener conectividad con los pares con los que deseas comunicarte —el proceso de *inicialización de la conectividad*. Una vez que hayas obtenido una o más definiciones de interfaz válidas, puedes agregarlas a la sección `[interfaces]` de tu configuración de Reticulum.  
  
Esta página proporciona la visión general más básica, pero para comprender completamente la flexibilidad y opciones disponibles para la inicialización de la conectividad, lee la sección [Inicialización de la Conectividad](manual/gettingstartedfast.html#creating-a-network-with-reticulum) del manual.  
  
## Conectarse a la Red Troncal Distribuida  
  
Una red troncal global y distribuida de Nodos de Transporte de Reticulum está siendo operada por voluntarios de todo el mundo. Esta red constituye una colección heterogénea de nodos tanto públicos como privados que forman una red troncal de interconexión voluntaria y no coordinada que actualmente proporciona capacidades de transporte e interconexión global para Reticulum.  
  
Un buen lugar para encontrar definiciones de interfaz para la inicialización de la conectividad son sitios web gestionados por la comunidad como [directory.rns.recipes](https://directory.rns.recipes/) y [rmap.world](https://rmap.world/).  
  
Reticulum fomenta el enfoque de *crecimiento orgánico*. En lugar de depender de conexiones estáticas permanentes a servidores remotos, puedes usar conexiones de inicialización temporales para continuamente *descubrir* infraestructura más relevante o local. Una vez descubiertos, tu sistema puede formar automáticamente enlaces más fuertes y directos con estos pares, y descartar los enlaces de inicialización temporales. Esto resulta en una red de conexiones que son geográficamente relevantes, resilientes y eficientes.  
  
## Construir Infraestructura Personal  
  
Recomendamos encarecidamente que todos, incluso los usuarios domésticos, piensen en términos de construir **infraestructura personal**. No conectes cada teléfono, tableta y computadora de tu casa directamente a una puerta de enlace de Internet pública. En su lugar, reutiliza una computadora vieja, una Raspberry Pi o un router compatible para que actúe como tu propio **Nodo de Transporte** personal:  
  
* Tu Nodo de Transporte local se encuentra en tu hogar, conectado a tu WiFi y quizás a una interfaz de radio (como un RNode).  
* Configuras este nodo con una interfaz `bootstrap_only` (quizás un túnel TCP a una red más amplia) y habilitas el descubrimiento de interfaces.  
* Mientras duermes, trabajas o cocinas, tu nodo escucha la red. Descubre otros miembros locales de la comunidad, valida sus Identidades de Red y establece automáticamente enlaces directos.  
* Tus dispositivos personales ahora se conectan a tu nodo *local*, que está integrado en una malla local viva y en constante evolución. Tu tráfico fluye a través de rutas locales proporcionadas por otras personas reales de la comunidad en lugar de rebotar en un servidor remoto.  
  
**No esperes a que otros construyan las redes que deseas ver**. Cada red es importante, quizás especialmente aquellas que apoyan a familias e individuos. Una vez que exista suficiente infraestructura personal y local de este tipo, conectarlas directamente entre sí, sin atravesar el Internet público, se vuelve inevitable.

<p align="right"><a href="docs_es.html">Siguiente tema: Leer el manual</a></p>
