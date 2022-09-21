## Link

Heroku App Link : http://pbp-website.herokuapp.com/mywatchlist/

## Perbedaan JSON, XML, dan HTML

Secara ringkas, HTML berfokus kepada penampilan data dan menjelaskan struktur webpage, XML berfokus kepada transfer dan penyimpanan data, dan JSON merupakan format data yang digunakan dalam aplikasi berbasis JavaScript.

## Mengapa butuh Data Delivery dalam Pengimplementasian Platform?

Agar data yang diminta oleh client dapat disampaikan dengan baik. Data ini nantinya dapat diperbarui, dihapus, dan juga dapat dibuat data-data baru. Implementasi data delivery dapat dilihat dari penggunaan HTML, XML, dan JSON.

## Implementasi Checklist Aplikasi mywatchlist

Saya menggunakan command python manage.py startapp mywatchlist di repo tugas 2 pekan lalu untuk membuat aplikasi baru bernama mywatchlist. Setelah itu, saya membuat format bagi data-data yang akan saya tampilkan di dalam models.py yang ada di direktori mywatchlist. Lalu, saya lakukan perintah makemigrations dan migrate untuk menerapkan skema model ke dalam database Django lokal. Setelah itu, saya membuat data film-film yang telah saya tonton dalam file json bernama initial_watchlist_data.json di folder baru bernama fixtures yang terdapat pada direktori mywatchlist. Lalu, saya masukkan data tersebut ke dalam database Django lokal dengan perintah loaddata. Agar aplikasi dapat di-run dari localhost, saya harus mendaftarkan aplikasi saya dan url-urlnya. Oleh karena itu, saya menambahkan nama aplikasi saya di settings.py yang terdapat pada direktori project_django dan menambahkan path mywatchlist pada file urls.py yang berada di direktori project_django dan juga folder mywatchlist. Agar data dapat ditampilkan dalam tiga format, saya membuat tiga fungsi baru pada views.py yang berada di folder mywatchlist yang masing-masing akan menampilkan data hasil query yang sudah diserialisasi menjadi JSON, XML, dan HTML. Agar fungsi dapat diakses, path beserta url (html/, json/, dan xml/) ditambahkan ke urlpatterns pada urls.py di folder mywatchlist. Lalu, saya mengubah tampilan website pada file mywatchlist.html sesuai dengan keinginan saya dan tentunya dengan menampilkan data juga. File ini terdapat pada folder templates di dalam folder mywatchlist. Setelah semua selesai, saya lakukan “4 mantra” tanpa pull, yaitu git add, commit, dan push ke repositori github saya.

## Postman

![html](/mywatchlist/HTML.jpg)
![json](/mywatchlist/JSON.jpg)
![xml](/mywatchlist/XML.jpg)
