# International Letter Cryptography Tool

Bu basit kriptografi aracı, sadece uluslararası harfler için tasarlanmıştır. Aracın şifreleme ve şifre çözme işlemleri için özelleştirilebilir bir karakter kümesi kullanır. Karakterler arasında büyük ve küçük harfler, rakamlar ve bazı yaygın semboller bulunur. İhtiyaç halinde, `character` listesine daha fazla karakter ekleyerek karakter kümesini genişletebilirsiniz.

## Caesar Şifreleme

Bu araç, en basit ve eski şifreleme tekniklerinden biri olan Caesar şifrelemesini kullanır. Her harfi belirli bir sayıda karakteri aşağı kaydırarak çalışır. Bu uygulamada, kaydırılacak karakter pozisyonları "scroll count" ile belirlenir.

### Kullanım

1. Programı başlatın ve istenen işlemi seçin:
   - Bir mesajı şifrelemek için `1` girin.
   - Bir şifreyi çözmek için `2` girin.

### Şifreleme

Eğer bir mesajı şifrelemek isterseniz:
1. "Scroll count" değerini girin. Bu değer, her karakterin kaç pozisyon aşağı kaydırılacağını belirler.
2. Program, "scroll count" değerine göre bir şifreleme anahtarı oluşturur.
3. Şifrelemek istediğiniz mesajı girin.
4. Program, oluşturulan şifreleme anahtarını ve şifrelenmiş şifreyi çıktı olarak verir.

### Şifre Çözme

Eğer bir şifreyi çözmek isterseniz:
1. Şifreleme sırasında kullandığınız aynı "scroll count" değerini girin.
2. Şifrelenmiş şifreyi girin.
3. Program, verilen "scroll count" değerini kullanarak şifreyi çözer.
4. Şifrelenmiş mesajı çözülmüş halde görüntüler.

## Dikkat Edilmesi Gereken Noktalar

- **Scroll Count:** Caesar şifrelemesinin güvenliği, "scroll count" değerinin gizliliğine dayanır. Scroll count'u bilen herkes kolayca mesajı çözebilir. Bu nedenle, scroll count'u gizli tutmak önemlidir.

- **Anahtar Uzayı:** Caesar şifrelemesinin anahtar uzayı sınırlıdır (karakter kümesindeki karakter sayısı kadardır) ve tüm olası kaydırmaları deneyerek kırılabilir.

- **Karakter Kümesi:** Şifrelemenin güvenliği, karakter kümesinin büyüklüğüne ve rastgeleliğine bağlıdır. Daha fazla karakter ve sembol eklemek, şifrelemenin güvenliğini artırabilir. Ancak bu, şifreleme sürecini daha karmaşık hale getirir.

- **Çevrimiçi Güvenlik:** Caesar şifrelemesi, basitliği ve brute force saldırılarına karşı savunmasızlığı nedeniyle modern çevrimiçi güvenlik gereksinimleri için uygun değildir. Eğitim amacıyla veya şifrelemenin temellerini anlamak için kullanılması daha uygundur.

- **Unicode Karakterleri:** Mevcut karakter kümesi temel İngiliz harflerini, rakamları ve sembolleri içerse de, özel karakterlere veya vurgu işaretlerine sahip diller için uygun olmayabilir. Daha geniş bir dil yelpazesini desteklemek için karakter kümesini genişletmek gerekebilir.

- **Algoritma Seçimi:** Güçlü güvenlik gerektiren gerçek dünya uygulamaları için AES veya RSA gibi daha gelişmiş şifreleme algoritmalarını kullanmayı düşünmelisiniz.

**Not:** Bu araç eğitim amaçları ve temel şifreleme ihtiyaçları için tasarlanmıştır. Güçlü güvenlik gerektiren hassas veya kritik bilgiler için kullanılmamalıdır. Güvenli iletişim için her zaman iyi kurulmuş şifreleme yöntemlerini seçin.

**--------------------------------------------------------------------------------------------------------------------------**

# International Letter Cryptography Tool

This is a basic cryptographic tool designed for international letters. The tool uses a customizable set of characters for encryption and decryption. The characters include uppercase and lowercase letters, numbers, and a few common symbols. If needed, you can expand the set of characters by adding more to the `character` list.

## Caesar Cipher

The tool employs the Caesar cipher, one of the simplest and oldest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the character set. In this implementation, the number of positions shifted is determined by the "scroll count."

### Usage

1. Run the program and select the desired operation:
   - Enter `1` to encrypt a message.
   - Enter `2` to decrypt a cipher.

### Encryption

If you choose to encrypt a message:
1. Provide a "scroll count." This count determines the number of positions each character will be shifted for encryption.
2. The program will generate an encryption key based on the scroll count.
3. Enter the message you want to encrypt.
4. The program will output the generated encryption key and the encrypted cipher.

### Decryption

If you choose to decrypt a cipher:
1. Provide the same "scroll count" used for encryption.
2. Enter the encrypted cipher.
3. The program will decrypt the cipher using the provided scroll count.
4. The decrypted message will be displayed.

## Important Points

- **Scroll Count:** The security of the Caesar cipher depends on the secrecy of the scroll count. Anyone who knows the scroll count can easily decrypt the message. Therefore, it's important to keep the scroll count confidential.

- **Key Space:** Since the Caesar cipher has a limited number of possible keys (equal to the number of characters in the character set), it can be easily cracked through brute force by trying all possible shifts.

- **Character Set:** The strength of the encryption relies on the size and randomness of the character set. Adding more characters and symbols can improve the security of the encryption. However, it also makes the encryption process more complex.

- **Online Security:** The Caesar cipher is quite weak for modern online security needs due to its simplicity and vulnerability to brute force attacks. It's more suitable for educational purposes or for understanding the basics of encryption.

- **Unicode Characters:** While the current character set covers basic English letters, numbers, and symbols, it might not work well for languages with special characters or diacritics. Expanding the character set would be necessary to support a wider range of languages.

- **Algorithm Choice:** For real-world applications requiring stronger security, consider using more advanced encryption algorithms like AES or RSA.

**Note:** This tool is designed for educational purposes and basic encryption needs. It should not be used for sensitive or critical information where strong security is required. Always choose well-established encryption methods for secure communication.
