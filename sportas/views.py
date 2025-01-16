from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Workout, Meal, Profile, Supplement, FoodProgram, Exercise
from .forms import WorkoutForm, MealForm, UserUpdateForm, ProfileUpdateForm, \
    MealProgramForm, SupplementForm


def index(request):
    return render(request, 'index.html')


@login_required
def workouts(request):
    categories = [
        {"name": "Jegos treniruote ", "slug": "jegos didinimas"},
        {"name": "Raumenu auginimo treniruote", "slug": "raumenu auginimas"},
        {"name": "Isvermes treniruote", "slug": "istvermes"},
    ]
    return render(request, "workouts/workouts.html", {"categories": categories})


def workout_details(request, category):
    workouts_data = {
        "jegos didinimas": {
            "Pirmoji diena": [
                {"exercise": "Pritūpimai", "sets_reps": "3 x 5"},
                {"exercise": "Kojų tiesimas treniruoklyje", "sets_reps": "3 x 8"},
                {"exercise": "Bulgariški įtūpstai", "sets_reps": "2 x 10"},
                {"exercise": "Štangos spaudimas kampu", "sets_reps": "3 x 6"},
                {"exercise": "Krūtinės spaudimas kampu su svarmenimis", "sets_reps": "3 x 8"},
                {"exercise": "Bicepsas su štanga stovint", "sets_reps": "3 x 10"},
            ],
            "Antroji diena": [
                {"exercise": "Prisitraukimai", "sets_reps": "3 x 6"},
                {"exercise": "Štangos trauka pasilenkus", "sets_reps": "3 x 8"},
                {"exercise": "Svarmens trauka pasilenkus", "sets_reps": "3 x 10"},
                {"exercise": "Pulloveriai sulenktomis rankomis", "sets_reps": "3 x 10"},
                {"exercise": "Gūžtelėjimas pečiais", "sets_reps": "3 x 8"},
                {"exercise": "Tricepso spaudimas žemyn su lynu", "sets_reps": "3 x 10"},
            ],
            "Trečioji diena": [
                {"exercise": "Klubų pakėlimai", "sets_reps": "3 x 5"},
                {"exercise": "Rumuniškoji mirties trauka", "sets_reps": "3 x 6"},
                {"exercise": "Kojų lenkimas treniruoklyje", "sets_reps": "2 x 10"},
                {"exercise": "Svarmenų spaudimas pakaitomis pečiams sėdint", "sets_reps": "3 x 8"},
                {"exercise": "Lyno trauka iš apačios prie krūtinės", "sets_reps": "3 x 8"},
                {"exercise": "Lyno kėlimas į priekį", "sets_reps": "3 x 12"},
            ],
        },
        "raumenu auginimas": {
            "Pirmoji diena – krūtinės pratimai": [
                {"exercise": "Horizontalus štangos spaudimas", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas krūtinei", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas krūtinei", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas krūtinei", "sets_reps": "3 x 8-12"},
            ],
            "Antroji diena – nugaros pratimai": [
                {"exercise": "Paprasti prisitraukimai tik plačiai paėmus",
                 "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas nugarai", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas nugarai", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas nugarai", "sets_reps": "3 x 8-12"},
                {"exercise": "Atsilenkimai nugarai", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
            ],
            "Trečia diena – kojų pratimai": [
                {"exercise": "Pritūpimai su štanga", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas kojom", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas kojom", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas kojom", "sets_reps": "3 x 8-12"},
            ],
            "Ketvirta diena – pečių pratimai": [
                {"exercise": "Spaudimas sėdint su štanga", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas pečiams", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas pečiams", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas pečiams", "sets_reps": "3 x 8-12"},
            ],
            "Penkta diena – rankų pratimai": [
                {"exercise": "Pratimas bicepsui", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas tricepsui", "sets_reps": "5 x 8-12 (kontrolinis pratimas)"},
                {"exercise": "Pratimas bicepsui", "sets_reps": "4 x 8-12"},
                {"exercise": "Pratimas tricepsui", "sets_reps": "4 x 8-12"},
            ],
            "Šešta diena – poilsis": [
                {"exercise": "Poilsis", "sets_reps": "-"},
            ],
            "Septinta diena – poilsis": [
                {"exercise": "Poilsis", "sets_reps": "-"},
            ],
        },
        "istvermes": {
            "Pirmoji diena": [
                {"exercise": "Lenta", "sets_reps": "3 x 30s"},
                {"exercise": "Sokinejimas virvute", "sets_reps": "3 x 10"},
                {"exercise": "Lipimas i kalna", "sets_reps": "3 x 20"},
                {"exercise": "atsispaudimai", "sets_reps": "3 x 15"},
            ],
            "Antroji diena": [
                {"exercise": "Sokinejimas virvute", "sets_reps": "3 x 20"},
                {"exercise": "Itupstai", "sets_reps": "3 x 15 each leg"},
                {"exercise": "Keliu kelimas aukstai", "sets_reps": "3 x 30s"},
                {"exercise": "Suoliai ant dezutes", "sets_reps": "3 x 10"},
            ],
            "Trečioji diena": [
                {"exercise": "Begimas", "sets_reps": "20 minutes"},
                {"exercise": "Dviracio minimas", "sets_reps": "20 minutes"},
                {"exercise": "Virves traukimas", "sets_reps": "3 x 2 minutes"},
            ],
            "Ketvirta diena": [
                {"exercise": "Dviracio minimas", "sets_reps": "30 minutes"},
                {"exercise": "Itupstai", "sets_reps": "3 x 12"},
                {"exercise": "Lipimas i kalna", "sets_reps": "3 x 25"},
            ],
            "Penkta diena": [
                {"exercise": "Atsispaudimai", "sets_reps": "3 x 20"},
                {"exercise": "Sokinejimas virve", "sets_reps": "3 x 2 minutes"},
                {"exercise": "Begimas", "sets_reps": "15 minutes"},
            ],
            "Šešta diena – poilsis": [
                {"exercise": "Poilsis", "sets_reps": "-"},
            ],
            "Septinta diena – poilsis": [
                {"exercise": "Poilsis", "sets_reps": "-"},
            ],
        },
    }

    # Paieška pagal kategoriją
    workouts = workouts_data.get(category, {})

    return render(request, "workouts/workout_details.html", {"category": category, "workouts": workouts})


@login_required
def meals(request):
    goal = request.GET.get('goal')  # Gauname tikslą iš GET parametro
    programs = []
    title = ""

    if goal == 'weight_loss':
        title = "Svorio metimas"
        programs = [
            "meal: Pusryčiai - keptas kiaušinių omletas su avokadu. ",
            "meal: Pietūs - orkaitėje kepta lašiša su smidrais ir sviestu",
            "meal: Vakarienė - kiaulienos kotletai su salotomis",
        ]
    elif goal == 'muscle_gain':
        title = "Raumenų auginimas"
        programs = [
            "meal: 10 kiaušinių baltymų",
            "meal: 1¼ puodelis avižinių dribsnių",
            "meal: 230 g vištienos krūtinėlės",
            "meal: 2-3 puodeliai keptų makaronų",
            "meal: 230 g liesos jautienos mėsos",
        ]
    elif goal == 'healthy_eating':
        title = "Sveika mityba"
        programs = [
            "meal: Pusryčiai - Jogurtas su riešutais ir vaisiais",
            "meal: Pietūs - Kepta kalakutiena su kuskusu ir salotomis",
            "meal: Vakarienė - Daržovių troškinys su tofu",
        ]

    # Pašalinti 'meal:' ir brūkšnelius
    cleaned_programs = [program.replace("meal:", "").replace("-", "").strip() for program in programs]

    context = {
        'goal': goal,
        'title': title,
        'programs': cleaned_programs,
    }
    return render(request, 'meals/meals.html', context)


@login_required
def calorie_calculator(request):
    result = None
    bmi_category = None

    if request.method == "POST":
        try:
            # Gauti formos duomenis
            gender = request.POST.get("gender")
            weight = request.POST.get("weight")
            height = request.POST.get("height")
            activity_level = request.POST.get("activity_level")

            # Patikrinkite, ar visi laukai užpildyti
            if weight and height and activity_level and gender:
                # Konvertuoti į reikiamus tipus
                weight = float(weight)
                height = float(height)

                # Apskaičiuoti KMI
                height_in_meters = height / 100
                bmi = weight / (height_in_meters ** 2)

                # KMI kategorijos
                if bmi < 18.5:
                    bmi_category = "Per mažas svoris"
                elif 18.5 <= bmi < 24.9:
                    bmi_category = "Normalus svoris"
                elif 25 <= bmi < 29.9:
                    bmi_category = "Antsvoris"
                else:
                    bmi_category = "Nutukimas"

                # Apskaičiuoti kalorijas pagal aktyvumo lygį
                if activity_level == "sedentary":
                    calories = weight * 24 * 1.2
                elif activity_level == "light":
                    calories = weight * 24 * 1.375
                elif activity_level == "moderate":
                    calories = weight * 24 * 1.55
                else:  # "very_active"
                    calories = weight * 24 * 1.725

                # Grąžinti rezultatus
                result = {
                    "bmi": round(bmi, 2),
                    "bmi_category": bmi_category,
                    "calories": round(calories, 2),
                }
            else:
                result = {
                    "error": "Prašome užpildyti visus laukus."
                }

        except ValueError:
            result = {
                "error": "Įveskite galiojančius skaičius svoriui ir ūgiui."
            }

    return render(request, "nutrition/calorie_calculator.html", {"result": result})


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                return redirect('register')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.info(request, f'Vartotojas {username} užregistruotas!')
                return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')


@login_required
def profilis2(request):
    return render(request, 'main.html')


def logout_view(request):
    logout(request)
    return redirect('index')





def paieska(request):
    query = request.GET.get('query', '')
    search_results = []

    if query:
        # Paieška per įvairius modelius
        search_results += Workout.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        search_results += Exercise.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        search_results += Supplement.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        search_results += FoodProgram.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        search_results += Meal.objects.filter(Q(meal_name__icontains=query) | Q(description__icontains=query))

    # Pridedame klasės pavadinimą kiekvienam rezultatui
    for result in search_results:
        result.class_name = result.__class__.__name__

    return render(request, 'paieska.html', {'query': query, 'search_results': search_results})

def supplement_list(request):
    supplements = [
        {'id': 1, 'name': 'Baltymai (Proteinas)', 'description': 'Baltymai yra esminiai raumenų atstatymui ir augimui.',
         'long_description': 'Baltymai padeda atstatyti raumenis po treniruočių. Jie taip pat stiprina imuninę sistemą ir padeda atkurti energiją.'},
        {'id': 2, 'name': 'Kreatinas',
         'description': 'Kreatinas padeda didinti jėgą ir našumą intensyvių treniruočių metu.',
         'long_description': 'Kreatinas padeda raumenims pasisavinti daugiau energijos, leidžiant atlikti daugiau pasikartojimų ir pasiekti geresnius rezultatus.'},
        {'id': 3, 'name': 'Omega-3 Riebalų Rūgštys',
         'description': 'Omega-3 riebalų rūgštys prisideda prie širdies ir smegenų sveikatos.',
         'long_description': 'Omega-3 riebalų rūgštys mažina uždegimus ir palaiko širdies bei kraujagyslių sistemą.'},
        {'id': 4, 'name': 'Multivitaminai',
         'description': 'Multivitaminai padeda užtikrinti, kad jūsų organizmas gautų reikiamų vitaminų ir mineralų.',
         'long_description': 'Multivitaminai yra svarbūs palaikyti bendrą sveikatą, energijos lygį ir stiprinti imuninę sistemą.'},
        {'id': 5, 'name': 'Glutaminas',
         'description': 'Glutaminas padeda atstatyti raumenis ir pagerina imuninės sistemos funkcijas.',
         'long_description': 'Glutaminas yra aminorūgštis, padedanti greičiau atsigauti po intensyvių treniruočių ir mažinanti raumenų skausmus.'},
        {'id': 6, 'name': 'Amino Rūgštys',
         'description': 'Amino rūgštys padeda raumenų atstatymui ir suteikia energijos.',
         'long_description': 'Amino rūgštys yra svarbios raumenų statybai ir atstatymui po treniruočių.'},
        {'id': 7, 'name': 'Pre-workout',
         'description': 'Pre-workout papildai padeda pagerinti energiją ir ištvermę treniruotėse.',
         'long_description': 'Pre-workout papildai suteikia energijos, didina ištvermę ir padeda geriau susikaupti prieš treniruotes.'},
    ]
    return render(request, 'nutrition/supplement_list.html', {'supplements': supplements})


def supplement_detail(request, id):
    supplements = {
        1: {'name': 'Baltymai (Proteinas)', 'description': 'Baltymai yra esminiai raumenų atstatymui ir augimui.',
            'long_description': 'Baltymai (protein) – Baltymai yra vienas iš trijų makroelementų, kuriuos gauname iš maisto kartu su angliavandeniais ir riebalais. Makroelementai suteikia energijos kalorijų pavidalu – riebalai turi 9 kalorijas grame, o baltymai ir angliavandeniai – po 4 kalorijas grame. Vis dėlto baltymai mums ne tik suteikia energijos, bet taip pat padeda atstatyti arba augti kūno audiniams, vykdyti medžiagų apykaitos reakcijas bei palaiko kasdienę organizmo veiklą. Baltymai yra grandinės sudarytos iš mažesnių blokelių, vadinamų aminorūgštimis.  Tam tikri aminorūgščių tipai lemia baltymo formą ir funkciją. Baltymų galima rasti tiek gyvulinės, tiek augalinės kilmės maiste. Vis dėlto didžiausia baltymų koncentracija yra randama mėsoje, paukštienoje, žuvyje, kiaušiniuose ir pieno produktuose. Jų taip pat galite rasti pupose, žirniuose, riešutuose, sojoje ir sėklose..',
            'dose': 'nuo 0.5kg iki 2kg ',
            'usage': 'Sveikam žmogui reikia 0,8-1,2 gramo baltymų vienam kilogramui kūno svorio. Taigi, jeigu sveriate 70 kilogramų, turėtumėte suvartoti apie 56-84 baltymų per dieną. Jeigu norite auginti masę ir išvysti kitus baltymų privalumus, skaičius 1 kilogramui kūno masės turėtų siekti nuo 1,2 iki 2,2 gramo.'},
        2: {'name': 'Kreatinas', 'description': 'Kreatinas padeda didinti jėgą ir našumą intensyvių treniruočių metu.',
            'long_description': 'Kreatinas (creatine) - Kreatinas yra vienas populiariausių ir daugiausiai tyrinėtų papildų, kurie parduodami rinkoje. Moksliniais tyrimais įrodyta, kad jis gerina fizinius rezultatus per itin trumpą laiką itin intensyviai treniruojantis, tad jis tampa nepakeičiamu jūsų treniruočių draugu. Kreatinas pasigamina iš amino rūgščių glicino, arginino ir metionino. Jau yra įrodyta, kad kreatinas padidina raumenų ištvermę ir jėgą. Kreatinas dalyvauja ATP gamyboje, kas yra energijos šaltinis ne tik mūsų raumenims, bet ir smegenims.',
            'dose': '500 g', 'usage': '3 g per dieną'},
        3: {'name': 'Omega-3 Riebalų Rūgštys',
            'description': 'Omega-3 riebalų rūgštys prisideda prie širdies ir smegenų sveikatos.',
            'long_description': 'Omega rūgštys – Tai maisto papildai, kurie turi būti vartojami neatsižvelgiant į tai, jog žmogus yra fiziškai aktyvus, ar ne. Jie yra privalomi kiekvienam organizmui. Omega rūgštys ir žuvies taukai turi didelę įtaką širdies ir kraujagyslių veiklai, palankiai veikia sąnarius, o taip pat yra atsakingos ir už odos sveikatą. Šie papildai teigiamai veikia ir žmogaus nuotaiką bei nervų sistemą. Juos galima vartoti įvairiais būdais, todėl belieka išsirinkti jums patogiausią formą: Skystis ar kapsulės. Omega 3 yra svarbiausios riebiosios rūgštys. Jos susideda iš EPA (EPR) Eikozapentaeno rūgšties, DHA (DHR) Dokozaheksaeno rūgšties ir ALA (ALR) Alfa-linoleno rūgšties..',
            'dose': '200 kapsulės', 'usage': '1 kapsulė per dieną'},
        4: {'name': 'Multivitaminai',
            'description': 'Multivitaminai padeda užtikrinti, kad jūsų organizmas gautų reikiamų vitaminų ir mineralų.',
            'long_description': 'Vitaminai ir mineralai – Čia rasite papildus, kurie yra atsakingi už įvairius rodiklius, tokius kaip: miego kokybė, imuniteto stiprinimas, energijos palaikymas bei daugelis kitų. Visiems žinoma, jog vien iš sveiko maisto susirinkimas visų organizmui būtinų medžiagų yra labai sunkus, todėl ir turime maisto papildus, į kuriuos įeina vitaminai bei mineralai esantys maisto produktuose, tačiau patiriant didesnį fizinį krūvį ar atsistatant po traumos prireikia ir papildų pagalbos norint įsisavinti didesnį mineralų ar vitaminų dalį..',
            'dose': '60 kapsulių', 'usage': '1 kapsulė per dieną'},
        5: {'name': 'Glutaminas',
            'description': 'Glutaminas padeda atstatyti raumenis ir pagerina imuninės sistemos funkcijas.',
            'long_description': 'Glutaminas yra aminorūgštis, padedanti greičiau atsigauti po intensyvių treniruočių ir mažinanti raumenų skausmus.',
            'dose': '500 g', 'usage': '5 g per dieną'},
        6: {'name': 'Amino Rūgštys', 'description': 'Amino rūgštys padeda raumenų atstatymui ir suteikia energijos.',
            'long_description': 'Amino rūgštys yra svarbios raumenų statybai ir atstatymui po treniruočių.',
            'dose': '300 g', 'usage': '10 g per dieną'},
        7: {'name': 'Pre-workout',
            'description': 'Pre-workout papildai padeda pagerinti energiją ir ištvermę treniruotėse.',
            'long_description': 'Pre-workout papildai suteikia energijos, didina ištvermę ir padeda geriau susikaupti prieš treniruotes.',
            'dose': '250 g', 'usage': '20 g prieš treniruotę'},
    }

    supplement = supplements.get(id)
    if supplement:
        return render(request, 'nutrition/supplement_detail.html', {'supplement': supplement})
    else:
        return render(request, 'nutrition/supplement_list.html', {'error': 'Papildas nerastas.'})


@login_required
def profile(request):
    # Tikriname, ar vartotojas nori redaguoti profilį
    is_editing = request.GET.get('edit') == 'true'

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {
        'u_form': u_form,
        'p_form': p_form,
        'is_editing': is_editing,
    })
