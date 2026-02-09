import time
import random

class Pemain:
    def __init__(self, nama, difficulty="normal"):
        self.nama = nama
        self.difficulty = difficulty
        self.nyawa_max = 20
        self.nyawa = 20
        self.serangan = 12
        self.pertahanan = 5
        self.level = 1
        self.pengalaman = 0
        self.pengalaman_max = 100
        self.potion = 0
        self.input_salah_berturut = 0
        
        # Difficulty modifier
        if difficulty == "easy":
            self.nyawa_max += 10
            self.nyawa += 10
            self.pertahanan += 5
        elif difficulty == "hard":
            self.nyawa_max -= 5
            self.nyawa -= 5
            self.serangan -= 3
        
    def serang(self):
        return random.randint(self.serangan - 5, self.serangan + 10)
    
    def bertahan(self, durasi=1):
        return self.pertahanan * 2
    
    def skill_khusus(self):
        return random.randint(self.serangan + 5, self.serangan + 20)
    
    def ambil_damage(self, damage):
        damage_final = max(1, damage - self.pertahanan)
        self.nyawa -= damage_final
        return damage_final
    
    def gunakan_potion(self):
        if self.potion > 0:
            penyembuhan = self.nyawa_max // 2
            self.nyawa = min(self.nyawa + penyembuhan, self.nyawa_max)
            self.potion -= 1
            return penyembuhan, True
        return 0, False
    
    def dapatkan_potion(self, jumlah=1):
        self.potion += jumlah
    
    def dapatkan_pengalaman(self, exp):
        self.pengalaman += exp
        if self.pengalaman >= self.pengalaman_max:
            self.level_up()
    
    def level_up(self):
        self.pengalaman = 0
        self.level += 1
        self.nyawa_max += 10
        self.nyawa = self.nyawa_max
        self.serangan += 5
        self.pertahanan += 5
        print(f"\n{'*'*40}")
        print(f"⭐ LEVEL UP! {self.nama} mencapai Level {self.level}!")
        print(f"{'*'*40}")
        print(f"  Nyawa Max: {self.nyawa_max}")
        print(f"  Serangan: {self.serangan}")
        print(f"  Pertahanan: {self.pertahanan}\n")
        time.sleep(1)
    
    def tampilkan_status(self):
        print(f"\n{'='*50}")
        print(f"STATUS {self.nama}")
        print(f"{'='*50}")
        print(f"  Level: {self.level}")
        print(f"  Nyawa: {self.nyawa}/{self.nyawa_max}")
        print(f"  Serangan: {self.serangan}")
        print(f"  Pertahanan: {self.pertahanan}")
        print(f"  Pengalaman: {self.pengalaman}/{self.pengalaman_max}")
        print(f"  Potion: {self.potion}")
        print(f"{'='*50}\n")

class Musuh:
    def __init__(self, nama, nyawa_max, serangan, pengalaman):
        self.nama = nama
        self.nyawa = nyawa_max
        self.nyawa_max = nyawa_max
        self.serangan = serangan
        self.pengalaman = pengalaman
        
    def serang(self):
        return random.randint(self.serangan - 2, self.serangan + 8)
    
    def ambil_damage(self, damage):
        self.nyawa -= damage
        return damage

class Boss:
    def __init__(self, nama, nyawa_max, serangan):
        self.nama = nama
        self.nyawa = nyawa_max
        self.nyawa_max = nyawa_max
        self.serangan = serangan
        
    def serang(self):
        return random.randint(self.serangan - 5, self.serangan + 20)
    
    def ambil_damage(self, damage):
        self.nyawa -= damage
        return damage


def cerita_pembukaan(pemain):
    print(f"\n{'='*60}")
    print("         🌍 SELAMAT DATANG KE DUNIA DARVINTOS 🌍")
    print(f"{'='*60}\n")
    
    print(f"🧙 Halo {pemain.nama}!")
    time.sleep(1)
    
    difficulty_text = {"easy": "🟢 EASY", "normal": "🟡 NORMAL", "hard": "🔴 HARD"}
    print(f"\n⚔️  Mode Kesulitan: {difficulty_text[pemain.difficulty]}")
    time.sleep(1)
    
    print("\n⚔️  Anda adalah seorang petualang pemberani yang baru saja tiba di kota kecil bernama Ashvale.")
    time.sleep(1)
    print("🌑 Kota ini pernah makmur, namun sekarang tenggelam dalam kegelapan dan ketakutan.\n")
    time.sleep(1)
    
    print("📖 Penduduk kota menceritakan legend yang mengerikan:")
    time.sleep(1)
    print('🔴 Dahulu kala, seorang naga raksasa berwarna MERAH bernama PYRAXION')
    time.sleep(1)
    print("⚡ menguasai langit dan membawa kehancuran ke seluruh kerajaan.")
    time.sleep(1)
    print("⚔️  Akan tetapi, para pahlawan masa lalu berhasil mengusirnya jauh ke sebuah kastil tua")
    time.sleep(1)
    print("🏔️  yang tersembunyi di Gunung Sulfur yang berbau belerang.\n")
    time.sleep(1)
    
    print("📊 Status Awal Pemain:")
    pemain.tampilkan_status()

def petualangan_awal(pemain):
    print("\n🚀 --- PETUALANGAN DIMULAI --- 🚀\n")
    time.sleep(1)
    
    print(f"🌲 {pemain.nama}, Anda memasuki hutan gelap di luar kota Ashvale.")
    time.sleep(1)
    print("🌳 Pohon-pohon besar menutup cahaya matahari.")
    time.sleep(1)
    print("👻 Suara aneh bergema di sekitar Anda...\n")
    time.sleep(1)
    
    print("🗺️  Anda menemukan beberapa jalan:")
    print("1. 🕳️  Jalan ke kanan menuju Gua Gelap (berbahaya)")
    print("2. 🏘️  Jalan ke depan menuju Desa Tua (aman)")
    print("3. ⛪ Jalan ke kiri menuju Kuil Kuno (misteri)")
    print("4. 🌲 Jalan ke utara menuju Hutan Misterius (sangat berbahaya)")
    print("5. 🏰 Jalan ke selatan menuju Menara Tua (menantang)")
    print("6. 🌊 Jalan ke tenggara menuju Danau Gelap (tidak diketahui)\n")
    
    pilihan = input_validasi(pemain, 1, 6)
    if pilihan is None:
        return
    
    if pilihan == "1":
        petualangan_gua_gelap(pemain)
    elif pilihan == "2":
        petualangan_desa_tua(pemain)
    elif pilihan == "3":
        petualangan_kuil_kuno(pemain)
    elif pilihan == "4":
        petualangan_hutan_misterius(pemain)
    elif pilihan == "5":
        petualangan_menara_tua(pemain)
    elif pilihan == "6":
        petualangan_danau_gelap(pemain)

def input_validasi(pemain, min_val, max_val):
    """Validasi input pemain dengan counter 3 kali salah = mati"""
    while True:
        pilihan = input(f"Pilihan Anda ({min_val}-{max_val}): ")
        if pilihan.isdigit() and min_val <= int(pilihan) <= max_val:
            pemain.input_salah_berturut = 0  # Reset counter
            return pilihan
        else:
            pemain.input_salah_berturut += 1
            print(f"\n❌ Input tidak valid! ({pemain.input_salah_berturut}/3)\n")
            
            if pemain.input_salah_berturut >= 3:
                print(f"{'='*60}")
                print("⚠️  ANDA TERLALU BINGUNG DAN TERSESAT DI HUTAN!")
                print(f"{'='*60}")
                print(f"Karena kebingungan yang ekstrem, {pemain.nama} pingsan dan tidak bangun lagi...")
                print(f"Petualangan Anda berakhir di sini.\n")
                return None

def pilih_jalur(pemain, fungsi_next):
    """Menampilkan pilihan jalur setelah setiap battle"""
    print("\n" + "="*60)
    print("🚪 ANDA TIBA DI PERCABANGAN JALAN 🚪")
    print("="*60 + "\n")
    
    jalur_options = [
        ("☀️  Jalan terang ke kanan", "cerah dan aman"),
        ("🌑 Jalan gelap ke depan", "penuh misteri"),
        ("🧗 Jalan berbatu ke kiri", "penuh tantangan")
    ]
    
    print("Anda menemukan tiga jalur berbeda:\n")
    for i, (nama, deskripsi) in enumerate(jalur_options, 1):
        print(f"{i}. {nama} ({deskripsi})")
    print()
    
    pilihan = input_validasi(pemain, 1, 3)
    if pilihan is None:
        return
    
    time.sleep(1)
    
    if pilihan == "1":
        print("\n☀️  Anda memilih jalan yang terang dan mudah...")
        print("✨ Semoga keputusan ini membawa Anda lebih dekat ke tujuan.\n")
    elif pilihan == "2":
        print("\n🌑 Anda memilih jalan yang gelap dan penuh misteri...")
        print("👀 Sensasi kesadaran meningkat saat Anda berjalan.\n")
    elif pilihan == "3":
        print("\n🧗 Anda memilih jalan berbatu yang menantang...")
        print("💪 Tantangan membuat Anda semakin kuat.\n")
    
    time.sleep(1)
    fungsi_next(pemain)

def tanya_minum_potion(pemain):
    """Tanya pemain apakah ingin minum potion setelah battle"""
    if pemain.potion > 0 and pemain.nyawa < pemain.nyawa_max:
        print()
        while True:
            tanya = input(f"Anda memiliki {pemain.potion} Potion. Ingin meminum? (Y/N): ").upper().strip()
            if tanya == "Y":
                penyembuhan, berhasil = pemain.gunakan_potion()
                if berhasil:
                    print(f"\n🧪 Anda meminum Potion!")
                    print(f"✨ Penyembuhan: +{penyembuhan} Nyawa")
                    print(f"Nyawa sekarang: {pemain.nyawa}/{pemain.nyawa_max}")
                    print(f"Potion tersisa: {pemain.potion}\n")
                break
            elif tanya == "N":
                print()
                break
            else:
                print("❌ Input tidak valid! Masukkan Y atau N.\n")

def petualangan_gua_gelap(pemain):
    print("\n🕳️  --- GUA GELAP --- 🕳️\n")
    time.sleep(1)
    print(f"💨 {pemain.nama} memasuki gua yang lembab dan gelap.")
    time.sleep(1)
    print("👁️  Mata Anda beradaptasi dengan kegelapan...")
    time.sleep(1)
    print("⚔️  Tiba-tiba, seekor GOBLIN BERSENJATA muncul dari ceruk batu!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Goblin Prajurit", 20, 6, 30):
        print("\nAnda mengalahkan Goblin dan menemukan Artefak Kuno!")
        bonus_serangan = random.randint(1, 5)
        pemain.serangan += bonus_serangan
        print(f"Serangan Anda meningkat! [+{bonus_serangan} Serangan]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        petualangan_lanjutan_1(pemain)
    else:
        game_over(pemain)

def petualangan_desa_tua(pemain):
    print("\n🏘️  --- DESA TUA --- 🏘️\n")
    time.sleep(1)
    print(f"👨 {pemain.nama} memasuki desa yang sudah ditinggalkan.")
    time.sleep(1)
    print("🏚️  Rumah-rumah terlihat kosong dan rusak.")
    time.sleep(1)
    print("💎 Sebuah peti harta karun bersinar di depan Anda!\n")
    time.sleep(1)
    
    print("Anda membuka peti dan menemukan:")
    bonus_nyawa = random.randint(1, 5)
    bonus_serangan = random.randint(1, 5)
    print(f"🧪 Potion Kesehatan (siap untuk diminum) [+{bonus_nyawa} Potion]")
    print(f"⚔️  Pedang Perak [+{bonus_serangan} Serangan]\n")
    pemain.dapatkan_potion(bonus_nyawa)
    pemain.serangan += bonus_serangan
    pemain.tampilkan_status()
    time.sleep(1)
    
    print("Dengan item baru, Anda merasa lebih siap untuk melanjutkan perjalanan...")
    petualangan_lanjutan_1(pemain)

def petualangan_kuil_kuno(pemain):
    print("\n⛪ --- KUIL KUNO --- ⛪\n")
    time.sleep(1)
    print(f"🙏 {pemain.nama} memasuki kuil yang penuh dengan patung-patung aneh.")
    time.sleep(1)
    print("✨ Cahaya mistis menerangi setiap sudut...")
    time.sleep(1)
    print("😈 Seorang PENDETA IBLIS muncul dan menyerangnya!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Pendeta Iblis", 28, 7, 40):
        print("\nAnda mengalahkan Pendeta Iblis!")
        print("Anda mendapat Sihir Perlindungan!")
        bonus_pertahanan = random.randint(1, 5)
        pemain.pertahanan += bonus_pertahanan
        print(f"Pertahanan Anda meningkat! [+{bonus_pertahanan} Pertahanan]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        petualangan_lanjutan_1(pemain)
    else:
        game_over(pemain)

def petualangan_hutan_misterius(pemain):
    print("\n🌲 --- HUTAN MISTERIUS --- 🌲\n")
    time.sleep(1)
    print(f"🌳 {pemain.nama} memasuki hutan yang penuh dengan pohon-pohon raksasa dan asap gelap.")
    time.sleep(1)
    print("🎵 Suara irama aneh bergema di seluruh tempat...")
    time.sleep(1)
    print("🪄 Tiba-tiba muncul PENYIHIR HUTAN yang dipenuhi energi gelap!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Penyihir Hutan", 32, 9, 50):
        print("\nAnda mengalahkan Penyihir Hutan!")
        bonus_potion = random.randint(1, 5)
        print(f"🧪 Anda menemukan {bonus_potion} Potion Kehidupan!")
        pemain.dapatkan_potion(bonus_potion)
        print(f"Potion ditambahkan! [+{bonus_potion} Potion]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        petualangan_lanjutan_1(pemain)
    else:
        game_over(pemain)

def petualangan_menara_tua(pemain):
    print("\n🏰 --- MENARA TUA --- 🏰\n")
    time.sleep(1)
    print(f"🏛️  {pemain.nama} menemukan menara kuno yang menjulang tinggi.")
    time.sleep(1)
    print("🌑 Aura kegelapan memancar dari pintu masuknya...")
    time.sleep(1)
    print("⚔️  Seorang KSATRIA JATUH yang dikurung di sini menyerang Anda!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Ksatria Jatuh", 36, 10, 55):
        print("\nAnda mengalahkan Ksatria Jatuh!")
        bonus_serangan = random.randint(1, 5)
        bonus_potion = random.randint(1, 5)
        pemain.serangan += bonus_serangan
        pemain.dapatkan_potion(bonus_potion)
        print(f"⚔️  Pedang Legendary [+{bonus_serangan} Serangan]")
        print(f"🧪 Potion Kehidupan [+{bonus_potion} Potion]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        petualangan_lanjutan_1(pemain)
    else:
        game_over(pemain)

def petualangan_danau_gelap(pemain):
    print("\n🌊 --- DANAU GELAP --- 🌊\n")
    time.sleep(1)
    print(f"💧 {pemain.nama} tiba di sebuah danau yang airnya berwarna gelap dan menakutkan.")
    time.sleep(1)
    print("🌫️  Kabut tebal menutupi permukaan air...")
    time.sleep(1)
    print("👹 Tiba-tiba, seekor MAKHLUK AKUATIK yang mengerikan muncul dari dalam danau!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Makhluk Air Gelap", 40, 10, 60):
        print("\nAnda mengalahkan Makhluk Air! Perairan kembali tenang.")
        bonus_pertahanan = random.randint(1, 5)
        bonus_potion = random.randint(1, 5)
        pemain.pertahanan += bonus_pertahanan
        pemain.dapatkan_potion(bonus_potion)
        print(f"💎 Perhiasan Kuno [+{bonus_pertahanan} Pertahanan]")
        print(f"🧪 Potion Kehidupan [+{bonus_potion} Potion]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        petualangan_lanjutan_1(pemain)
    else:
        game_over(pemain)

def petualangan_lanjutan_1(pemain):
    print("\n🐺 --- HUTAN DALAM --- 🐺\n")
    time.sleep(1)
    print(f"🌲 {pemain.nama} melanjutkan perjalanan ke dalam hutan yang semakin gelap.")
    time.sleep(1)
    print("👁️  Anda melihat mata merah bersinar di antara semak-semak!")
    time.sleep(1)
    print("🐺 Sekelompok SERIGALA LIAR menyerbu Anda!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Serigala Liar", 22, 7, 40):
        print("\nAnda berhasil mengalahkan Serigala Liar!")
        pemain.dapatkan_pengalaman(40)
        tanya_minum_potion(pemain)
        time.sleep(1)
        pilih_jalur(pemain, petualangan_lanjutan_2)
    else:
        game_over(pemain)

def petualangan_lanjutan_2(pemain):
    print("\n🌉 --- JEMBATAN TERKUTUK --- 🌉\n")
    time.sleep(1)
    print(f"⛓️  {pemain.nama} tiba di sebuah jembatan tua di atas jurang yang dalam.")
    time.sleep(1)
    print("💨 Angin bertiup kencang menggoyang struktur jembatan...")
    time.sleep(1)
    print("👹 Tiba-tiba, sesuatu yang besar muncul dari kegelapan!")
    time.sleep(1)
    print("✌️  Seekor TROLL RAKSASA melintang di jembatan!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Troll Raksasa", 35, 9, 60):
        print("\nAnda mengalahkan Troll! Jembatan aman untuk dilalui.")
        pemain.dapatkan_pengalaman(60)
        tanya_minum_potion(pemain)
        time.sleep(1)
        pilih_jalur(pemain, petualangan_lanjutan_3)
    else:
        game_over(pemain)

def petualangan_lanjutan_3(pemain):
    print("\n👻 --- HUTAN MISTIS --- 👻\n")
    time.sleep(1)
    print(f"🌙 {pemain.nama} memasuki hutan yang penuh cahaya aneh dan mistis.")
    time.sleep(1)
    print("✨ Pohon-pohon bersinar dengan cahaya biru di malam hari.")
    time.sleep(1)
    print("👁️  Anda merasakan kehadiran spiritual yang kuat...")
    time.sleep(1)
    print("⚔️  HANTU PRAJURIT dari era kuno muncul!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Hantu Prajurit", 30, 8, 50):
        print("\nAnda menghancurkan Hantu dan membebaskan jiwanya.")
        pemain.dapatkan_pengalaman(50)
        bonus_pertahanan = random.randint(1, 5)
        pemain.pertahanan += bonus_pertahanan
        print(f"[+{bonus_pertahanan} Pertahanan]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        pilih_jalur(pemain, petualangan_lanjutan_4)
    else:
        game_over(pemain)

def petualangan_lanjutan_4(pemain):
    print("\n🪄 --- MARKAS MUSUH GELAP --- 🪄\n")
    time.sleep(1)
    print(f"😈 {pemain.nama} menemukan markas para penyihir gelap yang melayani Pyraxion.")
    time.sleep(1)
    print("🏚️  Bangunan tua dengan patung-patung menakutkan berdiri di hadapan Anda.")
    time.sleep(1)
    print("😠 Seorang PENYIHIR HITAM keluar dari pintu, mata bersinar merah ganas!")
    time.sleep(1)
    print("🔥 Ia mengeluarkan kutukan dan api gelap!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Penyihir Hitam", 40, 10, 70):
        print("\nAnda mengalahkan Penyihir Hitam! Kekuatan gelap mulai melemah.")
        pemain.dapatkan_pengalaman(70)
        bonus_serangan = random.randint(1, 5)
        pemain.serangan += bonus_serangan
        print(f"[+{bonus_serangan} Serangan]\n")
        tanya_minum_potion(pemain)
        time.sleep(1)
        pilih_jalur(pemain, petualangan_lanjutan_5)
    else:
        game_over(pemain)

def petualangan_lanjutan_5(pemain):
    print("\n🔴 --- TANDUK GUNUNG SULFUR --- 🔴\n")
    time.sleep(1)
    print(f"⛰️  {pemain.nama} mendaki menuju puncak Gunung Sulfur.")
    time.sleep(1)
    print("🔥 Suhu semakin panas, bau belerang semakin menyengat.")
    time.sleep(1)
    print("🐉 Ketika hampir sampai puncak, sesuatu yang massive muncul!")
    time.sleep(1)
    print("🔴 NAGA KECIL MERAH, anaknya Pyraxion, menyerang Anda!\n")
    time.sleep(1)
    
    if pertarungan_dengan_aksi(pemain, "Naga Kecil Merah", 45, 12, 80):
        print("\nAnda mengalahkan Naga Kecil! Jalan menuju Pyraxion terbuka!")
        pemain.dapatkan_pengalaman(80)
        pemain.nyawa = pemain.nyawa_max
        print(f"Nyawa Anda dipulihkan sepenuhnya!")
        pemain.tampilkan_status()
        tanya_minum_potion(pemain)
        time.sleep(1)
        pilih_jalur(pemain, lanjut_ke_kastil)
    else:
        game_over(pemain)

def lanjut_ke_kastil(pemain):
    print("\n🏰 --- MEMASUKI KASTIL PYRAXION --- 🏰\n")
    time.sleep(1)
    print("⚔️  Setelah mengalahkan semua musuh, Anda akhirnya sampai di depan Kastil Batu raksasa!")
    time.sleep(1)
    print("🚪 Gerbang kastil terbuka perlahan-lahan dengan suara yang menggema...")
    time.sleep(1)
    print("🔊 Dan dalam gelapnya, Anda mendengar grutuan yang menggelegar...\n")
    time.sleep(1)
    
    print("🐉 Tiba-tiba, sosok raksasa merah bersayap meluncur keluar!")
    time.sleep(1)
    print("💯 PYRAXION, NAGA MERAH YANG LEGENDARIS TELAH MEMBANGKITKAN DIRI!\n")
    time.sleep(1)
    
    pertarungan_boss(pemain)

def pertarungan_dengan_aksi(pemain, nama_musuh, nyawa_musuh, serangan_musuh, exp_reward):
    print(f"\n{'='*60}")
    print(f"⚔️  PERTARUNGAN: {pemain.nama} LV{pemain.level} vs {nama_musuh}")
    print(f"{'='*60}\n")
    
    musuh = Musuh(nama_musuh, nyawa_musuh, serangan_musuh, exp_reward)
    putaran = 1
    sedang_bertahan = False
    input_salah_count = 0
    skill_sudah_digunakan = False
    
    while pemain.nyawa > 0 and musuh.nyawa > 0:
        print(f"\n--- PUTARAN {putaran} ---")
        print(f"{pemain.nama} Nyawa: {pemain.nyawa}/{pemain.nyawa_max}")
        print(f"{nama_musuh} Nyawa: {musuh.nyawa}/{musuh.nyawa_max}\n")
        
        # Menu Aksi Pemain
        print("Pilih Aksi:")
        print("1. ⚔️  Menyerang  (Damage tinggi)")
        print("2. 🛡️  Bertahan   (Kurangi damage)")
        if skill_sudah_digunakan:
            print("3. ✨ Skill Khusus (⛔ Sudah digunakan)")
        else:
            print("3. ✨ Skill Khusus (Damage sangat tinggi)")
        if pemain.potion > 0:
            print(f"4. 🧪 Minum Potion ({pemain.potion} tersedia)")
        
        max_aksi = 4 if pemain.potion > 0 else 3
        prompt_text = f"\nPilihan (1-{max_aksi}): " if pemain.potion > 0 else "\nPilihan (1-3): "
        aksi = input(prompt_text)
        
        # Validasi input
        if not aksi.isdigit() or int(aksi) < 1 or int(aksi) > max_aksi or (int(aksi) == 4 and pemain.potion == 0) or (int(aksi) == 3 and skill_sudah_digunakan):
            input_salah_count += 1
            print(f"\n❌ Input tidak valid! ({input_salah_count}/3)")
            
            if input_salah_count >= 3:
                print(f"\n{'='*60}")
                print("⚠️  ANDA TIDAK BISA MEMBUAT KEPUTUSAN DI SAAT KRITIS!")
                print(f"{'='*60}")
                print(f"Karena keraguan yang fatal, {pemain.nama} terpukul oleh {nama_musuh}!")
                print(f"Petualangan Anda berakhir di sini.\n")
                pemain.nyawa = 0
                break
            continue
        
        input_salah_count = 0  # Reset counter jika input valid
        aksi = int(aksi)
        
        if aksi == 1:
            # Menyerang Normal
            damage_pemain = pemain.serang()
            musuh.ambil_damage(damage_pemain)
            print(f"\n{pemain.nama} menyerang {nama_musuh}!")
            print(f"💥 Damage: {damage_pemain}")
            sedang_bertahan = False
            
        elif aksi == 2:
            # Bertahan
            print(f"\n{pemain.nama} mengambil posisi pertahanan!")
            print("🛡️  Pertahanan meningkat 50%!")
            sedang_bertahan = True
            damage_pemain = 0
            
        elif aksi == 3:
            # Skill Khusus
            damage_pemain = pemain.skill_khusus()
            musuh.ambil_damage(damage_pemain)
            print(f"\n{pemain.nama} menggunakan SKILL KHUSUS!")
            print(f"⚡ DAMAGE DAHSYAT: {damage_pemain}!")
            skill_sudah_digunakan = True  # Mark skill sebagai sudah digunakan
            sedang_bertahan = False
            
        elif aksi == 4:
            # Minum Potion
            penyembuhan, berhasil = pemain.gunakan_potion()
            if berhasil:
                print(f"\n{pemain.nama} meminum Potion!")
                print(f"🧪 Penyembuhan: +{penyembuhan} Nyawa")
                print(f"Nyawa sekarang: {pemain.nyawa}/{pemain.nyawa_max}")
                print(f"Potion tersisa: {pemain.potion}")
                sedang_bertahan = False
                damage_pemain = 0
        
        if musuh.nyawa <= 0:
            print(f"\n{'='*60}")
            print(f"✅ {nama_musuh} TELAH DIKALAHKAN!")
            print(f"{'='*60}\n")
            return True
        
        time.sleep(1)
        
        # Serangan Musuh
        print()
        damage_musuh = musuh.serang()
        
        if sedang_bertahan:
            damage_musuh = max(1, damage_musuh // 2)
            print(f"{nama_musuh} menyerang!")
            print(f"🛡️  Pertahanan Anda mengurangi damage!")
            print(f"💥 Damage diterima: {damage_musuh}")
        else:
            damage_diterima = pemain.ambil_damage(damage_musuh)
            print(f"{nama_musuh} menyerang balik!")
            print(f"💥 Damage diterima: {damage_diterima}")
            damage_musuh = damage_diterima
        
        pemain.nyawa = max(pemain.nyawa, 0)
        
        if pemain.nyawa <= 0:
            print(f"\n{'='*60}")
            print(f"❌ {pemain.nama} TELAH DIKALAHKAN!")
            print(f"{'='*60}\n")
            return False
        
        putaran += 1
        time.sleep(1)

def pertarungan_boss(pemain):
    print("\n" + "="*60)
    print(f"        PERTARUNGAN TERAKHIR: PYRAXION SI NAGA MERAH LEGENDARIS")
    print("="*60 + "\n")
    
    boss = Boss("PYRAXION", 200, 28)
    putaran = 1
    sedang_bertahan = False
    input_salah_count = 0
    skill_sudah_digunakan = False
    
    print("Naga raksasa dengan sisik merah berkilau mengaum menggelegar!")
    print("Api menyembur dari mulutnya yang besar!")
    print("Sayapnya yang luas menutup langit di atas Anda!")
    time.sleep(1)
    
    while pemain.nyawa > 0 and boss.nyawa > 0:
        print(f"\n{'*'*60}")
        print(f"PUTARAN {putaran}")
        print(f"{'*'*60}")
        print(f"{pemain.nama} (LV{pemain.level}) Nyawa: {pemain.nyawa}/{pemain.nyawa_max}")
        print(f"PYRAXION Nyawa: {boss.nyawa}/{boss.nyawa_max}\n")
        
        # Menu Aksi Pemain
        print("Pilih Aksi:")
        print("1. ⚔️  Menyerang  (Damage normal)")
        print("2. 🛡️  Bertahan   (Kurangi damage musuh)")
        if skill_sudah_digunakan:
            print("3. ✨ Skill Khusus (⛔ Sudah digunakan)")
        else:
            print("3. ✨ Skill Khusus (Damage maksimal)")
        if pemain.potion > 0:
            print(f"4. 🧪 Minum Potion ({pemain.potion} tersedia)")
        
        max_aksi = 4 if pemain.potion > 0 else 3
        prompt_text = f"\nPilihan (1-{max_aksi}): " if pemain.potion > 0 else "\nPilihan (1-3): "
        aksi = input(prompt_text)
        
        # Validasi input
        if not aksi.isdigit() or int(aksi) < 1 or int(aksi) > max_aksi or (int(aksi) == 4 and pemain.potion == 0) or (int(aksi) == 3 and skill_sudah_digunakan):
            input_salah_count += 1
            print(f"\n❌ Input tidak valid! ({input_salah_count}/3)")
            
            if input_salah_count >= 3:
                print(f"\n{'='*60}")
                print("⚠️  ANDA TIDAK BISA MEMBUAT KEPUTUSAN DI SAAT KRITIS!")
                print(f"{'='*60}")
                print(f"Karena keraguan yang fatal saat hadap PYRAXION, {pemain.nama} terpukul habis!")
                print(f"Petualangan Anda berakhir di sini.\n")
                pemain.nyawa = 0
                kekalahan_boss(pemain)
                return
            continue
        
        input_salah_count = 0  # Reset counter jika input valid
        aksi = int(aksi)
        
        if aksi == 1:
            # Menyerang Normal
            damage_pemain = pemain.serang()
            boss.ambil_damage(damage_pemain)
            print(f"\n{pemain.nama} menyerang Pyraxion dengan penuh kemarahan!")
            print(f"💥 Damage: {damage_pemain}")
            sedang_bertahan = False
            
        elif aksi == 2:
            # Bertahan
            print(f"\n{pemain.nama} mengambil posisi pertahanan defensif!")
            print("🛡️  Perlindungan meningkat 50%!")
            sedang_bertahan = True
            damage_pemain = 0
            
        elif aksi == 3:
            # Skill Khusus
            damage_pemain = pemain.skill_khusus()
            boss.ambil_damage(damage_pemain)
            print(f"\n{pemain.nama} mengumpulkan semua energi dan mengeluarkan SERANGAN TERAKHIR!")
            print(f"⚡ LEDAKAN ENERGI DAHSYAT: {damage_pemain}!")
            skill_sudah_digunakan = True
            sedang_bertahan = False
            
        elif aksi == 4:
            # Minum Potion
            penyembuhan, berhasil = pemain.gunakan_potion()
            if berhasil:
                print(f"\n{pemain.nama} meminum Potion!")
                print(f"🧪 Penyembuhan: +{penyembuhan} Nyawa")
                print(f"Nyawa sekarang: {pemain.nyawa}/{pemain.nyawa_max}")
                print(f"Potion tersisa: {pemain.potion}")
                sedang_bertahan = False
                damage_pemain = 0
        
        if boss.nyawa <= 0:
            kemenangan_boss(pemain)
            return
        
        time.sleep(1)
        
        # Serangan Boss
        print()
        persentase_nyawa = (boss.nyawa / boss.nyawa_max) * 100
        damage_boss = boss.serang()
        
        if persentase_nyawa > 60:
            deskripsi = "PYRAXION menggunakan SERANGAN GIGI DAN KUKU dengan ganas!"
        elif persentase_nyawa > 30:
            deskripsi = "PYRAXION MELEPASKAN LEDAKAN API BESAR yang menggelegar!"
        else:
            deskripsi = "PYRAXION DALAM KEADAAN SEKARAT! Ia melancarkan serangan gila-gilaan terakhir!"
        
        print(f"{'🔥  '}{deskripsi}")
        
        if sedang_bertahan:
            damage_boss = max(1, damage_boss // 2)
            print(f"🛡️  Pertahanan Anda mengurangi damage!")
            print(f"💥 Damage diterima: {damage_boss}")
        else:
            damage_diterima = pemain.ambil_damage(damage_boss)
            print(f"💥 Damage diterima: {damage_diterima}")
            damage_boss = damage_diterima
        
        pemain.nyawa = max(pemain.nyawa, 0)
        
        if pemain.nyawa <= 0:
            kekalahan_boss(pemain)
            return
        
        putaran += 1
        time.sleep(1)

def kemenangan_boss(pemain):
    print(f"\n{'='*60}")
    print("    ✅ KEMENANGAN! PYRAXION TELAH KALAH!")
    print(f"{'='*60}\n")
    
    time.sleep(1)
    print("🐉 Naga merah yang raksasa itu jatuh dan berhenti bergerak...")
    time.sleep(1)
    print("✨ Cahaya misterius memancar dari tubuhnya...")
    time.sleep(1)
    print("🌟 Kutukan yang menghancurkan kerajaan ini akhirnya hilang!\n")
    time.sleep(1)
    
    print(f"⭐ {pemain.nama}! Anda adalah sang PAHLAWAN SEJATI!")
    time.sleep(1)
    print(f"✨ Level akhir: {pemain.level}")
    time.sleep(1)
    print("🏰 Kota Ashvale akan dibebaskan dari kegelapan berkat kematian Pyraxion.")
    time.sleep(1)
    print("📖 Legenda Anda akan diceritakan turun-temurun oleh generasi mendatang!\n")
    time.sleep(1)
    
    tanya_minum_potion(pemain)
    
    print("="*60)
    print("    🎉 ANDA TELAH MENYELESAIKAN PETUALANGAN! 🎉")
    print("="*60)
    
    # Tanya pemain ingin ulang atau selesai
    print("\n") 
    while True:
        pilihan = input("Ingin bermain lagi? (Y/N): ").upper().strip()
        if pilihan == "Y":
            print("\n" * 3)
            game_utama()
            break
        elif pilihan == "N":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!\n")
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan Y atau N.\n")

def kekalahan_boss(pemain):
    print(f"\n{'='*60}")
    print("    ❌ KEKALAHAN! ANDA TELAH DIKALAHKAN OLEH PYRAXION!")
    print(f"{'='*60}\n")
    
    time.sleep(1)
    print(f"💀 {pemain.nama} tidur selamanya...")
    time.sleep(1)
    print("🔴 Pyraxion terus memerintah dengan kekuatan jahatnya.")
    time.sleep(1)
    print("🌑 Darvintos tetap berada dalam kegelapan...\n")
    time.sleep(1)
    
    # Tanya pemain ingin ulang atau selesai
    print()
    while True:
        pilihan = input("Ingin bermain lagi? (Y/N): ").upper().strip()
        if pilihan == "Y":
            print("\n" * 3)
            game_utama()
            break
        elif pilihan == "N":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!\n")
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan Y atau N.\n")

def game_loop(pemain):
    """Wrapper untuk petualangan utama"""
    petualangan_awal(pemain)

def game_over(pemain):
    print("\n" + "="*60)
    print("                    ❌ GAME OVER")
    print(f"            {pemain.nama} telah gugur dalam pertarungan...")
    print("="*60 + "\n")
    
    # Tanya pemain ingin ulang atau selesai
    print()
    while True:
        pilihan = input("Ingin bermain lagi? (Y/N): ").upper().strip()
        if pilihan == "Y":
            print("\n" * 3)
            game_utama()
            break
        elif pilihan == "N":
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!\n")
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan Y atau N.\n")

def game_utama():
    print("\n" + "="*60)
    print("      🎮 SELAMAT DATANG DI ADVENTURE BOT: DRAGON SLAYER 🎮")
    print("="*60 + "\n")
    
    print("--- MEMULAI PETUALANGAN DIGITAL ---\n")
    nama = input("Siapa nama pahlawanmu? ").strip()
    
    # Menu Pilih Kesulitan
    print("\n⚔️  PILIH TINGKAT KESULITAN:\n")
    print("1. 🟢 EASY   - Nyawa +10, Pertahanan +5 (Mudah)")
    print("2. 🟡 NORMAL - Standar (Seimbang)")
    print("3. 🔴 HARD   - Nyawa -5, Serangan -3 (Sulit)\n")
    
    while True:
        pilihan_difficulty = input("Pilihan kesulitan (1-3): ").strip()
        if pilihan_difficulty == "1":
            difficulty = "easy"
            break
        elif pilihan_difficulty == "2":
            difficulty = "normal"
            break
        elif pilihan_difficulty == "3":
            difficulty = "hard"
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan 1, 2, atau 3.\n")
    
    pemain = Pemain(nama, difficulty)
    
    cerita_pembukaan(pemain)
    
    game_loop(pemain)
    
if __name__ == "__main__":
    game_utama()