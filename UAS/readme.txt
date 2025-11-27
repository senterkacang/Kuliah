**************************************************************
                    PENJELASAN PROGRAM
            Angga Satriawan Aldi (22538141005)
**************************************************************

Semua algoritma Jaringan Syaraf Tiruan (Neural Network) ada 
di dalam file "network.py" dengan menggunakan metode
Backpropagation.


"load_n_train_data.ipynb" dipakai untuk load dataset dari
sklearn (iris_dataset), kemudian train dataset tersebut
dan di save modelnya ke dalam file terpisah (untuk program ini
saya save dengan nama "iris_nn_model.pkl", dengan training 
parameter epoch=600, learning rate=0.1, dan mini_batch_size=10).
Dengan parameter tersebut saya dapatkan hasil training sebesar
30/30 di epoch terakhir.


Untuk menguji model hasil training bisa menggunakan program
"run_model.py". Untuk variabel input sample = [var1_len, 
var1_width, var2_len, var2_width] bisa diubah nilainya 
untuk pengetesan.



Urutan proses dari awal:
1. Load dataset "iris_dataset" dari sklearn
2. Menampilkan isi dataset untuk di cek dulu
3. Inisialisasi konfigurasi Neural Network. Saya gunakan
   konfigurasi 3 layer NN dengan 2 x 20 neuron di hiden layer
   dan 3 neuron di output.
4. Lakukan training dataset dengan fungsi train yang sudah
   dibuat untuk menghasilkan weight dan bias yang cocok dan
   sesuai dengan konfigurasi NN.
5. Save model hasil training ke dalam file.
6. Test model dengan menggunakan input dari user.