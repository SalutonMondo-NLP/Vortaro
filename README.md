# Vortaro

```shell
git clone https://github.com/SalutonMondo-NLP/Vortaro.git
cd Vortaro/
mkdir via-lando-nomo
```
## 1. Elektu vortaron
- Metu la vortaron en dosierujo "via-lando-nomo"
```shell
git pull
cd via-lando-nomo
git add ./
git commit -m 'mia-lando vortaro'
git push
```
- Analiza la vortaron al "nacia lingo-esperanto " paro
- Enmeti  "nacia lingo-esperanto " paro al via datumbazojn


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
