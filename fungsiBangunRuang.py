import random
import math

PI1 = 3.14
PI2 = 22/7

# tutorial ada dibawah
# ctrl + end untuk langsung ke bawah


class BangunRuang:
    def pi_checker(r):
        if r % 7 == 0:
            pi_value = 22/7
        else:
            pi_value = 3.14

    def luas_permukaan_lingkaran(r):
        if r % 7 == 0:
            output = PI2 * r * r
        elif r % 7 != 0:
            output = PI1 * r * r
        return output

    def luas_selimut_tabung(r, t):
        if r % 7 == 0:
            output = 2 * PI2 * r * t
        elif r % 7 != 0:
            output = 2 * PI1 * r * t
        return output

    def luas_permukaan_tabung(r, t):
        if r % 7 == 0:
            output = 2 * PI2 * r * (r+t)
        elif r % 7 != 0:
            output = 2 * PI1 * r * (r+t)
        return output

    def volume_tabung(r, t):
        if r % 7 == 0:
            output = PI2 * r * r * t
        elif r % 7 != 0:
            output = PI1 * r * r * t
        output_konversi = output / 1000
        return output

    def luas_selimut_kerucut_1(q, s):
        output = q/360 * s * s
        if s % 7 == 0:
            return f"{output}π"
        else:
            return f"{output}π"

    def luas_selimut_kerucut_2(r, s):
        if r % 7 == 0:
            output = PI2 * r * s
        elif r % 7 != 0:
            output = PI1 * r * s
        return output

    def luas_permukaan_kerucut_1(r, q, s):
        if r % 7 == 0:
            output = PI2 * r * r + q/360 * PI2 * s * s
        elif r % 7 != 0:
            output = PI1 * r * r + q/360 * PI1 * s * s
        return output

    def luas_permukaan_kerucut_2(r, s):
        if r % 7 == 0:
            output = PI2 * r * r + PI2 * r * s
        elif r % 7 != 0:
            output = PI1 * r * r + PI1 * r * s
        return output

    def volume_kerucut(r, t):
        if r % 7 == 0:
            output = 1/3 * PI2 * r * r * t
        elif r % 7 != 0:
            output = 1/3 * PI1 * r * r * t
        return output

    def luas_permukaan_bola(r):
        if r % 7 == 0:
            output = 4 * PI2 * r * r
        elif r % 7 != 0:
            output = 4 * PI1 * r * r
        return output

    def keliling_bola(r):
        if r % 7 == 0:
            output = 2 * PI2 * r
        elif r % 7 != 0:
            output = 2 * PI1 * r
        return output

    def volume_bola(r):
        if r % 7 == 0:
            output = PI2 * r * r * r
            output *= 4/3
        elif r % 7 != 0:
            output = PI1 * r * r * r
            output *= 4/3
        return output

    def luas_permukaan_kubus(s):
        lp_kubus = 6 * pow(s, 2)
        output = lp_kubus
        return output

    def volume_kubus(s):
        v_kubus = pow(s, 3)
        output = v_kubus
        return output

    def luas_permukaan_balok(p, l, t):
        lp_balok = (p * l) + (p * t) + (l * t)
        lp_balok = 2 * lp_balok
        output = lp_balok
        return output

    def volume_balok(p, l, t):
        v_balok = p * l * t
        output = v_balok
        return output


br = BangunRuang
# x = br.volume_bola(10)
# print(x)


class AdvancedBangunRuang:

    def tinggi_dengan_ls_tabung(r, ls_tabung):
        t = int()
        if r % 7 == 0:
            output = 2 * PI2 * r
            output = ls_tabung / output
        if r % 7 != 0:
            output = 2 * PI1 * r
            output = ls_tabung / output
        return output

    def jari_jari_dengan_ls_tabung(t, ls_tabung):
        r = int()
        if t % 7 == 0:
            output = 2 * PI2 * t
            output = ls_tabung / output
        if t % 7 != 0:
            output = 2 * PI1 * t
            output = ls_tabung / output
        return output

    def tinggi_dengan_lp_tabung(r, lp_tabung):
        t = int()
        l_lingkaran = br.luas_permukaan_lingkaran(r)
        output = l_lingkaran * 2
        output = lp_tabung - output
        output = abr.tinggi_dengan_ls_tabung(r, output)
        # if r % 7 == 0:
        #     output = 2 * PI2 * r * (r)
        #     output = lp_tabung / output
        # if r % 7 != 0:
        #     output = 2 * PI1 * r * (r)
        #     output = lp_tabung / output
        return output

    def jari_jari_dengan_lp_tabung(t, lp_tabung):
        r = int()
        if lp_tabung % 7 == 0:
            output = lp_tabung / (2*PI2) * 7
            output = r*r + t * r - output
        else:
            output = lp_tabung / (2*PI1) * 7
            output = r*r + t * r - output

        print(output)
        # r = int()
        # hasil_sementara = int()
        # while hasil_sementara != lp_tabung:
        #     r = random.randint(1, 100)
        #     hasil_sementara = br.luas_permukaan_tabung(r, t)
        # else:
        return output

    def tinggi_dengan_volume_tabung(r, v_tabung):
        t = int()
        if r % 7 == 0:
            output = PI2 * r * r
            output = v_tabung / output
        elif r % 7 != 0:
            output = PI1 * r * r
            output = v_tabung / output
        output_konversi = output / 1000
        return output

    def jari_jari_dengan_volume_tabung(t, v_tabung):
        r = int()
        if v_tabung % 7 == 0:
            output = PI2 * t
            output = v_tabung / output
            output = math.sqrt(output)
        elif v_tabung % 7 != 0:
            output = PI1 * t
            output = v_tabung / output
            output = math.sqrt(output)
        return output

    def tinggi_dengan_ls_kerucut(r, ls_tabung):
        pass

    def jari_jari_dengan_ls_kerucut(t, ls_tabung):
        pass

    def tinggi_dengan_lp_kerucut(r, lp_kerucut):
        pass

    def jari_jari_dengan_lp_kerucut(t, lp_kerucut):
        pass

    def tinggi_dengan_volume_kerucut(r, v_kerucut):
        pass

    def jari_jari_dengan_volume_kerucut(t, v_kerucut):
        t *= 1/3
        output = PI1 * v_kerucut / t
        output = math.sqrt(output)
        # output = 1/3 * PI1 * t
        # output = output * v_kerucut
        # output = math.sqrt(v_kerucut)
        return output


abr = AdvancedBangunRuang
# x = abr.jari_jari_dengan_ls_tabung(12, 753.6)
# print(x)


class Pythagoras:
    def hipotenusa(b, c):
        a = pow(b, 2) + pow(c, 2)
        a = math.sqrt(a)
        output = a
        return output

    def garis_panjang(a, c):
        b = pow(a, 2) - pow(c, 2)
        b = math.sqrt(b)
        output = b
        return b

    def garis_pendek(a, b):
        c = pow(a, 2) - pow(b, 2)
        c = math.sqrt(c)
        output = c
        return output


pt = Pythagoras
# x = pt.hipotenusa(25, 7)
# print(x)


class Random:
    def luas_permukaan_bola(luas_permukaan):
        r = 4 * PI2
        r = luas_permukaan / r
        r = math.sqrt(r)
        output = r
        return output

    def volume_bola_terbesar_dalam_kubus(rusuk):
        s_kubus = 4 * rusuk
        v_kubus = pow(s_kubus, 3)
        output = int()
        r = int()
        while output <= v_kubus:
            r = r + 1

            if r % 7 == 0:
                output = 4 * 1/3 * PI2 * r * r * r
            elif r % 7 != 0:
                output = 4 * 1/3 * PI1 * r * r * r
        else:
            return output

    def luas_permukaan_setengah_bola_diameter(d):
        r = d/2
        if r % 7 == 0:
            output = 4 * PI2 * r * r / 2
        elif r % 7 != 0:
            output = 4 * PI1 * r * r / 2
        return output

    def luas_sebagian_permukaan_bola(r, persentase):
        if r % 7 == 0:
            output = 4 * PI2 * r * r * persentase/100
        elif r % 7 != 0:
            output = 4 * PI1 * r * r * persentase/100
        return output

    # error

    # def persamaan_permukaan_volume_bola():
        lp_bola = int()
        v_bola = int()
        output = int()
        r = int()
        while output != 0:
            r = r + 1
            if r % 7 == 0:
                lp_bola = 4 * PI2 * r * r
            elif r % 7 != 0:
                lp_bola = 4 * PI1 * r * r

            if r % 7 == 0:
                v_bola = 4 * 1/3 * PI2 * r * r * r
            elif r % 7 != 0:
                v_bola = 4 * 1/3 * PI1 * r * r * r
        else:
            return output

    def l_selimut_dengan_l_permukaan_kerucut(r, lp_kerucut):
        if r % 7 == 0:
            s = PI2 * r * r
            s = lp_kerucut - s
        elif r % 7 != 0:
            s = PI1 * r * r * PI1 * r
            s = lp_kerucut - s
        output = s
        return output

    def v_air_tabung_tumpah_dengan_bola(r, t, n_bola, r_bola):
        v_tabung = BangunRuang.volume_tabung(r, t)
        v_bola = BangunRuang.volume_bola(r_bola)
        v_bola *= 3
        air_tumpah = v_tabung - v_bola
        output = air_tumpah
        return output

    def v_air_tabung_penuh_dengan_kerucut(r1, t1, r2, t2):
        v_tabung = br.volume_tabung(r1, t1)
        v_kerucut = br.volume_kerucut(r2, t2)
        v_tabung_penuh = v_tabung - v_kerucut
        output = v_tabung_penuh
        return output

    def t_tabung_dengan_ls_tabung(r, ls_tabung):
        if r % 7 == 0:
            t = 2 * PI2 * r
            t = ls_tabung / t
        elif r % 7 != 0:
            t = 2 * PI1 * r
            t = ls_tabung / t
        output = t
        return output

    def t_kerucut_dengan_v_kerucut(r, v_kerucut):
        if r % 7 == 0:
            output = 1/3 * PI2 * r * r
            output = v_kerucut / output
        elif r % 7 != 0:
            output = 1/3 * PI1 * r * r
            output = v_kerucut / output
        return output

    def r_dengan_volume_kerucut(v_kerucut):
        r = int()
        hasil_sementara = int()
        while hasil_sementara != v_kerucut:
            r = random.randint(1, 200)
            t = random.randint(1, 200)
            hasil_sementara = br.volume_kerucut(r, t)
        else:
            return r, t

# r = jari jari
# t = tinggi
# s = garis pelukis


# tulis variabel
# contoh
# x = br.luas_permukaan_tabung()
# x merupakan variabel
# br.luas_permukaan_tabung() merupakan fungsi
# br.luas_permukaan_tabung(disini diisi dengan data yang diketahui dalam soal)
# contoh modul mtk tabung no. 3
# x = br.luas_permukaan_tabung(r=7, t=25)
# print(x)
# print() berguna untuk menampilkan hasil
