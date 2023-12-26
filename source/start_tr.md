# Hoş Geldiniz
Reticulum Ağı ile başlamanın en iyi yolu, ne yapmak istediğinize bağlıdır. Tam detaylar ve örnekler için [Hızlı Başlangıç](manual/gettingstartedfast.html) bölümüne [Reticulum Kılavuzu](manual/index.html)'nda göz atın.

## Deneysel Yazılım
*Dikkat!* Reticulum hala beta aşamasındadır. Şu an çok iyi çalışsa ve çok stabil olsa da, sistemde genel olarak kritik hatalar veya eksiklikler olabilir. Reticulum'u kullanıyorsanız buna rahatlıkla uyum sağlıyorsanız ve sonuçların ne anlama geldiğini anlıyorsanız kullanın.

## Topluluk ve Destek
Eğer sorun yaşarsanız veya bir şey çalışmıyorsa, yardım istemek için harika yerler şunlar:

- [GitHub'daki tartışma forumu](https://github.com/markqvist/Reticulum/discussions)
- `#reticulum:matrix.org` üzerinden [Reticulum Matrix Kanalı](element://room/!TRaVWNnQhAbvuiSnEK%3Amatrix.org?via=matrix.org)
- [Reticulum subreddit'i](https://reddit.com/r/reticulum)

## Kurulum
Sisteminize Reticulum'u ve ilgili araçları kurmanın en kolay yolu `pip` kullanmaktır:

```bash
pip install rns
```

Daha sonra Reticulum kullanan herhangi bir programı başlatabilir veya [rnsd aracı](manual/using.html#the-rnsd-utility) ile Reticulum'u bir sistem servisi olarak başlatabilirsiniz.

Eğer sisteminizde `pip` mevcut değilse, önce işletim sisteminiz için `python3` ve `python3-pip` paketlerini kurun.

İlk başlatıldığında Reticulum, yerel olarak erişilebilen diğer Reticulum eşlerine temel bağlantı sağlayan varsayılan bir yapılandırma dosyası oluşturacaktır. Bu yerel eşlerin herhangi biri Taşıma Örnekleri ise, sizi daha geniş ağlara bağlayabilirler. Varsayılan yapılandırma dosyası birkaç örnek ve daha karmaşık bir yapılandırma oluşturma referansları içerir.

Daha ayrıntılı örnekler için paket radyo veya LoRa, seri portlar veya hızlı IP bağlantıları ve UDP ve TCP arabirimlerini kullanarak İnternet üzerinden iletişimi genişletme konusunda [Desteklenen Arabirimler](manual/interfaces.html) bölümüne [Reticulum Kılavuzu](manual/index.html)'nda göz atın.

## Dahil Edilen Araçlar
Reticulum, ağlarınızı yönetmek, durum ve bilgi görüntülemek ve diğer görevler için bir dizi kullanışlı araç içerir. Bu programlar hakkında daha fazla bilgiyi [Dahil Edilen Yardımcı Programlar](manual/using.html#included-utility-programs) bölümünde [Reticulum Kılavuzu](manual/index.html)'nda bulabilirsiniz.

- Reticulum'u her zaman kullanılabilir bir servis olarak çalıştırmak için sistem arka plan uygulaması `rnsd`
- Arayüz durumu için bilgi gösteren `rnstatus` adlı bir araç
- Yol tablolarını görüntülemenizi ve değiştirmenizi sağlayan `rnpath` adlı bir yol arama ve yönetim aracı
- Bağlantıları kontrol etmek için `rnprobe` adlı bir teşhis aracı
- Uzak sistemlere dosya kopyalamayı kolaylaştıran basit bir dosya transfer programı olan `rncp`
- Uzak sistemlerden komutları ve programları çalıştırmanıza ve çıktıları almanıza izin veren uzaktan komut yürütme programı `rnx`

Tüm araçlar, `rnx` ve `rncp` dahil, düşük bant genişliği bağlantıları üzerinde bile güvenilir bir şekilde çalışır.

## Reticulum Kullanan Programlar
Reticulum'un ne yapabileceğine hızlı bir şekilde bir fikir edinmek istiyorsanız, aşağıdaki kaynaklara göz atın.

- Off-grid, şifreli ve dayanıklı bir ağ iletişim platformu için [Nomad Network](https://github.com/markqvist/NomadNet)
- Android, Linux ve macOS uygulaması [Sideband](https://github.com/markqvist/sideband) grafik arayüze sahiptir ve kullanım kolaylığına odaklanır.
- [LXMF](https://github.com/markqvist/lxmf), Reticulum üzerine inşa edilmiş dağıtılmış, gecikmeli ve kesintiye uğramış bir ileti transfer protokolüdür.

## Gereksinimler
Varsayılan `rns` paketinin kurulumu aşağıda listelenen gereksinimleri ister. Hemen hemen tüm sistemler ve dağıtımlar, bu bağımlılıklar için gereken hazır paketlere sahiptir ve `pip` ile `rns` paketi kurulduğunda indirilip kurulacaktır.

- [PyCA/cryptography](https://github.com/pyca/cryptography)
- [netifaces](https://github.com/al45tair/netifaces)
- [pyserial](https://github.com/pyserial/pyserial)

Daha sıra dışı sistemlerde ve bazı nadir durumlarda yukarıdaki modüllerden bir veya daha fazlasını kurmak veya hatta derlemek mümkün olmayabilir. Bu durumlarda `rnspure` paketini kullanabilirsiniz, bu kurulum için harici bağımlılıklar gerektirmez. Lütfen unutmayın ki `rns` ve

 `rnspure` paketlerinin içerikleri *aynıdır*. Tek fark, `rnspure` paketinin kurulum için gerekli bağımlılıkları listelememesidir.

Reticulum nasıl kurulup başlatılırsa başlatsın, dış bağımlılıkları sadece *gerektiğinde* ve *uygunsa* yükler. Örneğin, [pyserial](https://github.com/pyserial/pyserial) desteklemeyen bir sistemde Reticulum'u kullanmak istiyorsanız, bunu `rnspure` paketi kullanarak yapabilirsiniz, ancak Reticulum seri tabanlı arayüzleri kullanamayacaktır. Diğer tüm kullanılabilir modüller, ihtiyaç duyulduğunda yine yüklenecektir.

**Lütfen Dikkat Edin!** `rnspure` paketini [PyCA/cryptography](https://github.com/pyca/cryptography)'yi desteklemeyen sistemlerde Reticulum'u çalıştırmak istiyorsanız, bu sitenin [Şifreleme Temelleri](crypto.html) bölümünü okumanız gerekmektedir.

## Performans
Reticulum, çok geniş bir kullanılabilir performans aralığına yönelik olup, düşük bant genişliği ortamlarında işlevselliği ve performansı önceliklendirir. Hedef, normal donanımda 250 bit/s'den 1 gigabit/s'ye dinamik bir performans aralığı sağlamaktır.

Şu anda kullanılabilir performans aralığı yaklaşık olarak 500 bit/s ile 20 megabit/s arasındadır ve bu hızların üzerindeki fiziksel ortamlar doyurulmamaktadır. Mevcut seviyenin ötesinde performans, gelecekteki güncellemeler için ama wire formatı ve API kilitlendikten sonra öncelikli olarak düşünülmüyor.

<p align="right"><a href="hardware_tr.html">Sonraki Konu: Desteklenen Donanım</a></p>