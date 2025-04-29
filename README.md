# Symmetric_Encryption_and_Authentication\
首先，先讀取被加密檔案（secretFile.txt），並印出其檔案的大小（134830082 bytes）
![image](https://github.com/user-attachments/assets/f0962ee1-349c-40e9-995b-a344ff4fc3d9)
![image](https://github.com/user-attachments/assets/3688ab39-22b0-458d-9018-d91acd22c9e5)

## Encryption and decryption using AES-CCM mode
### 定義AES-CCM mode加密函式
其中有三個參數：key為加密用的金鑰、data為要被加密的資料內容、nonce為在串流加密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/6020e3f4-75cb-414d-a661-16a7799db0cd)

### 呼叫 AES-CCM mode加密函式
傳入三個引數： key為加密用的金鑰、data為要被加密的資料內容、AESCCM_nonce為在AES-CCM mode加密方法中只使用一次的隨機數，最後得到加密資料和加密花費時間。
再以二進制的方式開啟一個名為AESCCM_CipherFile.txt的檔案並寫入以AES-CCM mode所加密的資料。
最後印出使用AES-CCM mode加密檔案的速度（每秒加密多少data bytes）。
![image](https://github.com/user-attachments/assets/02cae0c7-6e55-4ef5-a0ee-22f12991e184)
![image](https://github.com/user-attachments/assets/2b8cd547-1b61-4c77-b477-d4142f92cb21)


### 定義 AES-CCM mode解密函式
其中有三個參數：key為解密用的金鑰、data為要被解密的資料內容、nonce為在串流解密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/bcd7be69-e000-4902-a7e8-bcaa8775a9b2)

### 呼叫AES-CCM mode解密函式
傳入三個引數： key為解密用的金鑰、AESCCM_encryptData為要被解密的已加密資料內容、AESCCM_nonce為在AES-CCM mode解密方法中只使用一次的隨機數，最後得到解密資料。
再開啟一個名為AESCCM_PlaintFile.txt的檔案並寫入以AES-CCM mode所解密的資料。
![image](https://github.com/user-attachments/assets/5bdd6af0-d95c-4a3c-8f8e-a6d6ec23d7e9)

### 驗證 AES-CCM mode加解密實作是否正確
若解密後的資料內容和原本的檔案內容相同，則表示加解密實作正確；反之則表示加解密實作有誤。
![image](https://github.com/user-attachments/assets/fe5ede5c-e48c-4e86-9f93-fdbb2e26f70a)
![image](https://github.com/user-attachments/assets/ee5d9590-80e5-4319-b787-417e558298c6)


## Encryption and decryption using AES-CTR mode (counter mode)
### 定義AES-CTR mode (counter mode) 加密函式
其中有三個參數：key為加密用的金鑰、data為要被加密的資料內容、iv為初始化向量，用於起始計數器的值。
![image](https://github.com/user-attachments/assets/e96ee648-64e7-4d7f-bed2-33eb8ae44dbb)

### 呼叫 AES-CTR mode (counter mode) 加密函式
傳入三個引數： key為加密用的金鑰、data為要被加密的資料內容、 iv為初始化向量，用於起始計數器的值。最後得到加密資料和加密花費時間。
再以二進制的方式開啟一個名為AESCTR_CipherFile.txt的檔案並寫入以AES- CTR mode所加密的資料。
最後印出使用AES-CTR mode加密檔案的速度（每秒加密多少data bytes）。
![image](https://github.com/user-attachments/assets/ad16c053-53a3-4a35-a110-53fd3d38c758)
![image](https://github.com/user-attachments/assets/fd324cb1-7e29-49d1-afa2-ab3345c6859c)


### 定義 AES-CTR mode (counter mode) 解密函式
其中有三個參數：key為解密用的金鑰、data為要被解密的資料內容、 iv為初始化向量，用於起始計數器的值。最後得到加密資料和加密花費時間。
![image](https://github.com/user-attachments/assets/715b200a-cfa2-4587-b813-9ec532da837d)

### 呼叫 AES-CTR mode (counter mode) 解密函式
傳入三個引數： key為加密用的金鑰、AESCTR_encryptData為要被解密的已加密資料內容、 iv為初始化向量，用於起始計數器的值。最後得到解密資料。
再開啟一個名為AESCTR_PlaintFile.txt的檔案並寫入以AES-CTR mode所解密的資料。
![image](https://github.com/user-attachments/assets/269d1d6a-e55b-4a24-a052-dacd4f671093)

### 驗證 AES-CTR mode (counter mode) 加解密實作是否正確
若解密後的資料內容和原本的檔案內容相同，則表示加解密實作正確；反之則表示加解密實作有誤。
![image](https://github.com/user-attachments/assets/16b49eb5-a118-45b3-9b34-f5ee0d8604f5)
![image](https://github.com/user-attachments/assets/89f06b29-6ac4-4743-a816-bfff0a967eb9)


## Encryption and decryption using ChaCha20
### 定義ChaCha20加密函式
其中有三個參數：key為加密用的金鑰、data為要被加密的資料內容、nonce為在串流加密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/7d1be430-09b7-48e4-9b70-58e7f5c4915c)

### 呼叫ChaCha20加密函式
傳入三個引數： key為加密用的金鑰、data為要被加密的資料內容、 ChaCha20_nonce為在 ChaCha20加密方法中只使用一次的隨機數，最後得到加密資料和加密花費時間。
再以二進制的方式開啟一個名為 ChaCha20_CipherFile.txt的檔案並寫入以 ChaCha20所加密的資料。
最後印出使用 ChaCha20加密檔案的速度（每秒加密多少data bytes）。
![image](https://github.com/user-attachments/assets/846a2830-a7e9-488c-8b49-6af04253b04a)
![image](https://github.com/user-attachments/assets/a0439e60-91ae-48f0-b02d-ccb9a5a39d8b)

### 定義 ChaCha20解密函式
其中有三個參數：key為解密用的金鑰、data為要被解密的資料內容、nonce為在串流解密上只使用一次的隨機數，用於確保安全。
![image](https://github.com/user-attachments/assets/e33d8c48-f0d7-4905-b7a7-463c48d508a1)

### 呼叫 ChaCha20解密函式
傳入三個引數： key為解密用的金鑰、 ChaCha20_encryptData為要被解密的已加密資料內容、 ChaCha20_nonce為在 ChaCha20解密方法中只使用一次的隨機數，最後得到解密資料。
再開啟一個名為 ChaCha20_PlaintFile.txt的檔案並寫入以 ChaCha20所解密的資料。
![image](https://github.com/user-attachments/assets/1dc9fd8e-56af-49f1-ac69-91fd366e3897)

###　驗證 ChaCha20加解密實作是否正確
若解密後的資料內容和原本的檔案內容相同，則表示加解密實作正確；反之則表示加解密實作有誤。
![image](https://github.com/user-attachments/assets/18104908-416b-4851-8ce3-d0cbcb1e6443)
![image](https://github.com/user-attachments/assets/452e2f00-601d-4a24-ae28-40577700a289)

## Compute the SHA-3-512 message digest of the string "I love cryptography." (without the quotes) and describe the tool or program you used to compute it.
SHA-3-512是SHA-3家族中的一種雜湊算法，產生512-bit的雜湊值。這個雜湊值是對輸入訊息進行高度安全的雜湊後的結果，通常用於確保數據的完整性和安全性， SHA-3-512的雜湊值通常以十六進制形式呈現。
定義了一個函數hash，接收一個參數：string為將進行雜湊的字串。

![image](https://github.com/user-attachments/assets/4ba2ffef-7471-46f4-a006-58753f75c8a7)
![image](https://github.com/user-attachments/assets/798e224e-37b2-4c62-8c86-afa9b84d1015)
![image](https://github.com/user-attachments/assets/2d21c230-9884-420d-b97f-bfff580cc6b3)



