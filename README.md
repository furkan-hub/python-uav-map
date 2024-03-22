bu repo pyqt5 web arayüzü ile html ve java script kullanılarak yapılan harita arayüzü örneğidir.

python ve pyqt5 kullanarak harita arayüzü yapmak her ne kadar mantıksız olsa da pyqt5 in webengine eklentisi ile bu bir sorun olmaktan çıkıyor 

haritalar ile çalışırken karşımıza 2 tane kavram çıkar; Dinamik ve Statik haritalar statik haritalar üzerinde herhangi bir gerçek zamanlı güncelleme yapılmayan sabit haritalardır dinamik haritalar ise tam tersi sürekli canlı verileri ile kendisini güncelleyen haritalardır. Örnek olarak harita üzerinde dağların konumlarını gösteren bir uygulama statik bir haritadır çünkü dağlar sürekli yer değitirmezler fakat siz bir hava trafiğini harita üzerinde göstermek isterseniz size dinamik olarak harita da ki bütün araçların konumunu güncelleyen dinamik yapıda bir harita uygulaması gerekir.

aslında pyqt5 için bir çok harita kütüphanesi mevcut fakat bu kütüphanelerin hepsi dinamik olarak güncellenmeye uygun değil
bu yüzden html,css java script tabanlı bir uygulamanın webengine kullanılarak dinamik haritalar oluşturulması daha doğrudur.

şimdi bu uygulamada kullanılan kütüphanelerden ve araçlardan bahsedeyim.

-- Pyqt5 --

python dili için geliştirilmiş bir arayüz oluşturma uygulamasıdır. 

-- QwebEngine --

Pyqt5 ile web uygulamalarını çalıştırmak için kullanılan bir eklentidir.

-- Leaflet --

leaflet kütüphanesi html, javascript tabanlı bir web harita geliştirme kütüphanesidir leaflet size oldukça fazla araç sunarak istediğiniz her türlü haritayı oluşturmanıza olanak tanır eğer istediğiniz görevi yerine getirecek bir fonksiyon yoksa merak etmeyin leflet kütüphanesinin topluluk desteği oldukça fazladır istediğiniz fonksiyonu yerine getiren bir eklenti muhakkak bulursunuz örnek olarak ben harita üzerin de ki iconları döndürmek için "leaflet.rotatedMarker.js" adında bir eklenti ekledim.

gelelim kodun çalışma mantığına

ilk olarak "map.html" adında leaflet kütüphanesini kullanarak oluşturulan web tabanlı bir harita arayüzü uygulaması var ve main python kodunda pyqt5 qwebengine kullanlıarak bu html sayfası bir pencerede gösterilir ardından icon konumu güncellemek için html kodunun içinden updateMarker fonksiyonu main kod üzerinden çağırılır ve güncellenir.


BU KıSıM ÇOK ÖNEMLI.!!!!!!!!!
-- resource.py dosyası ---

eğer qwebengine ile çalışıyorsanız pyqt5 güvenlik sebebi ile sizin local de ki javascript kütüphanelerinize erişemez bu yüzden indirdiğiniz js kütüphanelerini resource.qrc dosyasına dosya yolunu tanımlayıp dosya dizininde terminalde şu komutu

"pyrcc5 resources.qrc -o resources.py"

çalıştırıp bu dosyaları derleyip bir python dosyası haline getirmelisiniz. bu sayede main kodumuzda bu kütüphaneyi çağırıp html kodumuzda offline olarak js kütüphaneleri ile kullanabiliriz.
