
all: Sun Moon Mercury Venus Mars Jupiter Saturn Uranus Neptune

Sun:
	python run.py para/site_para.txt para/sun_para.txt data/Sun2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/sun_para.txt data/Sun2023.txt data/Sun2023.txt

Moon:
	python run.py para/site_para.txt para/moon_para.txt data/Moon2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/moon_para.txt data/Moon2023.txt data/Sun2023.txt

Mercury:
	python run.py para/site_para.txt para/mercury_para.txt data/Mercury2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/mercury_para.txt data/Mercury2023.txt data/Sun2023.txt

Venus:
	python run.py para/site_para.txt para/venus_para.txt data/Venus2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/venus_para.txt data/Venus2023.txt data/Sun2023.txt

Mars:
	python run.py para/site_para.txt para/mars_para.txt data/Mars2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/mars_para.txt data/Mars2023.txt data/Sun2023.txt

Jupiter:
	python run.py para/site_para.txt para/jupiter_para.txt data/Jupiter2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/jupiter_para.txt data/Jupiter2023.txt data/Sun2023.txt

Saturn:
	python run.py para/site_para.txt para/saturn_para.txt data/Saturn2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/saturn_para.txt data/Saturn2023.txt data/Sun2023.txt

Uranus:
	python run.py para/site_para.txt para/uranus_para.txt data/Uranus2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/uranus_para.txt data/Uranus2023.txt data/Sun2023.txt

Neptune:
	python run.py para/site_para.txt para/neptune_para.txt data/Neptune2022.txt data/Sun2022.txt
	python run.py para/site_para.txt para/neptune_para.txt data/Neptune2023.txt data/Sun2023.txt
