# Langkah-langkah:

1. Buat Environment Python 'conda create -n "nama_env" python=3.11'
2. Aktifkan Environment Yang Dibuat 'conda activate nama_env
![Buat env dan aktifkan](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/c067d75a-f195-43e0-adfa-5800c8dce524)
3. Jalankan app.py
![jalankan python app py](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/f9ea8268-4bfc-4125-a498-ade8c0ba1020)
4. Buka Browser Localhost:5000/data untuk melihat data yang muncul
![app py localhost data](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/6def0c34-8635-4035-af93-a850babc13ab)
5. Localhost:5000/metrics untuk melihat RMSE DAN R2
![app py localhost metric](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/9cec54b4-54b0-4d53-8353-0462554608d4)
6. Localhost:5000/predict-advertising?sales=50 untuk melihat data prediksi 50
![app py localhost sales 50](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/7e1bc362-7430-4163-b09a-2a6fed597675)
7. Localhost:5000/predict-advertising?sales=100 untuk melihat data prediksi 100
![app py localhost sales 100](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/86421ff4-315d-46e0-b509-88ff3260ae9e)
8. Localhost:5000/predict-advertising?sales=150 untuk melihat data prediksi 150
![app py localhost sales 150](https://github.com/ZidanAliZaqi/Machine_Learning_II/assets/97864880/cc96b6fc-06f3-4bea-8ba7-db9e0b082e07)

# Interpretasi
Model ini memiliki RMSE sebesar 15.019 dan R² score sebesar 0.271. RMSE yang tinggi menunjukkan bahwa prediksi model memiliki kesalahan rata-rata sekitar 15 juta dolar, yang cukup signifikan. R² score sebesar 0.271 mengindikasikan bahwa model hanya mampu menjelaskan sekitar 27.1% dari variabilitas dalam biaya iklan, menunjukkan bahwa banyak faktor lain yang mempengaruhi biaya iklan yang tidak ditangkap oleh model ini. Secara keseluruhan, ini mengindikasikan bahwa model memiliki kinerja yang kurang baik dalam memprediksi biaya iklan berdasarkan penjualan.

Prediksi biaya iklan untuk mencapai 50, 100, dan 150 penjualan adalah masing-masing $66.20 juta, $143.43 juta, dan $220.66 juta. Meskipun memberikan gambaran kasar tentang biaya yang diperlukan, akurasi prediksi ini dipertanyakan karena tingginya nilai RMSE dan rendahnya R² score. Oleh karena itu, prediksi ini sebaiknya digunakan sebagai estimasi awal yang harus ditindaklanjuti dengan analisis lebih mendalam dan pertimbangan faktor-faktor tambahan sebelum membuat keputusan bisnis yang signifikan terkait anggaran iklan.
