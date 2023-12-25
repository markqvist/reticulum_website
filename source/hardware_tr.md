# Desteklenen Donanım
Reticulum, en az yarı dubleks bir kanalı ve saniyede 500 bit iletim hızını destekleyebilen neredeyse her ortamda kullanılabilir ve MTU değeri 500 byte olan bir ortamda çalışabilir. Veri radyoları, modemler, LoRa radyoları, seri hatlar, AX.25 TNC'ler, amatör telsiz dijital modları, WiFi ve Ethernet cihazları, serbest uzay optik bağlantılar ve benzeri sistemler, Reticulum'un kullanabileceği fiziksel cihaz türlerine örnek olarak verilebilir. Desteklenen arayüz türleri şunları içerir:

- Herhangi bir Ethernet cihazı
- Neredeyse tüm WiFi tabanlı donanımlar
- [RNode](https://unsigned.io/rnode/) kullanılarak LoRa
- Paket Radyo TNC'leri (AX.25 ile veya olmadan)
- KISS uyumlu donanım ve yazılım modemleri
- Bir dizi seri porta sahip herhangi bir cihaz
- IP ağları üzerinden TCP
- IP ağları üzerinden UDP
- stdio veya borular aracılığıyla harici programlar
- stdio veya borular aracılığıyla özel donanım

Daha fazla bilgi ve desteklenen arayüz türlerinin tam listesi için lütfen [İletişim Donanımı](manual/hardware.html) ve [Desteklenen Arayüzler](manual/interfaces.html) bölümlerini okuyun.

Reticulum ayrıca mevcut IP ağları üzerinde de kapsülleyebilir, bu nedenle onu kablolu Ethernet, yerel WiFi ağınız veya İnternet üzerinden kullanmanıza engel bir şey yok, burada da aynı şekilde çalışacaktır. Aslında, Reticulum'un güçlü yanlarından biri, farklı ortamları kolayca birbirine bağlama yeteneğidir; bu, mevcut altyapının herhangi bir karışımını kullanarak özelleştirilebilir, dayanıklı ve şifreli bir mesh ağı oluşturmanıza izin verir.

Örneğin, bir Raspberry Pi'nin hem bir LoRa radyosuna, bir paket radyo TNC'sine ve bir WiFi ağına bağlı olduğu bir yapı kurmak mümkündür. Arayüzler yapılandırıldığında, Reticulum gerisini halledecek ve WiFi ağındaki herhangi bir cihaz, ağın LoRa ve paket radyo taraflarındaki düğümlerle iletişim kurabilir, ve tam tersi.

<p align="right"><a href="connect.html">Sonraki Konu: Genel Test Ağı</a></p>