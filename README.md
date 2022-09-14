## Link

Heroku App Link : http://pbp-website.herokuapp.com/katalog/

## Request Client, URL’s, Views, Models, dan HTML

![BAGAN](/static/Flowchart.png)

Website berjalan ketika seseorang mengetik URL-nya. Dalam kasus ini, url yang diketik adalah http://pbp-website.herokuapp.com/katalog/ dengan katalog/ merupakan path-nya. URL yang diketik lalu dikirim ke server Django dan server Django akan mengambil urls.py dari django_project untuk menentukan path/langkah berikutnya. Dalam kasus ini, urls.py dalam django_project akan lanjut ke urls.py di aplikasi katalog karena path katalog/. Langkah selanjutnya dari urls.py merupakan pemanggilan fungsi yang terdapat pada views.py, dalam hal ini show_katalog. Fungsi pada file tersebut mengumpulkan data apa saja yang akan nantinya akan dimasukkan ke file HTML lalu ditampilkan pada website. Dalam fungsi pada file views.py, akan di impor dari models.py ketentuan-ketentuan dan perilaku data yang akan digunakan lalu dikirim ke file HTML akhir. File HTML bernama katalog.html ini akan menampilkan kode serta data dari views.py ke website kembali melalui server Django lalu sampai pada user.

## Virtual Environments dan Apakah Kita Membutuhkannya?

Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer kita. Oleh karena itu, sebenarnya kita tetap dapat membuat aplikasi web berbasis Django apabila package dan dependency yang dimiliki komputer kita sesuai dengan package dan dependency yang dibutuhkan. Apabila tidak sama dan kita mengganti version dependency sesuai dengan kebutuhan satu aplikasi, aplikasi lainnya dapat saja tidak jalan karena membutuhkan dependency yang sama namun berbeda versi.

## Implementasi Poin 1 – 4

Setelah github repository yang dijadikan template di-clone, saya membuat virtual environment di dalam direktorinya yang sudah ada di dalam komputer saya. Lalu saya meng-install dependencies yang terdapat pada requirements.txt agar aplikasi dapat berjalan dengan lancar. Setelah itu, dengan manage.py saya jalankan command runserver agar website awal dapat dilihat di localhost. Langkah-langkah tadi merupakan permulaan dari dibangunnya website. Lalu, saya meng-edit file-file yang sudah tersedia.

Saya membuat fungsi show_katalog pada views.py. Fungsi ini memuat variabel-variabel yang akan digunakan pada katalog.html termasuk objek-objek yang terdapat pada katalog.models yang saya impor. File models.py berisi ketentuan dan perilaku data yang akan saya gunakan. Dengan return render, value pada dictionary context akan ditambahkan pada template (katalog.html) context. Namun, fungsi ini tidak akan jalan dan bahkan aplikasi ini tidak akan jalan apabila tidak dipetakan menggunakan routing. Oleh karena itu, saya membuka urls.py pada aplikasi katalog dan mengimpor path serta fungsi show_katalog terlebih dahulu lalu menambahkan app_name berupa katalog dan menambahkan urlpatters berisi nama fungsi yang akan dijalankan apabila path dijalankan. Agar data dapat ditampilkan, file HTML harus saya edit. Setelah semua file telah diedit, saya memberhentikan servernya lalu menjalankan command makemigrations dan migrate. Setelah itu, tetap dengan manage.py, saya runserver kembali dan setelah localhost dibuka dengan path katalog, semua data tertampil dengan benar. Terakhir, saya memberhentikan server sekali lagi untuk git add, commit, dan push ke repository pada github.

Lalu, saya membuat aplikasi baru pada heroku dan menyalin nama serta API key dari aplikasi tersebut. Nama serta API key dari aplikasi tersebut dijadikan repository secret pada repository github saya. Setelah itu, saya jalankan lagi semua workflow yang gagal. Aplikasi heroku selesai.
