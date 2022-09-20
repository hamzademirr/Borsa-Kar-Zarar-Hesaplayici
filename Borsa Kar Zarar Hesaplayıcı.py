import tkinter as tk
form = tk.Tk()

form.title('Risk Kazanç Hesaplama')
form.geometry('400x250')

def hesap():

    ana_para = (float((_ana_para_entry.get()).replace(",",".")))
    hedef_yüzde = float((_hedef_yüzde_entry.get()).replace(",","."))
    stop_loss_yüzdesi = float((_stop_loss_yüzdesi_entry.get()).replace(",","."))
    riske_edilecek_yüzde = float((_riske_edilecek_yüzde_entry.get()).replace(",","."))
    kaldıraç_oranı = float((_kaldıraç_oranı_entry.get()).replace(",",".")) 
    işlem_miktarı = ( ana_para / (( kaldıraç_oranı * stop_loss_yüzdesi ) / riske_edilecek_yüzde))

    _rr.config(text= ( hedef_yüzde / stop_loss_yüzdesi ))
    _stop_zarar.config(text= ( ( ana_para * riske_edilecek_yüzde ) / 100 ))
    _işlem_miktarı_s.config(text= ( ana_para / (( kaldıraç_oranı * stop_loss_yüzdesi ) / riske_edilecek_yüzde)))
    _kar_miktarı.config(text= ( işlem_miktarı * hedef_yüzde * kaldıraç_oranı / 100))


etiket = tk.Label(form,text='Risk Kazanç Hesaplama')
etiket.place(x=150, y=10)

_ana_para = tk.Label(text='Ana Para:')
_ana_para.place(x=20, y=50)

_ana_para_entry = tk.Entry(form, width = 10)
_ana_para_entry.place(x=140, y=50)


_kaldıraç_oranı = tk.Label(text='Kaldıraç Oranı:')
_kaldıraç_oranı.place(x=20, y=80)

_kaldıraç_oranı_entry = tk.Entry(form, width = 10)
_kaldıraç_oranı_entry.place(x=140, y=80)


_stop_loss_yüzdesi = tk.Label(text='Stop Loss Yüzdesi:')
_stop_loss_yüzdesi.place(x=20, y=110)

_stop_loss_yüzdesi_entry = tk.Entry(form, width = 10)
_stop_loss_yüzdesi_entry.place(x=140, y=110)


_riske_edilecek_yüzde = tk.Label(text='Riske Edilecek Yüzde:')
_riske_edilecek_yüzde.place(x=20, y=140)

_riske_edilecek_yüzde_entry = tk.Entry(form, width = 10)
_riske_edilecek_yüzde_entry.place(x=140, y=140)


_hedef_yüzde = tk.Label(text='Hedef Yüzde:')
_hedef_yüzde.place(x=20, y=170)

_hedef_yüzde_entry = tk.Entry(form, width = 10)
_hedef_yüzde_entry.place(x=140, y=170)


_kar_edilecek_miktar = tk.Label(text='Kar Edilecek Miktar:')
_kar_edilecek_miktar.place(x=220, y=50)

_kar_miktarı = tk.Label(text='______')
_kar_miktarı.place(x=330, y=50)


_stop_zararı = tk.Label(text='Stop Kaybı:')
_stop_zararı.place(x=220, y=80)

_stop_zarar = tk.Label(text='______')
_stop_zarar.place(x=330, y=80)


_rr_oranı = tk.Label(text='R/R oranı:')
_rr_oranı.place(x=220, y=110)

_rr = tk.Label(text='______')
_rr.place(x=330, y=110)


_işlem_miktarı = tk.Label(text='İşleme Girilecek miktar:')
_işlem_miktarı.place(x=240, y=140)

_işlem_miktarı_s = tk.Label(text='______')
_işlem_miktarı_s.place(x=280, y=160)



buton = tk.Button(form,text='Hesapla', command=hesap)
buton.place(x=180, y=200)

form.mainloop()
