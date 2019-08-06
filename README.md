# Vortaro
Ĉi tiu paĝo kolektas naciajn vortarojn, tradukas komercajn informojn de landoj al Esperanto kaj stokas ilin en la datumbazo  
La http-API povas aliri komercajn informojn de landoj stokitaj en Esperanto  
[Pli pri la projekto](https://github.com/SalutonMondo-NLP/Vortaro/blob/master/Multlingvakomercaj%20.pdf)

## Teknika bazo
- Ajna programlingvo
- Funkcios la datumbazo
- Ĝi analizos la vortara dokumento, ne limigita al：csv,txt,mdx
- Retejo-disvolviĝo： povas disvolvi HTTP API

## Celo
Stoki naciajn informojn en Esperanto, ligante naciajn informojn


# Kiel kontribui
[kreado de konto ĉe github](https://github.com/join). 

## 1. Elektu vortaron
- Metu la vortaron en dosierujo "via-lando-nomo"
```shell
git clone https://github.com/SalutonMondo-NLP/Vortaro.git
cd Vortaro/
mkdir via-lando-nomo
git add . #Aldoni nacian vortaron al dosierujo "via-lando-nomo"
git commit
git push
```
- Analiza la vortaron al "nacia lingo-esperanto " paro
- Enmeti  "nacia lingo-esperanto " paro al via datumbazojn
- Oferto HTTP API por aliron nacia lingo-esperanto en datumbazojn

**URI**  
**POST /komercajinformujo/china**  
**REQEST**  
```json
{
	"source":"English",
	"text":"hello"
}
```
**RESPONSE**
```json
{
	"content":"Saluton mondo"
}
```

## 2. Elektu viaj propraj plej taŭgan komercajn informojn en viaj lando
- Foliumi retejon, elektu viaj propraj plej taŭgan komercajn informojn en viaj lando

## 3. Traduki komercaj informojn al Esperanton kaj tiam konservas komercan informojn en Esperanto
- Ĉiuj informoj estas konservitaj en la datumbazo en Esperanto
- Uzu HTTP API, disponebla por uzantoj en aliaj landoj

### Ekzemplo por HTTP API (Bonvenon al pli bonaj ekzemploj)

**URI**  
**POST /komercajinformujo/china**  
**REQEST**  
```json
{
	"key-word":"UEA"
}
```
**RESPONSE**
```json
{
	"content":{
		"name":"Universala Esperanto-Asocio",
		"intro":"Nieuwe Binnenweg 176, 3015 BJ Rotterdam,Nederlando",
		"tel": "+31104361044",
		"retadreso":"info@uea.org"
	}
}
```

# Kunlabori kaj aldoni dosierojn

Por pli amplekse kunlabori kaj aldoni dosierojn, necesas instali `git` sur sia komputilo. Vi povas tiam elŝuti ĉiujn dosierojn sur vian komputilon helpe de 

    git clone https://github.com/SalutonMondo-NLP/Vortaro.git

Por komencantoj pri `git`, ni rekomendas uzi la grafikan interfacon git gui sekve:

1. Elŝutu kaj instalu git de https://git-scm.com/downloads
2. [Agordu bazajn informojn pri vi](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup): nomo kaj retpoŝtadreso
3. Uzu `git gui` por preni kaj aldoni dosierojn
