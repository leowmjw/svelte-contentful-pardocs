from pprint import pprint

import malaya
import simplejson as json
from unittest import TestCase
from main import hello_world
from PyPDF2 import PdfFileReader


class TestMyMalaya(TestCase):
    content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."

    def test_sentiment(self):
        print("Sentiment ..")
        # preprocessing = malaya.preprocessing.preprocessing()
        # pprint(' '.join(preprocessing.process(content)))
        tokenizer = malaya.preprocessing.SocialTokenizer().tokenize
        pprint(tokenizer(self.content))

    def test_pos(self):
        pprint(malaya.cluster.cluster_entities(self.content))


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        out = hello_world("bob", 123)
        print(out)
        # msg = '{"message": "Goodbye 123 World!! bob! Sib!!!", "took": 2.3743000000020498e-05}'
        msg = "{'message': 'Goodbye 123 World!! bob! Sib!!!', 'took': 3}"
        data = json.loads(msg)
        print("DATA ==> " + data['message'])
        # self.fail()

    def test_malaya(self):
        content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."
        preprocessing = malaya.preprocessing.preprocessing()
        pprint(preprocessing.process(content))

    def test_pdf(self):
        pread = PdfFileReader(open("/Users/leow/GOMOD/go-pardocs/splitout/par14sesi1-soalan-BukanLisan-3.pdf",  "rb"))

        print(pread.getNumPages())

        pg1 = pread.getPage(0).extractText()
        # pprint(' '.join(pg1.splitlines()).split())
        pg2 = pread.getPage(1).extractText()
        # pprint(pg2)
        # questionpg = ''.join(pg1.splitlines()).split()
        questionpg = ' '.join(''.join(pg1.splitlines()).split())
        questionpg += ' '.join(''.join(pg2.splitlines()).split())

        # finalpg = questionpg.splitlines()
        # pprint(questionpg.split()[12])

        pprint(questionpg)
        print("\n\n\n")
        print(questionpg)
        # pprint(' '.join(finalpg))
