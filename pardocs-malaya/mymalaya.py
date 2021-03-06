from pprint import pprint

import malaya


def test_emotion():
    content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."

    pprint(malaya.emotion.available_deep_model())

    emo = malaya.emotion.multinomial()
    pprint(emo.predict(content, get_proba = True))

    # Why CHina?
    emo_xgb = malaya.emotion.xgb()
    pprint(emo_xgb.predict(content, get_proba = True))

    # Deep models should  be much better
    emo_sparse_model = malaya.emotion.sparse_deep_model()
    pprint(emo_sparse_model.predict(content, get_proba = True))

    # Multiple at once
    print("================ COMBO =======================\n")
    # sa_emo = malaya.emotion.deep_model('self_attention')
    bahdanau_emo = malaya.emotion.deep_model('bahdanau')
    luong_emo = malaya.emotion.deep_model('luong')
    pprint(malaya.stack.predict_stack([emo, emo_xgb, bahdanau_emo, luong_emo], content))




def test_similiarity():
    content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."
    # pprint(malaya.topic.calon)
    pprint(malaya.similarity.available_deep_siamese())
    pprint(malaya.similarity.fuzzy_location(content))
    # Above useful for detecting parliamentariean?
    # {'dun': ['bandar', 'nilai', 'banggi', 'ladang'],
    #  'negeri': [],
    #  'parlimen': ['kudat', 'bakri']}
    ft = malaya.similarity.fuzzy(malaya.topic.topic)
    pprint(ft.get_similarity(content))
    fi = malaya.similarity.fuzzy(malaya.topic.influencer)
    pprint(fi.get_similarity(content))


def test_sentiment():
    content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."
    bahdanau = malaya.sentiment.deep_model('bahdanau')
    luong = malaya.sentiment.deep_model('luong')
    attention = malaya.sentiment.deep_model('self-attention')
    # ftc = malaya.sentiment.sparse_deep_model('fast-text-char') # Does not  seem to load ..
    multinomial = malaya.sentiment.multinomial()
    res = malaya.stack.predict_stack([bahdanau, luong, attention, multinomial], content)
    pprint(res)
    pprint(malaya.sentiment.available_deep_model())
    pprint(malaya.sentiment.available_sparse_deep_model())


def test_pos():
    # malaya.describe_pos()
    # malaya.describe_entities()
    content = "NO SOALAN : 3 1 PEMBERITAHUAN PERTANYAAN BUKAN LISAN DEWAN RAKYAT PERTANYAAN : BUKAN LISAN DARIPADA : DATUK ABD RAHIM BIN BAKRI [ KUDAT ] NO. SOALAN : 3 minta MENTERI PEMBANGUNAN LUAR BANDAR menyatakan apakah hala tuju dan masa depan projek agropolitan Pulau Banggi. Apakah tanaman getah projek tersebut telah mengeluarkan hasil dan berapakah anggaran hasil yang telah diperoleh daripada projek tersebut dan apakah para peneroka telah menikmati sebahagian daripada hasil tersebut. JAWAPAN Untuk makluman Ahli Yang Berhormat, komponen projek Agropolitan Pulau Banggi terdiri daripada penempatan dan ladang sejahtera. Sebanyak 100 buah rumah telah siap dibina dan telah diduduki di bawah Fasa 1, manakala sebanyak 36 buah rumah sedang dalam peringkat pelaksanaan di bawah Fasa 2. Bagi komponen ladang sejahtera, seluas 544 hektar telah ditanam sepenuhnya dengan tanaman getah dan daripada jumlah tersebut, seluas 200 hektar telah ditoreh secara berperingkat. Seramai 52 penduduk telah bekerja di ladang sejahtera ini dengan anggaran purata pendapatan antara RM800 hingga RM1,200 sebulan bergantung kepada bilangan hari bekerja. Projek tanaman getah ini telah mula berhasil pada tahun 2017 dengan jumlah 82,600 kg berat kering dengan nilai RM498,000 dan pada tahun 2018, jumlah hasil yang dikeluarkan adalah sebanyak 112,158kg berat kering dengan nilai RM448,000. Pada masa ini, pihak FELCRA BerhadNO SOALAN : 3 2 sedang melaksanakan kerja-kerja penyelenggaraan di kawasan selebihnya seluas 344 hektar dan dijangka akan ditoreh sepenuhnya pada tahun 2023. Merujuk kepada halu tuju Agropolitan Pulau Banggi, pihak Kementerian Pembangunan Luar Bandar bercadang untuk melaksanakan projek ternakan lembu di atas tanah seluas 1,000 hektar yang tidak dapat diusahakan dengan tanaman getah bagi memberi pendapatan tambahan kepada peserta. Bagi memberi kemudahan dan keselesaan kepada penduduk di Pulau Banggi, Kementerian juga telah menyediakan pelbagai kemudahan antaranya seperti jeti, jalan dan perparitan, kemudahan elektrik dan air, kemudahan sosial melibatkan surau, pusat kegiatan desa dan tadika termasuk gerai dan ruang niaga untuk usahawan tempatan."
    bahdanau_entities = malaya.entity.deep_model('bahdanau')
    bahdanau_pos = malaya.pos.deep_model('bahdanau')
    print("+++++++++++++========== ENT ------\n")
    # result_entities = bahdanau_entities.predict(content)
    # pprint(result_entities)
    pprint(bahdanau_entities.analyze(content))
    print("==========POS +++++++++++\n")
    # result_pos = bahdanau_pos.predict(content)
    # pprint(result_pos)
    pprint(bahdanau_pos.analyze(content))
    # print("xxxx CRF yyyyy\n")
    # crf = malaya.pos.crf()
    # pprint(crf.predict(content))
    # pprint(crf.analyze(content))
    print("*** fEATURES ****")
    bahdanau_entities.print_features(5)
    bahdanau_entities.print_transitions(5)
    bahdanau_pos.print_features(5)
    bahdanau_pos.print_transitions(5)
    malaya.generator.sentence_ngram()


def test_preprocess():
    content = "abc def hello"
    string_4 = 'aahhh, malasnye nak pegi keje harini #mondayblues'
    preprocessing = malaya.preprocessing.preprocessing()
    pprint(preprocessing.process(string_4))
    # pprint(malaya.preprocessing.get_normalize())
    # tokenizer = malaya.preprocessing.SocialTokenizer().tokenize
    # pprint(tokenizer(string_4))


def main():
    print("Hello Malaya!!  " + malaya.home)
    malaya.print_cache()
    # corpus = ["bob", "dude"]
    # pprint(malaya.pos.available_deep_model())
    # test_preprocess()
    # test_pos()
    # test_sentiment()
    # test_similiarity()
    test_emotion()


if __name__ == "__main__":
    main()