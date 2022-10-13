## Link

Heroku App Link : http://pbp-website.herokuapp.com/todolist/

## Perbedaan Asynchronous dan Synchronous Programming

Synchronous menjadikan laman responsif dan data dapat diupdate tanpa diharuskan refresh, sedangkan asynchronous tidak responsif dan harus refresh seluruh laman terlebih dahulu.

## Paradigma Event-Driven Programming

Event-Driven Programming merupakan paradigma dimana objek, action pengguna, ataupun yang lainnya dapat berkomunikasi secara tidak langsung satu dengan yang lainnya. Apabila suatu program menerapkan paradigma ini, program akan berjalan berdasarkan event atau action pengguna. Salah satu penerapan paradigma ini di todolist adalah pemanggilan fungsi modal untuk membuat task baru.

## Penerapan Asynchronous Programming pada AJAX

Secara prinsip, AJAX tidak memerlukan refresh seluruh laman untuk mengambil dan menaruh data pada database. Oleh karena itu, AJAX termasuk asynchronous programming.

## Pengimplementasian Checklist

Pertama, saya buat views untuk menampilkan data json dari todolist saya. Lalu, dengan menggunakan ajax pada todolist.html, saya mengambil data json tersebut. Kodenya terdapat diantara tag script. Data json kita ambil dari form yang terdapat dalam modal di todolist.html kita. Form tersebut juga akan melakukan operasi ajax yang fungsinya terdapat pada views dimana input dari form tersebut akan membuat objek baru dalam database kita. Lalu, data json akan kita olah pada todolist.html dengan cara menampilkannya di halaman tersebut. Terakhir, kita harus membuat path agar semua fungsi dapat berjalan satu dengan yang lain.
