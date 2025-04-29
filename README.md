# Symmetric_Encryption_and_Authentication\
首先，先讀取被加密檔案（secretFile.txt），並印出其檔案的大小（134830082 bytes）
![image](https://github.com/user-attachments/assets/45740948-d5be-47aa-8cc8-ea92be81dd8a)

## Encryption and decryption using AES-CCM mode
a.	定義AES-CCM mode加密函式
其中有三個參數：key為加密用的金鑰、data為要被加密的資料內容、nonce為在串流加密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/6020e3f4-75cb-414d-a661-16a7799db0cd)
b.	呼叫 AES-CCM mode加密函式
傳入三個引數： key為加密用的金鑰、data為要被加密的資料內容、AESCCM_nonce為在AES-CCM mode加密方法中只使用一次的隨機數，最後得到加密資料和加密花費時間。
再以二進制的方式開啟一個名為AESCCM_CipherFile.txt的檔案並寫入以AES-CCM mode所加密的資料。
最後印出使用AES-CCM mode加密檔案的速度（每秒加密多少data bytes）。
![image](https://github.com/user-attachments/assets/02cae0c7-6e55-4ef5-a0ee-22f12991e184)
![image](https://github.com/user-attachments/assets/46e9772f-1cec-461a-9352-7cec61ab26b7)
c.	定義 AES-CCM mode解密函式
其中有三個參數：key為解密用的金鑰、data為要被解密的資料內容、nonce為在串流解密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/bcd7be69-e000-4902-a7e8-bcaa8775a9b2)
d.	呼叫AES-CCM mode解密函式
傳入三個引數： key為解密用的金鑰、AESCCM_encryptData為要被解密的已加密資料內容、AESCCM_nonce為在AES-CCM mode解密方法中只使用一次的隨機數，最後得到解密資料。
再開啟一個名為AESCCM_PlaintFile.txt的檔案並寫入以AES-CCM mode所解密的資料。
![image](https://github.com/user-attachments/assets/5bdd6af0-d95c-4a3c-8f8e-a6d6ec23d7e9)
e.	驗證 AES-CCM mode加解密實作是否正確
若解密後的資料內容和原本的檔案內容相同，則表示加解密實作正確；
	反之則表示加解密實作有誤。
![image](https://github.com/user-attachments/assets/fe5ede5c-e48c-4e86-9f93-fdbb2e26f70a)
![image](https://github.com/user-attachments/assets/b3309083-6002-4668-b4aa-90d10648ee7a)

## Encryption and decryption using AES-CTR mode (counter mode)
a.	定義AES-CTR mode (counter mode) 加密函式
其中有三個參數：key為加密用的金鑰、data為要被加密的資料內容、iv為初始化向量，用於起始計數器的值。
![image](https://github.com/user-attachments/assets/e96ee648-64e7-4d7f-bed2-33eb8ae44dbb)
b.	呼叫 AES-CTR mode (counter mode) 加密函式
傳入三個引數： key為加密用的金鑰、data為要被加密的資料內容、 iv為初始化向量，用於起始計數器的值。最後得到加密資料和加密花費時間。
再以二進制的方式開啟一個名為AESCTR_CipherFile.txt的檔案並寫入以AES- CTR mode所加密的資料。
最後印出使用AES-CTR mode加密檔案的速度（每秒加密多少data bytes）。
![image](https://github.com/user-attachments/assets/ad16c053-53a3-4a35-a110-53fd3d38c758)
![image](https://github.com/user-attachments/assets/6528acd6-6938-4889-a986-d335226b5fef)
c.	定義 AES-CTR mode (counter mode) 解密函式
其中有三個參數：key為解密用的金鑰、data為要被解密的資料內容、 iv為初始化向量，用於起始計數器的值。最後得到加密資料和加密花費時間。
![image](https://github.com/user-attachments/assets/715b200a-cfa2-4587-b813-9ec532da837d)
d.	呼叫 AES-CTR mode (counter mode) 解密函式
傳入三個引數： key為加密用的金鑰、AESCTR_encryptData為要被解密的已加密資料內容、 iv為初始化向量，用於起始計數器的值。最後得到解密資料。
再開啟一個名為AESCTR_PlaintFile.txt的檔案並寫入以AES-CTR mode所解密的資料。
![image](https://github.com/user-attachments/assets/269d1d6a-e55b-4a24-a052-dacd4f671093)
e.	驗證 AES-CTR mode (counter mode) 加解密實作是否正確
若解密後的資料內容和原本的檔案內容相同，則表示加解密實作正確；
	反之則表示加解密實作有誤。
![image](https://github.com/user-attachments/assets/16b49eb5-a118-45b3-9b34-f5ee0d8604f5)
![image](https://github.com/user-attachments/assets/688ba8e1-75a6-47ed-a161-367f16aefe28)

## Encryption and decryption using ChaCha20
## Compute the SHA-3-512 message digest of the string "I love cryptography." (without the quotes) and describe the tool or program you used to compute it.
