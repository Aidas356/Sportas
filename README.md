Sporto Puslapis

Sveiki atvykę į Sporto Puslapį! Tai Django pagrindu sukurtas projektas, skirtas padėti vartotojams planuoti ir sekti savo sporto treniruotes, mitybą bei kitas sveikatos gerinimo veiklas.

Funkcionalumas

1.Vartotojo registracija ir prisijungimas

Galimybė užsiregistruoti ir prisijungti naudojant unikalų vartotojo vardą bei slaptažodį.

2.Profilio valdymas

Galimybė peržiūrėti ir redaguoti savo profilį (vardas, pavardė, amžius ir kt.).

3.Treniruočių planavimas

4.Mitybos stebėjimas

Sekite savo dienos racioną
Galima pasitikrinti kiek kaloriju reikia suvartoti

5. Galima susiskaiciuoti savo Kmi ir kiek kcal reikia suvartoti pagal svori ir ugi


5.Technologijos

Programavimo kalba: Python

Framework: Django

Duomenų bazė: SQLite (numatytoji; lengvai pakeičiama į PostgreSQL ar kitą pagal poreikį)

Front-end: HTML, CSS, Bootstrap

Formų tvarkymas: Django Crispy Forms

Įdiegimas

Aplinka

Sukurkite virtualią aplinką:

python -m venv venv

Aktyvuokite aplinką:

Windows:

venv\Scripts\activate

Įdiekite priklausomybes:

pip install -r requirements.txt

3. Migracijos ir paleidimas

Paleiskite migracijas:

python manage.py migrate

Paleiskite serverį:

python manage.py runserver

Atidarykite naršyklėje adresą:

http://127.0.0.1:8000

Naudojimas

Prisijunkite arba užsiregistruokite.

Tvarkykite savo profilį.

Rinkites is duotu sporto programu, mitybos planu ir papildu

Failų Struktūra

mysite/ – Projekto šakninis katalogas.

web/ – Pagrindinė aplikacija su visais funkcionalumais.

templates/ – HTML šablonai.

static/ – CSS


