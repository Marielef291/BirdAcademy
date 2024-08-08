import requests
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from Application.models import Bird, Song
from django.http import JsonResponse


@login_required(redirect_field_name="login")
def home (request) :
    return render (request, 'application/home.html')


@login_required(redirect_field_name="login")
def addBird(request):
    if request.method == "POST":
        user_birds = list(Bird.objects.filter(User_Bird=request.user).values_list('id', flat=True))
        selected_birds_ids = [int(bird_id) for bird_id in request.POST.get("tags", "").split(", ") if bird_id]
        user = request.user

        # Ajouter les nouveaux oiseaux sélectionnés
        for bird_id in selected_birds_ids:
            bird = Bird.objects.get(id=bird_id)
            bird.User_Bird.add(user)
            
            # Vérifier si des chants sont déjà enregistrés pour cet oiseau
            if not Song.objects.filter(Id_bird=bird).exists():
                # Construire l'URL de la requête
                url = "https://xeno-canto.org/api/2/recordings?query=cnt:france+"
                query_url = url + bird.Latin_name.replace(" ", "+")
                print(query_url)
                
                try:
                    response = requests.get(query_url)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get("recordings"):
                            recordings = data.get("recordings", [])
                            # Limiter à 10 enregistrements max
                            for record in recordings[:10]:
                                # Créer une nouvelle instance Song pour chaque enregistrement
                                song = Song(
                                    Id_bird=bird,  # Associe l'objet Bird à la clé étrangère Id_bird
                                    URL_Song=record.get("file"),
                                    List_Other_Birds=record.get("also", [])
                                )
                                song.save()
                    else:
                        print(f"Erreur lors de la requête API: {response.status_code}")
                except requests.RequestException as e:
                    print(f"Exception lors de la requête API: {e}")
        
        # Supprimer les oiseaux désélectionnés
        for birdUser in user_birds:
            if birdUser not in selected_birds_ids:
                bird = Bird.objects.get(id=birdUser)
                bird.User_Bird.remove(user)

        return redirect('home')

    nameBird = Bird.objects.all()
    user_birds = Bird.objects.filter(User_Bird=request.user).values_list('id', flat=True)

    return render(request, 'application/addBird.html', {
        "nameBird": nameBird,
        "userBirds": user_birds
    })


@login_required(redirect_field_name="login")
def quizz (request) :
    return render (request, 'application/quizz.html')



@login_required(redirect_field_name="login")
def get_user_birds(request):
    user_birds = Bird.objects.filter(User_Bird=request.user).values('id','Latin_name', 'Fr_name', 'Eng_name')
    return JsonResponse(list(user_birds), safe=False)

@login_required(redirect_field_name="login")
def get_song_birds_user(request):
    user_birds = Bird.objects.filter(User_Bird=request.user)
    song_birds = Song.objects.filter(Id_bird__in=user_birds).values('Id_bird', 'List_Other_Birds', 'URL_Song')
    
    return JsonResponse(list(song_birds), safe=False)