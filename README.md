# Site Admin Paneli Bulma Aracı

[![Admin Panel Finder Banner](https://via.placeholder.com/1200x400/007bff/ffffff?text=Admin+Panel+Finder+Tool)](https://github.com/seninkullaniciadin/seninprojen)

Bu Python projesi, web sitelerinin **admin paneli giriş sayfalarını otomatize bir şekilde bulmak** için tasarlanmıştır. Çeşitli yaygın dizinleri ve alt dizinleri deneyerek olası admin paneli URL'lerini hızlıca tespit eder.

---

## 🚀 Kurulum ve Kullanım

Bu aracı yerel makinenizde kurmak ve çalıştırmak oldukça kolaydır. Proje **Python** ile yazıldığı için, Python'un kurulu olduğu herhangi bir işletim sisteminde (Windows, macOS, Linux) rahatlıkla kullanabilirsiniz.

### Önkoşullar

Aracı çalıştırmak için bilgisayarınızda **Python 3.x**'in kurulu olması yeterlidir.

### Adımlar

1.  **Depoyu Klonlayın:** İlk olarak, proje dosyalarını bilgisayarınıza indirin. Terminal veya komut istemcinizi açarak aşağıdaki komutu çalıştırın:

    ```bash
    git clone [https://github.com/seninkullaniciadin/seninprojen.git](https://github.com/seninkullaniciadin/seninprojen.git)
    cd seninprojen
    ```
    *(**Not:** `seninkullaniciadin` ve `seninprojen` kısımlarını kendi GitHub kullanıcı adın ve projenin depo adıyla değiştirmeyi unutma.)*

2.  **Gerekli Kütüphaneleri Yükleyin:** Proje, web istekleri için büyük ihtimalle **`requests`** kütüphanesini kullanıyordur. Bu kütüphaneyi yüklemek için aşağıdaki komutu çalıştırın:

    ```bash
    pip install requests
    ```
    *(Eğer projen başka kütüphaneler de kullanıyorsa, onları da `pip install kütüphane_adı` şeklinde yüklemen gerekir.)*

### Aracı Çalıştırma

Kütüphaneleri yükledikten sonra, aracı çalıştırmaya hazırsın! Terminal veya komut istemcinizde aşağıdaki komutu kullanarak admin paneli aramasını başlat:

```bash
python admin_finder.py <hedef_url>
