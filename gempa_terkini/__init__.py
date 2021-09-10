from bs4 import BeautifulSoup
import requests

class Bencana:
    def __init__(self, url, description):
        self. result = None
        self.url = url
        self.description = description

    def extraction_data(self):
        pass

    def show_result(self):
        pass

    def run(self):
        self.extraction_data()
        self.show_result()

#class BencanaTerkini(Bencana):
    #def __init__(self, url):
        #super(BencanaTerkini, self).__init__(url, 'To get the latest news of disaster in Indonesia from BNPB.go.id')

    #def extraction_data(self):

class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url, 'To get the latest news of earthquake in Indonesia from BMKG.go.id')


    def extraction_data(self):

        try:
            r = requests.get(self.url)
        except Exception:
            return None

        if r.status_code == 200 :
            soup = BeautifulSoup(r.text, 'html.parser')
            result= soup.find('span', {'class': 'waktu'})
            result = result.text.split(', ')
            tanggal = result[0]
            waktu = result[1]
            result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
            result = result.findChildren('li')
            i = 0
            magnitudo = None
            kedalaman = None
            ls = None
            bt = None
            lokasi = None
            dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal
            hasil['waktu'] = waktu
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] = kedalaman
            hasil['koordinat'] = {'ls' : ls, 'bt' : bt}
            hasil['lokasi'] = lokasi
            hasil['dirasakan'] = dirasakan
            self.result = hasil

        else:
            return None


    def show_result(self):
        if self.result is None:
            print('Tidak bisa menemukan data gempa terkini')
            return
        print('Gempa Terakhir berdasarkan BMKG')
        print(f"Tanggal, {self.result['tanggal']}")
        print(f"Waktu, {self.result['waktu']}")
        print(f"lokasi: LS={self.result['koordinat']['ls']}, BT={self.result['koordinat']['bt']}")
        print(self.result['lokasi'])
        print(self.result['dirasakan'])

if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id')
    print('Deskripsi Package', gempa_di_indonesia.description)
    gempa_di_indonesia.run()

    #bencana_di_indonesia = BencanaTerkini('https://bnpb.go.id/')
    #print('Deskripsi Package', BencanaTerkini.description)
    #bencana_di_indonesia.run()