# Bağlantı Kurma

Reticulum, abone olduğunuz bir hizmet değildir, ayrıca "katıldığınız" tek bir küresel ağ da değildir. Bir *ağ yığınıdır* (networking stack); belirli değerleriniz, gereksinimleriniz ve operasyonel ortamınızla uyumlu iletişim sistemleri oluşturmak için bir araç setidir. Diğer Reticulum eşlerine bağlanma şeklini seçmek tamamen kendi tercihinizdedir.

Reticulum'u kullanmaya ilk başladığınızda, iletişim kurmak istediğiniz eşlerle bağlantı kurmanın bir yoluna ihtiyacınız vardır - bu da *bağlantı kurma* (bootstrapping connectivity) sürecidir. Bir veya daha fazla geçerli arayüz tanımı edindiğinizde, bunları Reticulum yapılandırmanızın `[interfaces]` bölümüne ekleyebilirsiniz.

Bu sayfa en temel genel bakışı sunar, ancak bağlantı kurma için mevcut esnekliği ve seçenekleri tam olarak anlamak için kılavuzun [Bağlantı Kurma](manual/gettingstartedfast.html#creating-a-network-with-reticulum) bölümünü okuyun.

## Dağıtık Omurgaya Bağlanın

Dünyanın dört bir yanındaki gönüllüler tarafından işletilen Reticulum Taşıma Düğümlerinden oluşan küresel, dağıtık bir omurga bulunmaktadır. Bu ağ, hem açık hem de özel düğümlerin heterojen bir koleksiyonundan oluşur ve koordine edilmemiş, gönüllü bir ağlar arası omurga oluşturarak Reticulum için şu anda küresel taşıma ve ağlar arası bağlantı yetenekleri sağlamaktadır.

Bağlantı kurmak için arayüz tanımları bulmanın iyi yerleri, [directory.rns.recipes](https://directory.rns.recipes/) ve [rmap.world](https://rmap.world/) gibi topluluk tarafından işletilen web siteleridir.

Reticulum *organik büyüme* yaklaşımını teşvik eder. Uzak sunuculara kalıcı statik bağlantılara güvenmek yerine, geçici önyükleme bağlantılarını kullanarak sürekli olarak daha alakalı veya yerel altyapı *keşfedebilirsiniz*. Keşfedildikten sonra, sisteminiz bu eşlerle otomatik olarak daha güçlü, daha doğrudan bağlantılar kurabilir ve geçici önyükleme bağlantılarını kaldırabilir. Bu, coğrafi olarak alakalı, dayanıklı ve verimli bir bağlantılar ağıyla sonuçlanır.

## Kişisel Altyapı Oluşturun

Herkesi, ev kullanıcılarını bile, **kişisel altyapı** oluşturma açısından düşünmeye şiddetle teşvik ediyoruz. Evinizdeki her telefonu, tableti ve bilgisayarı doğrudan genel bir ağ geçidine bağlamayın. Bunun yerine, eski bir bilgisayarı, bir Raspberry Pi'yi veya desteklenen bir yönlendiriciyi kendi, kişisel **Taşıma Düğümünüz** olarak kullanmak üzere yeniden amaçlandırın:

* Yerel Taşıma Düğümünüz evinizde durur, WiFi'inize ve belki de bir radyo arayüzüne (bir RNode gibi) bağlıdır.
* Bu düğümü bir `bootstrap_only` arayüzü (belki daha geniş bir ağa bir TCP tüneli) ile yapılandırır ve arayüz keşfini etkinleştirirsiniz.
* Siz uyurken, çalışırken veya yemek yaparken, düğümünüz ağa dinler. Diğer yerel topluluk üyelerini keşfeder, Ağ Kimliklerini doğrular ve otomatik olarak doğrudan bağlantılar kurar.
* Kişisel cihazlarınız artık canlı, nefes alan yerel bir ağa entegre olan *yerel* düğümünüze bağlanır. Trafiğiniz uzaktaki bir sunucuda sekmek yerine topluluktaki diğer gerçek kişiler tarafından sağlanan yerel yollardan akar.

**Görmek istediğiniz ağları başkalarının kurmasını beklemeyin**. Her ağ önemlidir, belki de en çok bireysel aileleri ve kişileri destekleyenler. Yeterli sayıda bu kişisel, yerel altyapı oluştuğunda, bunları herkese açık İnternet üzerinden geçmeden birbirlerine doğrudan bağlamak kaçınılmaz hale gelir.

<p align="right"><a href="docs_tr.html">Sonraki Konu: Kılavuzu Okuyun</a></p>